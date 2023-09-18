import mysql.connector
import geopy.distance
from geopy import distance

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='root',
    password='Blueberry12!',
    autocommit=True
    )
def lentoasemakoordinaatit(ICAO, ICAO2):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident='" + ICAO + "' OR ident='" + ICAO2 + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    print(f"{distance.distance(tulos[0], tulos[1]).km} kilometriä")
    return

ICAO = input('anna ICAO koodi')
ICAO2 = input('anna toisen lentoaseman ICAO koodi')
lentoasemakoordinaatit(ICAO,ICAO2)
