from flask import Flask, render_template, url_for, request, redirect
import csv

# we'll use a new folder. you can fix this one by just choosing the correct tags
app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def home():
    return render_template('index.html') 
    # this file must be in templates folder

# now, to ditch all that for a more dynamic means
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)
# much  easier

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email= data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline= '') as database2:
        email= data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(database2, delimiter=',' , quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # delimiter is what starts a new column
        # quotechar is quote character. any quotes around the characters? cannot be empty
        # quoting to instruct python to quote select fields
        # QUOTE_MINIMAL to quote only special feilds with either delimiter or quotechar
        csv_file.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        try:
            data= request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "error saving data"
    else:
        return 'something went wrong. retry please'
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)
    







# @app.route("/components.html")
# def components():
#     return render_template('components.html') 

# @app.route("/about.html")
# def about():
#     return render_template('about.html')


# @app.route("/works.html") # this needs to reflect in html
# def works(): # default name until...
#     return render_template('works.html') 
# #name parameter is in html

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/work.html")
# def work():
#     return render_template('work.html')


# @app.route("/favicon.ico")
# def icon():
#     return 
