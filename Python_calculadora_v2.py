#!/usr/bin/env python
# coding: utf-8

# In[9]:


operacoes = (1,2,3,4)

operacao = int(input("********** CALCULADORA PYTHON **********\n\nOlá, seja muito bem vindo à minha Calculadora Python.\n\nPara utilizá-la, basta selecionar o número da operação desejada\n\n 1-Adição \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \n\n"))

while operacao in operacoes:

    num1 = float(input("\nDigite o primeiro número:\n"))
    num2 = float(input("\nDigite o segundo número:\n"))

    if operacao == 1:
        resultado = num1+num2
        print ("\nO resultado de ", num1, " + ", num2, "é igual a: ", resultado)

    if operacao == 2:
        resultado = num1-num2
        print ("\nO resultado de ", num1, " - ", num2, "é igual a: ", resultado)

    if operacao == 3:
        resultado = num1*num2
        print ("\nO resultado de ", num1, " * ", num2, "é igual a: ", resultado)

    if operacao == 4:
        resultado = num1/num2
        print ("\nO resultado de ", num1, " / ", num2, "é igual a: ", resultado)
    
    continuar = str(input("\nDeseja realizar outra operação? (s/n)"))
    
    if continuar == "s":
        operacao = int(input("\nSelecione o número da operação desejada \n \n 1-Adição \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \n \n "))
    
    else:
        print ("\nObrigado por utilizar a calculadora Python!")
        break

else:
    operacao = int(input("\nOperação inválida! \n "))
    


# In[ ]:





# In[ ]:




