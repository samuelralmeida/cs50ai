- [English version](#english)
- [Versão em português brasileiro](#pt-br)


# <a id="english"></a> Neural network experiments for image classification

This project explores different architectures and configurations of a neural network to classify images. Through a series of tests, various structural and hyperparameter modifications were made to find the best combination for maximizing accuracy and minimizing loss.

The data set for this project is the [German Traffic Sign Recognition Benchmark](http://benchmark.ini.rub.de/?section=gtsrb&subsection=news) (GTSRB) dataset, which contains thousands of images of 43 different kinds of road signs. Download it [here](https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb.zip)

## Experiment Structure

1. Baseline Model (Simple Neural Network)

    - Initially, a basic model with a Flatten layer and a single Dense layer was used as a baseline.

    - Result: 80.71% accuracy and 30.8757 loss.

2. Adding a Convolutional Layer

    - A Conv2D layer with a 3x3 filter and different numbers of filters (32, 64, and 128) was tested.
    
    - **Best Configuration**: 64 filters with a 3x3 kernel.

    - **Result**: 92.31% accuracy and 0.8992 loss (better than configurations with 32 and 128 filters).

3. Changing the Filter Size

    - The filter size was changed to 5x5 to assess the impact.
    
    - **Result**: The 3x3 filter performed better, so it was kept.

4. Adding Pooling Layers

    - Pool sizes of 2x2 and 3x3 were tested after the convolutional layer.

    - **Best Configuration**: MaxPooling2D with a 2x2 pool size.

    - **Result**: 92.46% accuracy and 0.5695 loss (better than the 3x3 pool).

5. Duplicating Convolutional and Pooling Layers

    - A second convolutional and pooling layer was added.

    - **Result**: 94.49% accuracy and 0.3058 loss, indicating improved precision and significantly reduced loss.

6. Adding an Extra Dense Layer

    - An additional dense layer was tested with different sizes (128, 256, and 512 units).

    - **Best Configuration**: Dense layer with 128 units.

    - **Result**: 95.76% accuracy and 0.2433 loss (superior to the 256 and 512 unit layers).

7. Adding Dropout

    - Dropout rates of 0.2 and 0.5 were tested to reduce overfitting.

    - **Best Configuration**: Dropout of 0.5.

    - **Result**: 95.31% accuracy and 0.1663 loss, with reduced overfitting and improved generalization.

## Summary of Results

| Configuration | Accuracy | Loss |
| ------------- | -------- | ---- |
| Baseline Model | 0.8071 | 30.8757 |
| Conv2D with 32 filters (3x3) |	0.8725 |	1.2200 |
| Conv2D with 64 filters (3x3) |	0.9231 |	0.8992 |
| Conv2D with 128 filters (3x3) |	0.8566 |	1.1342 |
| Conv2D with 64 filters (5x5) |	0.9097 |	1.0322 |
| Conv2D with 64 filters (3x3) + MaxPooling2D (2x2) |	0.9246 |	0.5695 |
| Conv2D with 64 filters (3x3) + MaxPooling2D (3x3) |	0.9214 |	0.6258 |
| Duplicated: Conv2D with 64 filters (3x3) + MaxPooling2D (2x2) |	0.9449 |	0.3058 |
| Duplicated: Conv2D with 64 filters (3x3) + MaxPooling2D (2x2) + Dense layer (128 units) |	0.9576 |	0.2433 |
| Duplicated: Conv2D with 64 filters (3x3) + MaxPooling2D (2x2) + Dense layer (256 units) |	0.9337 | 0.3775 |
| Duplicated: Conv2D with 64 filters (3x3) + MaxPooling2D (2x2) + Dense layer (512 units) |	0.9497 | 0.2871 |
| Duplicated: Conv2D with 64 filters (3x3) + MaxPooling2D (2x2) + Dense layer (128 units) + Dropout (0.2) |	0.9531 |	0.1663 |
| Duplicated: Conv2D with 64 filters (3x3) + MaxPooling2D (2x2) + Dense layer (128 units) +  Dropout (0.5) |	0.9531 |	0.1663 |

## What Worked Well

- **Number of Filters**: 64 filters proved to be the best configuration for the initial convolutional layer.

- **2x2 Pooling**: Pooling with a 2x2 size performed slightly better than 3x3, with lower loss.

- **Layer Duplication**: Duplicating the convolutional and pooling layers led to a significant improvement in accuracy and a considerable reduction in loss.

- **Dense Layer with 128 Units**: Among the various sizes tested, a dense layer with 128 units provided the best balance of accuracy and low loss.

- **Dropout at 0.5**: Reduced overfitting, resulting in improved accuracy and lower loss.

## What Didn’t Work Well

- **5x5 Filter Size**: Using a 5x5 filter showed inferior performance compared to the 3x3 filter.

- **Dense Layers with 256 and 512 Units**: Additional dense layers with 256 and 512 units increased the loss and decreased accuracy, indicating overfitting.

## General Observations

- The model progressively improved as convolutional and pooling layers were added, highlighting the importance of feature extraction in neural networks for image classification.

- Dropout was essential for improving generalization, especially in more complex configurations.

- Intermediate dense layers with 128 units struck a good balance between complexity and performance, proving to be an excellent choice for avoiding overfitting.

- This README summarizes the experimental steps taken to build and refine an effective neural network model for image classification. Each step revealed key improvements or adjustments that guided the final model configuration.

---

# <a id="pt-br"></a>Experimentos com redes neurais para classificação de imagens

Este projeto explora diferentes arquiteturas e configurações de uma rede neural para classificar imagens. Através de uma série de testes, foram realizadas modificações estruturais e de parâmetros na rede para encontrar a melhor combinação para maximizar a acurácia e minimizar a perda.

O conjunto de dados para este projeto é o [German Traffic Sign Recognition Benchmark](http://benchmark.ini.rub.de/?section=gtsrb&subsection=news) (GTSRB), que contém milhares de imagens de 43 tipos diferentes de sinais de trânsito. Baixe-o [aqui](https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb.zip).

## Estrutura dos Experimentos

1. Modelo base (Rede Neural Simples)

    - Inicialmente, um modelo básico com uma camada Flatten e uma camada Dense foi usado como base de comparação.

    - Resultado: Acurácia de 80.71% e perda de 30.8757.

2. Adição de camada convolucional

    - Adicionou-se uma camada Conv2D com filtro 3x3 e diferentes quantidades de filtros (32, 64, e 128).

    - **Melhor configuração**: Filtro de 64 unidades com 3x3.

    - **Resultado**: Acurácia de 92.31% e perda de 0.8992 (melhor que os modelos com 32 e 128 filtros).

3. Alteração do Tamanho do Filtro

    - O filtro foi alterado para 5x5 para avaliar o impacto.

    - **Resultado**: O filtro 3x3 demonstrou ser mais eficaz, então foi mantido.

4. Adição de camadas de pooling

    - Foram testados tamanhos de pool 2x2 e 3x3 após a camada convolucional.

    - **Melhor configuração**: MaxPooling2D com pool de 2x2.

    - **Resultado**: Acurácia de 92.46% e perda de 0.5695 (melhor que a camada com pool 3x3).

5. Duplicação das camadas de Convolução e Pooling

    - Adicionada uma segunda camada convolucional e de pooling.

    - **Resultado**: Acurácia de 94.49% e perda de 0.3058, indicando melhoria na precisão e redução significativa da perda.

6. Adição de camada densa extra

    - Testados diferentes tamanhos de camada densa adicional (128, 256 e 512 unidades).

    - **Melhor configuração**: Camada densa com 128 unidades.

    - **Resultado**: Acurácia de 95.76% e perda de 0.2433 (superior às camadas de 256 e 512 unidades).

7. Adição de dropout

    - Foram testadas taxas de dropout de 0.2 e 0.5 para reduzir overfitting.

    - **Melhor configuração**: Dropout de 0.5.

    - **Resultado**: Acurácia de 95.31% e perda de 0.1663, com menor overfitting e melhor generalização.

## Resultados Resumidos

| Configuração | Acurácia | Perda |
| ------------- | -------- | ---- |
| Modelo base | 0,8071 | 30,8757 |
| Conv2D com 32 filtros (3x3) |	0,8725 |	1,2200 |
| Conv2D com 64 filtros (3x3) |	0,9231 |	0,8992 |
| Conv2D com 128 filtros (3x3) |	0,8566 |	1,1342 |
| Conv2D com 64 filtros (5x5) |	0,9097 |	1,0322 |
| Conv2D com 64 filtros (3x3) + MaxPooling2D (2x2) |	0,9246 |	0,5695 |
| Conv2D com 64 filtros (3x3) + MaxPooling2D (3x3) |	0,9214 |	0,6258 |
| Duplicação: Conv2D com 64 filtros (3x3) + MaxPooling2D (2x2) |	0,9449 |	0,3058 |
| Duplicação: Conv2D com 64 filtros (3x3) + MaxPooling2D (2x2) + Camada densa (128 unidades) |	0,9576 |	0,2433 |
| Duplicação: Conv2D com 64 filtros (3x3) + MaxPooling2D (2x2) + Camada densa (256 unidades) |	0,9337 | 0,3775 |
| Duplicação: Conv2D com 64 filtros (3x3) + MaxPooling2D (2x2) + Camada densa (512 unidades) |	0,9497 | 0,2871 |
| Duplicação: Conv2D com 64 filtros (3x3) + MaxPooling2D (2x2) + Camada densa (128 unidades) + Dropout (0,2) |	0,9531 |	0,1663 |
| Duplicação: Conv2D com 64 filtros (3x3) + MaxPooling2D (2x2) + Camada densa (128 unidades) +  Dropout (0,5) |	0,9531 |	0,1663 |

## O que funcionou bem

- **Quantidade de filtros**: 64 filtros demonstraram ser a melhor configuração para a camada convolucional inicial.

- **Pooling 2x2**: O pooling com tamanho 2x2 teve um desempenho ligeiramente superior ao de 3x3, com menor perda.

- **Duplicação das camadas**: A duplicação das camadas convolucionais e de pooling resultou em uma melhoria considerável na precisão e na redução da perda.

- **Camada densa com 128 unidades**: Ao testar diferentes tamanhos, uma camada densa com 128 unidades provou-se ideal em termos de acurácia e perda.

- **Dropout de 0,5**: Reduziu o overfitting, resultando em uma acurácia e perda aprimoradas.

## O que não funcionou bem

- **Filtro de tamanho 5x5**: O uso de filtros de 5x5 mostrou um desempenho inferior ao de 3x3.

- **Camadas densas com 256 e 512 unidades**: Camadas densas adicionais com 256 e 512 unidades aumentaram a perda e reduziram a acurácia, indicando overfitting.

## Observações gerais

- O modelo foi progressivamente melhorado à medida que camadas de convolução e pooling foram adicionadas, destacando a importância de extração de características visuais em redes neurais para classificação de imagens.

- Dropout foi fundamental para melhorar a generalização, especialmente com configurações mais complexas.

- Camadas densas intermediárias com 128 unidades atingiram um equilíbrio entre complexidade e performance, mostrando-se uma ótima escolha para evitar overfitting.

- Este README resume os passos experimentais realizados para construir e refinar uma rede neural eficaz para classificação de imagens. A cada etapa, observou-se uma melhora ou ajuste importante, guiando a escolha da configuração final do modelo.