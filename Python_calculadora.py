
# coding: utf-8

# In[1]:


print("\n******************** Calculadora Python ********************\n\nDigite o número da operação desejada:\n\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n")

operacoes = (1, 2, 3, 4)
operacao = int(input("Digite sua opção (1/2/3/4): "))

if operacao in operacoes:

    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("\nDigite o segundo número: "))

    if operacao == 1:
        resultado = num1+num2
        print("\n", num1, " + ", num2, " = ", resultado)

    elif operacao == 2:
        resultado = num1-num2
        print("\n", num1, " - ", num2, " = ", resultado)

    elif operacao == 3:
        resultado = num1*num2
        print("\n", num1, " * ", num2, " = ", resultado)

    elif operacao == 4:
        resultado = num1/num2
        print("\n", num1, " / ", num2, " = ", resultado)

else:
    print("\nOpção inválida!")

