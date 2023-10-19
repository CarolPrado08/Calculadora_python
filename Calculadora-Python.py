def operacao(n1, n2, op):
    if op == 1:
        print(f"{n1} + {n2} = {n1 + n2}")
    elif op == 2:
        print(f"{n1} - {n2} = {n1 - n2}")
    elif op == 3:
        print(f"{n1} * {n2} = {n1 * n2}")
    elif op == 4:
        if n2 != 0:  
            print(f"{n1} / {n2} = {n1 / n2}")
        else:
            print("Aconteceu um erro, não é possível fazer uma divisão por zero!")
    else:
        print("Erro na operação!")

def entrada():
    x1 = float(input("Digite um número: ")) 
    x2 = float(input("Digite outro número: "))

    op = int(input("Escolha a operação:\n1-Soma; 2-Subtração; 3-Multiplicação; 4-Divisão: "))

    print("----------------------------")
    operacao(x1, x2, op)
    print("----------------------------")

def main():
    rep = "s"

    while rep.lower() != "n":
        entrada()
        rep = input("Deseja fazer outra conta? (S/N): ")

if __name__ == "__main__":
    main()


