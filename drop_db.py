from app.models import Role,User
from app.exts import db
from app import create_app


app = create_app('development')

with app.app_context():
    print("Deleting db")
    db.drop_all()
    print("Done")