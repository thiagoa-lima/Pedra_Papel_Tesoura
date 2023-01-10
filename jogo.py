import time
def play_game():

    msg_abertura()
    comece_o_jogo()

def msg_abertura():
    print("=" * 41)
    print("           Pedra Papel Tesoura           ")
    print("=" * 41)

def comece_o_jogo():

    escolha = 0

    while escolha not in (1, 2, 3):

        print("\nVocê pode escolher:")
        print("[ 1 ] Pedra")
        print("[ 2 ] Papel")
        print("[ 3 ] Tesoura")

        escolha = int(input("\nQual você escolhe? "))

        if escolha not in (1, 2, 3):
            print("Opção inválida. Vamos começar novamente.")
            continue

        print("JO...")
        time.sleep(.5)
        print("KEN...")
        time.sleep(.5)
        print("PÔ...")
        time.sleep(.5)
        print("-" * 30)

        if escolha == 1:
            print("Você escolheu PEDRA.")
        elif escolha == 2:
            print("Você escolheu PAPEL.")
        elif escolha == 3:
            print("Você escolheou TESOURA.")

        print("-" * 30)





if (__name__ == "__main__"):
    play_game()
