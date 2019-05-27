import gc
import random
from functools import wraps

import dateutil.parser
import flask
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from flask import Flask, flash, render_template, request, session, redirect, url_for, json
from flask_login import LoginManager
from flask_mail import Mail, Message
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename

import sample_application.functiontest
from flask_adminlte import AdminLTE

app = Flask(__name__)
login = LoginManager(app)


class User(object):
    """
    Example User object.  Based loosely off of Flask-Login's User model.
    """
    full_name = "Fusion Informatics"
    avatar = "/static/img/fusion.jpg"
    created_at = dateutil.parser.parse("November 12, 2016")


def create_app(configfile=None):
    app = Flask(__name__)
    AdminLTE(app)

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'resume_store'

    mysql = MySQL(app)

    # This is a placeholder user object.  In the real-world, this would
    # probably get populated via ... something.
    current_user = User()

    app.config.update(
        DEBUG=True,
        # EMAIL SETTINGS
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME='mohitptl51@gmail.com',
        MAIL_PASSWORD='raqewbbrqvnvjqcg'
    )
    mail = Mail(app)

    global val3
    val3 = []
    global h
    h = []

    global x, y, size, lab, col, gradd
    x, y, size, lab, col, gradd = 0, 0, 0, [], "", ""

    @app.route('/send-mail/', methods=['GET', 'POST'])
    def send_mail():
        try:

            global username
            username = request.form['email']

            for x in range(10):
                j = (random.randint(95, 122))
                j = chr(j)
                h.append(j)
            h[0] = "/"
            # ...
            # m=base64.b64encode(bytes(username, 'utf-8')
            m = encode_utf8(username)
            link = "http://127.0.0.1:5000/resetpassword/" + m + str(''.join(h))
            alert = "we have sent you an email"
            msg = Message("Your Request to Generate New Password",
                          sender="mohitptl51@gmail.com",
                          recipients=["mohitptl51@gmail.com"])

            msg.body = 'Hello ' + username + ',\nYou or someone else has requested that a new password be generated for your account. If you made this request, then please follow this link:' + link

            mail.send(msg)
            return render_template('forget.html', current_user=current_user, error=alert, username=username, link=link)

        except Exception as e:
            return (str(e))

    def login_required(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if 'logged_in' in session:
                return f(*args, **kwargs)
            else:
                print("You need to login first")
                return redirect(url_for('home'))

        return wrap

    @app.route("/logout")
    @login_required
    def logout():
        session.clear()
        session['logged_in'] = False
        flash("You have been logged out!")
        gc.collect()
        session.pop('username', None)
        return redirect(url_for('home'))

    @app.route('/signUpUser', methods=['GET', 'POST'])
    def signUpUser():
        if request.method == 'POST':
            name = session.get('username')
            print(name)
            password = request.form['opassword'];
            print(password)
            cur = mysql.connection.cursor()
            # cur.execute("INSERT INTO record(name,password) VALUES(%s,%s)", (name, password))
            cur.execute("SELECT password FROM record WHERE name LIKE %s", (name,))

            row = cur.fetchall()
            stre = str(row[0])
            stre = stre.replace("(", "")
            stre = stre.replace(")", "")
            stre = stre.replace(",", "")
            stre = stre.replace("'", "")
            print(stre)
            if (password == stre):
                print("true")
                return json.dumps({'sucess': 'Please Enter New Password'});
            else:

                return json.dumps({'status': 'Incorrect password!', 'pass': password});

    @app.route('/')
    @login_required
    def index():
        if not session.get('logged_in'):
            return redirect('login')
        else:
            return render_template('index.html', current_user=current_user)

    @app.route('/resetpassword/<name>/<hash>', methods=['GET', 'POST'])
    def reset(name, hash):
        name = str(name)
        g = str(''.join(h))
        name = name.replace(g, '')
        if request.method == 'POST':
            userdetails = request.form
            password = userdetails['password']
            global error
            error = None
            rpassword = userdetails['rpass']
            cur = mysql.connection.cursor()
            # cur.execute("INSERT INTO record(name,password) VALUES(%s,%s)", (name, password))
            cur.execute("SELECT name FROM record where email LIKE %s", (name,))

            row = cur.fetchall()
            print(row)

            if (len(row) == 0):
                error = "we dont find any User!"
                return render_template('resetpassword.html', error=error)

            else:
                if password == rpassword:
                    if len(password) >= 8:
                        caps = str.upper(password)
                        print(caps, password)
                        if (any(x.isupper() for x in password) and any(x.islower() for x in password)
                                and any(x.isdigit() for x in password) and len(password) >= 8):
                            cur = mysql.connection.cursor()
                            cur.execute("Update record SET password=(%s)  where email like (%s) ", (password, name))
                            mysql.connect.commit()
                            cur.close()
                            return redirect(url_for('home', error="You can now try to log in!"))

                        else:
                            error = "Password should be contain atleast 1 captital 1 lower 1 number and 1 special charater character!"
                            return render_template('resetpassword.html', error=error)

                    else:
                        error = "Password should be atleast 8 characters long!"
                        return render_template('resetpassword.html', error=error)

                else:

                    error = "Password does not match!"
                    return render_template('resetpassword.html', error=error)

        return render_template('resetpassword.html', current_user=current_user)

    @app.route('/changepassword', methods=['GET', 'POST'])
    @login_required
    def changepass():

        # cur = mysql.connection.cursor()
        if request.method == 'POST':
            userdetails = request.form
            print(current_user)
            name = session.get('username')
            password = userdetails['password']
            global error
            error = None
            rpassword = userdetails['rpass']
            cur = mysql.connection.cursor()
            # cur.execute("INSERT INTO record(name,password) VALUES(%s,%s)", (name, password))
            cur.execute("SELECT * FROM record where name LIKE %s", (name,))

            row = cur.fetchall()
            print(row)

            if (len(row) == 0):
                error = "we dont find any User!"
                return render_template('changepassword.html', error=error)

            else:
                if password == rpassword:
                    if len(password) >= 8:
                        caps = str.upper(password)
                        print(caps, password)
                        if (any(x.isupper() for x in password) and any(x.islower() for x in password)
                                and any(x.isdigit() for x in password) and len(password) >= 8):

                            cur = mysql.connection.cursor()
                            cur.execute("Update record SET password=(%s)  where name like (%s) ", (password, name))
                            mysql.connect.commit()
                            cur.close()
                            session['logged_in'] = False
                            session['username'] = ''
                            return redirect(url_for('home'))

                        else:
                            error = "Password should be contain atleast 1 captital 1 lower 1 number and 1 special charater character!"
                            return render_template('changepassword.html', error=error)

                    else:
                        error = "Password should be atleast 8 characters long!"
                        return render_template('changepassword.html', error=error)

                else:

                    error = "Password does not match!"
                    return render_template('changepassword.html', error=error)

        return render_template('changepassword.html', current_user=current_user)

    labels = [
        'JAN', 'FEB', 'MAR', 'APR',
        'MAY', 'JUN', 'JUL', 'AUG',
        'SEP', 'OCT', 'NOV', 'DEC'
    ]

    value2 = [40, 30, 60]

    # @app.route('/login',methods=['POST'])
    # def login():
    #    if request.form['password'] == 'password' and request.form['username'] == 'admin':
    #            session['logged_in'] = True
    #  return render_template('login.html',current_user=current_user)
    @app.route('/index2')
    def index2():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            legend = 'Monthly Data'
            labelss = labels
            valuess = value2
            return render_template('index2.html', current_user=current_user, max=17000, values=valuess, labels=labelss,
                                   legend=legend)

    @app.route('/testing')
    @login_required
    def testing():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            bar_labels = labels
            bar_values = value2
            return render_template('testing.html', current_user=current_user, max=17000, labels=bar_labels,
                                   values=bar_values)

    @app.route('/forget', methods=['GET', 'POST'])
    def forget():

        alert = "Reset code was sent to your email."
        if request.method == 'POST':
            return render_template('forget.html', current_user=current_user, error=alert)

        return render_template('forget.html', current_user=current_user)

    @app.route('/login', methods=['GET', 'POST'])
    def home():

        error = None
        if request.method == 'POST':

            userdetails = request.form
            if request.form['do'] == 'log':

                name = userdetails['username']
                password = userdetails['password']
                cur = mysql.connection.cursor()
                # cur.execute("INSERT INTO record(name,password) VALUES(%s,%s)", (name, password))
                cur.execute("SELECT * FROM record where name=%s and password = %s", (name, password))
                row = cur.fetchall()
                if (len(row) == 0):
                    error = 'Invalid Credentials. Please try again.'
                    return render_template('login.html', error=error)
                else:
                    session['logged_in'] = True
                    session['username'] = request.form['username']
                    return redirect('/')
                mysql.connect.commit()
                cur.close()
                # return redirect('/')
            elif request.form['do'] == 'reg':
                return redirect(url_for('register'))
        return render_template('login.html')

    @app.route("/forward/", methods=['POST'])
    def move_forward():
        # Moving forward code
        forward_message = "Moving Forward..."
        return render_template('register.html', message=forward_message, current_user=current_user);

    @app.route("/forwa/", methods=['GET', 'POST'])
    def move_forwa():
        # Moving forward code
        forward_message = " Invalid Credentials. Please try again!"
        return render_template('login.html', error=forward_message, message=forward_message);

    @app.route("/forw/", methods=['GET', 'POST'])
    def move_forw():
        # Moving forward code
        forward_messag = " Invalid Credentials. Please try again!"

        return redirect(url_for('register', error=forward_messag));

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        # cur = mysql.connection.cursor()
        if request.method == 'POST':
            userdetails = request.form
            name = userdetails['username']
            password = userdetails['password']
            email = userdetails['email']
            global error
            error = None
            rpassword = userdetails['rpass']
            cur = mysql.connection.cursor()
            # cur.execute("INSERT INTO record(name,password) VALUES(%s,%s)", (name, password))
            cur.execute("SELECT * FROM record where name LIKE %s", (name,))

            row = cur.fetchall()

            if (len(row) != 0):
                error = "Username already exist!Pick another"
                return render_template('register.html', error=error)

            else:
                if '@' not in email:
                    error = "Invalid Email email must contain "'@'""
                    return render_template('register.html', error=error)

                if '.' not in email:
                    error = "Invalid Email email must contain "'.'""
                    return render_template('register.html', error=error)

                if password == rpassword:
                    if len(password) >= 8:
                        caps = str.upper(password)
                        for i in password:
                            for j in caps:
                                if i != j:
                                    error = "Password should be contain atleast 1 captital 1 lower 1 number and 1 special charater character!"
                                    return render_template('register.html', error=error)

                        cur = mysql.connection.cursor()
                        cur.execute("INSERT INTO record(name,password) VALUES(%s,%s)", (name, password))
                        mysql.connect.commit()
                        cur.close()
                        return redirect('/login')
                    else:
                        error = "Password should be atleast 8 characters long!"
                        return render_template('register.html', error=error)

                else:

                    error = "Password does not match!"
                    return render_template('register.html', error=error)

        return render_template('register.html')
    
    @app.route('/bokeh2')
    def bokeh2():
        import pandas as pd
        from bokeh.plotting import figure

        data = {'Cities': {'Des_Moines': 80.0, 'Lubbock': -300.0, 'Minneapolis': 85.7,
                           'Orange_County': 80.0, 'Salt_Lake_City': 81.8, 'San_Diego': 80.0,
                           'San_Francisco': -400.0, 'Troy': -400.0, 'Wilmington': -300.0}}
        # df_data = pd.DataFrame(data).sort_values('Cities', ascending=False)
        df_data = pd.DataFrame(data).sort_values('Cities', 0, False)

        this_series = df_data.loc[:, 'Cities']

        p = figure(width=600, height=400, y_range=this_series.index.tolist())

        p.background_fill_color = "white"

        p.grid.grid_line_alpha = 1.0
        p.grid.grid_line_color = "white"

        p.xaxis.axis_label = 'xlabel'
        p.xaxis.axis_label_text_font_size = '9pt'
        p.xaxis.major_label_text_font_size = '9pt'
        # p.x_range = Range1d(0,50)
        # p.xaxis[0].ticker=FixedTicker(ticks=[i for i in xrange(0,5,1)])

        p.yaxis.major_label_text_font_size = '9pt'
        p.yaxis.axis_label = 'ylabel'

        p.yaxis.axis_label_text_font_size = '9pt'
        p.y_range.range_padding = 0.1

        j = 1
        for k, v in this_series.iteritems():
            print(k, v, j)

            p.rect(x=v / 2, y=j, width=abs(v), height=0.4, color=(76, 114, 176),
                   width_units="data", height_units="data")
            j += 1

        # init a basic bar chart:
        # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars

        # grab the static resources
        js_resources = INLINE.render_js()
        css_resources = INLINE.render_css()

        # render template
        script, div = components(p)
        html = render_template(
            'grade.html', current_user=current_user,
            plot_script=script,
            plot_div=div,
            js_resources=js_resources,
            css_resources=css_resources,
        )
        return encode_utf8(html)

    @app.route('/pending')
    def pending():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM resume_master WHERE status='drop case'")
            if result > 0:
                userdetail = cur.fetchall()
                # return "hello"
                # return render_template('user.html', userdetail=userdetail)
                return render_template('pending.html', userdetail=userdetail, current_user=current_user)
            return render_template('pending.html', current_user=current_user)

    @app.route('/completed')
    def completed():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM resume_master WHERE status='completed'")
            if result > 0:
                userdetail = cur.fetchall()
                # return "hello"
                # return render_template('user.html', userdetail=userdetail)
                # return render_template('pending.html', userdetail=userdetail, current_user=current_user)
                return render_template('completed.html', current_user=current_user, userdetail=userdetail)
            return render_template('completed.html', current_user=current_user)

    @app.route('/parsedwitherror')
    def parsedwitherror():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM resume_master WHERE status='parsed with error'")
            if result > 0:
                userdetail = cur.fetchall()
                # return "hello"
                # return render_template('user.html', userdetail=userdetail)
                # return render_template('pending.html', userdetail=userdetail, current_user=current_user)
                return render_template('parsedwitherror.html', current_user=current_user, userdetail=userdetail)
            return render_template('parsedwitherror.html', current_user=current_user)

        # return render_template('parsedwitherror.html', current_user=current_user)

    @app.route('/lockscreen')
    def lockscreen():
        return render_template('lockscreen.html', current_user=current_user)

    UPLOAD_FOLDER = 'E:/flask/sample_application/uploads/'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @app.route('/uploader', methods=['GET', 'POST'])
    def upload_file():

        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                import os
                flash('No file part')
                print("nothing")
                file = request.files['files[]']
                print("file=:", file)

                uploaded_files = flask.request.files.getlist("files[]")
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                global grad, score, co, en, bk, poqu, soof, exin, stfl, sk
                grad, score, co, en, bk, poqu, soof, exin, stfl, sk = "", 0, 0, 0, 0, 0, 0, 0, 0, []

                grad, score, co, en, bk, sk, poqu,soof,exin,stfl = functiontest.function_test(
                    r"\{0}".format(filename))

                for i in sk:
                    lab.append(i)
                gradd, score = grad, score
                return redirect(url_for('upload_file',
                                        filename=filename)),"File uploaded"

                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                print('n2')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                import os
                print("inside")
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                functiontest.function_test(r"\{0}".format(filename))

                return redirect(url_for('upload_file',
                                        filename=filename))

        return render_template('grade.html', current_user=current_user, grade=grad)

    @app.route('/mainindex', methods=['GET', 'POST'])
    def mainindex():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            return render_template('mainindex.html', current_user=current_user)

    @app.route('/add_resume')
    def add_resume():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            return render_template('add_resume.html', current_user=current_user)

    @app.route('/grade')
    def grade():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            valu = []
            valu.extend((poqu, soof, exin, stfl))
            valuess = valu
            valuee = value2
            for i in range(0, int(len(lab))):
                x = random.randrange(-100, 100)
                y = random.randrange(-100, 100)
                size = random.randrange(600, 2000)
                col = '"sandybrown"'
                label = "label"

                color = r"color"

                val3.append(([x, y, size, lab[i]]))

            grade = grad
            print("grad",grad)
            print(grade)
            scor2=""
            scor = score
            if scor<=100 and  scor>=95:
                scor=100
                scor2="Very Excellent!"
            elif scor<95 and scor>=90:
                scor=95
                scor2 = "Excellent!"
            elif scor < 90 and scor >= 85:
                scor = 90
                scor2="Excellent!"
            elif scor < 85 and scor >= 80:
                scor = 85
                scor2 = "Impressive!"
            elif scor < 80 and scor >= 75:
                scor = 80
                scor2 = "Impressive!"
            elif scor < 75 and scor >= 70:
                scor = 75
                scor2 = "Very Good"
            elif scor < 70 and scor >= 65:
                scor = 70
                scor2 = "Good"
            elif scor < 65 and scor >= 60:
                scor = 65
                scor2 = "Good"
            elif scor < 60 and scor >= 55:
                scor = 60
                scor2 = "Average"
            elif scor < 55 and scor >= 50:
                scor = 55
                scor2 = "Average"
            elif scor < 50 and scor >= 45:
                scor = 50
                scor2 = "Average"
            elif scor<45 and scor>=40:
                scor=45
                scor2 = "Average"
            elif scor < 40 and scor >= 35:
                scor = 40
                scor2 = "Could be better"
            elif scor < 35 and scor >= 30:
                scor = 35
                scor2 = "Could be better"
            elif scor < 30 and scor >= 25:
                scor = 30
                scor2 = "Could be better"
            elif scor < 25 and scor >= 20:
                scor = 25
                scor2 = "Could be better"
            elif scor < 20 and scor >= 15:
                scor = 20
                scor2 = "Could be better"
            elif scor < 15 and scor >= 10:
                scor = 15
                scor2 = "Could be better"
            elif scor < 10 and scor >= 0:
                scor = 10
                scor2 = "Could be better"

            computer = co * 2.5
            entertainment = en * 1.5
            bank_loans = bk * 0.5
            le = int(len(val3))
            val2 = []
            val2.extend((computer, entertainment, bank_loans))
            return render_template('grade.html', current_user=current_user, grade=grade, score=scor,score2=scor2,sco=score, values=valuess,
                                   len=le, sk=lab, valuee=val2, bank_loans=bank_loans, computer=computer,
                                   entertainment=entertainment, val3=val3)

    @app.route('/search')
    def search():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM search_master LIMIT 10")
            if result > 0:
                userdetail = cur.fetchall()
                # return "hello"
                # return render_template('user.html', userdetail=userdetail)
                # return render_template('pending.html', userdetail=userdetail, current_user=current_user)
                return render_template('search.html', current_user=current_user, userdetail=userdetail)
            return render_template('search.html', current_user=current_user)

    @app.route('/Rocdetails')
    def Rocdetails():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            return render_template('Rocdetails.html', current_user=current_user)

    @app.route('/bubble')
    def bubble():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            return render_template('bubbleChart.html', current_user=current_user)

    @app.route('/modeldetails')
    def modeldetails():

        if not session.get('logged_in'):
            return redirect('login')
        else:
            return render_template('modeldetails.html', current_user=current_user)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
