#coding=utf-8
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

blog_page = Blueprint('blog_page', __name__, template_folder='templtes')

@blog_page.route('/')
def hello():
    return "Hello World测试!"

@blog_page.route('/test/<int:test_id>')
def test(test_id):
    return "url input id:%d" % test_id