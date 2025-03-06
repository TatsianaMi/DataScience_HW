import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

def plottingBar(df: pd.DataFrame):
  plt.bar(df['Type'], df['Price'])
  plt.xlabel("type")
  plt.ylabel("price")
  plt.title(" Vertical bar graph")
  plt.show()
  None

def plottingHistogramWithDensity(df: pd.DataFrame):
  sns.histplot(df, x=df['Type'], y=df['Price'], bins=10, kde=True, color='lightgreen', edgecolor='red')
  plt.xlabel('Values')
  plt.ylabel('Density')
  plt.title('Customized Histogram with Density Plot')
  plt.show()
  None

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

def plottingHexbin(df: pd.DataFrame):
  # Creating a 2D histogram (hexbin plot)
  plt.hexbin(df['Price'], df['Height'], gridsize=30, cmap='Blues')

  # Adding labels and title
  plt.xlabel('Price')
  plt.ylabel('Height')
  plt.title('Hexbin Plot')

  # Adding colorbar
  plt.colorbar()

  # Display the plot
  plt.show()
  None

print('plotting-charts.py loaded')
print('__name__ in plotting-charts.py: ', __name__)