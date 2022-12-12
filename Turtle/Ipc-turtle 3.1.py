#Bibliotecas
import turtle
import math


# Função para calcular a sequência e o gráfico de Fibonacci
def Calc_Fibo_Plot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    # Definindo a cor dos quadrados
    tortoise.color("#3a1b88")

    # Construção dos primeiros quadrados
    for i in range(3):
        tortoise.fd(b * factor)
        tortoise.lt(90)
    tortoise.fd(b * factor)

    # Prosseguindo com a sequência
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Desenhando demais quadrados
    for i in range(1, n):
        tortoise.bk(square_a * factor)
        tortoise.rt(90)
        tortoise.fd(square_b * factor)
        tortoise.lt(90)
        tortoise.fd(square_b * factor)
        tortoise.lt(90)
        tortoise.fd(square_b * factor)

        # Prosseguindo com a sequência
        temp = square_b
        square_b = square_b + square_a
        square_a = temp
    
    # Movendo a caneta para o início da espiral
    tortoise.penup()
    tortoise.setposition(factor, 0)
    tortoise.seth(0)
    tortoise.pendown()

    # Definindo a cor dos quadrados
    tortoise.color("red", "red")

    # Criando a espiral
    tortoise.lt(90)

    # Cálculo da sequência
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor/2
        fdwd /= 90

        for j in range(90):
            tortoise.fd(fdwd)
            tortoise.lt(1)
        
        temp = a
        a = b
        b = temp + b


# O "factor" representa o multiplicador
# que altera a escala do gráfico
factor = 1

# Número de iterações a serem executadas
n = int(input("Digite a quantidade de iterações (deve ser maior que 1): "))

if n > 0:
    print("Calculando a série de Fibonacci para ", n, "elementos.")

    turtle.bgcolor("#545e69")
    turtle.title("Fibonacci Sequence Emulator")

    # Criação da caneta
    tortoise = turtle.Turtle()
    tortoise.speed(120)

    # Ativar função
    Calc_Fibo_Plot(n)
    turtle.done()

else:
    print("Quantidade de iterações deve ser maior que 0")