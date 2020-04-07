from flask import Flask,render_template,url_for,request,redirect

app=Flask(__name__)

logins={}

@app.route("/")
def signin():
    return render_template("sign-in.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['userMail']
        password=request.form['password']
        print (email,password)
    #return redirect(url_for('signin'))
        if logins[email]==password:
            return "Hello you have been logged in"
        else:
            return "Not able to login"

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/newuser",methods=["GET","POST"])
def newuser():
    if request.method=="POST":
        name=request.form['yourName']
        email=request.form['yourMail']
        class_user=request.form['userClass']
        subject=request.form['userSub']
        password=request.form['pass1']
        conf_password=request.form['pass2']
        if request.form.get('check'):
            TandC_read=True
        else:
            TandC_read=False
        print("Name= ",name)
        print("email= ",email)
        print("Class= ",class_user)
        print("Subject= ",subject)
        print("Password= ",password)
        print("Confirm Passord= ",conf_password)
        print("Terms and Conditions= ",TandC_read)
        if email not in logins.keys() and password==conf_password:
            logins[email]=password
        if password != conf_password:
            return "Passwords do not match"
    return redirect(url_for('signin'))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)
