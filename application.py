import os
import logging
import logging.config
import yaml
from app import create_app
from dotenv import load_dotenv

load_dotenv()
app = create_app(os.getenv('flask_config') or 'default')

if not os.path.exists("log"):
    os.makedirs("log")

with open(file="logconfig.yaml", mode='r', encoding="utf-8") as file:
    logging_yaml = yaml.load(stream=file, Loader=yaml.FullLoader)
    logging.config.dictConfig(config=logging_yaml)

if __name__ == '__main__':
    # app.run(threaded=True, ssl_context=('ssl/server.crt', 'ssl/server.key'))
    app.run(threaded=True)