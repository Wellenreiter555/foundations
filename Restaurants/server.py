from wsgiref.simple_server import make_server
import sqlite3

db_con = sqlite3.connect("restaurants.db")
db_cursor = db_con.cursor()

PORT = 8000

sql = """SELECT restaurants.ID, restaurants.NAME, neighborhoods.NAME
    FROM restaurants
    INNER JOIN neighborhoods ON restaurants.NEIGHBORHOOD_ID=neighborhoods.ID
    where neighborhoods.NAME = 'Kreuzberg'"""

def get_restaurants():
    db_cursor.execute(sql)
    list_restaurants = db_cursor.fetchall()
    return list_restaurants

def html_code():
    html = "<h1>Restaurants in Kreuzberg</h1>"
    for row in get_restaurants():
        number = row[0]
        name = row[1]
        place = row[2]
        html += f"<li>Restaurant number {number} is called {name} and is in {place}</li>"
        
    return html

def simple_app(_environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/html; charset = utf-8")]

    start_response(status, headers)
    body = [html_code().encode("utf-8")]

    return body

httpd = make_server("localhost", PORT, simple_app)
print("Server runnin on port ", PORT)
httpd.serve_forever()