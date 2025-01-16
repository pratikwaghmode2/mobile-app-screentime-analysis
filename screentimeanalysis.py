import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('screentime_analysis.csv')

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Grouped summary statistics for apps
usage_summary = data.groupby('App').agg(
    total_usage=('Usage (minutes)', 'sum'),
    avg_usage=('Usage (minutes)', 'mean'),
    total_notifications=('Notifications', 'sum'),
    total_times_opened=('Times Opened', 'sum')
).sort_values('total_usage', ascending=False)

# Display summary statistics
print("Usage Summary by App:")
print(usage_summary)

# Top 5 apps by total usage
top_apps = usage_summary.head(5)

# Bar plot: Total usage by top 5 apps
plt.figure(figsize=(10, 6))
sns.barplot(x=top_apps.index, y=top_apps['total_usage'], palette='viridis')
plt.title('Top 5 Apps by Total Usage (Minutes)', fontsize=14)
plt.ylabel('Total Usage (Minutes)', fontsize=12)
plt.xlabel('App', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Daily total usage trend
daily_usage = data.groupby('Date')['Usage (minutes)'].sum().reset_index()

# Line plot: Overall app usage trend over time
plt.figure(figsize=(12, 6))
plt.plot(daily_usage['Date'], daily_usage['Usage (minutes)'], marker='o', linestyle='-', color='b')
plt.title('Daily Total App Usage Trend', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Usage (Minutes)', fontsize=12)
plt.grid(True)
plt.show()

# Correlation analysis
correlation_matrix = data[['Usage (minutes)', 'Notifications', 'Times Opened']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Heatmap for correlations
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap', fontsize=14)
plt.show()

# Distribution of usage times by app
plt.figure(figsize=(12, 6))
sns.boxplot(x='App', y='Usage (minutes)', data=data, palette='Set2')
plt.title('Distribution of Usage Times by App', fontsize=14)
plt.ylabel('Usage (Minutes)', fontsize=12)
plt.xlabel('App', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Notifications vs. Times Opened scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Notifications', y='Times Opened', hue='App', data=data, palette='tab10', s=100)
plt.title('Notifications vs. Times Opened', fontsize=14)
plt.xlabel('Notifications', fontsize=12)
plt.ylabel('Times Opened', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()
