def detect_anomaly(data):
    anomalies = []

    if data.get("amount", 0) > 500:
        anomalies.append("High-value transaction flagged")

    if "test" in data.get("vendor", "").lower():
        anomalies.append("Suspicious vendor name")

    return anomalies