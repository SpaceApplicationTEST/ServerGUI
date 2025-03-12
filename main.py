import socket
import pyodbc


server = 'localhost'
database = 'SpaceNotes'
username = ''
password = ''

dsn = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes'

def insert_info():
    try:
        choice = input("want to add?:  ")
        if choice == "da":
            name = input("Enter name: ")
            diameter = float(input("Enter diameter: "))
            howfar = float(input("Enter the distance from Earth: "))
            type = input("Enter type: ")

            conn_db = pyodbc.connect(dsn)
            cursor = conn_db.cursor()

            insert_data = """
                INSERT INTO [Planets] ([name], [diameter], [howfar], [Type]) 
                VALUES (?, ?, ?, ?)
            """

            values = (name, diameter, howfar, type)
            cursor.execute(insert_data, values)
            conn_db.commit()

            print("Data inserted")
            cursor.close()
            conn_db.close()
        else:
            print("tormozim")
            return True


    except Exception as e:
        print(f"Error: {e}")

def commands(conn, request):
    try:
        if request == 'vivod':
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


IP = '127.0.0.1'
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(2)
print(f"Подключен на {IP}:{PORT}")

insert_info()

try:
    while True:
        conn, addr = server.accept()
        print(f"Подключение от {addr}")
        if insert_info():
            try:
                data = conn.recv(1024).decode()
                if data:
                    print(f"Получен запрос: {data}")
                    commands(conn, data)
            except Exception as e:
                print(f"Error: {e}")
            finally:
                conn.close()
        else:
            break
except KeyboardInterrupt:
    print("\nServer stopped")
finally:
    server.close()