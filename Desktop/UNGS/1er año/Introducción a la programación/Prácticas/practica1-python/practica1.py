#EJERCICIO 1
puntoUno1 = 20 + (12 * 13)
 # => 20 + 156 => 176
puntoDos1 = 17/15 + 30
  # => 1.13 + 30 => 31.13
puntoTres1 = 17/15 * 30
 # => 1.13 * 30 => 34
puntoCuatro1 = (17/15) * 30
 # => 1.13 * 30 => 34

#EJERCICIO 2
x = int(input("agregue el valor de x"))
y = int(input("agregue el valor de y"))
z = int(input("agregue el valor de z"))
puntoUno2 = (x/y) + 1
puntoDos2 = (x + y) / (x -y)
puntoTres2 = (x + (y/z)) / (x - (y / z))
puntoCuatro2 = [(x + y) ** 2]**2

#EJERCICIO 3
a = int(input("agregue el valor de a"))
b = int(input("agregue el valor de b"))
puntoUno3 = a + b
print(puntoUno3)

#EJERCICIO 4
puntoUno4 = a + 1
print(puntoUno4)

#EJERCICIO 5
a = int(input("agregue el valor de a"))
b = int(input("agregue el valor de b"))
puntoUno5 = ( a + b) / 2
print(puntoUno5)

#EJERCICIO 6
print("Mi primer programa Python")

#EJERCICIO 7
print("\n v \n e \ r \n t \n i \n c \n a \n l")

#EJERCICIO 8
print("\n ***** \n *   * \n *   * \n *   * \n *****")

#EJERCICIO 9
print("\n * \n *** \n ***** \n ******* \n *********")

#EJERCICIO 10
puntoUno10 = input("Ingrese su nombre")
print(puntoUno10)

#EJERCICIO 11
valor = int(input("Ingrese un valor"))
print("\n ****************************** \n *El resultado es:", valor, "\n ******************************")

#EJERCICIO 13
inversion = int(input("Ingrese su inversion"))
meses = int(input("Ingrese la cantidad de meses a invertir"))
total13 = (((inversion * 6 ) / 100) * meses) + inversion
print("Su total es: ", total13)

#EJERCICIO 14
llamadas = int(input("Ingrese cantidad de llamadas"))
segundos = float(input("Ingrese cantidad se segundos"))
total14 = (llamadas * 12) + (segundos * 1.5)
##print("Su gasto total es: ", total14)

# EJERCICIO 15
venta1 = int(input("Ingrese el monto de su venta"))
venta2 = int(input("Ingrese el monto de su venta"))
venta3 = int(input("Ingrese el monto de su venta"))

sueldo15 = 42000 + ((venta1 * 10) / 100) + ((venta2 * 10) / 100) + ((venta3 * 10) / 100)

print("Su sueldo total es: ", sueldo15)

# EJERCICIO 16
segHora = 3600
segDia = 86400

seg = int(input("Exprese la cantidad de segundos"))

minutos = seg / 60
hora = (seg / 60) / 60
dia = ((seg / 60) / 60)/ 24

# EJERCICIO 17
monto = int(input("Ingrese su monto a sacar"))
cantMil = 0
cant500 = 0
cant100 = 0
if (monto >= 1000):
    cantMil = monto//1000
    monto = monto % 1000
    if(monto >= 500):
      cant500 = monto // 500
      monto = monto % 500
      if (monto >= 100):
       cant100 =  monto // 100
       monto = monto % 100
print(monto, cantMil, cant500, cant100)

# EJERCICIO 18
segundos = int(input("Ingrese la cantidad de segundos"))
cantDias = 0
cantHoras = 0
cantMinutos = 0
cantSegundos = 0

if (segundos >= 86400):
    cantDias = segundos // 86400
    segundos = segundos % 86400
if (segundos >= 3600):
        cantHoras = segundos // 3600
        segundos = segundos % 3600
if (segundos >= 60):
     cantMinutos = segundos // 60
     segundos = segundos % 60

print(cantDias, cantHoras, cantMinutos, segundos)