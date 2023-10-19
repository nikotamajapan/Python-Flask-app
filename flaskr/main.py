from flaskr import app
from flask import render_template


@app.route('/')
def index():
    books = [
        {
        'title':'harapeko',
        'price':1000,
        'arrival_day':'2020/7/12'
    },
    {
        'title':'harapeko',
        'price':1000,
        'arrival_day':'2020/7/12'
    }
    ]



    return render_template(
        'index.html',
        books=books
    )

