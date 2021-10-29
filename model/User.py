from config.dbconfig import pg_config
import psycopg2
class UserDAO:
    def __init__(self):
        connection_url="dbname=%s user=%s password=%s port=%s host='ec2-18-214-214-252.compute-1.amazonaws.com'"%(pg_config['dbname'],pg_config['user'],
                                                                        pg_config['password'],pg_config['dbport'])
        self.conn = psycopg2.connect(connection_url)

    def getAllParts(self):
        query="select user_id,user_name,authorizatio,email,password from User;"
        cursor = self.conn.cursor()
        cursor.execute(query)
        result=[]
        for row in cursor:
            result.append(row)
        return result

