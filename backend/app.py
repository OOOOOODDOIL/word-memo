from flask import Flask, request, jsonify
from event import Event
from handlers import EventDistributer

app = Flask(__name__)

@app.route('/MemoServer', methods=['POST', 'GET'])
def main():
    event = Event(dict(request.get_json()))  # 提取报文Event信息
    event = EventDistributer(event)  # 分发获取需求内容
    print(event.edetail)
    return jsonify(event.tojson())  # 返回json报文


if __name__ == '__main__':
    # 多线程启动后端服务器
    app.run(debug=True, threaded=True)