from extensions import db
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    table_name = 'users'
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)