import streamlit as st
import speedtest

# 🌌 Custom CSS styling ala Speedtest Ookla
st.markdown("""
    <style>
        .stApp {
            background-color: #0f0f0f;
            color: #f0f0f0;
        }

        .title-style {
            font-size: 44px;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            margin-top: 30px;
            margin-bottom: 40px;
        }

        .stButton > button {
            background-color: #6c63ff;
            color: white;
            font-size: 24px;
            padding: 20px 40px;
            border-radius: 100px;
            border: none;
            box-shadow: 0 0 20px #6c63ff88;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #8a85ff;
            box-shadow: 0 0 30px #8a85ffcc;
        }

        .result-box {
            background-color: #1a1a1a;
            border-radius: 20px;
            padding: 30px;
            margin-top: 30px;
            box-shadow: 0px 0px 25px rgba(108, 99, 255, 0.3);
        }

        .speed-label {
            font-size: 22px;
            color: #cccccc;
            font-weight: 600;
        }

        .speed-value {
            font-size: 36px;
            color: #6c63ff;
            font-weight: bold;
            margin-bottom: 20px;
        }
    </style>

    <div class="title-style">🌐⚡ Tes Kecepatan Internet</div>
""", unsafe_allow_html=True)

# Placeholder loading status
status_placeholder = st.empty()

if st.button("🚀 MULAI TES"):
    with status_placeholder:
        st.write("⌛ Sedang mengetes jaringan kamu...")

    try:
        # Proses pengecekan kecepatan internet
        stt = speedtest.Speedtest()
        stt.get_best_server()
        download = stt.download() / 1_000_000
        upload = stt.upload() / 1_000_000
        best = stt.get_best_server()
        ping = best['latency']
        
        # Kosongkan status loading
        status_placeholder.empty()

        # Tampilkan hasil
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(f"🛰️ Server: `{best['host']}` ({best['sponsor']}, {best['country']})")
        st.markdown('<div class="speed-label">📶 Latency:</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="speed-value">{ping:.2f} ms</div>', unsafe_allow_html=True)
        st.markdown('<div class="speed-label">📥 Download:</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="speed-value">{download:.2f} Mbps</div>', unsafe_allow_html=True)
        st.markdown('<div class="speed-label">📤 Upload:</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="speed-value">{upload:.2f} Mbps</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


    except Exception as e:
        status_placeholder.empty()
        st.error(f"❌ Gagal melakukan tes: {e}")
