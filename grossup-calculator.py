import streamlit as st

st.set_page_config(
    page_title="💙 Gross-Up Calculator",
    page_icon="💰",
    layout="centered"
)

# --- Custom CSS for sky-blue theme ---
st.markdown("""
    <style>
        body {
            background-color: #e6f3ff;
        }
        .stApp {
            background-color: #e6f3ff;
        }
        .title {
            color: #007acc;
            text-align: center;
            font-weight: 700;
        }
        .result-box {
            background-color: #cce6ff;
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            font-size: 1.5rem;
            color: #004d80;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 class='title'>Gross-Up Calculator 💸</h1>", unsafe_allow_html=True)

# --- Input form ---
st.markdown("Enter your **net payment** and **gross-up percentage** below:")

# initialize session state
if "net_amount" not in st.session_state:
    st.session_state.net_amount = 100000.0
if "gross_up_percent" not in st.session_state:
    st.session_state.gross_up_percent = 2.0

# inputs
net_amount = st.number_input(
    "Net Amount (₱ or any currency)",
    min_value=0.0,
    value=st.session_state.net_amount,
    step=100.0,
    format="%.2f",
    key="net_amount"
)

gross_up_percent = st.number_input(
    "Gross-Up Percentage (%)",
    min_value=0.0,
    value=st.session_state.gross_up_percent,
    step=0.1,
    format="%.2f",
    key="gross_up_percent"
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Calculate"):
        if gross_up_percent >= 100:
            st.error("Gross-up percentage cannot be 100% or more.")
        else:
            gross_value = (100 / (100 - gross_up_percent)) * net_amount
            rounded_result = round(gross_value)
            diff = rounded_result - net_amount

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<div class='result-box'>"
                        f"💰 Grossed-Up Amount: <br> <span style='font-size:1.8rem;'>{rounded_result:,.0f}</span>"
                        "</div>", unsafe_allow_html=True)

            st.markdown(f"**Details:**")
            st.write(f"- Formula used: (100 / (100 - {gross_up_percent})) × {net_amount:,.2f}")
            st.write(f"- Exact (unrounded): {gross_value:,.2f}")
            st.write(f"- Rounded difference: {diff:,.2f}")

with col2:
    if st.button("Reset"):
        st.session_state.net_amount = 100000.0
        st.session_state.gross_up_percent = 2.0
        st.rerun()

st.markdown("<br><hr><small style='color:#888;'>Internal use only — Gross-Up Calculator v1.1</small>", unsafe_allow_html=True)
