from flask import Flask,request,redirect, render_template,url_for
from flask_mysqldb import MySQL


app=Flask(__name__)

app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_DB']= "flask"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "Kgisl@123"
app.config['MYSQL_CURSORCLASS']="DictCursor"
app.secret_key="myapp"
conn = MySQL(app)

@app.route('/')
def home():
    return render_template("home.html")



@app.route('/signin')
def signin():
         
    return render_template('signin.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method  == 'POST' or 'GET':
        user_name1 = request.form['user_name']
        password1 = request.form['password']
        con=conn.connection.cursor()
        sql = "select * from 21_04_2023 WHERE user_name= %s and  password=%s"
        result=con.execute(sql,(user_name1,password1))
        con.connection.commit()
        con.close()
        return redirect(url_for('appl'))
               
                
    return render_template("signin.html") 
    
@app.route('/appl/',methods=['GET', 'POST'])
def appl():
    
    con=conn.connection.cursor()
    sql="select * from  addrbook"
    con.execute(sql)
    result= con.fetchall()
    con.connection.commit()    
    return render_template('appl.html',rows=result)

@app.route('/add', methods = ['POST', 'GET'])
def add():
    return render_template("add.html")

@app.route('/add1', methods = ['POST', 'GET'])
def add1():
    if request.method  == 'POST':
        name = request.form['name']
        watsapp_no = request.form['watsapp_no']
        door_no = request.form['door_no']
        street = request.form['street']
        city = request.form['city']
        pincode = request.form['pincode']
        con=conn.connection.cursor()
        sql = "insert into addrbook(name,watsapp_no,door_no,street,city,pincode) values  (%s,%s,%s,%s,%s,%s)"
        result=con.execute(sql,(name,watsapp_no,door_no,street,city,pincode))
        con.connection.commit()
        con.close()
        return  redirect(url_for('appl'))
        
    return render_template('add.html')

@app.route('/search',methods=['GET', 'POST'])
def search():
    
    if request.method  == 'POST':
        uname = request.form['uname']
        con=conn.connection.cursor()
        con.execute('select * from addrbook where name like %s' ,{ '%' +uname + '%'})
        result=con.fetchall()
        return render_template('search.html',rows=result) 
    return render_template('appl.html')


@app.route('/edit', methods = ['POST', 'GET'])
def edit():
    return render_template("edit.html")

@app.route('/edit1', methods = ['POST', 'GET'])
def edit1():
    if request.method  == 'POST':
        nam=request.form['nam']
        name = request.form['name']
        watsapp_no = request.form['watsapp_no']
        door_no = request.form['door_no']
        street = request.form['street']
        city = request.form['city']
        pincode = request.form['pincode']
        con=conn.connection.cursor()
        sql = "update addrbook SET name=%s, watsapp_no=%s, door_no=%s,street=%s,city=%s,pincode=%s WHERE name=%s "
        result=con.execute(sql,(name,watsapp_no,door_no,street,city,pincode,nam))
        con.connection.commit()
        con.close()
        return  redirect(url_for('appl'))
    return render_template("edit.html")

@app.route('/delete', methods = ['POST', 'GET'])
def delete():
    return render_template("delete.html")


@app.route('/delete1', methods = ['POST', 'GET'])
def delete1():
    if request.method  == 'POST':
        name = request.form['name']
        con=conn.connection.cursor()
        sql = "delete from addrbook WHERE name=%s"
        result=con.execute(sql,[name])
        con.connection.commit()
        con.close()
        return  redirect(url_for('appl'))
    
    
    return render_template("delete.html")

if __name__ == "__main__":
    app.run(debug=True)