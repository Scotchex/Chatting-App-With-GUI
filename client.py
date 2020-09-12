import tkinter as tk
from threading import Thread
from socket import AF_INET, socket, SOCK_STREAM



def receive():
    while True:
        try :
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tk.END, msg)
        except OSError:
            break

def send(even=None):
    msg = my_msg.get()
    my_msg.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "quit":
        client_socket.close()
        top.quit()

def on_closing(event=None):
    my_msg.set("quit")
    send()

top = tk.Tk()
top.title('Client')

top.geometry('300x400')

my_msg = tk.StringVar()
msg_list = tk.Listbox(top)
msg_list.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)
entry = tk.Entry(top, textvariable = my_msg)
entry.bind("<Return>", send)
entry.pack(padx=10,pady=10,fill=tk.BOTH,expand=False)
button = tk.Button(top, text = "Send", command = send)
button.pack(padx=5,pady=3,fill=tk.BOTH,expand=False)

#CANCER STARTS#

HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()





tk.mainloop()
