from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!!"


# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True,host='0.0.0.0',port=port)


if 'OPENSHIFT_APP_NAME' in os.environ:              #are we on OPENSHIFT?
    ip = os.environ['OPENSHIFT_PYTHON_IP']
    port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
else:
    ip = '0.0.0.0'                            #localhost
    port = 8051

app.run(debug=True,host='0.0.0.0',port=port)