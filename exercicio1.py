# importa opearções de sistema operacional
import sys

# Utils
LINE_BREAKER = "\n"
TAB = "\t"

# Define uma mensagem de boas vindas
WELCOME_MESSAGE = LINE_BREAKER + ">>> Emily Luz Calculator." + LINE_BREAKER

# Define uma mensagem de fim de execução
EXIT_MESSAGE = LINE_BREAKER + "Obrigado por utilizar a calculadora." + LINE_BREAKER

# Define a mensagem de operação inválida
INVALID_OPERATION_MESSAGE = LINE_BREAKER + "Operação inválida!" + LINE_BREAKER

# Substitui quaisquer 0's por 1's
RU = "3710807".replace("0", "1")
# RU = "54321" # RU para testes

# Determina uma operação extra para encerrar o programa
EXIT_OPERATION = "s"

# Determina quais são os operadores válidos para a calculadora.
VALID_OPERATIONS = [
    "+",
    "-",
    "*",
    "/",
    "^",
    "%",
    EXIT_OPERATION
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
        self.operation = None

    # Cria a operação +
    def add(self, num1, num2):
        return num1 + num2

    # Cria a operação -
    def sub(self, num1, num2):
        return num1 - num2

    # Cria a operação *
    def mul(self, num1, num2):
        return num1 * num2

    # Cria a operação /
    def div(self, num1, num2):
        return num1 / num2

    # Cria a operação +
    def exp(self, num1, num2):
        return pow(num1, num2)

    # Cria a operação %
    def mod(self, num1, num2):
        return num1 % num2

    def get_operation(self):
        # Le e valida a operação informada pelo usuário
        operation = input(MENU)
        while(operation not in VALID_OPERATIONS):
            print(INVALID_OPERATION_MESSAGE)
            operation = input(MENU)

        # Encerra a execuçao com o comando 's'
        if(operation == EXIT_OPERATION):
            print(EXIT_MESSAGE)
            sys.exit(0)

        return operation

    def get_number_operand(self, n):
        input_message = "Digite o " + n + " número: "

        # Le o input 'n' (1 ou 2) do usuário
        n_input = input(input_message)

        # Valida o input 'n' do usuário
        while(not n_input.isdigit()):
            if(not n_input.isdigit()):
                print(LINE_BREAKER + n + "o número invalido")
                n_input = input(input_message)

        n_input = n_input.replace("0", "1")

        # Retorna como inteiro (conforme enunciado)
        # o input 'n' do usuário
        return int(n_input)

    def show_menu(self):
        operation = self.get_operation()
        self.operation = operation

        # O enunciado diz "Possibilite ao usuário digiar os 2 numeros,
        # todavia, também diz que "os 2 numeros serão os 2 ultimos numeros do RU??"

        # Para ler 2 numeros do usuario:

        num1 = self.get_number_operand("1")
        num2 = self.get_number_operand("2")

        # Para apenas usar os numeros do RU como operandos:

        # num1 = int(self.ru[-(len(self.ru) - 1)])
        # num2 = int(self.ru[-(len(self.ru) - 2)])

        result = None

        # Transforma o input do usuário no resultado das operações

        if(operation == "+"):
            result = self.add(num1, num2)

        if(operation == "-"):
            result = self.sub(num1, num2)

        if(operation == "*"):
            result = self.mul(num1, num2)

        if(operation == "/"):
            result = self.div(num1, num2)

        if(operation == "^"):
            result = self.exp(num1, num2)

        if(operation == '%'):
            result = self.mod(num1, num2)

        print(LINE_BREAKER + "Operação: " + TAB + str(num1) +
              " " + operation + " " + str(num2))
        print("Resultado: " + TAB + str(result) + LINE_BREAKER)


if(__name__ == "__main__"):
    print(WELCOME_MESSAGE)
    m1 = Calculadora(RU)

    while(m1.operation != EXIT_OPERATION):
        m1.show_menu()
