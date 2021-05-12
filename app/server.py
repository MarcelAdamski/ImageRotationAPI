from flask import Flask, request, send_file
import cv2
import numpy as np
from PIL import Image
app = Flask(__name__)

@app.route('/rotate', methods=['POST'])
def rotate():
    try:
        img = Image.open(request.files['image'].stream)
    except:
        return 'Wrong format of file', 400

    if not 'PNG' in img.format:
        print(img.format)
        return 'Wrong image extension', 400

    lines = findLine(img)

    if lines['hR'] == True and lines['hL'] == False and lines['vU'] == False and lines['vD'] == False:
        img = img.transpose(Image.ROTATE_270)
        img.save('rotated_image.png')
        return send_file('rotated_image.png', mimetype='image/png'), 200

    elif lines['hR'] == False and lines['hL'] == True and lines['vU'] == False and lines['vD'] == False:
        img = img.transpose(Image.ROTATE_90)
        img.save('rotated_image.png')
        return send_file('rotated_image.png', mimetype='image/png'), 200

    elif lines['hR'] == False and lines['hL'] == False and lines['vU'] == True and lines['vD'] == False:
        img = img.transpose(Image.ROTATE_180)
        img.save('rotated_image.png')
        return send_file('rotated_image.png', mimetype='image/png'), 200

    elif lines['hR'] == False and lines['hL'] == False and lines['vU'] == False and lines['vD'] == True:
        img.save('rotated_image.png')
        return send_file('rotated_image.png', mimetype='image/png'), 200

    elif all(value == False for value in lines.values()):
        return '', 204

    else:
        return '', 400

def findLine(img):
    width, height = img.size
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    lines = {'hR': False, 'hL': False, 'vU': False, 'vD': False}
    white, red = [255, 255, 255], [0, 0, 255]
    solidLine = np.asarray(3*[white] + 3*[red])

    for x in range(height):
        for y in range(width):
            if np.array_equal(np.array(img[x, y]), np.array(white)):
                if y + 6 <= width and np.array_equal(solidLine, np.array(img[x, y:y+6])):
                    lines['hR'] = True
                if x + 6 <= height and np.array_equal(solidLine, np.array(img[x:x+6, y])):
                    lines['vD'] = True
                if y - 5 >= 0 and np.array_equal(solidLine, np.array(img[x, y:y-6:-1])):
                    lines['hL'] = True
                if x - 5 >= 0 and np.array_equal(solidLine, np.array(img[x:x-6:-1, y])):
                    lines['vU'] = True
    return lines

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)