from mysqlDB import * 

def chech_DB(strchar):
    return True
    # a = sqlDB("localhost","root","","alpd")
    # licensep = strchar.replace("'","")
    # query = "SELECT * FROM info WHERE license_plate_no = '%s' "%(licensep)
    # data = a.retrive_many(query)
    # if(data == []):
    #     print(strchar)
    #     print("============= USER NOT FOUND ============\n ===========UNAUTHORIZED TO PARK HERE========\n")
    #     return False
    # else:
    #     print("=====================USER FOUND=======================\n")
    #     print("USERNAME : "+str(data[0][1]))
    #     print("ADDRESS : "+str(data[0][2]))
    #     print("VEHICLE : "+str(data[0][3]))
    #     # print(data)
    #     print(str(data[0][1]) +" is Authorized to park here")
    #     a.closeDB()
    #     return True