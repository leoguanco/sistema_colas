from system import SystemQueue
from time import sleep
import os


def main():
    clear = lambda: os.system('clear')
    s = input("Ingrese la cant. de servidores: ")
    lmbda = input("Ingrese lambda: ")
    mu = input("Ingrese mu: ")
    nq = input("Ingrese cantidad de clientes iniciales: ")

    print "---------------------------------\n"

    system = SystemQueue(s, lmbda, mu, nq)

    while True:
        system.iterator()
        system.display()
        sleep(1)
        clear()


if __name__ == '__main__':
    main()