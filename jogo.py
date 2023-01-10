import time
import random

print("=" * 41)
print("           Pedra Papel Tesoura           ")
print("=" * 41)

jogar_novamente = "S"
pontos_jogador = 0
pontos_computador = 0
while jogar_novamente == "S":

    escolha = 0
    while escolha not in (1, 2, 3):

        print("\nVocê pode escolher:")
        print("[ 1 ] Pedra")
        print("[ 2 ] Papel")
        print("[ 3 ] Tesoura")

        jogador = int(input("\nQual você escolhe? "))

        if jogador not in (1, 2, 3):
            print("Opção inválida. Vamos começar novamente.\n")
            continue

        print("JO...")
        time.sleep(.5)
        print("KEN...")
        time.sleep(.5)
        print("PÔ...")
        time.sleep(.5)
        print("-" * 30)

        if jogador == 1:
            print("Você escolheu PEDRA.")
        elif jogador == 2:
            print("Você escolheu PAPEL.")
        elif jogador == 3:
            print("Você escolheu TESOURA.")

        computador = random.randint(1, 3)
        if computador == 1:
            print(f"Computador escolheu PEDRA.")
        elif computador == 2:
            print("Computador escolheu PAPEL.")
        elif computador == 3:
            print("Computador escolhou TESOURA.")
        print("-" * 30)

        if jogador == computador == jogador:
            print("EMPATOU! NINGUÉM GANHOU!!!")
        elif jogador == 1 and computador == 3:
            print("VOCÊ GANHOU, PARABÉNS!!!")
            pontos_jogador += 1
        elif jogador == 2 and computador == 1:
            print("VOCÊ GANHOU, PARABÉNS!!!")
            pontos_jogador += 1
        elif jogador == 3 and computador == 2:
            print("VOCÊ GANHOU, PARABÉNS!!!")
            pontos_jogador += 1
        else:
            print("VOCÊ PERDEU, QUE PENA!!!")
            pontos_computador += 1

        # imprimir PLACAR

        print("\nPLACAR DO JOGO")
        print(f"VOCÊ [{pontos_jogador}] X [{pontos_computador}] COMPUTADOR")

        break

    jogar_novamente = str(input("\nQuer jogar novamente? [S] para SIM. [N] para NÃO. ").upper())
