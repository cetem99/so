#Problema 1: "Desenvolva um programa que simule a criação de processos e a alocação de recursos em um Sistema Operacional. Cada processo deve requerer recursos específicos, e o programa deve garantir que nenhum processo entre em deadlock."
from threading import Thread
from time import sleep

lista_processos = []
memoria_total = 10
contador = 0


def execute_task():
    for contador in range(5):
        print(f"\n\n\t================OPERATING AT PROCESS TREE:============= =>: {contador}MB/s\n")
        sleep(1)


def repeat(execute_task):
    rodar = Thread(target=execute_task)
    rodar.start()
    rodar.join()


print("\t\t-------------STARTING OPERATION--------------\n")
c = 10
for d in range(c):
    sleep(0.5)
    print("\t-", end='')

while True:
    execute_task()
    memoria_total -= 1
    contador += 1
    if memoria_total == 0:
        print(
            "\n===============================QUANTIDADE DE MEMORIA TOTAL OCUPADA. O SISTEMA IRÁ PARAR AS EXECUÇÕES PARA EVITAR UM DEADLOCK!==============================\n")
        resposta = input("DESEJA INTERROMPER AS EXECUÇÕES? (Yes/No): ")
        if resposta.lower() == 'yes':
            print("\t\t------------SYSTEM INTERRUPTED----------\n")
            break
        else:
            print("\t\t============= [FATAL ERROR] UNEXPECTED CATASTROPHIC FAILURE!!=============\n")
            break