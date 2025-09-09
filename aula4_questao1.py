comprimento = int(input("digite o comprimeto"))
largura     = int(input("digite a largura")) 
preço_m2    =float(input("valor do m2"))

area= comprimento * largura #m2
preço_total= area * preço_m2

print(f"O terreno possui {area}m2 e custa R${preço_total:,..2f}")



