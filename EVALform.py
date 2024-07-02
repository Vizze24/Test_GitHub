
import os
import csv
import time

os.system("cls")

def cargar(trabajadores):
    os.system("cls")
    with open ("trabajadores.csv","w",newline="")as laburantes:
        escribircsv=csv.writer(laburantes)
        escribircsv.writerow(["Trabajador", "Cargo" , "Sueldo Bruto", "Descuento AFP", "Descuento Salud", "Sueldo Liquido"])
        escribircsv.writerows([
            ["Vicente Cossio", "CEO", 800000,50000,50000,700000],
            ["Benjamin Gaete", "Director", 600000,20000,30000,650000],
            ["Fernando Guzman", "Marketing", 500000,20000,30000,450000],
        ])

def nuevotrabajador(trabajadores):
    os.system("cls")
    nom=input("Ingrese el nombre del nuevo trabajador: ")
    cargo=input("Ingrese el cargo del nuevo trabajador: ")
    
    while True:
        try:
            sueldoB=int(input("Ingrese el sueldo bruto: ")) 
            break
        except ValueError:
            print("Ingrese un numero no un caracter")
            continue
    dsctAFP=sueldoB*7//100
    dsctSalud=sueldoB*5//100
    sueldoLiq=sueldoB-dsctAFP-dsctSalud
    with open("trabajadores.csv","a",newline="") as agregarcsv:
        agregarnuevo=csv.writer(agregarcsv)
        agregarnuevo.writerow([nom,cargo,sueldoB,dsctAFP,dsctSalud,sueldoLiq])
        print("Nuevo Trabajador ingresado correctamente")


def vertodos(trbajadores):
    os.system("cls")
    with open("trabajadores.csv","r",newline="") as laburantesR:
        lectorcsv=csv.DictReader(laburantesR)
        for fila in lectorcsv:
            nombre=fila["Trabajador"]
            cargoempresa=fila["Cargo"]
            sueldo=fila["Sueldo Bruto"]
            descAFP=fila["Descuento AFP"]
            descSAL=fila["Descuento Salud"]
            sueldoL=fila["Sueldo Liquido"]
            print(f"Trabajador: {nombre} /  Cargo: {cargoempresa}  /  Sueldo Base: {sueldo}  /  Desc AFP: {descAFP}  /  Desc Salud: {descSAL}  /  Sueldo Liquido: {sueldoL}")
            time.sleep(1)

def plantillasueldos(trbajadores):
    os.system("cls")
    with open("trabajadores.csv","r",newline="") as laburantesR:
        lectorcsv=csv.DictReader(laburantesR)
        for fila in lectorcsv:
            nombre=fila["Trabajador"]
            cargoempresa=fila["Cargo"]
            sueldoL=fila["Sueldo Liquido"]
            print(f"Trabajador: {nombre} /  Cargo: {cargoempresa}  /  Sueldo Liquido: {sueldoL}")
            time.sleep(1)
        
      

def menu(trabajadores):
    os.system("cls")
    print("-"*30 ,"\n", "BIENVENIDO AL PROGRAMA","\n","-"*30)
    time.sleep(4)
    os.system("cls")

    while True:  
        empezar=input("Si desea cargar los archivos presione ENTER si no, escriba no ").lower()
        if empezar=="":
            cargar("trabajadores.csv")
            break
        elif empezar=="no".lower():
            break
    os.system("cls")

    while True:


        print("-"*30 ,"\n", "MENU OPCIONES","\n","-"*30)        
        print("1. Registrar trabajador\n2. Lista de todos los trabajadores\n3. Imprimir Sueldos\n4. Salir ")
        
        try:
            opc=int(input("Ingrese la opcion deseada: "))
        except ValueError:
            print("Digito no valido(Recuerda usar numeros del 1 al 4 para seleccionar tu respuesta)")

        if opc==1:
            nuevotrabajador("trabajadores.csv")
        elif opc==2:
            vertodos("trabajadores.csv")
        elif opc==3:
            plantillasueldos("trabajadores.csv")
        elif opc==4:
            print("Gracias por usar el programa\nHasta luego...")
            break
        else:
            print("Ingrese una opcion valida (1 a 4)")
            continue
    
menu("trabajadores.csv")