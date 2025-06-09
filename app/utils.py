def calcular_juros_compostos(principal, taxa_juros, tempo_meses):

    taxa_decimal = taxa_juros / 100
    montante = principal * (1 + taxa_decimal) ** tempo_meses
    return round(montante, 2)


def calcular_media_ponderada(despesas):

    if not despesas:
        return 0.0
    total_peso = sum(peso for valor, peso in despesas)
    soma_ponderada = sum(valor * peso for valor, peso in despesas)
    if total_peso == 0:
        return 0.0
    return round(soma_ponderada / total_peso, 2)


def somar_montantes(investimentos):

    total = 0.0
    for valor, taxa, tempo in investimentos:
        montante = calcular_juros_compostos(valor, taxa, tempo)
        total += montante
    return round(total, 2)


def calcular_salario_ideal(media_despesas, total_lucros, margem=0.10):

    resultado = (media_despesas - total_lucros) * (1 + margem)
    return round(resultado, 2) if resultado > 0 else 0.0


def gerar_projecoes(salario_ideal):

    return {
        "Diário": round(salario_ideal / 30, 2),
        "Semanal": round(salario_ideal / 4, 2),
        "Mensal": round(salario_ideal, 2),
        "Anual": round(salario_ideal * 12, 2),
    }


def calcular_fluxo_financeiro(despesas, investimentos):

    media_despesas = calcular_media_ponderada(despesas)
    total_lucros = somar_montantes(investimentos)
    salario = calcular_salario_ideal(media_despesas, total_lucros)
    projecoes = gerar_projecoes(salario)

    return {
        "media_despesas": media_despesas,
        "total_lucros": total_lucros,
        "salario_ideal": salario,
        "projecoes": projecoes
    }

