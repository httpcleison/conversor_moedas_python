from forex_python.converter import CurrencyRates

moedas = ["EUR", "BRL", "USD"]
c = CurrencyRates()

for moeda in moedas:
    print(f"    ->{moeda}")

moeda_para_converter = str(input("Escolha uma moeda para converter seu dinheiro: "))
dinheiro_quant = float(input("Digite o valor do dinheiro: "))
moeda_converter = str(input("Escolha uma moeda para que o valor seja convertido: "))

resultado_convertido = c.convert(moeda_para_converter, moeda_converter, dinheiro_quant)

print(f"O valor de {dinheiro_quant} {moeda_para_converter} e igual a {resultado_convertido:.2f} {moeda_converter}")