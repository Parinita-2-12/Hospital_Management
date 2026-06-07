##########################################################################
##              Hospital Management System using python And Mysql       ##
#                       By Parinita Biswas                              ##
##                       MAIN MODULE                                    ##  
##########################################################################

import dbConnection
def mainModule():
      print("""\t
          ================================  
          CITY HOSPITAL MANAGEMENT SYSTEM
          ================================
        """)
      while(True):
        print("""
                Welcome User
                ============
                1. Sign In
                2. Registration
                3. Sign Out 
        """)
        choice = int(input('\t\tEnter your choice:'))
        if choice == 1:
             print("""
                    ==================================
                      !!!!!!!!    Sign In  !!!!!!!!!!
                    ==================================
                                                        """)
             _username = str(input('\t\t Enter User Name:'))    
             _password = str(input('\t\t Enter Password:'))
             _res = dbConnection.checkUserCredential(_username,_password)
             if len(_res) == 0:
                print('\t Invalid User Credentials')
             else:
                print('\n\n\t\t=======================================')
                print("\t\t :: WELCOME :: ",_res[0][1].upper(),"::")
                print("\t\t=========================================\n")
                while(True):
                    print("""
                        1.Administration
                        2.Doctor(Details)
                        3.Nurse(Details)
                        4.Patient(Details)
                        5.Staff(Details)
                        6.To Exit
                    """)
                    _ch = int(input('\t\tEnter your choice:'))
                    if _ch == 1:
                        while(True):
                            print("""
                                1.Add Doctor(Details)
                                2.Add Nurse(Details)
                                3.Add Staff
                                4.Add Patient(Details)
                                5.Discharge Patient
                                6.Return Main Menu
                            """)
                            _ch = int(input('\t\tEnter your choice:'))
                            if _ch == 1:
                                _name = str(input('\t\tEnter Doctor Name:'))
                                _address = str(input('\t\tEnter Address:'))
                                _age = str(input('\t\tEnter Age:'))
                                _specialist = str(input('\t\tEnter The Specilization:'))
                                _phone = str(input('\t\tEnter Contact Details:'))
                                _fees = str(input("\t\tEnter The Fees:"))
                                _ms = str(input("\t\tEnter Monthly Salary:"))
                                _response = dbConnection.insertDoctorData(_name,_address,_age,_specialist,_phone,_fees,_ms)
                                if _response == True:
                                    print('\n\t\t=====================================')
                                    print('\t\t Doctor Data Successfully Inserted')
                                    print('\n\t\t=====================================')
                                else:
                                    print('\n\t\t=====================================')
                                    print('\t\t Failed To Insert Data')    
                                    print('\n\t\t=====================================')
                            elif _ch == 2:
                                _name = str(input('\t\tEnter Nurse Name:'))
                                _address = str(input('\t\tEnter Address:'))
                                _age = str(input('\t\tEnter Age:'))
                                _phone = str(input('\t\tEnter Contact Details:'))
                                _ms = str(input("\t\tEnter Monthly Salary:"))
                                _response = dbConnection.insertNurseData(_name,_address,_age,_phone,_ms)
                                if _response == True:
                                    print('\n\t\t=====================================')
                                    print('\t\t Nurse Data Successfully Inserted')
                                    print('\n\t\t=====================================')
                                else:
                                    print('\n\t\t=====================================')
                                    print('\t\t Failed To Insert Data')    
                                    print('\n\t\t=====================================')
                            elif _ch == 3:
                                _name = str(input('\t\tEnter Staff Name:'))
                                _address = str(input('\t\tEnter Address:'))
                                _age = str(input('\t\tEnter Age:'))
                                _phone = str(input('\t\tEnter Contact Details:'))
                                _ms = str(input("\t\tEnter Monthly Salary:"))
                                _response = dbConnection.insertStaffData(_name,_address,_age,_phone,_ms)
                                if _response == True:
                                    print('\n\t\t=====================================')
                                    print('\n\t\t Staff Data Successfully Inserted')
                                    print('\n\t\t=====================================')
                                else:
                                    print('\n\t\t=====================================')
                                    print('\n\t\t Failed To Insert Data')    
                                    print('\n\t\t=====================================')
                            elif _ch == 4:
                                _name = str(input('\t\tEnter Patient Name:'))
                                _address = str(input('\t\tEnter Address:'))
                                _age = str(input('\t\tEnter Age:'))
                                _gender = str(input('\t\t Enter Gender:'))
                                _phone = str(input('\t\tEnter Contact Details:'))
                                _response = dbConnection.insertPaitentData(_name,_address,_age,_gender,_phone)
                                if _response == True:
                                    print('\n\t\t=====================================')
                                    print('\n\t\t Patient information Successfully Inserted')
                                    print('\n\t\t=====================================')
                                else:
                                    print('\n\t\t=====================================')
                                    print('\n\t\t Failed To Insert Data')    
                                    print('\n\t\t=====================================')    
                            elif _ch == 5:
                                break            
                            else:
                                print('\n\t\t=====================================')
                                break                      
                    elif _ch == 2:
                        print('\n\t\t ========== Doctors Details ==========')
                        _res = dbConnection.showAllDoc()
                        print('\n\t Id \t  Name \t\t  Address \t Age \t Specalist \t phone \t Fees \t Salary')
                        for i in _res:
                            for j in i:
                                print('\t',j,end=' ')
                            print()     
                    elif _ch == 3:
                        print('\n\t\t ========== Nurses Details ==========')
                        _res = dbConnection.showAllNurse()
                        print('\n\t Id \t  Name \t\t  Address \t Phone \t Salary \t Age \t Type')
                        for i in _res:
                            for j in i:
                                print('\t',j,end=' ')
                            print()         
                    elif _ch == 4:
                        print('\n\t\t ========== Patients Details ==========')
                        _res = dbConnection.showAllPatient()
                        print('\n\t Id \t  Name \t\t  Address \t Age \t Gender \t status \t Phone')
                        for i in _res:
                            for j in i:
                                print('\t',j,end=' ')
                            print() 
                    elif _ch == 5:
                        print('\n\t\t ========== Staffs Details ==========')
                        _res = dbConnection.showAllStaff()
                        print('\n\t Id \t  Name \t\t  Address \t Age \t Phone \t Salary')
                        for i in _res:
                            for j in i:
                                print('\t',j,end=' ')
                            print() 
                    else:
                        print('exit')
                        break                      
        elif choice == 2:
            print("""
                =======================================
                  !!!!!!!!!!Register Yourself!!!!!!!!
                =======================================
                                                    """)   
            _name = str(input('\t\t Enter Full Name: '))
            _user_name = str(input('\t\t Enter user name: '))
            _psw = str(input('\t\t Enter Password: '))
            _insResutl = dbConnection.insertUserInfo(_name,_user_name,_psw)
            if _insResutl == True:
                print('\t\t Information Saved Successful')
            else:
                print('\t\t Failed to Saved Information')  
        else:
            print('\t\t Thanks For Using!!!')
        
if __name__ == '__main__':
    mainModule()      