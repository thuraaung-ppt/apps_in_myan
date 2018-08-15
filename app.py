
from flask import Flask , render_template, request
import os 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "appdatabase.db"))


app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "Apps in Myanmar"
db = SQLAlchemy(app)

@app.route('/',methods=['POST','GET'])
def home():

	if request.method == 'POST' :
		# print("Hello")
		# print(request.form['app_name'])
		app_name = request.form['app_name']
		app = App(app_name=app_name)
		db.session.add(app)
		db.session.commit()

	return render_template("index.html")


class App(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	app_name = db.Column(db.String(80),unique=True,nullable=False)

	def __init__(self,*args,**kwargs):
		super(App,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<App %r>' % self.app_name


if __name__ == '__main__':
	app.run(debug=True)