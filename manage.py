from app import app as application
from app.blueprints import blueprint

application.register_blueprint(blueprint)
if __name__ == "__main__"
    application.run(debug=True)