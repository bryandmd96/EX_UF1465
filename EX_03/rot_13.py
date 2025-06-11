
def main():
    """
    Esta función recibe un string (str_in) <stdin>, transforma solo carateres del alfabeto de la entrada 
    en codigo ASCII, lo guarda en lista_str_in [], le suma 13 valores mas a las letras entre (a-m) o 
    le resta 13 valores entre (n-z) <independientemente si son mayus o minus>, agrega los valores a 
    lista_str_out [], cambia los valores de las letras del alfabeto a caracteres y los guarda en lista_str_out_ascii []
    se imprime el mensaje de forma cifrada
    """
    lista_str_in = [] # lista de letras transformadas a ASCII
    str_in = input("str_in: ") # entrada de string
    
    # itera en la entrada "string" y convierte a valores en ASCII
    for char in str_in:
        lista_str_in.append(ord(char)) # transformacion de str a int ASCII y guarda en lista_str_in

    lista_str_out = [] # lista de valores ASCII de carateres, ya modificados

    # itera en los valores y dependiendo de su valor ASCII, suma o resta cantidad y agrega a lista_str_out 
    for rot_13 in lista_str_in:
        if rot_13 >= 65 and rot_13 <= 77: # modifica valores entre (A-M) y agrega a lista
            rot_13 += 13
            lista_str_out.append(rot_13)
        elif rot_13 >= 78 and rot_13 <= 90: # modifica valores entre (N-Z) y agrega a lista
            rot_13 -= 13
            lista_str_out.append(rot_13)
        elif rot_13 >= 97 and rot_13 <= 109: # modifica valores entre (a-m) y agrega a lista
            rot_13 += 13
            lista_str_out.append(rot_13)
        elif rot_13 >= 110 and rot_13 <= 122: # modifica valores entre (n-z) y agrega a lista
            rot_13 -= 13
            lista_str_out.append(rot_13)
        else:
            lista_str_out.append(rot_13) # no modifica valores que no sean letras del alfabeto y los agrega directamente

    lista_str_out_ascii = [] # lista de letras del alfabeto <Mensaje> ya transformas del ASCII

    # ciclo para transformar mensaje codificado en letras del alfabeto y agregarlas a lista_str_out_ascii
    for character in lista_str_out:
        lista_str_out_ascii.append(chr(character)) # tranforma ASCII en caracteres <chr> y agrega a lista 
    
    print ("str_out: ", end = "") # imprime <str_out:> sin dejar espacios, ni saltos de linea 
    # itera en la lista_str_out_ascci (mensaje codificado) y va imprimiendo cada caracter, sin deja espacios
    for letter_rot_13 in lista_str_out_ascii:
        print(letter_rot_13,  end = "")



if __name__ == "__main__":
    main()