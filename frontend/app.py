import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(
    page_title="AI Receipt Intelligence System",
    layout="centered"
)

st.title("🧾 AI Receipt Intelligence System")
st.write("Upload a receipt and instantly extract structured financial data using AI + OCR.")

uploaded_file = st.file_uploader(
    "Upload Receipt Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Receipt", use_container_width=True)

    st.markdown("---")

    if st.button("🚀 Process Receipt with AI"):

        with st.spinner("Analyzing receipt... OCR + AI processing in progress"):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            response = requests.post(
                "http://localhost:8000/process-receipt/",
                files=files
            )

        if response.status_code == 200:
            result = response.json()

            st.success("Processing Complete!")

            st.subheader("📊 Extracted Structured Data")
            st.json(result["structured_data"])

            st.subheader("⚠️ Anomaly Detection")
            st.write(result["anomalies"])

            st.subheader("📄 Raw OCR Text")
            st.text(result["raw_text"])

        else:
            st.error("Error processing receipt. Check backend connection.")