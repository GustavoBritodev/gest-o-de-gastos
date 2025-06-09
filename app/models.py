# from app import db

# class Item(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(100), nullable=False)


from app import db

class FinanceData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    despesa_valor = db.Column(db.Float, nullable=False)
    despesa_peso = db.Column(db.Integer, nullable=False)
    investimento_valor = db.Column(db.Float, nullable=False)
    investimento_taxa = db.Column(db.Float, nullable=False)
    investimento_tempo = db.Column(db.Integer, nullable=False)
    salario_ideal = db.Column(db.Float, nullable=False)
