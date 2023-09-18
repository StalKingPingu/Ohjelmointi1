import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='root',
    password='Blueberry12!',
    autocommit=True
    )
def asemienmaara(maakoodi):
    sql = "SELECT COUNT(type), type FROM airport WHERE iso_country='" + maakoodi + "' GROUP BY type"
    print(sql),
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    if cursor.rowcount >0:
        for rivi in tulos:
            print(rivi)
    return

maakoodi = input('anna maakoodi')
asemienmaara(maakoodi)