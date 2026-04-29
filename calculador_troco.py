def atualizar_troco(valor_moeda, valor_troco, quantidade=0):
    valor_total = valor_moeda * quantidade
    valor_inteiro = int(valor_total)

    troco_atualizado = valor_troco - valor_inteiro
    return troco_atualizado, valor_inteiro # return múltiplo retorna uma tupla

def validar_numero(msg_numero):
    while True:
        try:
            return int(input(msg_numero))
        except ValueError:
            print('Digite apenas números.\n')

# Programa principal
valores = {
    1: 0.10,
    2: 0.25,
    3: 0.5,
    4: 1
}

print('Conte 2 moedas de 5 centavos como se fosse 10 centavos.\n')
quantidades = []

for i in valores: # O loop encerra quando termina de percorrer o dicionário valores.
    quantidade = validar_numero(f'Quantidade de R${valores[i]:.2f}: ')
    quantidades.append(quantidade)

print(f'Quantidade: {quantidades}')

# O troco é atualizado a cada rodada.
moeda10 = atualizar_troco(0.10, 50, quantidades[0])
moeda25 = atualizar_troco(0.25, moeda10[0], quantidades[1])
moeda50 = atualizar_troco(0.5, moeda25[0], quantidades[2])
moeda1 = atualizar_troco(1, moeda50[0], quantidades[3])

# Informar quantas moedas o usuário precisa reservar de cada valor
print('\n--- COMPOSIÇÃO DO TROCO ---')
print(f'R$0,10: {int(moeda10[1] / valores[1])} moedas')
print(f'R$0,25: {int(moeda25[1] / valores[2])} moedas')
print(f'R$0,50: {int(moeda50[1] / valores[3])} moedas')
print(f'R$1,00: {moeda1[1]} moedas')

if moeda1[0] > 2:
    print(f'\nVocê precisa completar seu troco com R${moeda1[0]:.2f} em cédulas.')


