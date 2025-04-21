from flask import Flask, render_template
from flask_smorest import Api
from db import db  # db.py에 db = SQLAlchemy() 있어야 함
from models import User, Board 

app = Flask(__name__)

# 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:2925@localhost/orrm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # ✅ 오타 수정

# API 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

from routes.board import board_blp
api.register_blueprint(board_blp)

# 블루프린트는 아직 등록 안 했으면 그대로 둬도 됩니다
# api.register_blueprint(...)

@app.route('/manage-boards')
def manage_boards():
    return render_template('boards.html')  # ✅ 파일명이 boards.html 이 맞는지 확인

@app.route('/manage-users')
def manage_user():
    return render_template('users.html')

# ✅ 여기 문자열 오타 수정
if __name__ == '__main__':
    with app.app_context():
        print("여기 실행?")
        db.create_all()
    app.run(debug=True)
