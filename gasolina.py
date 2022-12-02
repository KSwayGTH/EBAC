import seaborn as sns 
import pandas 
import matplotlib.pyplot as plt
data = pandas.read_csv("gasolina.csv") 
data.head()
sns.lineplot( data['dia'], data['venda'])
plt.savefig('gasolina.png')
