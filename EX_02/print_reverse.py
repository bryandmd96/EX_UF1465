
def print_reverse():
    """Esta funcion genera una lista [] de las letras del alfabeto, invierte el listado 
    y las muestra en pantalla """

    lista_characters = [] # lista de caracteres

    # Este ciclo agrega las letras del alfabeto a la lista de cracteres 
    for letter in range(ord('a'), ord('z') + 1): # el rango se define por medio de la transformacion de caracteres a ASCII
        lista_characters.append(chr(letter)) # en cada iteración <letter> tiene un valor distinto, se convierte a caracter <ord()> y se agrega a lista de caracteres <lista_characters.append()>
        
    lista_characters_inverse = lista_characters[::-1] # se invierte la lista de caracteres

    print(lista_characters_inverse) # se imprime la lista de caracteres invertida



if __name__ == "__main__":
    print_reverse()