from flask import Flask, render_template, request, redirect

MP = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  MP.run(port=33507)
