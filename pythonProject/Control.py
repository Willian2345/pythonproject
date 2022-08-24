from Model import Model

class Control:

    def __init__(self):
        self.model = Model()
        self.opcao = -1

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("\n\n\nEscolha uma das opções abaixo: \n" +
              "\n0. Sair"                         +
              "\n1. Exercício 01"                 +
              "\n3. Exercício 03"                 +
              "\n5. Exercício 05"                 +
              "\n7. Exercicio 07"                 +
              "\n9. Exercicio 09 "                +
              "\n11. Exercício 11")
        self.setOpcao(int(input()))

    def operacao(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado!")

            elif self.getOpcao() == 1:
                self.model.exercicio1()

            elif self.getOpcao() == 3:
                self.model.exercicio3()

            elif self.getOpcao() == 5:
                i = 0
                for i in range(20):
                    print("Informe o {}º número: ".format(i + 1))
                    self.model.exercicio5(int(input()))

                print("\nCom ordenação!...")
                self.model.ordenar()

            elif self.opcao == 7:
                self.model.exercicio7()

            elif self.opcao == 9:
                i = 0
                for i in range(10):
                    print("Informe o {}º número: ".format(i + 1))

                    self.model.preencherVetor(int(input()))
                self.model.ordenarCrescente()

            elif self.opcao == 11:
                self.model.exercicio11()





