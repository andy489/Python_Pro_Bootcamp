from flask import Flask
from datetime import datetime

app = Flask(__name__)

curr_year = datetime.now().year

@app.context_processor
def inject_footer_data():
    return {
        "curr_year": curr_year,
    }