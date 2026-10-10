#En un circo, las entradas se venden de acuerdo a la edad. La entrada general 
#tiene un costo de 10000 Bs, pero:

#* Si es un niño menor a 2 años la entrada es gratis. 
#* Si es un niño con edad entre 2 y 5 años, le aplica un descuento de 50% 
#* Si es un niño de 6 a 10 años tiene un descuento de 20%
#* A partir de 55 años el descuento es de 30% 

#Dependiendo si la persona es estudiante o no, el monto del descuento será lo que 
#sea mayor, entre el descuento por edad (si aplica) y el 25% de descuento. 

#*El resto de las personas pagan entrada general. Se conoce la edad (verificar que 
#sea mayor o igual que 0) de la persona y si es estudiante. Se pide mostrar cual fue el 
#porcentaje de descuento aplicado, el monto de descuento y el monto a pagar por la 
#entrada. 

edad = int(input("Introduzca la edad:"))

if  edad < 0:
    print("la edad no puede ser un valor negativo")
else:
    entrada = 10000
    
    if edad < 2:
        porc_descuento = 100
    elif edad <= 5:
        porc_descuento = 50
    elif edad <= 10:
        porc_descuento = 20
    elif edad < 55:
        porc_descuento = 0
    else: # para el caso de edades mayores a 55 años
        sexo = input("Introduzca el genero (M o F):")
        if (sexo.upper()=="M" and edad>=65) or (sexo.upper()=="F"):
            porc_descuento = 30 
        else:
            porc_descuento=0

    if porc_descuento < 30:
        estudiante = input("Es estudiante (si o no):")
        if estudiante.lower() == "si":
            porc_descuento = 25

    if porc_descuento != 0:
        descuento = entrada * porc_descuento / 100
        print(f"El porcentaje de descuento asignado es {porc_descuento}%")
        print(f"El monto del descuento es {descuento}")
    else:
        descuento = 0

    monto_pagar = entrada - descuento

    print(f"El monto a pagar es {monto_pagar}")