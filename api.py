from flask import Flask, request

app = Flask(__name__)


@app.get("/")
def home():
    return "this is home"


@app.get("/sum")
def summer():

    print(type(request.args))
    a = int(request.args["a"])
    b = int(request.args["b"])

    s = 2 * (a + b)

    return f"the sum is {s}"


if __name__ == "__main__":
    app.run("127.0.0.1", port=3000, debug=True)
