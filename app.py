import json
import os

from azure.storage.queue import QueueClient
from flask import Flask, render_template, request

queue = QueueClient.from_connection_string(
    conn_str=os.environ.get("AZURE_STORAGE_CONNECTION_STRING"),
    queue_name=os.environ.get("AZURE_STORAGE_QUEUE_NAME"),
)


def load_msg():
    raw_msg = queue.receive_message().content
    return json.loads(raw_msg)["text"]


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", message=load_msg())


@app.route("/message")
def message():
    return load_msg()


if __name__ == "__main__":
    app.run()
