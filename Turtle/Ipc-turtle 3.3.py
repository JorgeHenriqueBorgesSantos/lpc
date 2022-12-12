# Bibliotecas
import turtle


# Função criadora de triângulos
def Triangle_Maker(x_coord, y_coord):

    # Mover a caneta pela tela
    tortoise.penup()
    tortoise.goto(x_coord, y_coord)
    tortoise.pendown()

    # Desenhar o triângulo
    for i in range(3):
        tortoise.fd(100)
        tortoise.lt(120)
        tortoise.fd(100)
        

# Configurações da janela
field = turtle.Screen()
field.bgcolor("#545e69")
field.title("Triangle Maker")

# Configurações da caneta
tortoise = turtle.Turtle()
tortoise.color("#fd5b21")
tortoise.pensize(3)

# Listener para criar o triângulo ao click
turtle.onscreenclick(Triangle_Maker, 1)
turtle.listen()
turtle.done()