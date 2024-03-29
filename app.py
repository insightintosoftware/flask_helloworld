from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

if __name__ == "__main__":
  context = ('DependentCert.pem', 'MyDependentCertPrivate.key')
  app.run(debug=True, host="0.0.0.0", port=8443, ssl_context=context)
