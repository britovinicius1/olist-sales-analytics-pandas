#%%

import pandas as pd

# %%

notas = pd.read_csv("../data02/ratings.csv")
# %%
notas.shape
# %%
notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']

# %%
notas.head(5)
# %%
notas['nota'].unique()
# %%
notas["nota"].value_counts()
# %%
resultado = (
    notas.groupby('nota')[['nota']]
         .count()
         .rename(columns={'nota': 'quantidade'})
         .reset_index()
)

# %%
resultado = resultado.sort_values('nota', ascending=False)
# %%
resultado['frequencia_relativa'] = resultado['quantidade'] / resultado['quantidade'].sum()

# %%
resultado['requencia_acumulada'] = resultado['quantidade'].cumsum()
resultado
# %%
resultado['frequencia_acumulada_percent'] = resultado['requencia_acumulada'] / resultado['quantidade'].sum()
resultado
# %%
notas['nota'].mean()
# %%
notas["nota"].plot(kind='hist')
# %%

# %%
mediana = notas['nota'].median()
media = notas['nota'].mean()
# %%
# %%
notas['nota'].describe()
# %%
notas[['nota']].reset_index().sort_values('nota', ascending=True)
# %%
import seaborn as sns

# %%

#interpretação
# mediana -> 3.5
## 25% tao entre 3.5 e 4
## 50% tao entre 3 e 4


sns.boxplot(notas['nota'])
# %%
filmes = pd.read_csv("../data02/movies.csv")
filmes.head(5)

# %%
filmes.columns = ['filmeId', 'titulo', 'generos']
filmes
# %%
notas.head(5)
# %%
notas.query('filmeId == 2')['nota'].mean()
# %%
filmes.head(5)
# %%
medias_por_filme = notas.groupby('filmeId')['nota'].mean()
# %%
medias_por_filme.head(5)
# %%
#a maioria dos filmes tem nota entre 3 e 4
medias_por_filme.plot(kind='hist')
# %%
