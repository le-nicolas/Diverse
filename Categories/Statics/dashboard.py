from flask import Flask, jsonify, render_template
import random
import time

app = Flask(__name__)

# Simulate monitoring data
def get_monitoring_data():
    data = {
        "temperature": random.uniform(20, 30),
        "humidity": random.uniform(40, 60),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return data

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/data')
def data():
    return jsonify(get_monitoring_data())

if __name__ == '__main__':
    app.run(debug=True)
