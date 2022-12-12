# Bibliotecas
import turtle
import random


# Configurção da janela
field = turtle.Screen()
field.bgcolor("#0e67ec")
field.title("Turtle Runners")

# Configurações do Player 1
player_1 = turtle.Turtle()
player_1.color("#70de02", "#da10f9")
player_1.shape("turtle")
player_1.pensize(2)
player_1.penup()
player_1.goto(-200, 100)

# Configurações do Player 2
player_2 = player_1.clone()
player_2.color("#f9fd1c", "#7c3803")
player_2.penup()
player_2.goto(-200, -100)

# Definição das linhas de chegadas
player_1.goto(300, 60)
player_1.pendown()
player_1.circle(40)
player_1.penup()
player_1.goto(-200, 100)

player_2.goto(300, -140)
player_2.pendown()
player_2.circle(40)
player_2.penup()
player_2.goto(-200, -100)

# Configuração do Dado
die = [1, 2, 3, 4, 5, 6]

for i in range(20):

    # Analíse de vitória
    if player_1.pos() >= (300, 100):
        print("Player One Wins!")
        break

    elif player_2.pos() >= (300, -100):
        print("Player Two Wins!")
        break
    
    else:

        # Turno do Player 1
        player_1_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ", die_outcome)
        print("The number of steps will be: ", 20 * die_outcome)
        player_1.fd(20 * die_outcome)

        # Turno do Player 2
        player_2_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ", die_outcome)
        print("The number of steps will be: ", 20 * die_outcome)
        player_2.fd(20 * die_outcome)