from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import functions

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dibyanshu69@localhost/height_data'

db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120),unique=True)
    height_=db.Column(db.Integer)
    
    def __init__(self,email_,height_):
        self.email_ = email_
        self.height_ = height_
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        print(email, height)
        send_email(email,height)
        if db.session.query(Data).filter(Data.email_ == email).count()==0:
            
            data = Data(email, height)
            with app.app_context():
                db.create_all()  # Create database tables if they don't exist
                db.session.add(data)
                db.session.commit()
                average_height=db.session.query(functions.avg(Data.height_))
            return render_template('success.html')
    return render_template('index.html',text="Seems like u have entered the email already !!")

if __name__ == "__main__":
    app.run(debug=True)
