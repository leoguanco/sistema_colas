from system import SystemQueue
from time import sleep
import os


def main():
    sist = os.name
    if "nt" in sist:
        clear = lambda: os.system('cls')
    elif "posix" in sist:
        clear = lambda: os.system('clear')
    else:
        clear = lambda: os.system('clear')

    s = input("Ingrese la cant. de servidores: ")
    lmbda = input("Ingrese lambda: ")
    mu = input("Ingrese mu: ")
    nq = input("Ingrese cantidad de clientes iniciales: ")

    print "---------------------------------\n"

    system = SystemQueue(s, lmbda, mu, nq)

    while True:
        clear()
        system.iterator()
        system.display()
        sleep(1)


if __name__ == '__main__':
    main()