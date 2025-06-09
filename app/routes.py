# from flask import request, redirect, url_for, render_template
# from app import app, db
# from app.models import Item

# @app.route('/')
# def index():
#     items_ = Item.query.all()
#     return render_template('index.html', items=items_)

# @app.route('/create', methods=['GET', 'POST'])
# def create():
#     if request.method == 'POST':
#         name = request.form['name']
#         description = request.form['description']
#         new_item = Item(name=name, description=description)
#         db.session.add(new_item)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('create.html')

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     item = Item.query.get_or_404(id)
#     if request.method == 'POST':
#         item.name = request.form['name']
#         item.description = request.form['description']
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('update.html', item=item)

# @app.route('/delete/<int:id>')
# def delete(id):
#     item = Item.query.get_or_404(id)
#     db.session.delete(item)
#     db.session.commit()
#     return redirect(url_for('index'))

from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import FinanceData
from app.utils import calcular_juros_compostos, calcular_media_ponderada, calcular_salario_ideal, calcular_fluxo_financeiro

@app.route('/')
def index():
    dados = FinanceData.query.all()
    return render_template('index.html', dados=dados)

# @app.route('/create', methods=['GET', 'POST'])
# def create():
#     if request.method == 'POST':
#         nome = request.form['nome']

#         # Coletar despesas
#         despesas = []
#         for i in range(1, 4):
#             valor = request.form.get(f'despesa{i}')
#             peso = request.form.get(f'peso{i}')
#             if valor and peso:
#                 despesas.append((float(valor), int(peso)))

#         # Coletar investimentos
#         investimentos = []
#         for i in range(1, 4):
#             valor = request.form.get(f'inv_valor{i}')
#             taxa = request.form.get(f'inv_taxa{i}')
#             tempo = request.form.get(f'inv_tempo{i}')
#             if valor and taxa and tempo:
#                 montante = calcular_juros_compostos(float(valor), float(taxa), int(tempo))
#                 investimentos.append(montante)

#         total_despesas = calcular_media_ponderada(despesas)
#         total_lucros = sum(investimentos)
#         salario = calcular_salario_ideal(total_despesas, total_lucros)

#         novo = FinanceData(
#             nome=nome,
#             despesa_valor=total_despesas,
#             despesa_peso=1,
#             investimento_valor=total_lucros,
#             investimento_taxa=0,
#             investimento_tempo=0,
#             salario_ideal=salario
#         )
#         db.session.add(novo)
#         db.session.commit()
#         return redirect(url_for('index'))

#     return render_template('create.html')

@app.route('/delete/<int:id>')
def delete(id):
    dado = FinanceData.query.get_or_404(id)
    db.session.delete(dado)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nome = request.form['nome']

        # Coletar despesas dinâmicas
        despesas = []
        for key in request.form:
            if key.startswith("despesa_valor_"):
                idx = key.split("_")[-1]
                valor = float(request.form.get(f"despesa_valor_{idx}", 0))
                peso = int(request.form.get(f"despesa_peso_{idx}", 1))
                despesas.append((valor, peso))

        # Coletar investimentos
        investimentos = []
        for key in request.form:
            if key.startswith("investimento_valor_"):
                idx = key.split("_")[-1]
                valor = float(request.form.get(f"investimento_valor_{idx}", 0))
                taxa = float(request.form.get(f"investimento_taxa_{idx}", 0))
                tempo = int(request.form.get(f"investimento_tempo_{idx}", 0))
                investimentos.append((valor, taxa, tempo))

        # Aplicar fluxo financeiro completo
        resultados = calcular_fluxo_financeiro(despesas, investimentos)

        #    Salvar no banco apenas o resumo (como antes)
        novo = FinanceData(
            nome=nome,
            despesa_valor=resultados['media_despesas'],
            despesa_peso=1,
            investimento_valor=resultados['total_lucros'],
            investimento_taxa=0,
            investimento_tempo=0,
            salario_ideal=resultados['salario_ideal']
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('create.html')
