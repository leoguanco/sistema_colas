from system import SystemQueue
from queue import PriorityQueue
from time import sleep


def main():
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


if __name__ == '__main__':
    main()