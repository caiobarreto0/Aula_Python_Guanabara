tipo = input('Digite algo: ')

print('O tipo primitivo desse valor é : ', type(tipo))
print('Só tem espaços?', tipo.isspace())
print('É um número?', tipo.isnumeric())
print('É alfabético?', tipo.isalpha())
print('É alfanumérico?', tipo.isalnum())