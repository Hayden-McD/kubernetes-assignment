from flask import Flask, render_template
import redis
import os
import socket

app = Flask(__name__)

# All use the env variables but will use these defaults if not set
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", "6379"))
redis_password = os.getenv("REDIS_PASSWORD")

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "production")
FEATURE_TOGGLE = os.getenv("FEATURE_TOGGLE", "false")

db = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password,
    db=0,
    decode_responses=True
)

@app.route("/")
def homepage():
    count = db.incr("page_views")

    container_id = socket.gethostname()

    return render_template(
        "home.html",
        count=count,
        container_id=container_id,
        app_version=APP_VERSION,
        app_env=APP_ENV,
        feature_toggle=FEATURE_TOGGLE,
        db_pass=redis_password
    )
