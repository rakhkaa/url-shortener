from flask import Flask, redirect, render_template, request, flash
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"

def generate_code():
  return ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUPWXYZabcdefghijklmnopqrstupwxyz1234567890", k=10))

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    url = request.form['url']
    code = generate_code()
    with open('url.txt', 'a') as f:
      f.write(f"{code}|{url}\n")
      short_url = f'http://localhost:5000/{code}'
      return render_template('index.html', short_url=short_url)
  return render_template('index.html')
  

@app.route("/<code>")
def to_url(code):
  all_url = open('url.txt', 'r').read()
  if code in all_url:
    urls = all_url.split('\n')
    for url in urls:  
      to_url = url.split('|')
      if code in to_url:
        return redirect(to_url[1])
  return render_template('not_found.html')

if __name__ == '__main__':
  app.run(debug=True)
