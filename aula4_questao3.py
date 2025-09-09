#codigo de entrada
valor=int(input("qual valor"))
#576

#processamento
#### começar da maoir nota (quantas notas)
notas_100= int(valor//100) #576/100 =5
#### atualizar  quantas faltam depois da maior nota
valor = valor %100 # 576-5*100=76

notas_50 = valor// 50 # 76 //50 =1
valor = valor % 50 # valor -50*notas_50 # 26

notas_20 = valor// 20 # 26 //20 =1
valor = valor % 20 # 6

notas_10 = valor // 10 # 6 // 10 = 0
valor = valor % 10  # 6

notas_5 = valor // 5 # 6 // 5 = 1
valor = valor % 5 #1

notas_2 = valor // 2 # 1 // 2 = 0
valor = valor % 50 # 1

notas_1 = valor

# Impressão de dados (saída)
print(f"{notas_100}notas de 100")
print(f"{notas_50}notas de 50")
print(f"{notas_20}notas de 20")
print(f"{notas_10}notas de 10")
print(f"{notas_5}notas de 5")
print(f"{notas_2}notas de 2")
print(f"{notas_1}notas de 1")