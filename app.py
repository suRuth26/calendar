from flask import Flask
from controller.User import BaseUser
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World Sara !'
@app.route('/a')
def hello_world2():  # put application's code here
    return 'Hello World Nataly !'

# @app.route('/AppParts/parts')
# def partsRoute():
#     return BaseParts().getAllParts()
@app.route('/AppUser/User')
def UserRoute():
    return BaseUser().getAllUser()

# @app.route('/AppParts/parts/<int:pid>')
# def partsdDetailRoute(pid):
#     return BaseParts().getPartbyId(pid)

if __name__ == '__main__':
    app.run(debug=True)