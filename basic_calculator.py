while True:
    try:
        x = int(input("Type the first number: "))
        y = int(input("\nType the second:  "))

        print('''add, subtract, multiply, divide 
        or you can type exit if you want to exit...''')
        print("")
        islem = input()

        if islem == "add":
            print(f"\nResult: {x + y}")
    
        elif islem == "subtract":
            print(f"\nResult: {x - y}")
                
    
        elif islem == "multiply":
            print(f"\nResult: {x * y}")
    
        elif islem == "divide":
            if y == 0:
                print('''\nHow u gonna divide with 0 dumass''')
                continue
            else:
                print(f"\nResult: {x / y}")
        
        elif islem.lower() == "exit":
            print("\nCalculator is closing...")
            break
            
        
        
        else:
            print("\nINVALID OPERATION ")
            
           

    except ValueError:
         print("\nPlease type a valid operation")
        
