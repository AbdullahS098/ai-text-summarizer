import os
from flask import Flask, render_template, request, jsonify
from summarizer import summarize_text

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        try:
            summary = summarize_text(text)
            return jsonify({'summary': summary})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)