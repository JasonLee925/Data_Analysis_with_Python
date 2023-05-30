import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']

  # Create scatter plot
  plt.scatter(x=x, y=y)

  # Create first line of best fit
  ret = linregress(x, y)
  x_pd1 = np.arange(x.min(), 2050)
  plt.plot(x_pd1, ret.intercept + ret.slope*x_pd1, color='r') # intercept: value which intersacts with y-axis; slope: steepness
  # https://support.minitab.com/en-us/minitab/21/help-and-how-to/statistical-modeling/regression/supporting-topics/basics/slope-and-intercept-of-the-regression-line/#:~:text=The%20slope%20indicates%20the%20steepness,an%20average%20rate%20of%20change.

  # Create second line of best fit
  df_2000 = df[df['Year'] >= 2000]
  ret = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
  x_pd2 = np.arange(2000, 2050)
  plt.plot(x_pd2, ret.intercept + ret.slope*x_pd2, color='g')
  
  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
