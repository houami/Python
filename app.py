from flask import Flask, render_template, request
import logging, sys
import commands

app = Flask(__name__)
logging.basicConfig(stream=sys.stderr)

@app.route('/')
def root():
    return "Welcome to this web application!"

@app.route('/stats')
def stats():
    logging.error("Sample error message")
    return render_template("app.html.j2", some_message="Hello world")

@app.route('/mstats')
def mstats():
    status, output = commands.getstatusoutput("memcstat --servers=localhost 11211 | grep get_hits")
    return render_template("app.html.j2",some_message1=output)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
