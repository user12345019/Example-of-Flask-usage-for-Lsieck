# u import flask
from flask import Flask, render_template
#Define app
app = Flask(__name__)

# when the user routes to yoursite.com/
@app.route('/')
#it calls this function (the one directly under it)
def home():
    var1 = "This text is frm in pythin"
    title = "Super cool title"
    #render the template index.html, but with the var text(in the html) = var1(from the python)
    #so instead of sending the index.html, it changes the {{text}} to the var1, so it would change {{text}} to This text is frm in pythin
    return render_template('index.html', text = var1, title=title)

#riun it then
if __name__ == '__main__':
    app.run()