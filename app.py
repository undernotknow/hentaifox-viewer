from flask import Flask, jsonify, make_response, render_template, request, url_for
from handler.data import processGalleryById

app = Flask(__name__)

@app.route('/')
def home():
    response = make_response(render_template('index.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.get('/pattern')
def getImagePattern():
    gallery_id=request.args.get('gallery_id')
    pattern= processGalleryById(gallery_id)
    *head,tail=pattern.split('/')
    _,extension=tail.split('.')
    return jsonify({
        'patternUrl':f"{'/'.join(head)}/$index.{extension}",
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
