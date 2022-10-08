#Настройки
import time, socket, sys
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080
new_socket.bind((host_name, port))
#Настройки пользователя
print( "Начинаем общение")
print("IP вашего компьютера: ", s_ip)

name = input('Введите имя: ')

new_socket.listen(1) 

conn, add = new_socket.accept()

print("Соендинение установленно c ", add[0])
print('Подключено от: ',add[0])

client = (conn.recv(1024)).decode()
print(client + ' подключён.')
conn.send(name.encode())
#Продолжение общения
while True:
    message = input('Я : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
