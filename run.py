from logging import debug
from relay_registery import app

app.run(host="0.0.0.0", port=80, debug=True)