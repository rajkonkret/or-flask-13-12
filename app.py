from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World!!<h1>"


# dynamiczny routing
@app.route('/cantor/<currency>/<int:amount>')
def cantor(currency, amount):
    message = f"<h1>You selected {currency} and amount {amount}<h1>"
    return message


@app.route('/about')
def about():
    a = 10
    b = 1
    return f"<h1>We are programmers {a / b}<h1>"


if __name__ == '__main__':
    # app.run(debug=True, port=8080)
    app.run(debug=True)
