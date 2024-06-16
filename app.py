# crear un minijuego de piedra papel o tijera
# La persona elige su jugada escribiendo la palabra
# La máquina elige aleatoriamente su jugada
# siempre luego de cada turno se debe decir si se gano, perdió o empató y después se pregunta si se quiere continuar o no
# al final se muestra el puntaje total de la partida
import random

def play_game():

    choices = ["piedra", "papel", "tijera"]
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Elige tu jugada (piedra, papel, tijera): ")
        computer_choice = random.choice(choices)

        print(f"Tu jugada: {player_choice}")
        print(f"Jugada de la máquina: {computer_choice}")

        if player_choice == computer_choice:
            print("Empate!")
        elif (
            (player_choice == "piedra" and computer_choice == "tijera")
            or (player_choice == "papel" and computer_choice == "piedra")
            or (player_choice == "tijera" and computer_choice == "papel")
        ):
            print("¡Ganaste!")
            player_score += 1
        else:
            print("Perdiste :(")
            computer_score += 1

        play_again = input("¿Quieres continuar? (s/n): ")
        if play_again.lower() != "s":
            break

    print(f"Puntaje total: Jugador {player_score} - Máquina {computer_score}")

play_game()