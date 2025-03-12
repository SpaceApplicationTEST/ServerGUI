import socket
import pyodbc


server = 'localhost'
database = 'SpaceNotes'
username = ''
password = ''

dsn = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes'

def commands(conn, request):
    try:
        if request.startswith('insert:'):
            data = request[len('insert:'):]
            name, diameter, howfar, type = data.split(',')

            name = name.strip()
            diameter = float(diameter.strip())
            howfar = float(howfar.strip())
            type_ = type.strip()

            conn_db = pyodbc.connect(dsn)
            cursor = conn_db.cursor()

            insert_data = "INSERT INTO [Planets] ([name], [diameter], [howfar], [Type]) VALUES (?, ?, ?, ?)"
            values = (name, diameter, howfar, type_)
            cursor.execute(insert_data, values)
            conn_db.commit()

            result_str = "Data inserted"
            conn.send(result_str.encode())
            cursor.close()
            conn_db.close()