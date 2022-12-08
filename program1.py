def simple(p,t,r):
    simple_interest = (p*t*r)/100
    print("Simple interest is:",simple_interest)


def compound(principal,rate,time):
    compound_interest = principal * ( (1+rate/100)**time - 1)
    print("Compound interest is:",compound_interest)


while True:  
    print("\nMENU")  
    print("1. Simple interest")  
    print("2. compound interest")
    choice = int(input("\nEnter the Choice: "))  

    if choice == 1:  
        print( "\n Simple interest\n")  
        simple(100,4,5)
    elif choice == 2:  
        print( "\compound interest\n")  
        compound(100,5,7)
      
    elif choice == 3:  
        break  
      
    else:  
        print( "Please Provide a valid Input!")