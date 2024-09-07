# Função simples para verificar se um número está na sequência de Fibonacci
def fibonacci_seq(num):
    a, b = 0, 1  # Iniciando a sequência com os dois primeiros números
    while a < num:  # Enquanto 'a' for menor que o número informado
        a, b = b, a + b  # Atualiza os valores de 'a' e 'b'
    if a == num:  # Se 'a' for igual ao número, ele pertence à sequência
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")

# Entrada do usuário
n = int(input("Digite um número: "))
fibonacci_seq(n)
