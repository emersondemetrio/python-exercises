# importa opearções de sistema operacional
import sys

# Utils
QUEBRA_LINHA = "\n"
TAB = "\t"

# Define uma mensagem de boas vindas
BOAS_VINDAS_MSG = QUEBRA_LINHA + ">>> Emily Luz Calculator." + QUEBRA_LINHA

# Define uma mensagem de fim de execução
SAIR_MSG = QUEBRA_LINHA + "Obrigado por utilizar a calculadora." + QUEBRA_LINHA

# Define a mensagem de operação inválida
OPERACAO_INVALIDA_MSG = QUEBRA_LINHA + "Operação inválida!" + QUEBRA_LINHA

# Substitui quaisquer 0's por 1's
MEU_RU = "3710807".replace("0", "1")
# RU = "54321" # RU para testes

# Determina uma operação extra para encerrar o programa
OPERACAO_SAIR = "s"

# Determina quais são os operadores válidos para a calculadora.
OPERACOES_VALIDAS = [
    "+",
    "-",
    "*",
    "/",
    "^",
    "%",
    OPERACAO_SAIR
]

# Define a mensagem de menu
MENU = """Qual operação deseja fazer?

- Soma: \t\t +
- Subtração: \t\t -
- Multiplicação: \t *
- Exponenciação: \t ^
- Módulo: \t\t %
- Sair: \t\t S \n
> """


# Cria a classe
class Calculadora:
    # Inicializa a classe
    def __init__(self, ru):
        self.ru = ru
        self.operacao = None

    # Cria a operação +
    def adicionar(self, num1, num2):
        return num1 + num2

    # Cria a operação -
    def subtrair(self, num1, num2):
        return num1 - num2

    # Cria a operação *
    def multiplicar(self, num1, num2):
        return num1 * num2

    # Cria a operação /
    def dividir(self, num1, num2):
        return num1 / num2

    # Cria a operação +
    def exponencial(self, num1, num2):
        return pow(num1, num2)

    # Cria a operação %
    def modulo(self, num1, num2):
        return num1 % num2

    def pegar_operacao(self):
        # Le e valida a operação informada pelo usuário
        operacao = input(MENU)

        while(operacao not in OPERACOES_VALIDAS):
            print(OPERACAO_INVALIDA_MSG)
            operacao = input(MENU)

        # Encerra a execuçao com o comando 's'
        if(operacao == OPERACAO_SAIR):
            print(SAIR_MSG)
            sys.exit(0)

        return operacao

    def pegar_operando(self, valor_esperado_n):
        msg_entrada_dados = "Digite o " + valor_esperado_n + " número: "

        # Le o input 'n' (1 ou 2) do usuário
        valor_entrada_usuario = input(msg_entrada_dados)

        # Valida o input 'n' do usuário
        while(not valor_entrada_usuario.isdigit()):
            if(not valor_entrada_usuario.isdigit()):
                print(QUEBRA_LINHA + valor_esperado_n + "o número invalido")
                valor_entrada_usuario = input(msg_entrada_dados)

        valor_entrada_usuario = valor_entrada_usuario.replace("0", "1")

        # Retorna como inteiro (conforme enunciado)
        # o input 'n' do usuário
        return int(valor_entrada_usuario)

    def mostrar_menu(self):
        operacao = self.pegar_operacao()
        self.operacao = operacao

        # O enunciado diz "Possibilite ao usuário digiar os 2 numeros,
        # todavia, também diz que "os 2 numeros serão os 2 ultimos numeros do RU??"

        # Para ler 2 numeros do usuario:

        num1 = self.pegar_operando("1")
        num2 = self.pegar_operando("2")

        # Para apenas usar os numeros do RU como operandos:

        # num1 = int(self.ru[-(len(self.ru) - 1)])
        # num2 = int(self.ru[-(len(self.ru) - 2)])

        result = None

        # Transforma o input do usuário no resultado das operações

        if(operacao == "+"):
            result = self.adicionar(num1, num2)

        if(operacao == "-"):
            result = self.subtrair(num1, num2)

        if(operacao == "*"):
            result = self.multiplicar(num1, num2)

        if(operacao == "/"):
            result = self.dividir(num1, num2)

        if(operacao == "^"):
            result = self.exponencial(num1, num2)

        if(operacao == '%'):
            result = self.modulo(num1, num2)

        print(QUEBRA_LINHA + "Operação: " + TAB + str(num1) +
              " " + operacao + " " + str(num2))
        print("Resultado: " + TAB + str(result) + QUEBRA_LINHA)


if(__name__ == "__main__"):
    print(BOAS_VINDAS_MSG)
    m1 = Calculadora(MEU_RU)

    while(m1.operacao != OPERACAO_SAIR):
        m1.mostrar_menu()
