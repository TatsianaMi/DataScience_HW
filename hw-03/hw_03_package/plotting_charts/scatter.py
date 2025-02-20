import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def plottingScatter(df: pd.DataFrame):
  plt.figure()
  plt.xlabel('Carat Weight')
  plt.ylabel('Price')
  df_GIA = df.query('Type == "GIA"')
  df_GIA_Lab_Grown = df.query('Type == "GIA Lab-Grown"')
  df_IGI_Lab_Grown = df.query('Type == "IGI Lab-Grown"')

  plt.scatter(df_GIA['Carat Weight'], df_GIA['Price'], color='#23d4e8')
  plt.scatter(df_GIA_Lab_Grown['Carat Weight'], df_GIA_Lab_Grown['Price'], color='#32cd68')
  plt.scatter(df_IGI_Lab_Grown['Carat Weight'], df_IGI_Lab_Grown['Price'], color='#8d2062')
  plt.legend(["GIA", "GIA Lab-Grown", "IGI Lab-Grown" ])
  plt.show()
  None