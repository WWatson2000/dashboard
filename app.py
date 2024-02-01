from flask import Flask, render_template
import pandas as pd
import logging
import plotly.express as px

app = Flask(__name__)

# Setup logging to assist with debugging and monitoring
logging.basicConfig(filename="app.log", level=logging.DEBUG)

# Load the CSV file into a DataFrame
csv_path = "/Users/charlottewatson/Documents/2023-10-dorset-street.csv"
df = pd.read_csv(csv_path)

@app.route('/')
def index():
    # Create Pie chart for 'Crime type'
    crime_type_chart = px.pie(df, names='Crime type', title='Crime Type Distribution')

    # Create Pie chart for 'Last Outcome Category'
    outcome_category_chart = px.pie(df, names='Last outcome category', title='Last Outcome Category Distribution')

    # Create Bubble chart for the relationship between 'Crime type' and 'Location'
    bubble_chart_df = df.groupby(['Location', 'Crime type']).size().reset_index(name='Count')
    bubble_chart = px.scatter(bubble_chart_df, x='Location', y='Crime type', size='Count',
                               title='Relationship between Crime Type and Location',
                               labels={'Count': 'Number of Crimes'})

    # Convert the plots to HTML
    crime_type_chart_html = crime_type_chart.to_html(full_html=False)
    outcome_category_chart_html = outcome_category_chart.to_html(full_html=False)
    bubble_chart_html = bubble_chart.to_html(full_html=False)

    return render_template('index.html', crime_type_chart_html=crime_type_chart_html,
                           outcome_category_chart_html=outcome_category_chart_html,
                           bubble_chart_html=bubble_chart_html)

if __name__ == '__main__':
    app.run(debug=True)
