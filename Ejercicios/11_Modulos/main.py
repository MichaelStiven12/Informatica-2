import interfaz 
import logica

print(dir(interfaz))

print(interfaz.__doc__)
print(interfaz.__file__)

interfaz.separador("-")
interfaz.separador("~")

interfaz.imprimirNombre("Michael")

interfaz.imprimirVariable("v", 5)

logica.sumaDeTresNumeros(4,5,6)

logica.sumaDeNNumeros(4,5,7,8,4,3,2)

logica.sumaDeDosListas([3,6,3,2],[6,2,1,6])
