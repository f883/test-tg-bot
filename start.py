import http.server, socketserver, os

PORT = int(os.environ.get("PORT", 17995))
#PORT = 8081
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()







"""
from flask import Flask, request



app = Flask(__name__)

@app.route("/")

def simple():
    id_ = request.args.get('id')
    if id_ == 'one':
        return 'result - one'
    elif id_ == 'two':
        return 'result - two'
    else:
        return 'no result'
 
 
if __name__ == "__main__":
    print("hello heroku")
    app.run(debug=True)
    print("bye heroku")
    """