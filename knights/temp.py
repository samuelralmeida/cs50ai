from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

resp = Not(AKnight)

# temp_e = And(Not(AKnight), AKnave)
temp_or = Or(And(AKnight, Not(AKnave)), And(Not(AKnight), AKnave))
temp_and = And(Or(AKnight, Not(AKnave)), Or(Not(AKnight), AKnave))

# print(AKnight.formula(), AKnight.symbols())
# print(AKnave.formula(), AKnave.symbols())
# print(resp.formula(), resp.symbols())

# print(Sentence.parenthesize(AKnight.formula()))
print(temp_and.formula(), temp_and.symbols())
print(temp_or.formula(), temp_or.symbols())