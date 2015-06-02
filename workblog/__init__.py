#coding=utf-8
from flask import Flask, redirect, render_template

from blog.view import blog_page

app = Flask(__name__)
app.register_blueprint(blog_page, url_prefix='/blog')

@app.route('/')
@app.route('/index')
def index():
    return redirect('/blog')    #redirect重定向url

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)