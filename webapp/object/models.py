from webapp.db import db

class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    img = db.Column(db.LargeBinary, nullable=False)
    starting_price = db.Column(db.Integer, nullable=True)
    last_bet = db.Column(db.Integer, nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'<objects {self.id}>'
