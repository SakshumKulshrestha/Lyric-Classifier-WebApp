from flask import Flask, render_template
from predictor import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def display():
    return render_template('show_results.html')
    
if __name__ == "__main__":
    app.run(debug=True)