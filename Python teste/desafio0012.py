produto = float(input("Digite o preço do produto: "))
desconto = produto * 0.05
produto_desc = produto - desconto

print(f"Com base no valor do seu produto R${produto} com o desconto de 5% R${desconto} o valor total do produto será de R${produto_desc}")