import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

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