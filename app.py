# importar o modulo random
import random

options = ["pedra", "papel", "tesoura"] # lista de opções
score = 0
rounds_played = 0

while True:
    random_choice = random.choice(options) # escolher uma opção aleatória
    player_choice = input("Escolha pedra, papel ou tesoura: ") # pedir ao jogador para escolher uma opção

    # se o meu jogador escolher pedra
    if player_choice == "pedra":
        rounds_played += 1
        if random_choice == "pedra":
            print("Empate!")
        elif random_choice == "papel":
            print("Você perdeu!")
        else:
            print("Você ganhou!")
            score += 1
    
    # se o meu jogador escolher papel
    elif player_choice == "papel":
        rounds_played += 1
        if random_choice == "papel":
            print("Empate!")
        elif random_choice == "tesoura":
            print("Você perdeu!")
        else:
            print("Você ganhou!")
            score += 1

    # se o meu jogador escolher tesoura
    elif player_choice == "tesoura":
        rounds_played += 1
        if random_choice == "tesoura":
            print("Empate!")
        elif random_choice == "pedra":
            print("Você perdeu!")
        else:
            print("Você ganhou!")
            score += 1

    # se o jogador escolher algo diferente de pedra, papel ou tesoura
    else:
        play_again = input("Escolha inválida! Deseja jogar novamente? (s/n): ")
        if play_again == "s":
            continue
        elif play_again == "n":
            if score == 1:
                print(f"Você ganhou {score} rodada!", rounds_played, " rodadas jogadas.")
            break
        else:
            print("Escolha inválida!")  
            

