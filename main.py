import glfw
from OpenGL.GL import *
import numpy as np

# Variáveis globais para a posição do triângulo
position_x = 0.0
position_y = 0.0

# Função de callback para capturar teclas
def key_callback(window, key, scancode, action, mods):
    global position_x, position_y

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP and position_y < 0.5 :
            position_y += 0.1
        elif key == glfw.KEY_DOWN and position_y > -0.5:
            position_y -= 0.1
        elif key == glfw.KEY_LEFT and position_x > -0.5:
            position_x -= 0.1
        elif key == glfw.KEY_RIGHT and position_x < 0.5:
            position_x += 0.1

# Inicializa a janela usando GLFW
if not glfw.init():
    raise Exception("GLFW não pôde ser inicializado")

window = glfw.create_window(800, 600, "Movendo um Triângulo", None, None)

if not window:
    glfw.terminate()
    raise Exception("A janela não pôde ser criada")

glfw.make_context_current(window)
glfw.set_key_callback(window, key_callback)

# Configura o viewport
glViewport(0, 0, 800, 600)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-1, 1, -1, 1, -1, 1)  # Definindo o espaço de coordenadas ortográficas

# Loop principal
while not glfw.window_should_close(window):
    # Limpa a tela
    glClear(GL_COLOR_BUFFER_BIT)

    # Desenha o triângulo na posição atual
    glPushMatrix()
    glTranslatef(position_x, position_y, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 0.5)
    glEnd()
    glPopMatrix()

    # Troca o buffer de exibição
    glfw.swap_buffers(window)

    # Processa eventos de input
    glfw.poll_events()

# Finaliza o GLFW
glfw.terminate()
