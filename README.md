# mobile-app-screentime-analysis
A Python project for analyzing  mobile app screen time data with visualizations
# Mobile App Screen Time Analysis

## Project Description
This project analyzes mobile app screen time data to provide insights into user behavior. It uses Python for data analysis and visualization, showcasing patterns such as total usage, notifications received, and app usage trends over time. The dataset includes information on app usage (in minutes), notifications, and times opened for various mobile applications.

## Features
- **Exploratory Data Analysis (EDA):**
  - Summarizes app usage statistics (total usage, average usage, etc.).
  - Identifies the most and least used apps.
- **Visualizations:**
  - Bar chart for top 5 apps by usage.
  - Line plot showing daily usage trends.
  - Correlation heatmap between notifications, times opened, and usage.
  - Distribution of usage times by app.
  - Scatter plot of notifications vs. times opened.

## Technologies Used
- **Python Libraries:**
  - `pandas` for data manipulation.
  - `matplotlib` and `seaborn` for visualizations.

## Dataset
The dataset contains the following columns:
- `Date`: Date of app usage.
- `App`: Name of the app.
- `Usage (minutes)`: Time spent on the app (in minutes).
- `Notifications`: Number of notifications received from the app.
- `Times Opened`: Number of times the app was opened.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mobile-app-screentime-analysis.git
   cd mobile-app-screentime-analysis
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis script:
   ```bash
   python analysis.py
   ```

4. Explore the visualizations and results.

## Visualizations
The project generates various visualizations, including:
- Top 5 apps by total usage.
- Daily total app usage trends.
- Correlation heatmap.
- Usage time distribution by app.
- Scatter plot of notifications vs. times opened.

## Insights
Some key insights you can uncover:
- Which apps are used the most or least.
- How notifications and times opened correlate with app usage.
- Daily usage trends over time.

## Future Enhancements
- Add interactive dashboards using tools like Plotly or Dash.
- Extend the dataset to include more detailed user behavior metrics.
- Perform predictive analysis to estimate future usage patterns.

## Author
[Pratik](https://github.com/pratikwaghmode2)

