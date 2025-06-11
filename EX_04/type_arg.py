import sys 

def type_argv():
    """
    busca si hay algún caracter que no sea entero en el array sys.argv 
    y verifica que no falten parametros en el array
    """    
    if len(sys.argv) >= 2: # verifica haya 2 o mas argumentos dentro del array
         
        for x in sys.argv[1:]: #itera buscando algo que no sea un numero entero, desde la posición 1 hasta el final del array

            try:
                isinstance( int(x) , int) # verifica si es entero, si lo es: no se hace nada
            except ValueError: # cuando detecta que hay un error por que se ingreso un valor diferente de enteros
                print("ERROR ARGV: " + x + " is not INT") # se envia un mensaje por pantalla diciendo cual es el error
                return # si hay error, se cierra. He impide el siguiente paso
        
        # itera en el array del sys.argv desde la posición 1 hasta terminar y va imprimiendo "int: " con el valor de cada posicion del array
        for y in sys.argv[1:]:
            print ("int: " + y)
        
    else: # si son solo 2 argumentos pide un numero entero
        print("ERROR ARGV: Enter an argument")


if __name__ == "__main__":
    type_argv()