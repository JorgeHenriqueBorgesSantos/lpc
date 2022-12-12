#Bibliotca
from turtle import *


speed('fastest')

# Voltar a caneta para cima
rt(-90)

# Definir o angulo de abertura
# tentre os "galhos"
angle = 30

# Montar a função para criar a
# árvore de fractais
def Generate_Fractal(size, level):

	if level > 0:
		colormode(255)
		
		# Divide o espectro verde do RGB em
        # seções para pintar cada nível
		pencolor(0, 255//level, 0)
		
		# Criação da base
		fd(size)
		rt(angle)

		# Geração do lado direito
		Generate_Fractal(0.8 * size, level-1)
		pencolor(0, 255//level, 0)
		lt( 2 * angle )

		# Geração do lado esquerdo
		Generate_Fractal(0.8 * size, level-1)
		pencolor(0, 255//level, 0)
		rt(angle)
		fd(-size)
		
		
# Teste usando size = 80
# e level = 7
Generate_Fractal(80, 7)