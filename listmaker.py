def add_codes_to_list(input_string): 
    # Split the input string by spaces and convert it to a list
    codes_list = input_string.split()
    return codes_list

#Exemplo de uso:
lista = "code1 code2 code3"
codes = add_codes_to_list(lista)
print(codes)