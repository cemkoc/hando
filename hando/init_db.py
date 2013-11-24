import sqlite3
conn = sqlite3.connect('hando.db')
c = conn.cursor()
c.execute("CREATE TABLE hando (username, password, locks)")
c.execute("INSERT INTO hando VALUES ('Smith Lock', 'password', 1)")
conn.commit()
conn.close()