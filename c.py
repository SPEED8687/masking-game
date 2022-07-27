from flask import Flask, jsonify, request
app = Flask(__name__)
students = [
    {
        "id": 1,
        "name": "Andrew",
        "number": "3147863322",
        "course": "coding"
    },
    {
        "id": 2,
        "name": "Adam",
        "number": "3147763322",
        "course": "coding"
    }

]


@app.route('/name')
def displayMyName():
    return "Rivaan"


@app.route('/SchoolName')
def displayMySchoolName():
    return "Parkway Central High School"

@app.route('/Student',methods=['POST'])
def addStudent():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide student details"
        })
    s = {
        "id": students[-1]['id']+1,
        "name": request.json["name"],
        "number": request.json["number"],
        "course": request.json["course"]
    }
    students.append(s)
    return jsonify({
        "status": "success",
        "message": "student added successfully"
    })

@app.route('/ShowStudents')
def showStudents():
    return jsonify({
        "data":students
    })
  
if __name__ == "__main__":
    app.run(debug=True)
