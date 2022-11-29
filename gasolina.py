import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('/content/EBAC/gasolina.csv', sep=',')

gasolina_df.head()

with sns.axes_style('darkgrid'):
  grafico = sns.lineplot(x='dia', y='venda', data=gasolina_df, palette='pastel')
  grafico.set(title='Preço de Venda Gasolina', xlabel='Dia', ylabel='Preço de Venda')

fig = grafico.get_figure()

fig.savefig('gasolina.png')
