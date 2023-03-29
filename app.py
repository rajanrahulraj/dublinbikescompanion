from flask import Flask

from scripts.core.services.station_service import station_service_router
from scripts.constants import app_constants

app = Flask(__name__)

app.register_blueprint(station_service_router)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)