from flask import Flask, request, jsonify
from risk_engine import calculate_risk_score
import requests

app = Flask(__name__)

@app.route('/access', methods=['POST'])
def access_request():
    context = request.json
    risk = calculate_risk_score(context)
    opa_input = {
        "input": {
            "context": context,
            "risk": risk
        }
    }

    print("Sending to OPA:", opa_input)
    try:
        response = requests.post("http://localhost:8181/v1/data/accesscontrol/out", json=opa_input)
        decision = response.json().get("result")
        print("OPA returned:", decision)
        return jsonify({
            "decision": decision,
            "calculated_risk": risk
        })
    except Exception as e:
        print("OPA error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)