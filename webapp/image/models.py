from webapp.db import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column(db.Integer, db.ForeignKey('object.id'))
    link  = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'<images {self.id}>'