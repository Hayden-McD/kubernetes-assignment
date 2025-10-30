from flask import Flask, render_template
import redis
import os
import socket

app = Flask(__name__)

# Defaults to 'redis' and '6379' if environment variables are not set or running locally
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", "6379"))
redis_password = os.getenv("REDIS_PASSWORD")

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

    return render_template("home.html", count=count, container_id=container_id)
