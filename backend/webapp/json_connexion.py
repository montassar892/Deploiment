import json 
import sqlite3 
connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()
traffic  =json.load(open('Result.json'))
cols = ['nom_prenom','email','contact','profil','langues','formation','projects','experience','competences','autres','id']
col = ['name','lastname','email','phonenum','dateofbirth','id']

for row in traffic: 
    keys  = tuple(row[c] for c in columns)
    cursor.execute('insert into Candidat values(?,?,?)',keys)
     