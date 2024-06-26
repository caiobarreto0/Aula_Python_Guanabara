real = float(input('Digite um valor em real: '))
cambio = float(input('Digite a taxa de câmbio: '))
usd = real / cambio


print('O valor que você tem em real {:.3f}, pode comprar {:.3f} em dolares americanos'.format(real,usd))