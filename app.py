import sentry_sdk
from flask import Flask

sentry_sdk.init(
    dsn="https://4cbbfabe1a71b1bb4408e6669a462a1a@o4505365730885632.ingest.sentry.io/4506424530436096",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    1/0  # raises an error
    return "<p>Hello, World!</p>"

@app.route("/works")
def works():
    return "<p>This works</p>"

@app.route("/error")
def error():
    raise Exception


