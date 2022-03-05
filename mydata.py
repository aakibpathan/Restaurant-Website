import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='mydatabase')
    
def addEmp(t):
    db=getConnection()
    sql='insert into food values(%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()


def selectAllEmp():
    db=getConnection()
    sql='select * from customer'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

    
def deleteEmp(id):
    db=getConnection()
    sql='delete from customer where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()

def selectEmpById(id):
    db=getConnection()
    sql='select * from customer where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateEmp(t):
    db=getConnection()
    sql='update customer set fname=%s,lname=%s,contact=%s,email=%s,passw=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def loginvalidation(a):
    db=getConnection()
    sql="select * from food where email=%s and passw=%s"
    cr=db.cursor()
    cr.execute(sql,a)
    users=cr.fetchall()
    db.commit()
    db.close()
    return users
