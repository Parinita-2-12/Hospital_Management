import mysql.connector
mysql = mysql.connector.connect(
        host="localhost", user='root', passwd='', database='hmsdb1')
mycursor = mysql.cursor()


## user credentials  function 
def checkUserCredential(_username, _password):
    mycursor.execute(
        "SELECT * FROM users WHERE userid='" + _username + "' AND password='"+ _password +"'")  
    row = mycursor.fetchall()
    return row


## user registration function 
def insertUserInfo(_name,_user_name,_psw):
    mycursor.execute(
        "INSERT INTO users(fname, userid, password) VALUES('"+_name+"', '"+_user_name+"', '"+_psw+"')")
    mysql.commit()
    return True

## doctor data insertion
def insertDoctorData(_name,_address,_age,_specialist,_phone,_fees,_ms):
    mycursor.execute(
        "INSERT INTO doctors(name, address, age, specialist, phone, fees, ms) VALUES('"+_name+"', '"+_address+"','"+_age+"', '"+_specialist+"','"+_phone+"','"+_fees+"','"+_ms+"')")
    mysql.commit()
    return True
    
          
## nurse data insertion
def insertNurseData(_name,_address,_age,_phone,_ms):
    mycursor.execute(
        "INSERT INTO nurse (name, address, age, phone, ms) VALUES('"+_name+"', '"+_address+"', '"+_age+"','"+_phone+"', '"+_ms+"')"
    )
    mysql.commit()
    return True

## Staff Data insertion
def insertStaffData(_name,_address,_age,_phone,_ms):
    mycursor.execute(
        "INSERT INTO staff (name, address, age, phone,ms) VALUES('"+_name+"', '"+_address+"', '"+_age+"', '"+_phone+"','"+_ms+"')"
        )
    mysql.commit()
    return True

## Patient Data insertion
def insertPaitentData(_name,_address,_age,_gender,_phone):
    mycursor.execute(
        "INSERT INTO patients (name, address, age, gender,phone) VALUES('"+_name+"', '"+_address+"', '"+_age+"','"+_gender+"','"+_phone+"')"        
    )
    mysql.commit()
    return True

## show all doctors
def showAllDoc():
    mycursor.execute(
        "SELECT * FROM doctors"
    )
    row = mycursor.fetchall()
    return row

## show all nurse
def showAllNurse():
    mycursor.execute(
        "SELECT * FROM nurse"
    )
    row = mycursor.fetchall()
    return row

## show all patient 
def showAllPatient():
    mycursor.execute(
        "SELECT * FROM patients"
    )
    row = mycursor.fetchall()
    return row

## show all staff
def showAllStaff():
    mycursor.execute(
        "SELECT * FROM staff"
    )
    row = mycursor.fetchall()
    return row