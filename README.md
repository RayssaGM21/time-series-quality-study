# Time Series Data Quality - Testes e Análise

Este repositório foi desenvolvido com o propósito de realizar testes e investigações sobre a qualidade dos dados em séries temporais, com foco no tratamento de dados ausentes e na detecção de anomalias. Através deste código, busquei aprofundar o entendimento sobre as metodologias aplicáveis à análise de séries temporais e as implicações da qualidade dos dados em análises subsequentes.

## Objetivos e Funcionalidades

O código implementado neste repositório disponibiliza um conjunto de ferramentas para análise e melhoria da qualidade dos dados em séries temporais, abordando especificamente as questões relacionadas ao tratamento de valores ausentes e à identificação de anomalias. As funcionalidades incluem:

- **Verificação de valores ausentes**: Cálculo e identificação da quantidade de valores ausentes e da porcentagem desses valores em relação ao total de dados disponíveis.
- **Preenchimento de dados ausentes**: Implementação de diferentes estratégias de imputação para lidar com valores faltantes, incluindo média, mediana e métodos de preenchimento por propagação (forward fill, backward fill).
- **Detecção de anomalias**: Utilização de métodos estatísticos clássicos (Z-score e IQR) para identificar outliers ou comportamentos atípicos nas séries temporais.
- **Visualização dos dados**: Geração de gráficos para ilustrar as séries temporais com a sobreposição de anomalias detectadas, permitindo uma análise exploratória mais detalhada.

## Conhecimentos Adquiridos

Durante a implementação deste projeto, pude aprofundar minha compreensão sobre diversos aspectos da análise de séries temporais, com ênfase em:

### 1. **Tratamento de Valores Ausentes**
O tratamento de valores ausentes é uma etapa crucial em qualquer análise de dados. A escolha da técnica adequada de imputação pode impactar significativamente os resultados da análise. Foram explorados os seguintes métodos:
- **Média (mean)**: Preenchimento dos valores ausentes pela média da série temporal.
- **Mediana (median)**: Substituição dos valores ausentes pela mediana.
- **Preenchimento por propagação para frente (ffill)**: Preenchimento dos valores ausentes com os valores anteriores à lacuna.
- **Preenchimento por propagação para trás (bfill)**: Substituição dos valores ausentes com os valores posteriores à lacuna.

### 2. **Detecção de Anomalias**
A detecção de anomalias é uma das abordagens fundamentais na análise de dados para identificar comportamentos inesperados ou erros nos dados. Foram implementados dois métodos principais:
- **Z-score**: Identificação de pontos de dados que estão a uma distância padrão significativa da média, caracterizando-os como anômalos.
- **IQR (Interquartile Range)**: Definição de limites com base no intervalo interquartil para identificar valores que estão fora da faixa esperada de variação da série temporal.

### 3. **Visualização de Séries Temporais**
A visualização de dados é uma ferramenta essencial para a análise exploratória. A criação de gráficos permite não apenas a compreensão da tendência dos dados, mas também a identificação visual de anomalias e outros padrões que poderiam passar despercebidos em uma análise puramente quantitativa.

### 4. **Importância da Qualidade dos Dados**
A qualidade dos dados é um fator determinante para a precisão e confiabilidade das análises. Através da aplicação das técnicas de imputação e detecção de anomalias, ficou evidente como erros ou lacunas nos dados podem prejudicar os resultados de modelos analíticos, tornando fundamental a aplicação cuidadosa dessas abordagens para garantir a integridade das conclusões.

## Funcionalidades Implementadas

### 1. **Verificação de Dados Ausentes**
Identificação da quantidade de valores ausentes e cálculo da porcentagem desses valores em relação ao total de dados disponíveis.

### 2. **Preenchimento de Valores Ausentes**
Diversos métodos de imputação estão disponíveis para lidar com dados ausentes:
- **Média (mean)**
- **Mediana (median)**
- **Preenchimento por propagação para frente (ffill)**
- **Preenchimento por propagação para trás (bfill)**

### 3. **Detecção de Anomalias**
Os seguintes métodos são usados para detectar anomalias na série temporal:
- **Z-score**: Utiliza o desvio padrão para identificar valores fora de um intervalo padrão de variação.
- **IQR (Interquartile Range)**: Utiliza os quartis da distribuição dos dados para identificar pontos fora da faixa interquartil.

### 4. **Visualização**
Os dados são visualizados em gráficos com a detecção de anomalias, facilitando a análise e compreensão do comportamento da série temporal.

## Como Utilizar

### Instalação

Para utilizar este código, clone este repositório e instale as dependências necessárias com o seguinte comando:

```bash
git clone https://github.com/RayssaGM21/time-series-quality-study.git
cd time-series-quality
pip install pandas numpy matplotlib
