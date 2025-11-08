import streamlit as st

st.title("📊 Applicability Checker")

# --- Input fields ---
turnover = st.number_input("Enter Turnover (in Crores):", min_value=0.0)
share_capital = st.number_input("Enter Paid-up Share Capital (in Crores):", min_value=0.0)
reserves = st.number_input("Enter Reserves & Surplus (in Crores):", min_value=0.0)
borrowings = st.number_input("Enter Outstanding Borrowings (in Crores):", min_value=0.0)
net_worth = st.number_input("Enter Net Worth (in Crores):", min_value=0.0)
deposits = st.number_input("Enter Outstanding Deposits (in Crores):", min_value=0.0)

holding = st.radio("Is the company a holding/subsidiary of a public company?", ["no", "yes"])
listed = st.radio("Is the company listed on any stock exchange?", ["no", "yes"])
indas_related = st.radio("Is the company a holding/subsidiary/JV/associate of a company where Ind AS applies?", ["no", "yes"])

if st.button("Check Applicability"):
    # Default results
    caro_applicable = "CARO Not Applicable"
    indas_applicable = "Ind AS Not Applicable"
    internal_audit = "Internal Audit NOT Applicable"

    # --- Ind AS applicability logic ---
    if indas_related == "yes" or listed == "yes" or net_worth >= 250:
        indas_applicable = "Ind AS Applicable"

    # --- CARO applicability logic ---
    if indas_related == "yes" or holding == "yes":
        caro_applicable = "CARO Applicable"
    else:
        if not (turnover <= 40 and share_capital <= 4):
            caro_applicable = "CARO Applicable"

    # --- Internal Audit applicability logic ---
    if turnover >= 200 or borrowings >= 100:
        internal_audit = "Internal Audit Applicable"

    # --- Output Section ---
    st.subheader("--- Applicability Results ---")
    st.write(f"**CARO Applicability:** {caro_applicable}")
    st.write(f"**Ind AS Applicability:** {indas_applicable}")
    st.write(f"**Internal Audit Applicability:** {internal_audit}")
