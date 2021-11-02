from flask import jsonify
from model.User_Availability import AvaDAO

class BaseAva:
    def build_row_dict(self,row):
        result= {
            "user_av_id": row[0],
            "user_start_time": row[1],
            "user_end_time": row[2]
        }
        return result
    def getAllAva(self):

        dao=AvaDAO()
        tuples=dao.getAllAva()
        result=[]
        for t in tuples:
            result.append(self.build_row_dict(row=t))
        return jsonify(result)