from flask import Flask
import cProfile

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

if __name__ == "__main__":
  context = ('DependentCert.pem', 'MyDependentCertPrivate.key')
  with cProfile.Profile() as pr:
    app.run(debug=True, host="0.0.0.0", port=8443, ssl_context=context)
    pr.dump_stats('flask_app.prof')
