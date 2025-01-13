import json
import os.path
import charts
import data
import processing
from flask import Flask, jsonify, send_from_directory, request

app = Flask(__name__)

# Serve static files (index.html, ajax.js, etc.)
@app.route("/")
def index():
    return send_from_directory('client', 'index.html')

@app.route("/ajax.js")
def ajax():
    return send_from_directory('client', 'ajax.js')

# Bar chart endpoint
@app.route("/bar")
def bar_chart():
    bar_data = charts.BarChartData()
    return jsonify(bar_data)

# Pie chart endpoint
@app.route("/pie")
def pie_chart():
    pie_data = charts.PieChartData()
    return jsonify(pie_data)

# Line chart endpoint
@app.route("/line", methods=["POST"])
def line_chart():
    blob = request.data.decode()
    location = json.loads(blob)
    line_data = charts.LineGraphData(location)
    return jsonify(line_data)

# Load data if not already present
def load_data():
    if not os.path.isfile('saved_data.csv'):
        url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
        info = data.json_loader(url)
        heads = ['date', 'location', 'administered_janssen', 'administered_moderna', 'administered_pfizer',
                 'administered_unk_manuf', 'series_complete_pop_pct']
        data.save_data(heads, info, 'saved_data.csv')

# Initialize data loading
load_data()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
