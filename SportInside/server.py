from waitress import serve
import news_website.__init__

serve(news_website.__init__.app, host='0.0.0.0', port=80)