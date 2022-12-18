from flask import Flask


from .blueprints import BlueprintsRegistrator


class FlaskApplication:

    def __init__(self):
        self.flaskApp = Flask(__name__)

        self.register_blueprints()
    def __configurate(self):
        pass

    def register_blueprints(self):
        BlueprintsRegistrator(self.flaskApp)

    def run(self):
        self.flaskApp.run()