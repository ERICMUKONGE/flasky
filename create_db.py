from app.models import Role,User
from app.exts import db
from app import create_app
from app.models import User,Role
from werkzeug.security import generate_password_hash

app = create_app('development')

with app.app_context():
    db.create_all()

    user =User(  
         username ="muknoge123",
        email="mukonge123@gmail.com",
        password_hash=generate_password_hash('password'))

    db.session.add(user)
    db.session.commit()