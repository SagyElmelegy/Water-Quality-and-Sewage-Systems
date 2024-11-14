import pandas as pd

#Load dataset
df = pd.read_csv('water quality and sewage system.csv')
df.head()

#Cleaning the data

#Dropping rows with missing values
df.dropna(inplace=True)

#Converting relevant columns to appropriate data types if needed
df['Sampling Date'] = pd.to_datetime(df['Sampling Date'])
df['Sampling Date'] = df['Sampling Date'].dt.year

#Checking for duplicates and removing them
df.drop_duplicates(inplace=True)

#Displaying a sample of the cleaned dataset
df.head()

#Answering some Explanatory Data Analysis questions

#Statistical Analysis Questions

# 1.What is the average nitrogen concentration (mg/L) across all samples?
average_nitrogen = df['Nitrogen (mg/L)'].mean()
print("Average Nitrogen Concentration (mg/L):", average_nitrogen)

# 2.What is the standard deviation of phosphorus levels in regions with a “Good” sewage system condition?
good_sewage_condition = df[df['State of Sewage System'] == 'Good']
std_phosphorus_good = good_sewage_condition['Phosphorus (mg/L)'].std()
print("Standard Deviation of Phosphorus in 'Good' Sewage System Condition:", std_phosphorus_good)

#Conditional Filtering Questions

# 3.How many samples show a nitrogen level above 7 mg/L and a phosphorus level above 2 mg/L?
filtered_samples = df[(df['Nitrogen (mg/L)'] > 7) & (df['Phosphorus (mg/L)'] > 2)]
num_filtered_samples = filtered_samples.shape[0]
print("Number of samples with nitrogen > 7 mg/L and phosphorus > 2 mg/L:", num_filtered_samples)

# 4.How many samples taken in 2022 have a sewage system condition labeled as “Moderate”?
moderate_sewage_2022 = df[(df['Sampling Date'] == 2022) & (df['State of Sewage System'] == 'Moderate')]
num_moderate_2022 = moderate_sewage_2022.shape[0]
print("Number of samples in 2022 with 'Moderate' sewage system condition:", num_moderate_2022)

#Grouping Data Questions

# 5.What is the average nitrogen concentration for each sewage system condition category (e.g., "Good," "Moderate")?
avg_nitrogen_by_condition = df.groupby('State of Sewage System')['Nitrogen (mg/L)'].mean()
print("Average Nitrogen Concentration by Sewage System Condition:")
print(avg_nitrogen_by_condition)

# 6.For each year, what is the average phosphorus level in areas with a “Good” sewage system condition?
good_sewage_condition = df[df['State of Sewage System'] == 'Good']
good_sewage_by_year = good_sewage_condition.groupby('Sampling Date')['Phosphorus (mg/L)'].mean()
print("Average Phosphorus Level in 'Good' Sewage System Condition by Year:")
print(good_sewage_by_year)

#Sorting Data Question
top_10_locations_nitrogen = df[['Location', 'Nitrogen (mg/L)']].sort_values(by='Nitrogen (mg/L)', ascending=False).head(10)
print("Top 10 Locations with Highest Nitrogen Concentration Levels:")
print(top_10_locations_nitrogen)

#Combination Question
top_5_regions_nitrogen = df.groupby('Location')['Nitrogen (mg/L)'].mean().sort_values(ascending=False).head(5).index
top_5_samples = df[df['Location'].isin(top_5_regions_nitrogen)]
average_phosphorus_top_5 = top_5_samples['Phosphorus (mg/L)'].mean()
print("Average Phosphorus Concentration in Top 5 Regions with Highest Average Nitrogen Levels:", average_phosphorus_top_5)

#Visualizations

# 1.Calculating and visualizing the average phosphorus level by sewage system condition
avg_phosphorus_by_condition = df.groupby('State of Sewage System')['Phosphorus (mg/L)'].mean()

print("Average Phosphorus Level by Sewage System Condition:")
print(avg_phosphorus_by_condition)

avg_phosphorus_by_condition.plot(kind='bar', color='lightgreen')
plt.title('Average Phosphorus Level by Sewage System Condition')
plt.xlabel('Sewage System Condition')
plt.ylabel('Average Phosphorus (mg/L)')
plt.show()

# 2.Visualizing the rate of change of nitrogen and phosphorus levels over time
avg_nitrogen_by_year = df.groupby('Sampling Date')['Nitrogen (mg/L)'].mean()
avg_phosphorus_by_year = df.groupby('Sampling Date')['Phosphorus (mg/L)'].mean()

plt.plot(avg_nitrogen_by_year, label='Average Nitrogen Level', marker='o')
plt.plot(avg_phosphorus_by_year, label='Average Phosphorus Level', marker='x')
plt.title('Trends in Nitrogen and Phosphorus Levels Across the Years')
plt.xlabel('Year')
plt.ylabel('Concentration (mg/L)')
plt.legend()
plt.show()