import streamlit as st
from backend.detector import analyze
from backend.report import generate_report
from backend.heatmap import generate_heatmap
from backend.tts import speak
from backend.explainer import spoken_message
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Deepfake Detection",
    layout="wide"
)

st.title("🛡️ AI – Deepfake Detection System")
st.caption("Detect manipulated Images, Audio, Video & Malicious URLs")

st.divider()

# ---------------- OPTION SELECT ----------------
option = st.selectbox(
    "Choose Scan Type",
    ["Image", "Audio", "Video", "URL"]
)

# ======================================================
#              IMAGE / AUDIO / VIDEO SCAN
# ======================================================
if option != "URL":

    uploaded_file = st.file_uploader(
        "Upload file",
        type=["jpg", "png", "mp4", "wav", "mp3"]
    )

    if uploaded_file:
        file_path = "temp_" + uploaded_file.name

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        with st.spinner("🔍 Analyzing content..."):
            result = analyze(file_path, option.lower())

        verdict = result["verdict"]
        score = result["score"]

        # ---------------- METRICS ----------------
        col1, col2 = st.columns(2)
        col1.metric("Trust Score", f"{score}%")
        col2.metric("Scan Type", option)

        st.subheader(verdict)

        # ---------------- TRAFFIC LIGHT UI ----------------
        if verdict.startswith("🔴"):
            st.error("🚨 HIGH RISK – Do NOT trust this content")
        elif verdict.startswith("⚠️"):
            st.warning("⚠️ CAUTION – Verification uncertain")
        else:
            st.success("✅ Looks Safe")

        # ---------------- EXPLANATION ----------------
        st.subheader("🧠 Why this verdict?")
        st.info(result["why"])

        # ---------------- FORENSIC FLAGS ----------------
        if result.get("flags"):
            st.subheader("🔎 Forensic Flags")
            for flag in result["flags"]:
                st.write("•", flag)

        # ==================================================
        # 🔊 READ RESULT ALOUD  (THIS IS WHERE IT GOES)
        # ==================================================
        if st.button("🔊 Read Result Aloud"):
            message = spoken_message(result)
            speak(message)

        # ---------------- HEATMAP (IMAGE ONLY) ----------------
        if option == "Image":
            st.subheader("🔍 Forensic Heatmap")
            heatmap = generate_heatmap(file_path)
            st.image(heatmap, caption="Suspicious regions highlighted")

        # ---------------- REPORT DOWNLOAD ----------------
        st.divider()
        if st.button("📄 Generate Police Report"):
            report_file = generate_report(result)
            with open(report_file, "rb") as f:
                st.download_button(
                    "⬇️ Download Report",
                    f,
                    file_name=report_file
                )

# ======================================================
#                     URL SCANNER
# ======================================================
else:
    st.subheader("🌐 Website Safety Scanner")

    url = st.text_input("Enter website URL")

    if url:
        with st.spinner("🔍 Scanning website..."):
            result = analyze(url, "url")

        verdict = result["verdict"]

        st.subheader(verdict)
        st.write("📅 Domain Age (days):", result.get("age", "Unknown"))

        # 🔊 READ URL RESULT ALOUD
        if st.button("🔊 Read Result Aloud"):
            message = spoken_message(result)
            speak(message)

        if verdict.startswith("🔴"):
            st.error("🛑 POSSIBLE SCAM / PHISHING WEBSITE")
        else:
            st.success("✅ DOMAIN LOOKS SAFE")
