from app import db, create_app
from app.models import User, Room, Department, Position, Booking
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Room': Room,
        'Position': Position,
        'Booking': Booking,
        'Department': Department,
    }

if __name__ == '__main__':
    app.run()