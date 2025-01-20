def fibonacci_checar(num):
        a, b = 0, 1

        while a <= num:
            if a == num:
                return f"O número {num} pertence à sequência de Fibonacci."
            a, b = b, a + b
        return f"O número {num} não pertence à sequência de Fibonacci."

try:
    numero  = int(input("Digite um número inteiro: "))
    if numero < 0:
        print("Insira um número inteiro não negativo.")
    else:
        print(fibonacci_checar(numero))
except ValueError:
     print("Insira um número inteiro válido.")
