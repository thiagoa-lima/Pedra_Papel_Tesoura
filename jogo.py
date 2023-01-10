
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

        if escolha == 1:
            print("Você escolheu PEDRA.")
        elif escolha == 2:
            print("Você escolheu PAPEL.")
        elif escolha == 3:
            print("Você escolheou TESOURA.")
        else:
            print("Opção inválida. Vamos começar novamente.")
            continue






if (__name__ == "__main__"):
    play_game()
