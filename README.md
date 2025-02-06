# Previs-o-do-Pre-o-das-A-es-da-PETR4-com-Prophet
 Prophet usada em analise financeira
 Descrição do Projeto

Este projeto utiliza dados históricos das ações da Petrobras (PETR4) para realizar previsões de preços futuros usando Facebook Prophet, além de detectar outliers e avaliar o desempenho do modelo. Foi adicionado também um modelo de regressão linear para análise comparativa.

🔍 Objetivos

Baixar dados históricos da PETR4 usando a API do Yahoo Finance.

Detectar outliers para melhorar a qualidade dos dados.

Treinar um modelo Prophet para previsão de preços.

Avaliar o desempenho do modelo utilizando métricas de validação cruzada.

Gerar gráficos interativos com Plotly para melhor visualização.

🛠️ Tecnologias Utilizadas

Python (para manipulação e análise de dados)

yFinance (para extração de dados financeiros)

Pandas (para manipulação dos dados)

Prophet (para modelagem e previsão)

Scikit-Learn (para modelo de regressão linear)

Plotly (para visualização interativa)

📊 Metodologia

1️⃣ Coleta de Dados

Os dados históricos da Petrobras são obtidos via Yahoo Finance.

2️⃣ Detecção de Outliers

A técnica de IQR (Interquartile Range) é utilizada para detectar e tratar valores extremos.

3️⃣ Modelagem com Prophet

O modelo Prophet é ajustado com sazonalidade anual e semanal, prevendo os próximos 365 dias.

4️⃣ Avaliação do Modelo

A validação cruzada é aplicada para medir métricas como RMSE e MAPE.

5️⃣ Visualização dos Resultados

Os resultados são apresentados com gráficos interativos usando Plotly.
