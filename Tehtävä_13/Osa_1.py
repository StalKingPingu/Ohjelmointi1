from flask import Flask, request

app = Flask(__name__)

isprime = False
@app.route('/alkuluku')
def alkuluku():
    args = request.args
    luku = int(args.get("luku"))

    for i in range(2, luku):

        if (luku % i) == 0:
            isprime = False
            break
    else:
        isprime = True

    vastaus = {
        "Number" : luku,
        "isPrime" : isprime
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)