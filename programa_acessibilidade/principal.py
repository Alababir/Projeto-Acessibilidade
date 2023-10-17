import pyautogui
import winsound
import keyboard
from tkinter import *

#distância da borda ai ó
distancia_limite = 90


som_path = 'audio_alerta.wav' #som aqui ó
winsound.SND_ASYNC = winsound.SND_FILENAME

def reproduzir_som():
    winsound.PlaySound(som_path, winsound.SND_ASYNC)

def main():
    exit_key = 'esc'  # Tecla fecha tudo

    while True:
        x, y = pyautogui.position()
        largura_tela, altura_tela = pyautogui.size()

        if x < distancia_limite or x > largura_tela - distancia_limite or \
           y < distancia_limite or y > altura_tela - distancia_limite:
            reproduzir_som()

        # Vê se o q foi pressionado
        if keyboard.is_pressed(exit_key):
            print("Encerrando o programa.")
            break  # Sai do loop




if __name__ == "__main__":
    main()
