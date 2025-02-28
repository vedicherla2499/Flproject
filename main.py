from flask import Flask, jsonify, request, render_template, redirect, url_for
from config import Config
from models import db,EmployeeTable

app=Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
print("Db connected")

with app.app_context():
    db.create_all()
    print("table created")

@app.route('/home',methods=['GET'])
def home_func():
    return "Hello python! this is my demo project"

@app.route('/path_parameter/<id>',methods=["GET"])
def path_parameter_func(id):
    return jsonify(message=f"hello world from flask : {id}")

@app.route('/query_parameter',methods=["GET"])
def query_param():
    name=request.args.get('name')
    age=request.args.get('age')
    data=request.args.to_dict(flat=False)
    return  jsonify(message=f"hello {name} {age}")

@app.route('/insert_data',methods=['GET'])
def insert_data_func():
    user = EmployeeTable(name=request.args.get('name'), age=request.args.get('age'))
    db.session.add(user)
    db.session.commit()
    return {"id": user.id, "name": user.name, "age": user.age},200

@app.route('/html',methods=['GET'])
def html_func():
    dc={"name":"raju","age":25,"location":"hyd"}
    return render_template('Demo.html')

@app.route('/redirect',methods=['GET'])
def redirect_func():
    print("from redirect_func")
    return redirect(url_for('home'))

@app.route("/insert_form_data", methods=['POST'])
def insert_form_data():
    # name = request.form.get('name')
    # name = request.form.getlist('name')
    # return name

    # data = request.form.to_dict()
    data=request.get_json()
    if not data:
        return jsonify(message="please provide name and age")

    user = EmployeeTable(name=data.get('name'), age=data['age'],salary=data['salary'])
    db.session.add(user)
    db.session.commit()
    return {"id": user.id, "name": user.name, "age": user.age,"salary":user.salary}, 201

if __name__=='__main__':
    app.run(debug=True)