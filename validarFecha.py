dia = int(input("digita el dia"))
mes = int (input("digita el mes"))
año = int(input("digita el año"))

if año>0:
    if mes> 0 and mes <=12:
        maximo_dias=31
        if mes==4 or mes == 6 or mes == 9 or mes == 11:
            maximo_dias= 30
        else:
            if mes ==2:
                if año % 4 ==0:
                    if año % 100 ==0:
                        if año % 400 ==0:
                            #si es bisiesto
                            maximo_dias = 29
                        else:
                            maximo_dias = 28

                    else:
                        #no es divisible por 100 , es bisiesto
                        maximo_dias = 29
                
                else:
                    #no  es bisiesto
                    maximo_dias = 28
        
        #todo bien hasta ahora
        #validar el dia
        if dia >0 and dia <= maximo_dias:
            print("Fecha correcta")
        else:
            print("el dia es incorrecto")
    else:
        print("el mes es incorrecto")

else:
    print("el año es incorrecto")