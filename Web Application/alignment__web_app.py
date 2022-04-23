import flask
from flask import Flask, request
from algorithm import needleman_wunsch

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/get_sequences', methods=['GET'])
def get_seqs():
    result, sequence1, sequence2 = "", "", ""
    if request.method == 'GET':
        sequence1 = request.args.get("seq1")
        sequence2 = request.args.get("seq2")
        if sequence1 is None:
            sequence1 = ""
        if sequence2 is None:
            sequence2 = ""
        result = needleman_wunsch(sequence1, sequence2)
    return flask.render_template(
        'get_seqs.html',
        seq1=sequence1,
        seq2=sequence2,
        res=result,
    )


if __name__ == '__main__':
   app.run(debug=True)