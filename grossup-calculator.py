import streamlit as st

st.set_page_config(
    page_title="💙 Gross-Up & Tax Deduction Calculator",
    page_icon="💰",
    layout="wide"
)

# --- Sky-blue theme ---
st.markdown("""
    <style>
        body, .stApp { background-color: #e6f3ff; }
        .title { color: #007acc; text-align: center; font-weight: 700; margin-bottom: 1rem; }
        .result-box {
            background-color: #cce6ff;
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            font-size: 1.4rem;
            color: #004d80;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>💸 Gross-Up & Tax Deduction Calculator</h1>", unsafe_allow_html=True)

# --- Initialize session state ---
for key in ["gross_result", "net_result"]:
    if key not in st.session_state:
        st.session_state[key] = None

# --- Layout: two calculators ---
left_col, right_col = st.columns(2, gap="large")

# --- Gross-Up Calculator ---
with left_col:
    st.markdown("### 💙 Gross-Up Calculator")
    net_amount = st.number_input("Net Amount", min_value=0.0, value=100000.0, step=100.0, format="%.2f", key="gross_net")
    rate = st.number_input("Gross-Up Percentage (%)", min_value=0.0, value=2.0, step=0.1, format="%.2f", key="gross_rate")

    col1, col2 = st.columns(2)
    if col1.button("Calculate Gross-Up"):
        if rate >= 100:
            st.error("Gross-up percentage cannot be 100% or more.")
        else:
            gross_value = (100 / (100 - rate)) * net_amount
            st.session_state.gross_result = round(gross_value)

    if col2.button("Reset Gross-Up"):
        st.session_state.gross_result = None
        st.rerun()

# --- Tax Deduction Calculator ---
with right_col:
    st.markdown("### 💙 Tax Deduction Calculator")
    gross_amount = st.number_input("Gross Amount", min_value=0.0, value=100000.0, step=100.0, format="%.2f", key="deduct_gross")
    deduction_rate = st.number_input("Deduction Rate (%)", min_value=0.0, value=2.0, step=0.1, format="%.2f", key="deduct_rate")

    col3, col4 = st.columns(2)
    if col3.button("Calculate Deduction"):
        deduction_value = gross_amount * (deduction_rate / 100)
        st.session_state.net_result = round(gross_amount - deduction_value)

    if col4.button("Reset Deduction"):
        st.session_state.net_result = None
        st.rerun()

# --- Results side-by-side ---
if st.session_state.gross_result or st.session_state.net_result:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### ✨ Results Comparison")

    res_col1, res_col2 = st.columns(2)
    with res_col1:
        if st.session_state.gross_result:
            st.markdown(
                f"<div class='result-box'>Grossed-Up Amount:<br>"
                f"<span style='font-size:1.8rem;'>{st.session_state.gross_result:,.0f}</span></div>",
                unsafe_allow_html=True
            )

    with res_col2:
        if st.session_state.net_result:
            st.markdown(
                f"<div class='result-box'>Net After Deduction:<br>"
                f"<span style='font-size:1.8rem;'>{st.session_state.net_result:,.0f}</span></div>",
                unsafe_allow_html=True
            )

st.markdown("<br><hr><small style='color:#888;'>Internal use only — Gross-Up & Tax Deduction v2.2</small>", unsafe_allow_html=True)
