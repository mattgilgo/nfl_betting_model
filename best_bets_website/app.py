from flask import Flask, render_template, jsonify
from best_bets import best_bets

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_picks')
def get_best_bets():
    picks = best_bets()
    return jsonify({"value": picks})

if __name__ == "__main__":
    app.run(debug=True)
