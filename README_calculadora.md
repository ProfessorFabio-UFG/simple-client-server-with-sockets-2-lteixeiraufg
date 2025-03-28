# Sistema de Calculadora Remota

O servidor agora tem uma funcionalidade de calculadora remota, onde o cliente envia dois números e uma operação matemática (como soma, subtração, multiplicação ou divisão) e o servidor retorna o resultado da operação.

## Como usar

1. Execute o `server.py`.
2. Em outra janela do terminal, execute o `client.py`.

O cliente irá solicitar ao usuário os dois números e a operação desejada, e enviará esses dados para o servidor. O servidor então responderá com o resultado da operação ou, no caso de erro, retornará uma mensagem de erro.

## EXEMPLO

**Cliente:**

Digite o primeiro número: 5
Digite o segundo número: 3
Digite a operação (add, subtract, multiply, divide): add


**Resposta do servidor**

O resultado de 5.0 add 3.0 é: 8.0
