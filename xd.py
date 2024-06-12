

listnomb=[]
listcargo=[]
listsueld=[]
descuentosalud=[]
descuentoafp=[]
sueldoliquido=[]
while True:
    print("Bienvenido")
    print("1.Registrar trabajador")
    print("2.Listar todos los trabajadores")
    print("3.Imprimir planilla de sueldos")
    print("4.Salir del Programa")
    opc=int(input("ingrese una opción: "))
    if opc==1:
        nom=input("ingrese su nombre: ")
        cargo=input("ingrese su cargo: ")
        sueld=int(input("ingrese su sueldo bruto: "))
        listnomb.append(nom)
        listsueld.append(sueld)
        listcargo.append(cargo)
        descuentosalud=round(sueld*0.07)
        descuentoafp=round(sueld*0.12)
        salud=descuentoafp+descuentosalud
        sueldoliquido=sueld-salud
    elif opc==2:
      print("TRABAJADOR CARGO SUELDO BRUTO DESC.SALUD DESC.AFP LIQUID A PAGAR")
      print(listnomb,listcargo,listsueld,descuentosalud,descuentoafp,sueldoliquido)    
    elif opc==3:
        print("1.imprimir todos")
        print("2:imprimir por cargos")
        opcion=int(input("ingrese una opción: "))
    else:
        print("que tengas un buen dia")
