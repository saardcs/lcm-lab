import streamlit as st
import math
import qrcode
import io

# --------------------------
# Setup: LCM Problem List (Sequential)
problems = [
    (3, 5), (4, 6), (5, 7), (8, 9),
    (2, 7), (3, 8), (6, 9), (5, 11)
]

# Initialize session state
if "lcm_index" not in st.session_state:
    st.session_state.lcm_index = 0
    st.session_state.lcm_score = 0

# --------------------------
# Header
st.title("🔁 LCM Lab (Sequential Mode)")
st.markdown("Type the LCM of the number pair shown. Get instant feedback and move to the next!")

# Sidebar with QR code
st.sidebar.header("Scan This QR Code to View Menu Online")

qr_link = "https://lcm-lab.streamlit.app"
qr = qrcode.make(qr_link)
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)

st.sidebar.image(buf, width=300, caption=qr_link)

# --------------------------
# LCM Calculation Function
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# --------------------------
# Problem Display
if st.session_state.lcm_index < len(problems):
    a, b = problems[st.session_state.lcm_index]
    st.subheader(f"📘 Problem {st.session_state.lcm_index + 1} of {len(problems)}")
    st.write(f"What is the LCM of **{a} and {b}**?")

    user_answer = st.number_input("Your answer:", min_value=1, step=1, key="input_lcm")

    if st.button("Submit"):
        correct = lcm(a, b)
        if user_answer == correct:
            st.success("✅ Correct!")
            st.session_state.lcm_score += 1
            st.session_state.lcm_index += 1
            st.rerun()
        else:
            st.error("❌ Incorrect. Try again!")

else:
    st.success("🎉 You've completed all LCM problems!")
    st.write(f"Your score: **{st.session_state.lcm_score} / {len(problems)}**")

    if st.button("🔁 Start Over"):
        st.session_state.lcm_index = 0
        st.session_state.lcm_score = 0
        st.rerun()
