
▼
▼
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = ["date"], parse_dates = True)

# Clean data
df = df[(df["value"]>=df["value"].quantile(0.025)) & (df["value"]<=df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize = (6,6))
    plt.plot( df["value"], "r")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    #plt.show()
        
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
  
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df["month"]=df.index.month
    df["years"]= df.index.year
    df["day"] = df.index.day
    df_bar = df.groupby(["years", "month"])["value"].mean()
    df_bar = df_bar.unstack()
        
    
    # Draw bar plot
    #fig = plt.figure(figsize = (10,5))
    #df_bar.plt.bar()
    fig =  df_bar.plot.bar().figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    plt.legend( title ="Months", labels = Months)
    #plt.show()
    
    # Save image and return fig (don't change this part)
    #fig.savefig('bar_plot.png')
    return fig
  
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    # Draw box plots (using Seaborn)
    df_box["month_no"] = df_box['date'].dt.month
    df_box = df_box.sort_values("month_no")
    fig, (ax1,ax2) = plt.subplots(1,2, figsize=(12,5))
    ax1 = sns.boxplot(ax = ax1, data=df_box, x=df_box["year"], y=df_box["value"])
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set(xlabel="Year", ylabel = "Page Views")
    ax2 = sns.boxplot(ax = ax2, data=df_box, x=df_box["month"], y=df_box["value"])
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set(xlabel="Month", ylabel = "Page Views")
    #plt.show()
        
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig