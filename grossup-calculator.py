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
        .calc-box {
            background-color: #ffffffaa;
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
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

# --- Layout: two columns for calculators ---
left_col, right_col = st.columns(2, gap="large")

# --- Gross-Up Calculator ---
with left_col:
    st.markdown("### 💙 Gross-Up Calculator")
    net_amount = st.number_input("Net Amount", min_value=0.0, value=100000.0, step=100.0, format="%.2f", key="gross_net")
    rate = st.number_input("Gross-Up Percentage (%)", min_value=0.0, value=2.0, step=0.1, format="%.2f", key="gross_rate")

    calc_gross = st.button("Calculate Gross-Up", key="calc_gross")
    reset_gross = st.button("Reset Gross-Up", key="reset_gross")

# --- Tax Deduction Calculator ---
with right_col:
    st.markdown("### 💙 Tax Deduction Calculator")
    gross_amount = st.number_input("Gross Amount", min_value=0.0, value=100000.0, step=100.0, format="%.2f", key="deduct_gross")
    deduction_rate = st.number_input("Deduction Rate (%)", min_value=0.0, value=2.0, step=0.1, format="%.2f", key="deduct_rate")

    calc_deduct = st.button("Calculate Deduction", key="calc_deduct")
    reset_deduct = st.button("Reset Deduction", key="reset_deduct")

# --- Calculations ---
gross_result = None
net_result = None

if calc_gross:
    if rate >= 100:
        st.error("Gross-up percentage cannot be 100% or more.")
    else:
        gross_value = (100 / (100 - rate)) * net_amount
        gross_result = round(gross_value)

if calc_deduct:
    deduction_value = gross_amount * (deduction_rate / 100)
    net_result = round(gross_amount - deduction_value)

if reset_gross or reset_deduct:
    st.rerun()

# --- Results display ---
if gross_result is not None or net_result is not None:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### ✨ Results Comparison")

    res_col1, res_col2 = st.columns(2)

    with res_col1:
        if gross_result is not None:
            st.markdown(
                f"<div class='result-box'>Grossed-Up Amount:<br>"
                f"<span style='font-size:1.8rem;'>{gross_result:,.0f}</span></div>",
                unsafe_allow_html=True
            )
        else:
            st.empty()

    with res_col2:
        if net_result is not None:
            st.markdown(
                f"<div class='result-box'>Net After Deduction:<br>"
                f"<span style='font-size:1.8rem;'>{net_result:,.0f}</span></div>",
                unsafe_allow_html=True
            )
        else:
            st.empty()

st.markdown("<br><hr><small style='color:#888;'>Internal use only — Gross-Up & Tax Deduction v2.1</small>", unsafe_allow_html=True)
