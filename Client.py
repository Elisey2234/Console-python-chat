import time, socket, sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

print('IP вашего компьютера: ',ip)
server_host = input('Вветите IP адресс друга: ')
name = input('Введите имя: ')


socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name,' зашёл в чат.')
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Я : ")
    socket_server.send(message.encode())  
