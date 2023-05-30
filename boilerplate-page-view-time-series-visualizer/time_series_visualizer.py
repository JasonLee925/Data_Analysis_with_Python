import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import calendar

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0, parse_dates=True)

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025))
        & (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
  # Draw line plot
  # The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019.
  # The label on the x axis should be Date and the label on the y axis should be Page Views.
  fig = df.plot(figsize=(12, 6),
                title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
                xlabel="Date",
                ylabel="Page Views").get_figure()

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar = df.groupby([df.index.year, df.index.month]) \
                                    .mean() \
                                    .reset_index(level=1) \
                                    .rename(columns={"date": "month"}) \
                                    .reset_index() \
                                    .rename(columns={"date": "year"})

  df_bar['month'] = df_bar['month'].apply(lambda x: calendar.month_name[x])

  # Draw bar plot
  fig = plt.figure(figsize=(8, 8))

  sns.barplot(data=df_bar,
                    x="year",
                    y="value",
                    hue="month",
                    hue_order=calendar.month_name[1:],
                    palette="tab10",
                    ec="grey",
             )
  
  # fig = sns.catplot(data=df_bar,
  #                   x="year",
  #                   y="value",
  #                   hue="month",
  #                   hue_order=calendar.month_name[1:],
  #                   palette="tab10",
  #                   ec="grey",
  #                   kind="bar",
  #                   height=8)

  # #https://seaborn.pydata.org/generated/seaborn.move_legend.html
  # sns.move_legend(fig,
  #                 "upper left",
  #                 bbox_to_anchor=(.15, 0.95),
  #                 title='Months',
  #                 frameon=True)
  # fig.set(xlabel="Years", ylabel="Average Page Views")

  plt.xlabel('Years')
  plt.ylabel('Average Page Views')
  plt.legend(title='Months', loc='upper left')

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(24, 10))
  sns.boxplot(
    data=df_box,
    ax=ax1,
    x="year",
    y="value",
  )

  sns.boxplot(
    data=df_box,
    ax=ax2,
    x="month",
    y="value",
    order=calendar.month_abbr[1:],
  )

  ax1.set(xlabel='Year',
          ylabel='Page Views',
          title='Year-wise Box Plot (Trend)')
  ax2.set(xlabel='Month',
          ylabel='Page Views',
          title='Month-wise Box Plot (Seasonality)')

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
