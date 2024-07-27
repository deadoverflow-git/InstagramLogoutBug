from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('https://instagram.com/accounts/logout')

app.run()