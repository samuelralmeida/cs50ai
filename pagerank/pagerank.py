import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print("PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    distribution = {}

    to_pages = corpus[page]

    if len(to_pages) == 0:
        prob = 1 / len(corpus)
        for corpus_page in corpus:
            distribution[corpus_page] = prob

        return distribution

    damping_probability = damping_factor / len(to_pages)

    damping_probability_random = (1 - damping_factor) / len(corpus)

    for page in to_pages:
        distribution[page] = damping_probability

    for corpus_page in corpus:
        if corpus_page in to_pages:
            distribution[corpus_page] += damping_probability_random
        else:
            distribution[corpus_page] = damping_probability_random

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    pagerank = {}

    page = random.choice(list(corpus))

    for i in range(n - 1):
        model = transition_model(corpus, page, damping_factor)

        page = random.choices(population=list(model), weights=model.values(), k=1).pop()

        if page in pagerank:
            pagerank[page] += 1
        else:
            pagerank[page] = 1

    for page in pagerank:
        pagerank[page] = pagerank[page] / n

    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    pagerank = {}

    for page in corpus:
        pagerank[page] = 1 / len(corpus)

    result_step = False
    while not result_step:
        pagerank_copy = {}
        for key, value in pagerank.items():
            pagerank_copy[key] = value

        pagerank_diff = {}

        for page in corpus.keys():
            probability = 0

            for page_i, pages in corpus.items():
                if page in pages:
                    probability += pagerank_copy[page_i] / len(pages)

                elif len(pages) == 0:
                    probability += 1 / len(corpus)

            pagerank[page] = (1 - damping_factor) / len(corpus) + (
                damping_factor * probability
            )

            pagerank_diff[page] = abs(pagerank_copy[page] - pagerank[page])

        result_step = True
        for page in pagerank_diff:
            if pagerank_diff[page] > 0.001:
                result_step = False

    sum_pagerank = 0
    for k in pagerank:
        sum_pagerank += pagerank[k]

    for k in pagerank:
        pagerank[k] = pagerank[k] / sum_pagerank

    return pagerank


if __name__ == "__main__":
    main()
