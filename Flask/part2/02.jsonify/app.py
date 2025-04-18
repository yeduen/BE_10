from flask import Flask, jsonify, request

app = Flask(__name__)

# 루트 경로 ("/")에 대한 응답 추가
@app.route('/')
def index():
    return "Welcome to the Flask API!"

# GET - 전체 게시글
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    data = {'result': 'success', 'data': {'feed1': 'data1', 'feed2': 'data2'}}
    return jsonify(data)

# GET - 특정 게시글
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    data = {'result': 'success', 'data': {f'feed{feed_id}': f'data for feed {feed_id}'}}
    return jsonify(data)

# POST - 게시글 작성 (JSON 방식)
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    print(name, age)  # 서버 콘솔 출력

    return jsonify({'result': 'success', 'received': {'name': name, 'age': age}})

# GET - 전체 데이터 조회
datas = [{"items": [{"name": "item1", "price": 10}]}]

@app.route('/api/v1/datas', methods=['GET'])
def get_datas():
    return jsonify({"datas": datas})

# POST - 새로운 데이터 추가
@app.route('/api/v1/datas', methods=['POST'])
def create_data():
    request_data = request.get_json()

    # 데이터 처리 오류 수정
    new_data = {'items': request_data.get("items", [])}
    datas.append(new_data)

    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(debug=True)
