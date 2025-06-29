while True:
    try:
        x = int(input("işlem için ilk sayıyı giriniz: "))
        y = int(input("\nişlem için ikinci sayıyı giriniz: "))

        print('''toplama, çıkarma, çarpma, bölme ya da
        çıkmak istiyorsanız çık yazın... \n''')
        print("")
        islem = input()

        if islem == "toplama":
            print(f"\nSonuç: {x + y}")
    
        elif islem == "çıkarma":
            print(f"\nSonuç: {x - y}")
                
    
        elif islem == "çarpma":
            print(f"\nSonuç: {x * y}")
    
        elif islem == "bölme":
            if y == 0:
                print('''\nsıfırla bölünür mü amk!
                bidaha dene…''')
                continue
            else:
                print(f"\nSonuç: {x / y}")
        
        elif islem.lower() == "çık":
            print("\nProgramdan çıkılıyor…")
            break
            
        
        
        else:
            print("\ngeçersiz işlem amk dört islemlerden yaz")
            
           

    except ValueError:
         print("\nLütfen geçerli bir sayı girin")
        