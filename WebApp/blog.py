'''
# Sample Python WebApp to be deployed on Google cloud
'''
from flask import Flask, render_template

blog = Flask(__name__)

@blog.route('/')
def welcome():
    # return 'Hello World from John :)'
    return render_template('welcome.html')

@blog.route('/about/')
def about():
    # return 'Hello World from John :)'
    return render_template('about.html')

if __name__ == '__main__':
    blog.run(host='127.0.0.1', port=7770, debug=True)
