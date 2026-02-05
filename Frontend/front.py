import streamlit as st
import requests
from PIL import Image

# ================== CONFIG ================== #
st.set_page_config(page_title="TACOS", layout="wide")

API_URL = "http://127.0.0.1:8000/moderate"  # FastAPI endpoint

LABEL_COLS = [
    "toxic",
    "severe_toxic",
    "obscene",
    "threat",
    "insult",
    "identity_hate"
]

# ================== STYLE ================== #
st.markdown("""
<style>
* { font-family: 'Inter', sans-serif; }

.stApp {
    background: linear-gradient(
        135deg,
        #0B0F2F 0%,
        #141A4A 50%,
        #2A1B5E 100%
    );
}

.title {
    font-size: 4rem;
    font-weight: 900;
    color: #DC95E1;
    text-align: center;
    letter-spacing: .45rem;
}

.subtitle {
    color: rgba(255,255,255,.85);
    text-align: center;
    letter-spacing: .28rem;
    font-size: 1.03rem;
}

.comment {
    background: rgba(255,255,255,0.07);
    padding: 1.2rem 1.4rem;
    margin-bottom: 1.2rem;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}

.safe {
    background: linear-gradient(135deg,#6EE7B7,#3ABAB4);
    padding: .35rem .9rem;
    border-radius: 999px;
    font-weight: 700;
    font-size: .85rem;
    color: #062925;
    display: inline-block;
    margin-top: .3rem;
}

textarea, input {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 16px !important;
    border: none !important;
    color: white !important;
}

button[kind="primary"] {
    background: linear-gradient(135deg,#DC95E2,#B983FF);
    border-radius: 16px;
    font-weight: 700;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ================== SESSION STATE ================== #
if "comments" not in st.session_state:
    st.session_state.comments = []

if "page" not in st.session_state:
    st.session_state.page = "home"

if "flag_scores" not in st.session_state:
    st.session_state.flag_scores = None

if "image" not in st.session_state:
    st.session_state.image = None

# ================== API CALL ================== #
def moderate_comment(text):
    try:
        response = requests.post(
            API_URL,
            json={"comment": text},
            timeout=5
        )

        if response.status_code != 200:
            return "ERROR", {}

        data = response.json()
        return data.get("action", "ALLOW"), data.get("scores", {})

    except requests.exceptions.RequestException:
        return "ERROR", {}

# ================== HEADER ================== #
st.markdown('<div class="title">TACOS</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Toxicity Analysis & Comment Observation System</div><br>',
    unsafe_allow_html=True
)

# ================== FLAGGED PAGE ================== #
if st.session_state.page == "flagged":
    st.markdown('<h2 style="color:#ff6b6b;">🚨 Comment Blocked</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:white;font-size:1.1rem;">This comment violates community guidelines.</p>',
        unsafe_allow_html=True
    )

    for label, score in st.session_state.flag_scores.items():
        st.progress(score, text=f"{label.replace('_',' ').title()} — {score:.2f}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Edit Comment"):
            st.session_state.page = "home"
            st.rerun()
    with col2:
        if st.button("Discard"):
            st.session_state.flag_scores = None
            st.session_state.page = "home"
            st.rerun()

    st.stop()

# ================== MAIN INPUT ================== #
col1, col2 = st.columns([1, 1.2])

with col1:
    uploaded = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if uploaded:
        st.session_state.image = Image.open(uploaded)
    if st.session_state.image:
        st.image(st.session_state.image, width=260)

with col2:
    comment = st.text_area("Write Comment", height=130)

    if st.button("Post Comment"):
        if not comment.strip():
            st.warning("Please write a comment")
        elif st.session_state.image is None:
            st.warning("Please upload an image")
        else:
            action, scores = moderate_comment(comment)

            if action == "BLOCK":
                st.session_state.flag_scores = scores
                st.session_state.page = "flagged"
                st.rerun()

            elif action == "WARN":
                st.warning("⚠️ Comment contains offensive language")
                st.session_state.comments.append(comment)
                st.rerun()

            elif action == "ALLOW":
                st.session_state.comments.append(comment)
                st.rerun()

            else:
                st.error("Backend not reachable")

# ================== FEED ================== #
if st.session_state.comments:
    st.markdown("<hr>", unsafe_allow_html=True)
    for c in reversed(st.session_state.comments):
        st.markdown(f"""
        <div class="comment">
            <p style="color:white;">{c}</p>
            <span class="safe">Safe Comment</span>
        </div>
        """, unsafe_allow_html=True)

