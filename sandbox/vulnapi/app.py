from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@app.get('/echo')
def echo():
    return jsonify({"q": request.args.get('q', '')})

@app.get('/xss')
def xss():
    q = request.args.get('q', '')
    return render_template_string('<!doctype html><div>Q={{q|safe}}</div>', q=q)

@app.get('/redir')
def redir():
    url = request.args.get('url', '/')
    return ("", 302, {"Location": url})

@app.get('/')
def index():
    return 'vulnapi ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


