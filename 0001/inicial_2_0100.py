year = input("Digite um ano: ")

if(0 < len(year) == 4 and year.isdigit()):
    year = int(year)
    if (year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
        print("Ano bissexto!")
    else:
        print("Não é ano bissexto")
        

else:
    print("Por favor digite um ano válido(4 digitos)")