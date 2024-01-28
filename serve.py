from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def handle_requests():
    if request.method == "POST":
        
        subprocess.Popen(["python3", "stress_cpu.py"])
        return "Stress CPU initiated!"
    elif request.method == "GET":
        
        return socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
