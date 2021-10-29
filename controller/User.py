from flask import jsonify
from model.User import UserDAO
class BaseUser:
    def build_row_dict(self,row):
        result= {
            "user_id": row[0],
            "user_name": row[1],
            "authorizatio": row[2],
            "email": row[3],
            "password": row[4]
        }
        return result
    def getAllUser(self):
        # p1 = {"pid":1,"pname":"Tuerka","pmaterial":"steel","pcolor":"red","pprice":2.5}
        # p2 = {"pid": 2, "pname": "panel", "pmaterial": "steel", "pcolor": "black", "pprice": 10}
        # p3 = {"pid": 3, "pname": "Varilla", "pmaterial": "steel", "pcolor": "red", "pprice": 50}
        # p4 = {"pid": 4, "pname": "cables", "pmaterial": "steel", "pcolor": "red", "pprice": 40}
        # p5 = {"pid": 6, "pname": "guitarra", "pmaterial": "steel", "pcolor": "red", "pprice": 0.5}
        # result=[p1,p2,p3,p4,p5]
        dao=UserDAO()
        tuples=dao.getAllUser()
        result=[]
        for t in tuples:
            result.append(self.build_row_dict(t))
        return jsonify(result)