from flask import Flask, render_template, request
from predictor import predictor as pred

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        lyrics = request.form['song_text']
        lyrics = str(lyrics)
        result_string, results_probability = pred.predict(lyrics)
        return render_template('show_results.html', result_string=result_string, result_probability=results_probability)
    
    else:
        return render_template('index.html')

@app.route('/results')
def display():
    return render_template('show_results.html')
    
if __name__ == "__main__":
    app.run(debug=True)