from app.main import bp

@bp.route("/")
@bp.route("/home")
def home():
    return "Hello in my rooms!"
