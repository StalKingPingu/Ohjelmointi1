from flask import Flask, request

app = Flask(__name__)

isprime = False
@app.route('/kenttä')
def kenttä():
    import mysql.connector

    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port='3306',
        database='flight_game',
        user='root',
        password='Blueberry12!',
        autocommit=True
    )



    def haelentoasema(ICAO):
        sql  = "SELECT ident, name, municipality FROM airport WHERE ident='" + ICAO + "'"
        print(sql)
        cursor = yhteys.cursor()
        cursor.execute(sql)
        tulos = cursor.fetchall()
        if cursor.rowcount > 0:
            for rivi in tulos:
                print(f"{rivi[1]}, {rivi[2]}")
        return

    ICAO = request.args
    haelentoasema(ICAO)

    return

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)