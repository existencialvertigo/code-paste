def add_codes_to_list(input_string): 
    # Split the input string by spaces and convert it to a list
    codes_list = input_string.split()
    return codes_list

#Exemplo de uso:
lista = """code1 code2 code3""" #Pode editar aqui diretamente e por os códigos -> Para printar a lista com eles para usar no codepaste.py
codes = add_codes_to_list(lista)
print(codes)
