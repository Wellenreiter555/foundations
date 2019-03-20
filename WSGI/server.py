from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

html_code = """
<html>
<head>
  <title>A super simple python WSGI server</title>
</head>
<body>
<form action="" method="post">
<p>
  <label for="Name">Your Name: </label>
  <input type="text" id="Name" name="name">
  <input type="submit" value="Send">
</p>
</form>
</body>
</html> """

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]

    start_response(status, headers)

    return [html_code.encode("utf-8")]

with make_server('', 8000, simple_app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()

