def validate_data(data):
    if not data.get("amount"):
        data["validation_error"] = "Missing amount"

    if data.get("amount", 0) < 0:
        data["validation_error"] = "Invalid amount"

    return data