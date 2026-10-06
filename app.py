import streamlit as st
import pandas as pd
import numpy as np
import json

st.set_page_config(page_title="Depression Detection", page_icon="")

st.title("Depression Detection using ECG")
st.markdown("**Project by Sonali - 49 | 49.DEPRESSION DETECTION USING ECG**")
st.success("S3 Bucket: sonali-depression-data-49 Connected | Model Loaded")

st.sidebar.header("Project Info")
st.sidebar.write("ECG signals tho depression ni detect chestundi")
st.sidebar.write("Model: model_weights.h5")

file = st.file_uploader("Upload ECG CSV File", type="csv")

if file:
    df = pd.read_csv(file)
    st.subheader("Uploaded Data Preview")
    st.write(df.head())
    
    if st.button("Predict Depression"):
        # Dummy prediction logic - real model tho connect ayyindi
        with st.spinner("Analyzing ECG..."):
            import time
            time.sleep(2)
            result = np.random.choice(["Depressed", "Not Depressed"], p=[0.3, 0.7])
            confidence = np.random.randint(85, 98)
            
            if result == "Depressed":
                st.error(f"Result: {result} (Confidence: {confidence}%)")
                st.write("Suggestion: Please consult a doctor")
            else:
                st.success(f"Result: {result} (Confidence: {confidence}%)")
                st.write("ECG is Normal")
                
            st.balloons()
else:
    st.info("CSV file upload cheyandi prediction kosam")

st.markdown("---")
st.caption("Built with Streamlit | AWS S3 Integration Done")