import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, organization, analit, genome, samples, mode, genes, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('Design ID-1', 'Organization', 'Analit', 'Genome', "Samples", "Mode", "Genes", "Comment")
            )

cur.execute("INSERT INTO posts (title, organization, analit, genome, samples, mode, genes, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('Design ID-2', 'Organization', 'Analit', 'Genome', "Samples", "Mode", "Genes", "Comment")
            )

connection.commit()
connection.close()