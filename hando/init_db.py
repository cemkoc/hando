import sqlite3
from flask import Flask, g

conn = sqlite3.connect('hando.db')
c = conn.cursor()
c.execute("CREATE TABLE hando (username, password)")
conn.commit()
conn.close()
