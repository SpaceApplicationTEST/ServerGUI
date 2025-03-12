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

        elif request == 'vivod':
          with pyodbc.connect(dsn) as conn_db:
            cursor = conn_db.cursor()
            cursor.execute("SELECT * FROM [Planets]")
            rows = cursor.fetchall()

            result_str = ""
            for row in rows:
              result_str += f"\nID:{row[0]} Name: {row[1]}, Diameter: {row[2]}, How far from Earth: {row[3]}, Type: {row[4]}"

            conn.send(result_str.encode())

        else:
            conn.send("Error".encode())

    except Exception as e:
        print(f"Error: {e}")
        conn.send(f"Error: {e}".encode())