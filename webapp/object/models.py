from webapp.db import db


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    img = db.Column(db.LargeBinary, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    starting_price = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f'<objects {self.id}>'
