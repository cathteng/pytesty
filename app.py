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
    i = 0
    j = 1
    k = 2
    l = 3
    # this will print to the server
    print(i/j)
    print(k == 3)
    print(k*l)
    j/i  # raises an error
    return "<p>Hello, World!</p>"

@app.route("/works")
def works():
    # Lorem ipsum dolor sit amet, consectetur 
    # adipiscing elit. Vestibulum commodo nunc 
    # vitae lacus molestie fringilla. Aenean 
    # luctus magna nec tempus bibendum. Etiam 
    # molestie, neque at efficitur placerat, nibh 
    # orci tincidunt mi, fermentum blandit ligula 
    # mi luctus tellus. Nullam venenatis diam 
    # ultricies, euismod ex sed, suscipit turpis. 
    # Vivamus porta augue magna, at consequat leo 
    # molestie at. In non sollicitudin massa, in 
    # tincidunt ipsum. Aliquam erat volutpat. 
    # Mauris tortor sem, lacinia nec viverra eget, 
    # sollicitudin sit amet diam. Pellentesque a 
    # nulla a ante blandit sagittis. 
    return "<p>Changing the text</p>"

@app.route("/error")
def error():
    # raises an UnboundLocalError
    raise UnboundLocalError()


