from flask import Flask,render_template,url_for,request,redirect

app=Flask(__name__)

global logins
logins={"prashantarya.juit@gmail.com":"qwerty"}
global qno
qno=0

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
            #return "Hello you have been logged in"
            return redirect(url_for("question1"))
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

@app.route("/question1")
def question1():
    return render_template("Maths-q1.html")

@app.route("/quesAns1",methods=["GET","POST"])
def quesAns1():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question2"))

@app.route("/question2")
def question2():
    return render_template("Maths-q2.html")

@app.route("/quesAns2",methods=["GET","POST"])
def quesAns2():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question3"))

@app.route("/question3")
def question3():
    return render_template("Maths-q3.html")

@app.route("/quesAns3",methods=["GET","POST"])
def quesAns3():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question4"))

@app.route("/question4")
def question4():
    return render_template("Maths-q4.html")

@app.route("/quesAns4",methods=["GET","POST"])
def quesAns4():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question5"))

@app.route("/question5")
def question5():
    return render_template("Maths-q5.html")

@app.route("/quesAns5",methods=["GET","POST"])
def quesAns5():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question6"))

@app.route("/question6")
def question6():
    return render_template("Maths-q6.html")

@app.route("/quesAns6",methods=["GET","POST"])
def quesAns6():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question7"))

@app.route("/question7")
def question7():
    return render_template("Maths-q7.html")

@app.route("/quesAns7",methods=["GET","POST"])
def quesAns7():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question8"))

@app.route("/question8")
def question8():
    return render_template("Maths-q8.html")

@app.route("/quesAns8",methods=["GET","POST"])
def quesAns8():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question9"))

@app.route("/question9")
def question9():
    return render_template("Maths-q9.html")

@app.route("/quesAns9",methods=["GET","POST"])
def quesAns9():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question10"))

@app.route("/question10")
def question10():
    return render_template("Maths-q10.html")

@app.route("/quesAns10",methods=["GET","POST"])
def quesAns10():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question11"))

@app.route("/question11")
def question11():
    return render_template("Maths-q11.html")

@app.route("/quesAns11",methods=["GET","POST"])
def quesAns11():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question11"))

@app.route("/question12")
def question12():
    return render_template("Maths-q12.html")

@app.route("/quesAns12",methods=["GET","POST"])
def quesAns12():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question13"))

@app.route("/question13")
def question13():
    return render_template("Maths-q13.html")

@app.route("/quesAns13",methods=["GET","POST"])
def quesAns13():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question14"))

@app.route("/question14")
def question14():
    return render_template("Maths-q14.html")

@app.route("/quesAns14",methods=["GET","POST"])
def quesAns14():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question15"))

@app.route("/question15")
def question15():
    return render_template("Maths-q15.html")

@app.route("/quesAns15",methods=["GET","POST"])
def quesAns15():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question16"))

@app.route("/question16")
def question16():
    return render_template("Maths-q16.html")

@app.route("/quesAns16",methods=["GET","POST"])
def quesAns16():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question17"))

@app.route("/question17")
def question17():
    return render_template("Maths-q17.html")

@app.route("/quesAns17",methods=["GET","POST"])
def quesAns17():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question18"))

@app.route("/question18")
def question18():
    return render_template("Maths-q18.html")

@app.route("/quesAns18",methods=["GET","POST"])
def quesAns18():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question19"))

@app.route("/question19")
def question19():
    return render_template("Maths-q19.html")

@app.route("/quesAns19",methods=["GET","POST"])
def quesAns19():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question20"))

@app.route("/question20")
def question20():
    return render_template("Maths-q20.html")

@app.route("/quesAns20",methods=["GET","POST"])
def quesAns20():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question21"))

@app.route("/question21")
def question21():
    return render_template("Maths-q21.html")

@app.route("/quesAns21",methods=["GET","POST"])
def quesAns21():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question22"))

@app.route("/question22")
def question22():
    return render_template("Maths-q22.html")

@app.route("/quesAns22",methods=["GET","POST"])
def quesAns22():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question23"))

@app.route("/question23")
def question23():
    return render_template("Maths-q23.html")

@app.route("/quesAns23",methods=["GET","POST"])
def quesAns23():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question24"))

@app.route("/question24")
def question24():
    return render_template("Maths-q24.html")

@app.route("/quesAns24",methods=["GET","POST"])
def quesAns24():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question25"))

@app.route("/question25")
def question25():
    return render_template("Maths-q25.html")

@app.route("/quesAns25",methods=["GET","POST"])
def quesAns25():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question26"))

@app.route("/question26")
def question26():
    return render_template("Maths-q26.html")

@app.route("/quesAns26",methods=["GET","POST"])
def quesAns26():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question27"))

