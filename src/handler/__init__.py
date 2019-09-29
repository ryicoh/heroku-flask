from flask import Flask
import handler.hello

app = Flask(__name__)

app.register_blueprint(hello.bp)

