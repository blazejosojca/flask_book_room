from app import db, create_app
from app.models import User, Room
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Room': Room
    }

if __name__ == '__main__':
    app.run()