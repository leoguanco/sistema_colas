from system import SystemQueue
from time import sleep
import os
import sys
import select


def main():
    sist = os.name
    pause = False

    if "nt" in sist:
        clear = lambda: os.system('cls')
    elif "posix" in sist:
        clear = lambda: os.system('clear')
    else:
        clear = lambda: os.system('clear')

    serv = input("Ingrese la cant. de servidores en paralelo: ")
    systems = []
    s, lmbda, mu, nq = initial_value()
    pre_s = s
    pre_lmbda = lmbda
    pre_mu = mu
    pre_nq = nq

    for ser in range(0, serv):
        systems.append(SystemQueue(s, lmbda, mu, nq))

    while True:
        input_menu = select.select([sys.stdin], [], [], 1)[0]
        if input_menu:
            value = sys.stdin.readline().rstrip()
            if value == 'P':
                pause = True if (pause is False) else False
                if pause:
                    print "En pausa"
            elif value == 'R':
                for ser in range(0, s):
                    systems.append(SystemQueue(pre_s, pre_lmbda, pre_mu, pre_nq))
            elif value == 'E':
                sys.exit(0)
            elif value == 'D':
                pause = True
                print "\n Lambda (L)    Mu (M)  Servers (S)   NQ (N)"
                edit = sys.stdin.readline().rstrip()
                if edit == 'L':
                    lmbda = input("Ingrese lambda: ")
                    for system in systems:
                        system.set_status(0, lmbda, mu, 0)
                    pause = False
                elif edit == 'M':
                    mu = input("Ingrese mu: ")
                    for system in systems:
                        system.set_status(0, lmbda, mu, 0)
                    pause = False
                elif edit == 'S':
                    s = input("Ingrese la cant. de servidores: ")
                    for system in systems:
                        system.set_status(s, lmbda, mu, 0)
                    pause = False
                elif edit == 'N':
                    n = input("Ingrese cantidad de clientes nuevos: ")
                    for system in systems:
                        system.set_status(0, lmbda, mu, n)
                    pause = False

        if not pause:
            clear()
            for ser in systems:
                ser.iterator()
                ser.display()
            print "\n Pause/Restart (P)    Reset (R)    Exit (E)    Edit (D) "
            # sleep(0.5)


def initial_value():
    s = input("Ingrese la cant. de servidores: ")
    lmbda = input("Ingrese lambda: ")
    mu = input("Ingrese mu: ")
    nq = input("Ingrese cantidad de clientes iniciales: ")
    print "---------------------------------\n"

    return s, lmbda, mu, nq


if __name__ == '__main__':
    main()