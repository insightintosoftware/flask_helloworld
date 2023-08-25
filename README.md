# flask_helloworld



### Summary

* This is a simple Hello World app designed to be used for other projects.
* This python project was created for Windows environment. You can follow instructions in "How this project was created" section to create your project in Linux environment.
* As a prerequisite, you should have Python 3 installed.



### How to run this app

1. Clone this app.
2. Go inside hello_world directory
3. Run `Scripts\activate` to activate virtual environment.
4. Run `pip install -r requirements.txt`
5. Run `python app.py`
6. In your browser, go to http://127.0.0.1:8080/ and see "Hello, World!"



### How this project was created

1. Created hello_world directory and went inside.
2. Ran `python -m venv .` 
3. Ran `Scripts\activate`
4. Ran `pip install flask`
5. Ran `pip freeze > requirements.txt`
6. Created app.py





### Hot to use cProfile

#### Set up

* You don't need to install anything. Just run the code with cProfile wrapped around it.

```
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
```

#### Visualize profile data with snakeviz

* Then install snakeviz and run snakeviz command

* ```
  pip install snakeviz
  snakeviz flask_app.prof
  ```

* This will bring up a website with visualization of flask_app.prof file.

#### Visualize profile data with gprof2dot

* Install gprof2dot. This is a tool that converts *.prof to *.dot file.

* ```
  pip install gprof2dot
  gprof2dot -f pstats flask_app.prof -o flask_app.dot
  ```

* Download and install Graphviz for Windows. Use the following command to convert *.dot to *.png

* ```
  dot -Tpng flask_app.dot -o flask_app.png
  ```



## How to use line profiler

