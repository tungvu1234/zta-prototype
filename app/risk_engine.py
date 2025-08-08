trusted_locations = ["Vietnam", "UK", "Canada"]
known_devices = {
    "alice": ["dev1", "dev2"],
    "bob": ["dev3"],
}

def calculate_risk_score(context):
    user_id = context.get("user_id")
    device_id = context.get("device_id")
    location = context.get("location")
    behavior = context.get("login_behavior")

    print("Evaluating risk for:")
    print(f"user_id: {user_id}")
    print(f"device_id: {device_id}")
    print(f"location: {location}")
    print(f"behavior: {behavior}")

    risk = 0.0

    if location not in trusted_locations:
        print("Untrusted location")
        risk += 0.4

    if user_id in known_devices:
        if device_id not in known_devices[user_id]:
            print("Unknown device for known user")
            risk += 0.3
    else:
        print("Unknown user")
        risk += 0.3

    if behavior == "anomalous":
        print("Anomalous behavior")
        risk += 0.3

    risk = round(min(risk, 1.0), 2)
    print(f"Final risk: {risk}")
    return risk