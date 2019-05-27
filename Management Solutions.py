###MANAGEMENT SOLUTIONS


##Introduction


#Who are you?

name = input("What's your name?\n")
print("\nHello ",name,"!\n")

#Do you already work with me?

consultants = ["Leonardo", "Victor", "Ana", "Felipe"]
managers = ["Iker", "Jesús", "Mariano"]
MS = consultants + managers

if name in (MS):
    print("It's great to have a co-worker running my program :)\n")

else:
    pass


##Learning about Management Solutions


#Who we are Y

whoweare = ("y", "n")
whoweare = input("\nDo you want to know about Management Solutions? (y/n)\n")

if whoweare == "y":
    print("\nManagement Solutions is an international consulting Firm whose core mission is to deliver business, risk, financial, organization, technology and process-related advisory services.\n")
    
    
    #What we do Y
    
    whatwedo = ("y", "n")
    whatwedo = input("\nDo you want to know about what we do? (y/n)\n")
        
    if whatwedo == "y":
        print("\nWe help our clients to effectively meet and deal with their current business management challenges, based on our in-depth knowledge of the business and industries in which they operate.\n")
        
        
        #Where we are Y

        whereweare = ("y", "n")
        whereweare = input("\nDo you want to know about where we are? (y/n)\n")
    
        if whereweare == "y":
            print("\nWe operate through 27 offices, 13 in Europe (Madrid, Barcelona, Bilbao, London, Frankfurt, Paris, Amsterdam, Oslo, Warsaw, Zurich, Milan, Rome, Lisbon), 13 in the Americas (New York -from where Atlanta is managed-, Boston, Birmingham, San Juan de Puerto Rico, Mexico City, Medellín, Bogota, Quito, Sao Paulo, Lima, Buenos Aires, Santiago de Chile) and 1 in Asia (Beijing), from where we also serve clients operating in other countries (most notably the Belgium, Luxembourg, Denmark, Sweden, Finland, Andorra in Europe; Canada, Panama, Costa Rica, Uruguay, Paraguay, Venezuela, Nicaragua, Honduras, El Salvador, Dominican Republic, Guatemala in the Americas; Singapore, Turkey, India in Asia; and Senegal, Equatorial Guinea, Angola in Africa).\n")
            print("\nThanks for using Python!\n")
            print("For more information, please contact Leonardo Damasio.\n")
            print("leoleonardo1996@hotmail.com\n")
        
        #Where we are N
        
        elif whereweare == "n":
            
            print("\nOk, ",name," thanks for using Python!\n")
            print("For more information, please contact Leonardo Damasio.\n")
            print("leoleonardo1996@hotmail.com\n")
            
        else:
            print("\nInvalid command.\n")
            
            
    #What We Do N
    
    elif whatwedo == "n":
        
        print("\nOk, ",name," thanks for using Python!\n")
        print("For more information, please contact Leonardo Damasio.\n")
        print("leoleonardo1996@hotmail.com\n")
        
    else:
        print("\nInvalid command.\n")


#Who we are N

elif whoweare == "n":
    
    print("\nOk, ",name," thanks for using Python!\n")
    print("For more information, please contact Leonardo Damasio.\n")
    print("leoleonardo1996@hotmail.com\n")
    
else:
    print("\nInvalid command.\n")