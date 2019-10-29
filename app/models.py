from app import db


class Data(db.Model):
    id = db.Column(db.String(50), primary_key=True, unique = True)
    url= db.Column(db.String(120))
    email = db.Column(db.String(120), index=True)
    state = db.Column(db.String(12))
    md5_hash = db.Column(db.String(128))
    

    def __repr__(self):
        return "<Data {}>".format(self.email) 