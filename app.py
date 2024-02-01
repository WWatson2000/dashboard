from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Load the CSV file into a DataFrame
csv_path = "/Users/charlottewatson/Documents/2023-10-dorset-street.csv"
df = pd.read_csv(csv_path)

@app.route('/')
def index():
    # Create Pie chart for 'Crime type'
    crime_type_chart = px.pie(df, names='Crime type', title='Crime type distribution')

    # Create Pie chart for 'Last Outcome Category'
    outcome_category_chart = px.pie(df, names='Last outcome category', title='Last outcome category distribution')

    # Convert the plots to HTML
    crime_type_chart_html = crime_type_chart.to_html(full_html=False)
    outcome_category_chart_html = outcome_category_chart.to_html(full_html=False)

    return render_template('index.html', crime_type_chart_html=crime_type_chart_html, outcome_category_chart_html=outcome_category_chart_html)

if __name__ == '__main__':
    app.run(debug=True)
