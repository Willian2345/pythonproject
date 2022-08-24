class Model:


    def __init__(self):
        self.vetor  = []

    def exercicio1(self):
        nota = []
        media = 0
        soma = 0
        maior = 0
        for i in range(20):
            print("Informe a nota do {}° aluno:".format(i + 1))
            num = float(input())

            while num < 0 or num > 10:
                if num < 0 or num > 10:
                    print("Valor inválido.")
                    print("Informe a nota do {}° aluno:".format(i + 1))
                    num = float(input())

            nota.append(num)
            soma = soma + num
        media = soma / 20
        for i in range(20):
            if nota[i] > media:
                maior = maior + 1
        print("A média da turma é: {}\nO total de alunos acima da média é: {}.".format(media, maior))

    def exercicio3(self):
        q = []
        menor = 0
        posicao = 0
        for i in range(3):
            print("Informe o {}° número:".format(i + 1))
            num = int(input())
            while num < 0:
                if num < 0:
                    print("Valor inválido.")
                    print("Informe o {}° número:".format(i + 1))
                    num = int(input())
            if i == 0:
                menor = num
                posicao = i + 1
            else:
                if num < menor:
                    menor = num
                    posicao = i + 1
            q.append(num)
        print("A menor valor é: {}\nSua posição é: {})".format(menor, posicao))

    def exercicio5(self, num):

         self.vetor.append(num)  # Incluindo dados no vetor


    def visualizarVetor(self):
        for i in range(len(self.vetor)):
            print("{}º número: {}\n".format(i+1,self.vetor[i]))

    def preencherVetor(self, num):
        self.vetor.append(num)  # Incluindo dados no vetor


    def ordenar(self):
        self.vetor.sort(reverse=True)
        self.visualizarVetor()


    def exercicio7(self):
        temperatura = []
        media = 0
        soma = 0
        maior = 0
        abaixomedia = 0
        menor = 0
        for i in range(365):
            print("Informe a temperatura do dia {}° ".format(i + 1))
            num = float(input())

            temperatura.append(num)
            soma = soma + num
            media = soma / 365

            if i == 0:
                maior = num
            else:
               if num > maior:
                    maior = num

            if i == 0:
                menor = num
            else:
                if num < menor:
                 menor = num

        for i in range(365):
            if temperatura[i] < media:
                abaixomedia = abaixomedia + 1

        print("\nMenor temperatura do ano: {}°\nMaior temperatura do ano: {}°\nMédia anual: {}°\nDias com temperatura abaixo da média: {} dias".format(
                        menor, maior, media, abaixomedia))



    def ordenarCrescente(self):
            self.vetor.sort()
            self.visualizarVetor()

    def exercicio11(self):
        v1 = [1,15]
        v2 = [1,15]


        for i in range(1,15):
            print("Digite o {} número do vetor 1 :".format(i))
            v1.append(input())

        for i in range(1,15):
            print("Digite o {} número do vetor 2 :".format(i))
            v2.append(input())

            quantidade = 0

        for i in range(1,15):
          if (v1[i] == v2[i]):
               quantidade = quantidade + 1

        print("Existem {} números iguais nas mesmas posições dos vetores".format(quantidade))




















