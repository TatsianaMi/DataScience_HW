import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def plotting_heatmap(df: pd.DataFrame):
    correlation_matrix = df.corr()
   # print(correlation_matrix)
    plt.figure(figsize=(15, 9))
    heatmap_plot = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.show()
    None