import streamlit as st
import random
import urllib.parse

st.set_page_config(page_title="Fake News Generator", page_icon="🗞️", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@400;700&display=swap');

    * { font-family: 'Poppins', sans-serif; }

    .main { background-color: #0f0f0f; }

    .title {
        font-family: 'Bebas Neue', cursive;
        font-size: 60px;
        text-align: center;
        background: linear-gradient(90deg, #ff6b6b, #feca57, #ff6b6b);
        background-size: 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 3s infinite;
    }

    @keyframes shimmer {
        0% { background-position: 0% }
        100% { background-position: 200% }
    }

    @keyframes popIn {
        0% { transform: scale(0.5); opacity: 0; }
        70% { transform: scale(1.05); }
        100% { transform: scale(1); opacity: 1; }
    }

    .headline-box {
        background: linear-gradient(135deg, #ff6b6b, #feca57);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
        animation: popIn 0.5s ease forwards;
        box-shadow: 0 0 30px rgba(255, 107, 107, 0.5);
    }

    .breaking {
        font-size: 13px;
        color: #1a1a2e;
        font-weight: bold;
        letter-spacing: 4px;
        margin-bottom: 10px;
    }

    .headline-text {
        font-size: 26px;
        font-weight: bold;
        color: #1a1a2e;
        line-height: 1.4;
    }

    .history-item {
        background: #1a1a2e;
        color: #feca57;
        padding: 12px 18px;
        border-radius: 10px;
        margin: 6px 0;
        border-left: 5px solid #ff6b6b;
        font-size: 15px;
        transition: transform 0.2s;
    }

    .history-item:hover { transform: translateX(5px); }

    .share-btn {
        display: inline-block;
        background: #25D366;
        color: white !important;
        padding: 8px 20px;
        border-radius: 20px;
        text-decoration: none !important;
        font-weight: bold;
        margin: 5px;
        font-size: 14px;
    }

    .twitter-btn {
        background: #1DA1F2;
        display: inline-block;
        color: white !important;
        padding: 8px 20px;
        border-radius: 20px;
        text-decoration: none !important;
        font-weight: bold;
        margin: 5px;
        font-size: 14px;
    }

    .counter {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #feca57;
    }

    .subtitle {
        text-align: center;
        color: #ff6b6b;
        font-size: 16px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Data — Pakistani + International
subjects = [
    "Imran Khan", "Nawaz Sharif", "Bilawal Bhutto",
    "Fahad Mustafa", "Wasim Akram", "Babar Azam",
    "Mehwish Hayat", "Mahira Khan", "Ushna Shah",
    "Elon Musk", "Bill Gates", "Mark Zuckerberg",
    "Arijit Singh", "Ranveer Singh", "Shah Rukh Khan"
]

actions = [
    "secretly buys", "accidentally destroys", "dramatically launches",
    "shamelessly steals", "hilariously donates", "mysteriously sells",
    "boldly announces", "quietly bans", "publicly hugs",
    "officially declares war on", "gets married to", "starts a podcast about"
]

things = [
    "a flying rickshaw", "the Eiffel Tower", "a biryani restaurant on Mars",
    "a secret underground disco", "Pakistan's largest cat cafe",
    "an army of trained parrots", "a time machine made of samosas",
    "the moon", "a controversial chatbot", "KFC's secret recipe",
    "a luxury spaceship", "a new political party for cats",
    "the world's spiciest nihari", "an AI that only speaks in poetry",
    "a startup that sells bottled karachi air"
]

# Session state
if "history" not in st.session_state:
    st.session_state.history = []
if "count" not in st.session_state:
    st.session_state.count = 0
if "current" not in st.session_state:
    st.session_state.current = ""

# Title
st.markdown("<div class='title'>🗞️ FAKE NEWS GENERATOR</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>100% Fake • 0% Real • 200% Fun! 😄</div>", unsafe_allow_html=True)

# Counter
if st.session_state.count > 0:
    st.markdown(f"<div class='counter'>📰 {st.session_state.count} Headlines Generated!</div>", unsafe_allow_html=True)

st.divider()

# Generate button
if st.button("🎲 GENERATE BREAKING NEWS!", use_container_width=True):
    headline = f"{random.choice(subjects)} {random.choice(actions)} {random.choice(things)}!"
    st.session_state.history.insert(0, headline)
    st.session_state.current = headline
    st.session_state.count += 1

# Show headline
if st.session_state.current:
    headline = st.session_state.current
    st.markdown(f"""
        <div class="headline-box">
            <div class="breaking">⚡ BREAKING NEWS ⚡</div>
            <div class="headline-text">📢 {headline}</div>
        </div>
    """, unsafe_allow_html=True)

    # Share buttons
    whatsapp_url = f"https://wa.me/?text={urllib.parse.quote('BREAKING NEWS: ' + headline + ' 😂 (Generated by Fake News Generator)')}"
    twitter_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote('BREAKING NEWS: ' + headline + ' 😂 #FakeNews #Fun')}"

    st.markdown(f"""
        <div style='text-align:center; margin-top:15px;'>
            <a href='{whatsapp_url}' target='_blank' class='share-btn'>📱 Share on WhatsApp</a>
            <a href='{twitter_url}' target='_blank' class='twitter-btn'>🐦 Share on Twitter</a>
        </div>
    """, unsafe_allow_html=True)

# History
if st.session_state.history:
    st.divider()
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("<h3 style='color:#feca57;'>📜 Headlines History</h3>", unsafe_allow_html=True)
    with col2:
        if st.button("🗑️ Clear All"):
            st.session_state.history = []
            st.session_state.current = ""
            st.session_state.count = 0
            st.rerun()

    for i, item in enumerate(st.session_state.history):
        st.markdown(f"<div class='history-item'>#{len(st.session_state.history)-i} 🔴 {item}</div>", unsafe_allow_html=True)

st.divider()
st.markdown("<p style='text-align:center; color:#444; font-size:12px;'>Made with ❤️ by Iffat | All news is 100% FAKE!</p>", unsafe_allow_html=True)