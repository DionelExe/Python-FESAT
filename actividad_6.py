class Cuenta:
    
    def __init__(self,titular,cantidad):
        self.titular=titular
        self.cantidad=cantidad               

    def mostrar(self) :
        if self.cantidad > 0:
            print(f"El titular de la cuenta es: {self.titular} y tiene: ${self.cantidad}")
        else:
            print(f"El titular de la cuenta es: {self.titular} y adeuda: ${self.cantidad}")

    def ingresar(self,sumar):
        print("Ingrese la cantidad a ingresar: ")
        if sumar > 0:
            self.cantidad += sumar
        
    def retirar(self, restar):
        print("Ingrese la cantidad a retirar: ")
        self.cantidad -= restar

cuenta1=Cuenta("Dionel",100)
cuenta1.mostrar()
cuenta1.ingresar(100)
cuenta1.mostrar()
cuenta1.retirar(250)
cuenta1.mostrar()
