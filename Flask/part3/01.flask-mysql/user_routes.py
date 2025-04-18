from flask import request
from flask_smorest import Blueprint, abort

def create_user_blueprint(mysql):
    user_blp = Blueprint("user_routes", __name__, url_prefix='/users')

    @user_blp.route('/', methods=['GET'])
    def get_users():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()

        users_list = []
        for user in users:
            users_list.append({
                'id': user[0],
                'name': user[1],
                'email': user[2]
            })

        return users_list

    @user_blp.route('/', methods=['POST'])
    def add_user():
        user_data = request.get_json()

        if not user_data.get('name') or not user_data.get('email'):
            abort(400, message="name과 email은 필수입니다")

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users(name, email) VALUES(%s, %s)",
                       (user_data['name'], user_data['email']))
        mysql.connection.commit()
        cursor.close()

        return {"msg": "successfully added user"}, 201

    @user_blp.route('/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user_data = request.get_json()

        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s",
                       (user_data['name'], user_data['email'], user_id))
        mysql.connection.commit()
        cursor.close()

        return {"msg": "successfully updated user"}, 201

    @user_blp.route('/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        mysql.connection.commit()
        cursor.close()

        return {"msg": "successfully deleted user"}, 201

    return user_blp
