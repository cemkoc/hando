import sqlite3
conn = sqlite3.connect('hando.db')
c = conn.cursor()
c.execute("CREATE TABLE hando (username, password)")
conn.commit()
conn.close()
