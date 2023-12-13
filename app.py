from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    print(request.query_string)

    color = 'black'
    if 'color' in request.args:
        color = request.args['color']

    style = 'normal'
    if 'style' in request.args:
        style = request.args['style']

    for p in request.args:
        print(p, request.args[p])

    return f'<h1 style="color: {color};font-style: {style};">Hello World!!<h1>'


# dynamiczny routing
@app.route('/cantor/<currency>/<int:amount>')
def cantor(currency, amount):
    message = f"<h1>You selected {currency} and amount {amount}<h1>"
    return message


@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    if request.method == 'GET':
        body = '''
        <form id="exchange_form" action="/exchange" method="POST">
            <label for="currency">Currency</label>
            <input type="text" id="currency" name="currency" value="EUR"><br>
            <label for="amount">Amount</label>
            <input type="text" id="amount" name="amount" value="100"><br>
            <input type="submit" value="Send">
        </form>
        '''
        return body
    else:
        currency = 'EUR'
        if 'currency' in request.form:
            currency = request.form['currency']

        amount = 100
        if 'amount' in request.form:
            amount = request.form['amount']

        body = f"You want to exchange {amount} {currency}"

        return body


@app.route('/exchange_process', methods=['POST'])
def exchange_process():
    currency = 'EUR'
    if 'currency' in request.form:
        currency = request.form['currency']

    amount = 100
    if 'amount' in request.form:
        amount = request.form['amount']

    body = f"You want to exchange {amount} {currency}"

    return body


@app.route('/about')
def about():
    a = 10
    b = 1
    return f"<h1>We are programmers {a / b}<h1>"


if __name__ == '__main__':
    # app.run(debug=True, port=8080)
    app.run(debug=True)
