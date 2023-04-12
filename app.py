from flask import Flask
from flask_cors import CORS

from scripts.core.services.station_service import station_service_router
from scripts.core.services.prediction_service import prediction_service_router


app = Flask(__name__)
CORS(app)

app.register_blueprint(station_service_router)
app.register_blueprint(prediction_service_router)

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
