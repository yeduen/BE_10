from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is Main page!"

@app.route('/about')
def about():
    return "This is the about page!"

# 동적 URL - 사용자 이름
@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}'

# 동적 URL - 숫자
@app.route('/number/<int:number>')
def number_profile(number):  # ⚠️ 함수 이름 변경!
    return f'Number : {number}'

@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url, data=data)
    return response.text

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")
    elif request.method == 'POST':
        print("POST method***", request.data)

    return Response("success", status=200)

if __name__ == "__main__":
    app.run(debug=True)
