from flask import Flask, make_response, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template('index.html')

@app.route('/transform', methods=["POST"])
def show():
    df = pd.read_csv(request.files.get('data_file'), encoding = "ISO-8859-1")

   # result = df.to_html()
    result = df.to_json(orient='index')

    return render_template('show.html', data=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)