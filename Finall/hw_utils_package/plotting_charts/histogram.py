import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def plotting_histogram(df: pd.DataFrame, column: str, xlabel: str, ylabel: str, title: str, bins: int = 50, color: str = 'skyblue', edgecolor: str = 'black'):
    """
    Plotting a histogram with specified parameters.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data to plot.
    - column (str): The column name in the DataFrame to plot.
    - xlabel (str): The label for the x-axis.
    - ylabel (str): The label for the y-axis.
    - title (str): The title of the histogram.
    - bins (int): The number of bins for the histogram (default is 50).
    - color (str): The color of the bars (default is 'skyblue').
    - edgecolor (str): The color of the edges of the bars (default is 'black').
    """
    
    # Check if the specified column exists in the DataFrame
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    # Create histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df[column], bins=bins, color=color, edgecolor=edgecolor)
    
    # Add labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    # Show grid for better readability
    plt.grid(axis='y', alpha=0.75)
    
    # Display the plot
    plt.tight_layout()  # Adjust layout to make room for the labels
    plt.show()
    None

def plot_bar_chart(data, labels, title='Bar Chart', xlabel='Categories', ylabel='Values'):
    """
    Function to plot a bar chart.
    
    :param data: List of values for the bars
    :param labels: List of labels for the categories
    :param title: Title of the chart
    :param xlabel: Label for the X-axis
    :param ylabel: Label for the Y-axis
    """
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, data, color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    
    # Adding the data values on top of the bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()
    None

#print('histogram.py loaded')
#print('__name__ in histogram.py: ', __name__)