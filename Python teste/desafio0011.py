largura = float(input("Digite a largura: "))
altura = float(input("Diigite a altura: "))
area = altura * largura

tinta = 2**0.5

consumo_tinta = area / tinta

print(f'com base na sua largura  {largura} e na sua altura  {altura} o total da sua área é de {area} e seu consumo de tinta vai ser de {consumo_tinta}')
