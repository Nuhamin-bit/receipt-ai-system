from fastapi import FastAPI, UploadFile, File
from services.ocr_service import extract_text
from services.llm_parser import parse_receipt
from services.validation_service import validate_data
from services.anomaly_detector import detect_anomaly

app = FastAPI(title="AI Receipt Intelligence System")

@app.post("/process-receipt/")
async def process_receipt(file: UploadFile = File(...)):
    image_bytes = await file.read()


    raw_text = extract_text(image_bytes)

    structured_data = parse_receipt(raw_text)

    validated_data = validate_data(structured_data)

    anomaly_report = detect_anomaly(validated_data)

    return {
        "raw_text": raw_text,
        "structured_data": validated_data,
        "anomalies": anomaly_report
    }