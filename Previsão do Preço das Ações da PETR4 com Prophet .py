import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics

# Baixar os dados históricos da Petrobras (PETR4)
ticker = 'PETR4.SA'
dados = yf.download(ticker, start='2010-01-01', end='2025-01-01')

# Detecção de Outliers (exemplo simples com IQR)
Q1 = dados['Close'].quantile(0.25)
Q3 = dados['Close'].quantile(0.75)
IQR = Q3 - Q1
outliers = (dados['Close'] < (Q1 - 1.5 * IQR)) | (dados['Close'] > (Q3 + 1.5 * IQR))
dados['outlier'] = outliers

# Preparar os dados para o Prophet
df = dados[['Close']].reset_index()
df.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)

# Criar e treinar o modelo Prophet
modelo = Prophet(daily_seasonality=False, yearly_seasonality=True, weekly_seasonality=True)
modelo.fit(df)

# Criar DataFrame de previsão para os próximos 365 dias
future = modelo.make_future_dataframe(periods=365)
forecast = modelo.predict(future)

# Avaliação do Modelo
df_cv = cross_validation(modelo, initial='365 days', period='180 days', horizon='365 days')
df_p = performance_metrics(df_cv)
print(df_p.head())

# Gráfico interativo com fundo branco
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], mode='lines', name='Histórico'))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Previsão', line=dict(dash='dot')))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode='lines', name='Limite Superior', line=dict(dash='dot')))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], mode='lines', name='Limite Inferior', line=dict(dash='dot')))

fig.update_layout(
    title='Previsão do Preço das Ações da PETR4 com Prophet',
    xaxis_title='Data',
    yaxis_title='Preço de Fechamento (R$)',
    template='plotly_white',
    width=1000,  # Aumentar o tamanho do gráfico
    height=600
)

# Mostrar gráfico
fig.show()
