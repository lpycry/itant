from flask import Blueprint, request, url_for, redirect, render_template, flash

admin = Blueprint('admin',__name__,template_folder="templates")
@admin.route("/")
@admin.route("/login")
def login():
    return render_template('home.html')
@admin.route("/signup")
def signup():
    return "signup"
@admin.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404