# condicionales

print (" Ingrese su edad:")
edad_str = input()
edad_int = int(edad_str)

if edad_int >=18:
    print("Usted es mayor de edad.")
else:
    print ("Usted es menor de edad.")

# Grupos socioeconómicos y sus ingresos promedio 
#AB: Clase alta, con ingresos promedio de $4.386.000
#C1a: Clase media acomodada, con ingresos promedio de $2.070.000
#C1b: Clase media emergente, con ingresos promedio de $1.374.000
#C2: Clase media típica, con ingresos promedio de $810.000
#C3: Clase media baja, con ingresos promedio de $899.000
#D: Vulnerables, con ingresos promedio de $562.000
#E: Pobres, con ingresos promedio de $324.000

print ("Ingrese su sueldo:")
sueldo_str = input()
sueldo_int = int(sueldo_str)

if sueldo_int >=4386000:
    print("Usted esta en el grupo AB")
elif sueldo_int >=2070000:
    print("Usted esta en el grupo C1a")
elif sueldo_int >=1334000:
    print("Usted esta en el grupo C1b")
elif sueldo_int >=810000:
    print("Usted esta en el grupo C2")
elif sueldo_int >=810000:
    print("Usted entro a la clase media baja")
elif sueldo_int >=562000:
    print("Usted esta en el grupo D")
elif sueldo_int >=324000:
    print ("Usted esta en el grupo E")

else:
    print("Estas en situacion de calle")