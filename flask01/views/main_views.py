from flask import Blueprint


# 특정 /url/ 하위에 있는 함수들을 일괄적으로 관리하기 위한 속성
        #코드에서 부르는 상대적 이름, 실제 파일명, url에 매칭되는 경로
mbp = Blueprint('main', __name__, url_prefix='/')

# localhost:5001/main/
# <변수명>를 통해 매개변수도 전달 가능
@mbp.route('/<username>')
def hello_username(username):
    return f'{__name__} {username} hello'

# <변수명:path>를 통해 매개변수도 전달 가능
@mbp.route('/path/<path:subpath>')
def print_path(subpath):
    return f'{__name__} {subpath} hello'


# <변수명:path>를 통해 매개변수도 전달 가능
@mbp.route('/items/')
@mbp.route('/items/<itemname>')
@mbp.route('/items/<itemname>/<int:quantity>')
def print_itemname(itemname='기본값', quantity=0):
    return f'{__name__} {itemname, quantity} hello'