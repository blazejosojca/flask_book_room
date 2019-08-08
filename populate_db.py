from app import create_app, db
from datetime import datetime
from app.models import User, Booking, Department, Position, Room


app = create_app()
# add Department
dep1=Department(id=1,department_name='Admin')
db.session.add(dep1)
dep2=Department(id=2,department_name='Business')
db.session.add(dep2)
dep3=Department(id=3,department_name='Support')
db.session.add(dep3)
dep4=Department(id=4,department_name='Devs')
db.session.add(dep4)
dep5=Department(id=5,department_name='HR')
db.session.add(dep5)
dep6=Department(id=6,department_name='Test')
db.session.add(dep6)

# add Position
pos1=Position(id=1,position_name='Intern')
db.session.add(pos1)
pos2=Position(id=2,position_name='Junior')
db.session.add(pos2)
pos3=Department(id=3,position_name='Regular')
db.session.add(pos3)
pos4=Position(id=4,position_name='Senior')
db.session.add(pos4)
pos5=Department(id=5,position_name='Specialist')
db.session.add(pos5)
pos6=Position(id=6,position_name='Team Leader')
db.session.add(pos6)
pos7=Department(id=7,position_name='Boss')
db.session.add(pos7)
pos8=Position(id=8,position_name='CEO')
db.session.add(pos8)
pos9=Department(id=9,position_name='Lord')
db.session.add(pos9)

# add Users
# add admin & users
admin=User(id=1, first_name='John', second_name='Doe', email='admin@mail.com', mobile_phine='666777888', position_id=1,department_id=1)
admin.set_password('123')
db.session.add(admin)

db.commit()
