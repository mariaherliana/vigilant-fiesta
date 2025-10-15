import streamlit as st

st.set_page_config(
    page_title="💙 Gross-Up Calculator",
    page_icon="💰",
    layout="centered"
)

# --- Sky-blue theme ---
st.markdown("""
    <style>
        body, .stApp { background-color: #e6f3ff; }
        .title { color: #007acc; text-align: center; font-weight: 700; }
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

st.markdown("<h1 class='title'>Gross-Up Calculator 💸</h1>", unsafe_allow_html=True)
st.markdown("Enter your **net payment** and **gross-up percentage** below:")

# --- defaults ---
DEFAULT_NET = 100000.0
DEFAULT_RATE = 2.0

# --- session state init ---
if "calc_trigger" not in st.session_state:
    st.session_state.calc_trigger = False

# --- inputs ---
net_amount = st.number_input(
    "Net Amount (₱ or any currency)",
    min_value=0.0,
    value=DEFAULT_NET,
    step=100.0,
    format="%.2f"
)
gross_up_percent = st.number_input(
    "Gross-Up Percentage (%)",
    min_value=0.0,
    value=DEFAULT_RATE,
    step=0.1,
    format="%.2f"
)

# --- buttons ---
col1, col2 = st.columns(2)
calc = col1.button("Calculate")
reset = col2.button("Reset")

# --- logic ---
if calc:
    if gross_up_percent >= 100:
        st.error("Gross-up percentage cannot be 100% or more.")
    else:
        gross_value = (100 / (100 - gross_up_percent)) * net_amount
        rounded_result = round(gross_value)
        diff = rounded_result - net_amount

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f"<div class='result-box'>💰 Grossed-Up Amount:<br>"
            f"<span style='font-size:1.8rem;'>{rounded_result:,.0f}</span></div>",
            unsafe_allow_html=True
        )
        st.markdown("**Details:**")
        st.write(f"- Formula: (100 / (100 - {gross_up_percent})) × {net_amount:,.2f}")
        st.write(f"- Exact (unrounded): {gross_value:,.2f}")
        st.write(f"- Rounded difference: {diff:,.2f}")

elif reset:
    # rebuild page with defaults
    st.experimental_set_query_params(reset="true")
    st.rerun()

st.markdown("<br><hr><small style='color:#888;'>Internal use only — Gross-Up Calculator v1.3</small>", unsafe_allow_html=True)
