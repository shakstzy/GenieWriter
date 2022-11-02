from flask import Flask, jsonify
import actuallyCleaned
app = Flask(__name__)


@app.route('/serve/<artist>/<lyric>')
def hello(artist, lyric):
    return jsonify({'body': list(actuallyCleaned.compute(artist, lyric))})


@app.route('/')
def regg():
    return jsonify({'body': 'Error: Must specify correct route'})


@app.route('/serve/<string:artist>', methods=['GET'])
def reg(artist):
    return jsonify({'body': artist})


if __name__ == '__main__':
    app.run(debug=True)
