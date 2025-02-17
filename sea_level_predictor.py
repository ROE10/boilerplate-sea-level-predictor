import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Create first line of best fit
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series(range(1880, 2051))
sea_levels_predicted = intercept + slope * years_extended
plt.plot(years_extended, sea_levels_predicted, 'r', label='Fit: 1880-2050')
    # Create second line of best fit
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
sea_levels_predicted_recent = intercept_recent + slope_recent * years_extended
plt.plot(years_extended, sea_levels_predicted_recent, 'green', label='Fit: 2000-2050')

    # Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
