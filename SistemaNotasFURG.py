"""

Universidade Federal do Rio Grande - FURG

Nome: Luis Guilherme Souto Miranda
Curso: Matemática Aplicada
Matrícula: 168516

e-mail: luis.miranda10@icloud.com

Nome do programa: Sistema de avaliação de notas da FURG

"""

nome = str("")
matricula = 0
frequencia = 0
notas = []
media = 0.0


# Dados do Aluno
def DadosAluno():
    global nome, matricula
    while True:
        nome = input("Nome do aluno: ")
        if not nome:
            print("\nNOME DO ALUNO É OBRIGATÓRIO\n")
        else:
            break
    while True:
        matricula = input(f"Digite a matrícula do(a) {nome}: ")
        if not nome:
            print(f"\nMATRÍCULA DO(A) {nome} ALUNO É OBRIGATÓRIO\n")
        else:
            try:
                matricula = int(matricula)
                if matricula > 0:
                    break
                else:
                    print(f"\nMATRÍCULA DO(A) {nome} ALUNO DEVE SER UM NÚMERO POSITIVO\n")
            except ValueError:
                print(f"\nMATRÍCULA DO(A) {nome} ALUNO DEVE SER UM NÚMERO INTEIRO\n")
                pass


# Dados de Frequência
def Frequencia():
    global nome, frequencia
    while True:
        aulas = input("Digite a quantidade de aulas ministradas: ")
        if not aulas:
            print(f"\nQUANTIDADE DE AULAS MINISTRADAS É OBRIGATÓRIO\n")
        else:
            try:
                aulas = int(aulas)
                if aulas > 0:
                    break
                else:
                    print(f"\nQUANTIDADE DE AULAS MINISTRADAS DEVE SER UM NÚMERO POSITIVO\n")
            except ValueError:
                print(f"\nQUANTIDADE DE AULAS MINISTRADAS DEVE SER UM NÚMERO INTEIRO\n")
                pass
    while True:
        frequencia = input(f"Digite a frequência do(a) {nome}: ")
        if not frequencia:
            print(f"\nFREQUÊNCIA É OBRIGATÓRIO\n")
        else:
            try:
                frequencia = int(frequencia)
                if 0 <= frequencia <= aulas:
                    frequencia = frequencia/aulas
                    break
                else:
                    print(f"\nFREQUÊNCIA DEVE SER MENOR OU IGUAL A QUANTIDADE DE AULAS MINISTRADAS\n")
            except ValueError:
                print(f"\nFREQUÊNCIA DEVE SER UM NÚMERO INTEIRO\n")
                pass


# Sistema de Avaliação
def SistemaAvaliacao():
    global nome, matricula, notas, media
    while True:
        op = input("""
Sistema de Avaliação

1 -> Sistema de avaliação anual
2 -> Sistema de avaliação semestral

Opção: """)
        if not op:
            print(f"\nALGUMA OPÇÃO DEVE SER ESCOLHIDA")
        else:
            try:
                op = int(op)
                # Sistema de avaliação anual
                if op == 1:
                    print("\nSistema de Avaliação Anual\n")
                    for i in range(4):
                        while True:
                            nota = input(f"Digite a nota {i + 1}: ")
                            if not nota:
                                print(f"\nNOTA {i + 1} É OBRIGATÓRIA\n")
                            else:
                                try:
                                    nota = float(nota)
                                    if 0.0 <= nota <= 10.0:
                                        notas.append(nota)
                                        break
                                    else:
                                        print(f"\nNOTA {i + 1} DEVE SER ENTRE 0 E 10\n")
                                except ValueError:
                                    print(f"\nNOTA {i + 1} DEVE SER UM NÚMERO\n")
                                    pass
                    print("\nNotas registradas\n")
                    break
                # Sistema de avaliação semestral
                elif op == 2:
                    print("\nSistema de Avaliação Semestral\n")
                    notas = []
                    for i in range(2):
                        while True:
                            nota = input(f"Digite a nota {i + 1}: ")
                            if not nota:
                                print(f"\nNOTA {i + 1} É OBRIGATÓRIA\n")
                            else:
                                try:
                                    nota = float(nota)
                                    if 0.0 <= nota <= 10.0:
                                        notas.append(nota)
                                        break
                                    else:
                                        print(f"\nNOTA {i + 1} DEVE SER ENTRE 0 E 10\n")
                                except ValueError:
                                    print(f"\nNOTA {i + 1} DEVE SER UM NÚMERO\n")
                                    pass
                    print("\nNotas registradas\n")
                else:
                    print(f"\nOPÇÃO INVALIDA")
            except ValueError:
                print(f"\nOPÇÃO INVALIDA")
                pass


# Cálculo de Média
def Media():
    global nome, notas, frequencia, media
    media = sum(notas) / len(notas)
    print(f"Média do(a) {nome} é: {media:.2f}")
    print(f"Frequência do(a) {nome} é de {(frequencia*100):.2f}%")
    if frequencia < 0.75:
        print(f"\n{nome} não atingiu a frequência mínima de 75% para aprovação")
        print(f"\n{nome} está reprovado")
    elif media < 7.0:
        print(f"\n{nome} ainda não atingiu média suficiente para aprovação\n")
        while True:
            exame = input("Digite a nota do exame: ")
            if not exame:
                print(f"\nNOTA DO EXAME É OBRIGATÓRIA\n")
            else:
                try:
                    exame = float(exame)
                    break
                except ValueError:
                    print(f"\nNOTA DO EXAME DEVE SER UM NÚMERO\n")
                    pass
        while True:
            peso = input("Digite o peso da nota do exame: ")
            if not peso:
                print(f"\nPESO DA NOTA DO EXAME É OBRIGATÓRIO\n")
            else:
                try:
                    peso = int(peso)
                    if 0 <= peso <= 10:
                        peso = float(peso/10)
                        break
                    else:
                        print(f"\nPESO DA NOTA DO EXAME DEVE SER ENTRE 0 E 10\n")
                except ValueError:
                    print(f"\nPESO DA NOTA DO EXAME DEVE SER UM NÚMERO INTEIRO\n")
                    pass
        media = ((media * (1.0 - peso)) + (exame * peso))
        print(f"Média do(a) {nome} após o exame é: {media:.2f}")
        if media < 5:
            print(f"\n{nome} não atingiu média suficiente para aprovação mesmo após o exame")
            print(f"\n{nome} está reprovado")
        else:
            print(f"\n{nome} está aprovado")
    else:
        print(f"\n{nome} está aprovado")


# Programa
def main():
    print("Sistema de Avaliação de Notas de FURG\n")
    # Entrada de dados do aluno
    DadosAluno()
    # Entrada dos dados de frequência
    Frequencia()
    # Tipo de sistema de avaliação e registro de notas
    SistemaAvaliacao()
    # Cálculo da média
    Media()


if __name__ == '__main__':
    main()
