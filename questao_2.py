# Função 
def contar_a(string):
    contador = 0  # Inicializa o contador
    for letra in string:  # Percorre cada letra da string
        if letra == 'a' or letra == 'A' or letra == 'á' or letra == 'Á' or letra == 'à' or letra == 'À':  # Verificação
            contador += 1  # Se for, incrementa o contador
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vezes.")
    else:
        print("A letra 'a' não aparece na string.")

# Entrada do usuário
texto = input("Digite uma string: ")
contar_a(texto)
