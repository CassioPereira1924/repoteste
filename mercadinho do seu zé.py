
print('BEM VINDO AO MERCADINHO DO SEU ZÉ"\nO MELHOR DO BAIRRO\n')


valor_total = float(input("Digite o valor total da compra: "))
metodo_pagamento = input("Digite o método de pagamento (dinheiro, pix, cartao): ").lower()

if metodo_pagamento == "dinheiro":
    valor_total  = valor_total - (valor_total*0.027)
    print(valor_total)
elif metodo_pagamento == "pix":
    valor_total = valor_total - (valor_total*0.0195)
elif metodo_pagamento == "cartao":
    valor_total = valor_total + (valor_total*0.0485)
else:
    print("Método de pagamento inválido.")

