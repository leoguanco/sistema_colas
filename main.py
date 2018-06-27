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

    s, lmbda, mu, nq = initial_value()
    system = SystemQueue(s, lmbda, mu, nq)

    while True:
        input_menu = select.select([sys.stdin], [], [], 1)[0]
        if input_menu:
            value = sys.stdin.readline().rstrip()
            if value == 'P':
                pause = True if (pause is False) else False
                if pause:
                    print "En pausa"
            elif value == 'R':
                system = SystemQueue(s, lmbda, mu, nq)
            elif value == 'E':
                sys.exit(0)
            elif value == 'D':
                pause = True
                print "\n Lambda (L)    Mu (M)  Servers (S)   NQ (N)"
                edit = sys.stdin.readline().rstrip()
                if edit == 'L':
                    lmbda = input("Ingrese lambda: ")
                    system.set_status(s, lmbda, mu, nq)
                    pause = False
                elif edit == 'M':
                    mu = input("Ingrese mu: ")
                    system.set_status(s, lmbda, mu, nq)
                    pause = False
                elif edit == 'S':
                    s = input("Ingrese la cant. de servidores: ")
                    system.set_status(s, lmbda, mu, nq)
                    pause = False
                elif edit == 'N':
                    n = input("Ingrese cantidad de clientes nuevos: ")
                    system.set_status(s, lmbda, mu, n)
                    pause = False

        if not pause:
            clear()
            system.iterator()
            system.display()
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