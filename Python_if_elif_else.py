
# coding: utf-8

# In[ ]:


nome= str(input("Digite seu nome:\n"))
idade = int(input("\nDigite sua idade:\n"))

print("\n{0}, sua idade é {1} anos.".format(nome, idade))

if idade >= 18:
    
    def func():
        cnh = input("\nVocê já tirou sua habilitação? (s/n)\n")
    
        if (cnh == "s") or (cnh == "n"):

            if cnh == "s":
                print("\nEntão, você já pode dirigir.")

            elif cnh == "n":
                print("\nVocê ainda não pode dirigir. Primeiro é necessário ser habilitado.")

        else:
            cnh == print("\nDigite um valor válido! (s/n)")
            func()
    
    func()
    
else:
    print("\nVocê ainda não pode dirigir.")

