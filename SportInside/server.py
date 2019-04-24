from waitress import serve
import flaskr.__init__

serve(flaskr.__init__.app, host='0.0.0.0', port=80)