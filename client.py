from socket import *
from constCS import *  #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))  # connect to server (block until accepted)


num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
operação = input("Digite a operação (add, subtract, multiply, divide): ")

mensagem = f"{num1} {num2} {operação}"

s.send(str.encode(mensagem))  
data = s.recv(1024)           

print(bytes.decode(data))    
s.close()                     