@app.route("/question27")
def question27():
    return render_template("Maths-q27.html")

@app.route("/quesAns27",methods=["GET","POST"])
def quesAns27():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question28"))

@app.route("/question28")
def question28():
    return render_template("Maths-q28.html")

@app.route("/quesAns28",methods=["GET","POST"])
def quesAns28():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question29"))

@app.route("/question29")
def question29():
    return render_template("Maths-q29.html")

@app.route("/quesAns29",methods=["GET","POST"])
def quesAns29():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question30"))

@app.route("/question30")
def question30():
    return render_template("Maths-q30.html")

@app.route("/quesAns30",methods=["GET","POST"])
def quesAns30():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question31"))

@app.route("/question31")
def question31():
    return render_template("Maths-q31.html")

@app.route("/quesAns31",methods=["GET","POST"])
def quesAns31():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question32"))

@app.route("/question32")
def question32():
    return render_template("Maths-q32.html")

@app.route("/quesAns32",methods=["GET","POST"])
def quesAns32():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question33"))

@app.route("/question33")
def question33():
    return render_template("Maths-q33.html")

@app.route("/quesAns33",methods=["GET","POST"])
def quesAns33():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question34"))

@app.route("/question34")
def question34():
    return render_template("Maths-q34.html")

@app.route("/quesAns34",methods=["GET","POST"])
def quesAns34():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question35"))

@app.route("/question35")
def question35():
    return render_template("Maths-q35.html")

@app.route("/quesAns35",methods=["GET","POST"])
def quesAns35():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question36"))

@app.route("/question36")
def question36():
    return render_template("Maths-q36.html")

@app.route("/quesAns36",methods=["GET","POST"])
def quesAns36():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question37"))

@app.route("/question37")
def question37():
    return render_template("Maths-q37.html")

@app.route("/quesAns37",methods=["GET","POST"])
def quesAns37():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question38"))

@app.route("/question38")
def question38():
    return render_template("Maths-q38.html")

@app.route("/quesAns38",methods=["GET","POST"])
def quesAns38():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question39"))

@app.route("/question39")
def question39():
    return render_template("Maths-q39.html")

@app.route("/quesAns39",methods=["GET","POST"])
def quesAns39():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question40"))

@app.route("/question40")
def question40():
    return render_template("Maths-q40.html")

@app.route("/quesAns40",methods=["GET","POST"])
def quesAns40():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question41"))

@app.route("/question41")
def question41():
    return render_template("Maths-q41.html")

@app.route("/quesAns41",methods=["GET","POST"])
def quesAns41():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question42"))

@app.route("/question42")
def question42():
    return render_template("Maths-q42.html")

@app.route("/quesAns42",methods=["GET","POST"])
def quesAns42():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question43"))

@app.route("/question43")
def question43():
    return render_template("Maths-q43.html")

@app.route("/quesAns43",methods=["GET","POST"])
def quesAns43():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question44"))

@app.route("/question44")
def question44():
    return render_template("Maths-q44.html")

@app.route("/quesAns44",methods=["GET","POST"])
def quesAns44():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question45"))

@app.route("/question45")
def question45():
    return render_template("Maths-q45.html")

@app.route("/quesAns45",methods=["GET","POST"])
def quesAns45():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question46"))

@app.route("/question46")
def question46():
    return render_template("Maths-q46.html")

@app.route("/quesAns46",methods=["GET","POST"])
def quesAns46():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question47"))

@app.route("/question47")
def question47():
    return render_template("Maths-q47.html")

@app.route("/quesAns47",methods=["GET","POST"])
def quesAns47():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question48"))

@app.route("/question48")
def question48():
    return render_template("Maths-q48.html")

@app.route("/quesAns48",methods=["GET","POST"])
def quesAns48():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question49"))

@app.route("/question49")
def question49():
    return render_template("Maths-q49.html")

@app.route("/quesAns49",methods=["GET","POST"])
def quesAns49():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("question50"))

@app.route("/question50")
def question50():
    return render_template("Maths-q50.html")

@app.route("/quesAns50",methods=["GET","POST"])
def quesAns50():
    if request.method=="POST":
        option1=""
        if request.form.get("defaultCheck1"):
            option1=True
        else:
            option1=False
        option2=""
        if request.form.get("defaultCheck2"):
            option2=True
        else:
            option2=False
        option3=""
        if request.form.get("defaultCheck3"):
            option3=True
        else:
            option3=False
        option4=""
        if request.form.get("defaultCheck4"):
            option4=True
        else:
            option4=False
        print(option1,option2,option3,option4)
        return redirect(url_for("signin"))

@app.route("/terms")
def terms():
    return "Bhai ne bola Accept karna hai toh karna hai"
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)
