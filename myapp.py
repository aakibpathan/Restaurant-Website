from flask import *

from mydata import addEmp, loginvalidation, selectAllEmp

f = Flask(__name__)

@f.route('/')
def home():
	return render_template('rest.html')

@f.route('/home2')
def home2():
	return render_template('home2.html')

@f.route('/reg')
def register():
	return render_template('reg.html')

@f.route('/rest')
def restaurent():
	return render_template('rest.html')

@f.route('/contact')
def cont():
	return render_template('contact.html')

@f.route('/about')
def about():
	return render_template('about.html')

@f.route('/addEmp', methods=["POST"])
def add_emp():
	fname = request.form["fname"]
	lname = request.form["lname"]
	contact = request.form["contact"]
	uname = request.form["uname"]
	passw = request.form["pass"]

	t = (fname, lname , contact, uname, passw)
	addEmp(t)
	return redirect('/home2')

@f.route("/loginvalidation",methods=["POST"])
def login_validation():
	uname=request.form.get('email')
	passw=request.form.get('passw')

	a=(uname,passw)
	el=loginvalidation(a)

	if len(el)>0:
		return render_template("rest.html",users="el")

	else:
		return render_template("home2.html", users="el")

@f.route('/admin')
def emp_list():
	el = selectAllEmp()

	return render_template('admin.html',elist=el)


if (__name__ == '__main__'):
	f.run(debug=True)