import threading
import subprocess
from multiprocessing import process
import time


def funcao_1():
    while True:
        subprocess.run(["python", "principal.py"])


def funcao_2():
    while True:
        subprocess.run(["python", "canva.py"])


thread_1 = threading.Thread(target=funcao_1)
thread_2 = threading.Thread(target=funcao_2)


thread_1.start()
thread_2.start()

# def funcao_1():
# while True:
#   subprocess.run(["python", "principal.py"])
