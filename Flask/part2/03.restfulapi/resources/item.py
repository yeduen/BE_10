from flask import Flask
from flask.views import MethodView
from flask_smorest import Blueprint, Api, abort
from schemas import ItemSchema

# Flask 애플리케이션 객체 생성
app = Flask(__name__)

# OpenAPI 관련 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# 블루프린트 생성: 'items'라는 이름으로, URL 접두사는 '/items'
blp = Blueprint("items", "items", url_prefix="/items", description="Operations on items")

# 간단한 데이터 저장소 역할을 하는 리스트
items = []

# 'ItemList' 클래스 - GET 및 POST 요청을 처리
@blp.route("/")
class ItemList(MethodView):
    @blp.response(200)
    def get(self):
        return items

    @blp.arguments(ItemSchema)
    @blp.response(201, description="Item added")
    def post(self, new_data):
        items.append(new_data)
        return new_data

# 'Item' 클래스 - GET, PUT, DELETE 요청을 처리
@blp.route("/<int:item_id>")
class Item(MethodView):
    @blp.response(200)
    def get(self, item_id):
        item = next((item for item in items if item["id"] == item_id), None)
        if item is None:
            abort(404, message="Item not found")
        return item

    @blp.arguments(ItemSchema)
    @blp.response(200, description="Item updated")
    def put(self, new_data, item_id):
        item = next((item for item in items if item["id"] == item_id), None)
        if item is None:
            abort(404, message="Item not found")
        item.update(new_data)
        return item

    @blp.response(204, description="Item deleted")
    def delete(self, item_id):
        global items
        if not any(item for item in items if item["id"] == item_id):
            abort(404, message="Item not found")
        items = [item for item in items if item["id"] != item_id]
        return ''

# API 객체 생성 및 블루프린트 등록
api = Api(app)
api.register_blueprint(blp)

# 애플리케이션 실행
if __name__ == "__main__":
    app.run(debug=True)
