from flask import Flask, render_template, request, redirect, url_for,session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime 
import os


app = Flask(__name__)
app.secret_key = 'jyoti23'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:psql@localhost/facebook'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER']='static/uploads'

db = SQLAlchemy(app)

class Loginn(db.Model):
    email = db.Column(db.String(50), primary_key=True)
    user = db.Column(db.String(50))
    password = db.Column(db.String(50))
    date=db.Column(db.Date,nullable=False)
    gender=db.Column(db.String)
    user_posts = db.relationship('Post1', backref='user', lazy=True)  # Change the backref name

# ... (rest of your code remains the same)

    #created_at=db.Column(db.DateTime,default=datetime.utcnow)

@app.route('/')
def coder():
    return render_template("coder.html")
@app.route('/login')
def login():
    return render_template('login.html')


# @app.route('/check_login', methods=['POST'])
# def check_login():
#     email = request.form.get("email")
#     password=request.form.get("password")
#     existing_user = Loginn.query.filter_by(email=email,password=password).first()

#     if existing_user:
#         return redirect(url_for("home"))
#     else:
#         return redirect(url_for("singin"))

@app.route('/check_login', methods=['POST'])
def check_login():
    email = request.form.get("email")
    password = request.form.get("password")
    existing_user = Loginn.query.filter_by(email=email, password=password).first()

    if existing_user:
        session['email'] = email  # Store email in the session
        return redirect(url_for("home"))
    else:
        return redirect(url_for("singin"))
    

@app.route('/singin', methods=['GET','POST'])
def singin():
    if request.method == 'POST':
        email = request.form.get("email")
        user = request.form.get("user")
        password = request.form.get("password")
        date=request.form.get("date")
        gender=request.form.get("gender")  #psw=psw
        new_login = Loginn(email=email, user=user, password=password,date=date,gender=gender)
        db.session.add(new_login)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("singin.html")

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form.get("email")
        new_password = request.form.get("new_password")
        user = Loginn.query.filter_by(email=email).first()

        if user:
            user.password = new_password
            db.session.commit()

            return redirect(url_for("login"))
        else:
            return "User not found"

    return render_template("reset_password.html")
class Post1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    photo_filename = db.Column(db.String(100))
    description = db.Column(db.String(200))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    user_email = db.Column(db.String(50), db.ForeignKey('loginn.email'), nullable=False)
    user_related_posts = db.relationship('Loginn', foreign_keys=[user_email], backref=db.backref('user_posts1', lazy=True))  # Change the backref name

# ... (rest of your code remains the same)


@app.route('/post_data', methods=['POST'])
def post_data():
    post_content = request.form.get("post_content")
    post_description = request.form.get("post_description")
    post_photo = request.files.get("post_photo")  # Use request.files to get the uploaded file

    email = session.get('email')  # Get user's email from session

    if post_photo:
        filename = secure_filename(post_photo.filename)
        post_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_post = Post1(content=post_content, description=post_description, photo_filename=filename, user_email=email)  # Set the user_email
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("home")) 
    return redirect(url_for('home')) 



    #return redirect(url_for("home"))  # Redirect to the home page after posting
# @app.route('/home')
# def home():
#     return render_template("home.html")
@app.route('/home')
def home():
    email = session.get('email')
    
    if email:
        user_data = Loginn.query.filter_by(email=email).first()
        if user_data:
            user_posts = Post1.query.filter_by(user_email=email).all()

            return render_template("home.html", user=user_data.user, user_data=user_data, posts=user_posts  )
        else:
            return "User data not found"
    else:
        return redirect(url_for("login"))
@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post_to_delete = Post1.query.get(post_id)
    
    if post_to_delete:
        db.session.delete(post_to_delete)
        db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
