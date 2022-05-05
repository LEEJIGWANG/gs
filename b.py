from flask import Flask, make_response, jsonify, request
import re
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    data = request.get_json()
    print(data)
    file = open('hello.txt', 'w', encoding='utf8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write(str(data))            # 파일에 문자열 저장
    file.close()                     # 파일 객체 닫기
    with open('hello.txt',encoding='utf8') as f:
     text = f.read()
    href_regex = r'href=[\'"]?([^\'" >]+)'
    urls = re.findall(href_regex, text)
    print(urls)
    return jsonify({'data':data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)