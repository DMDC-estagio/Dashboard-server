from app import db, timezone, datetime

class Measure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now(timezone('America/Sao_Paulo')))
    voltageMed = db.Column(db.Float)
    currentMed = db.Column(db.Float)
    voltageMAx = db.Column(db.Float)
    currentMAx = db.Column(db.Float)
    voltageMin = db.Column(db.Float)
    currentMin = db.Column(db.Float)