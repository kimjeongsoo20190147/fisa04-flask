# Blueprint 기능을 사용해서 collection/no1/
# Blueprint 기능을 사용해서 collection/no2/
from flask import Blueprint

mbp2 = Blueprint('app', __name__, url_prefix='/collection/')

@mbp2.route('/no1')
def hello2_no1():
    return f'{__name__} no1_hello'
    
@mbp2.route('/no2')
def hello3_no2():
    return f'{__name__} no2_hello'
    