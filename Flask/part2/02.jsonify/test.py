from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    data = {'result': 'success', 'data': {'feed1': 'data1', 'feed2': 'data2'}}
    return jsonify(data)

@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    data = {'result': 'success', 'data': {f'feed{feed_id}': f'data for feed {feed_id}'}}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
