from flask import Flask, request
import numpy as np
import base64

from detect import main, parse_opt
app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def test():
    r = request
    img = r['img']
    imgDecoded = base64.b64decode(img)

    with open(r'C:\Users\C-ROAD\Desktop\yolov5\data\images\image.jpg', 'wb') as outFile:
        outFile.write(imgDecoded)
    return {'result': main(parse_opt())}


@app.after_request
def after_request(response):
    print("log: setting cors", file=sys.stderr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response



if __name__ == '__main__':
    app.run()