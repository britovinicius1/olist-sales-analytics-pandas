
#%%
import pandas as pd
import matplotlib.pyplot
import seaborn as sns
#%%
tmdb = pd.read_csv('../data02/tmdb_5000_movies.csv')
# %%
tmdb.head(5)
# %%

total_por_lingua = tmdb["original_language"].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc["en"]
total_do_resto = total_geral - total_de_ingles
print(total_geral, total_de_ingles, total_do_resto)
# %%
dados = {
  "lingua" : ["ingles", "outros"],
  "total" : [total_de_ingles, total_do_resto]
}
dados = pd.DataFrame(dados)
dados
# %%

sns.barplot(data=dados, x="lingua", y="total")
# %%
total_de_outros_filmes_por_lingua = tmdb.query("original_language != 'en'")["original_language"].value_counts()
total_de_outros_filmes_por_lingua.head()
# %%

sns.countplot(data=tmdb.query("original_language != 'en'"),
              x="original_language")
# %%

sns.countplot(data=tmdb.query("original_language != 'en'"),
              order=total_de_outros_filmes_por_lingua.index,
              hue="original_language",
              x="original_language")
# %%
