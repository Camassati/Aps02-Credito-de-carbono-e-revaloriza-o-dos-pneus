print("Crédito de carbono: Calculadora Mobilidade Urbana")


fatores_emissao = {
    'transporte_metro': 0.062,
    'transporte_moto': 0.1,
    'transporte_carro': 0.37,
    'transporte_onibus': 0.013,
    'voos': 0.070
}

def inputC(prompt):
    while True:
        try:
            valor = float(input(prompt))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")


consumo_metro = inputC("Quilômetros percorridos por mês (Metrô): ")         
consumo_onibus = inputC("Quilômetros percorridos por mês (Ônibus): ")
quilometros_dirigidos = inputC("Quilômetros dirigidos por mês (Carro): ")
quilometros_aviao = inputC("Quilômetros viajados de avião por ano: ")
quilometros_pilotados = inputC("Quilômetros pilotados por mês (Moto): ")


emissoes_totais = (

    (consumo_metro * fatores_emissao['transporte_metro'] * 12) +
    (consumo_onibus * fatores_emissao['transporte_onibus'] * 12) +
    (quilometros_dirigidos * fatores_emissao['transporte_carro'] * 12) +
    (quilometros_pilotados * fatores_emissao['transporte_moto'] * 12) +
    (quilometros_aviao * fatores_emissao['voos'])
)

venda = emissoes_totais / 1000 * 26          #26 é o valor referente ao preço do crédito de carbono por tonelada
compensacao = (emissoes_totais / 1000) * 7   #7 é o valor referente a quantidade de plantio de árvores para compensar uma tonelada de crédito

print(f'\n\nCom base nos dados inseridos você emite {emissoes_totais/1000:.2f} toneladas de Carbono por ano.')
print(f'Para compensar os gastos é necessário o plantio de : {compensacao:.0f} árvores. E em 20 anos compensarão os gastos.')
print(f'Este é o valor a ser pago pelo crédito de carbono R$: {venda:,.2f}')
print(f'Este é o quanto você gasta de pneus no ano : {(quilometros_dirigidos * 12) / 50000} ') #50000 é a media da vida útil do pneu
