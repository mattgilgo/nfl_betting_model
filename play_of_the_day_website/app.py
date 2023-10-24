from flask import Flask, render_template, jsonify
from play_of_the_day import play_of_the_day

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_value')
def get_pick():
    pick, confidence = play_of_the_day(print_play_of_the_day=False)
    return jsonify({"value": pick})

if __name__ == "__main__":
    app.run(debug=True)
