from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app=Flask(__name__)

@app.route("/employee")
def employee():
    con=sql.connect("db_employee.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from Employee")
    data=cur.fetchall()
    return render_template('employee.html',datas=data)

@app.route("/edit/<string:E_id>",methods=['POST','GET'])
def edit(E_id):
    if request.method=='POST':
            Ename=request.form['employee_name']
            E_ID=request.form['employee_ID']
            Desg=request.form['designation']
            Jdate=request.form['joining_date']
            B_salary=request.form['basic_salary']
            con=sql.connect("db_employee.db")
            cur=con.cursor()
            cur.execute("update Employee set Ename=?,Desg=?,Jdate=?,B_salary=? where E_ID=?", (Ename,Desg,Jdate,B_salary,E_id)) 
            con.commit()         
            return redirect(url_for("employee"))
    con=sql.connect("db_employee.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from Employee where E_ID=?",(E_id,))
    data=cur.fetchone()
    return render_template("edit.html",datas=data)

@app.route("/delete/<string:E_id>", methods=['GET'])
def delete(E_id):
    con=sql.connect("db_employee.db")
    cur=con.cursor()
    cur.execute("delete from Employee where E_ID=?",(E_id,)) 
    con.commit()         
    return redirect(url_for("employee"))
     
    
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        Ename=request.form['employee_name']
        E_ID=request.form['employee_ID']
        Desg=request.form['designation']
        Jdate=request.form['joining_date']
        B_salary=request.form['basic_salary']
        con=sql.connect("db_employee.db")
        cur=con.cursor()
        cur.execute("insert into Employee(E_ID,Ename,Desg,Jdate,B_salary) values (?,?,?,?,?)",(E_ID,Ename,Desg,Jdate,B_salary))
        con.commit()
        flash('User Added Successfully','success')
        return redirect(url_for("index"))
    return render_template('index.html')

@app.route('/salary',methods=['GET','POST'])
def salary():
    con=sql.connect('db_employee.db')
    cur=con.cursor()
    cur.execute("select E_ID from Employee")
    data=cur.fetchall()
    emp_details = None
    salary_details = None
    if request.method == 'POST':
        E_ID = request.form['E_ID']
        Salary_Month = request.form['Salary_Month']
        Leave_days = int(request.form['Leave'])
        cur.execute("SELECT * FROM Employee WHERE E_ID=?",(E_ID,))
        emp_details = cur.fetchone()
        print("Selected ID:", E_ID)
        print("Fetched Details:", emp_details)

        if emp_details:
            Actual_basic = float(emp_details[4])
            day = Actual_basic/30
            ded = day*Leave_days
            
            basic = Actual_basic - ded
            
            hra = basic * 20 / 100
            da = basic * 10 / 100
            allowance = basic * 5 / 100
            
            gross = basic + hra + da + allowance
            
            pf = basic * 12 / 100
            esi = gross * 0.75 / 100
            
            net_salary = gross - pf - esi
            
            salary_details = {
            'month': Salary_Month,
            'basic': basic,
            'hra': hra,
            'da': da,
            'allowance': allowance,
            'gross': gross,
            'pf': pf,
            'esi': esi,
            'net_salary': net_salary,
            'Leave_days': Leave_days
            }
            cur.execute("""select * from Salary where E_ID=? AND Salary_Month=?""",(E_ID,Salary_Month))
            existing_salary = cur.fetchone()
            
            if not existing_salary:
                cur.execute("""insert into Salary(E_ID,Salary_Month,B_salary,HRA,DA,Allowance,Gross,PF,ESI,Net_salary,Leave_days) values(?,?,?,?,?,?,?,?,?,?,?)""",(E_ID,Salary_Month,basic,hra,da,allowance,gross,pf,esi,net_salary,Leave_days))
                con.commit()
            
        
    con.close()
    return render_template("salary.html",datas=data,emp_details=emp_details,salary_details=salary_details)

@app.route('/payslip',methods=['GET','POST'])
def payslip():
    payslip_details = None
    searched = False

    con=sql.connect('db_employee.db')
    cur=con.cursor()

    cur.execute("SELECT E_ID FROM Employee")
    data = cur.fetchall()
    if request.method=='POST':
        searched = True
        E_ID=request.form['E_ID']
        Salary_Month=request.form['Salary_Month']

        cur.execute("""select Employee.E_ID,Employee.Ename,Employee.Desg,Salary.Salary_Month,Salary.B_salary,Salary.HRA, Salary.DA,Salary.Allowance, Salary.Gross, Salary.PF, Salary.ESI, Salary.Net_salary, Salary.Leave_days from Employee INNER JOIN Salary on Employee.E_ID = Salary.E_ID where Employee.E_ID=? AND Salary.Salary_Month=?""",(E_ID,Salary_Month))
            
        payslip_details = cur.fetchone()
    con.close()
    return render_template("payslip.html",payslip_details=payslip_details,data=data,searched=searched)





if __name__=='__main__':
    
    app.secret_key='admin123'
    app.run(debug=True)

