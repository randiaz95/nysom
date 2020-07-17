from app1 import db

class Contact(db.Model):
    __tablename__= 'contacts'

    id = db.Column('id', db.Integer, primary_key=True)
    firstname = db.Column('firstname', db.String)
    lastname = db.Column('lastname', db.String)
    email = db.Column('email', db.String)
    notes = db.Column('notes', db.String)

    def __repr__(self):
        return f"<Contact {self.firstname} {self.lastname}: {self.email}"