import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def plottingHistogram(df: pd.DataFrame, xlabel: str, ylabel: str, title: str):
    """
    histogram(df: pd.DataFrame, xlabel: str, ylabel: str, title: str
    Plotting a basic histogram. Adding labels and title
    """
    
    plt.hist(df[xlabel], bins=50, color='skyblue', edgecolor='black')
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    plt.show()
    None