from app import db

class User(db.Model):
    id = db.Colummn(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {"id": self.id, "name": self.nome, "email": self.email}