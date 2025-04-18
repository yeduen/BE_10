import unittest
from app import app  # 'app.py'에 있는 Flask 애플리케이션을 가져옵니다.

class FlaskAppTests(unittest.TestCase):

    # 각 테스트 전에 테스트 클라이언트를 설정합니다.
    def setUp(self):
        self.client = app.test_client()  # 테스트 클라이언트 인스턴스를 생성합니다.
        self.client.testing = True  # 테스트 모드 활성화

    # GET 요청 - /api/v1/feeds 전체 게시글 조회
    def test_get_all_feeds(self):
        response = self.client.get('/api/v1/feeds')
        self.assertEqual(response.status_code, 200)
        self.assertIn('feed1', response.get_data(as_text=True))
        self.assertIn('feed2', response.get_data(as_text=True))

    # GET 요청 - /api/v1/feeds/<int:feed_id> 특정 게시글 조회
    def test_get_one_feed(self):
        response = self.client.get('/api/v1/feeds/1')  # 예시로 feed_id 1
        self.assertEqual(response.status_code, 200)
        self.assertIn('feed1', response.get_data(as_text=True))
        self.assertIn('data for feed 1', response.get_data(as_text=True))

    # POST 요청 - /api/v1/feeds 게시글 작성
    def test_create_feed(self):
        data = {'name': 'John', 'age': 30}
        response = self.client.post('/api/v1/feeds', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.get_data(as_text=True))
        self.assertIn('received', response.get_data(as_text=True))

    # GET 요청 - /api/v1/datas 데이터 조회
    def test_get_datas(self):
        response = self.client.get('/api/v1/datas')
        self.assertEqual(response.status_code, 200)
        self.assertIn('datas', response.get_data(as_text=True))

    # POST 요청 - /api/v1/datas 새로운 데이터 추가
    def test_create_data(self):
        new_data = {'items': [{'name': 'item2', 'price': 20}]}
        response = self.client.post('/api/v1/datas', json=new_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('items', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()  # 테스트 실행
