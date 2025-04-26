import random  # Importa o módulo random para gerar números aleatórios

# Gera um número aleatório entre 1 e 100 antes do jogo começar
numero_gerado = random.randint(1, 100)

# O loop 'for' vai se repetir 5 vezes (tente adivinhar até 5 vezes)
for i in range(5):  
    # Solicita ao jogador para digitar um número
    tentativa = int(input("Digite um número: "))

    # Verifica se o número gerado é maior que a tentativa
    if numero_gerado > tentativa:
        print("A sua tentativa é menor que o número gerado.")  # Dica se o número gerado é maior
        
    # Verifica se o número gerado é menor que a tentativa
    elif numero_gerado < tentativa:
        print("A sua tentativa é maior que o número gerado.")  # Dica se o número gerado é menor
    else:
        # Caso o número gerado seja igual à tentativa do jogador
        print("Parabéns! Você acertou o número!")
        break  


# Após as tentativas, ou caso o jogador acerte, o número gerado é mostrado
print(f"O número gerado era: {numero_gerado}")


