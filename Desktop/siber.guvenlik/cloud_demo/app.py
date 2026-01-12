from flask import Flask, request, jsonify
import time

app = Flask(__name__)
START = time.time()
REQUESTS_TOTAL = 0


@app.get("/pay")
def pay():
    global REQUESTS_TOTAL
    REQUESTS_TOTAL += 1
    amount = request.args.get("amount", "0")
    return jsonify({"payment": "received", "amount": amount, "status": "ok"})


@app.get("/metrics")
def metrics():
    return jsonify(
        {
            "uptime_sec": int(time.time() - START),
            "requests_total": REQUESTS_TOTAL,
        }
    )


@app.get("/")
def home():
    return "DigiBank Cloud Demo is running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
