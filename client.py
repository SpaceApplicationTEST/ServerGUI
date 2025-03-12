import socket
import tkinter as tk

root = tk.Tk()
root.title("Space")
root.geometry("600x600")

IP = '127.0.0.1'
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
client.settimeout(2)

def Opravka():
    choice = entry_file.get().strip()

    if choice == "+":
        label_think.config(text="Отправляем запрос..")
        client.send('vivod'.encode())
        try:
            response = client.recv(1024).decode()
        except socket.timeout:
            response = "Сервер не отвечает"

        label_result.config(text=f"Ответ сервера: {response}")

    elif choice == "-":
        label_think.config(text="Всего доброго")
        client.close()
        root.after(2000, root.destroy)

    else:
        label_think.config(text="Выберите + или -")
        client.close()

tk.Label(root, text="Вы хотите просмотреть таблицу про космические тела (+) или выйти (-)?: ").pack()
entry_file = tk.Entry(root, width=30)
entry_file.pack()

tk.Button(root, text="Поиск", command=Opravka).pack()

label_think = tk.Label(root, text="")
label_think.pack()

label_result = tk.Label(root, text="", fg="blue")
label_result.pack()

root.mainloop()