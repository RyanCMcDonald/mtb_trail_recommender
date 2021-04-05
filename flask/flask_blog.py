from flask import Flask, render_template
# instantiate a Flask instance
app = Flask(__name__)

post = [
    {
        'author':'Corey Shafer',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 1 2021'

    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'April 2 2021'

    }

]
# decorater (handles backend stuff!)
@app.route('/')
@app.route('/home')  # root page of site
def home():
    return render_template('home.html', posts = posts)
@app.route('/about')  # root page of site
def about():
    return render_template('about.html')

# if we run with python directly, otherwise this if-statement will not be true!  Only run in dubug from Python
if __name__ =='__main__':
    app.run(debug = True)
