from DatosPersona import DatosPersona
from Direccion import Direccion
from Domicilio import Domicilio
from HandlerPersona import HandlerPersona
from HandlerDomicilio import HandlerDomicilio

hper = HandlerPersona()
hdom = HandlerDomicilio()


def main():
    exit = False
    while exit==False:
        print("¡Buenas!\n")
        print("     1-Agregar persona")
        print("     2-Ver personas")
        print("     3-Agregar domicilio")
        print("     4-Ver todos los domicilios")
        print("     5-Consultar domicilio")
        print("     0-Salir")
        opt = input("Selecione una opción: ")
        print("\n")
        match str(opt):
            case "1":
                agregarPersona()
            case "2":
                hper.printPersonas()
            case "3":
                agregarDomicilio()
            case "4":
                hdom.printDomicilios()
            case "5":
                consultarDomicilio()
            case "0": 
                exit = True
    


def agregarPersona():
    print("Ingrese los siguientes datos: \n")
    CI = input("Cédula: ")
    name = input("Nombre: ")
    surname = input("Apellido: ")
    age = input("Edad: ")
    datosPersona = DatosPersona(CI, name, surname, age)
    print(str(datosPersona))
    hper.addPersona(datosPersona)
    
def agregarDomicilio():
    print("Ingrese los siguientes datos: \n")
    CI = input("Cédula de la persona: ")
    persona = hper.findPersona(CI)
    
    print("Ingrese los siguientes datos de dirección (si no corresponde, ingrese 0): \n")
    departamento = input("Departamento: ")
    localidad = input("Localidad: ")
    calle = input("Calle: ")
    nro = input("Nro. de puerta: ")
    apartamento = input("Nro. de apartamento: ")
    padron = input("Padron: ") 
    ruta = input("Ruta: ")
    km = input("Km: ")
    letra = input("Letra: ")
    barrio = input("Barrio: ")
    
    direccion = Direccion(departamento, localidad, calle, nro, apartamento, padron, ruta, km, letra, barrio)
    
    domicilio = Domicilio(hdom.giveDomicilioID(), persona, direccion)
    
    hdom.addDomicilio(domicilio)

def consultarDomicilio():
    CI = input("Ingrese la cédula del usuario: ")
    hdom.consultarDomicilio(CI)
    
def domiciliosPorCriterio():
    print("Criterios: \n")
    print("     Departamento\n")
    print("     Localidad\n")
    print("     Calle\n")
    print("     Nro. de puerta (nro)\n")
    print("     Apartamento\n")
    print("     Padron\n")
    print("     Ruta\n")
    print("     Km\n")
    print("     Letra\n")
    print("     Barrio\n")
    criterio = input("Escriba el criterio por el que quiere sortear los domicilios: ")
    
    hdom.domiciliosPorCriterio(criterio)
    
if __name__ == "__main__":
    main()