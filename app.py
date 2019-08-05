from flask import Flask, render_template, request
from predictor import predict

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        return render_template('show_results')
    else:
        return render_template('index.html')

@app.route('/results')
def display():
    return render_template('show_results.html')
    
if __name__ == "__main__":
    app.run(debug=True)