import streamlit as st
import pandas as pd
import datetime
import sqlite3

# ----------------- PAGE CONFIGURATION -----------------
st.set_page_config(
    page_title="Broiler Poultry Sales & Database App",
    page_icon="🐔",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main-title {
        color: #1F4E79;
        font-size: 26px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #1F4E79;
        color: white;
        font-weight: bold;
        width: 100%;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🐔 Broiler Sales & Ledger App (Database Saved)<br><span style='font-size:18px; color:#595959;'>(ब्रॉयलर विक्री व उधारी डेटाबेस ॲप)</span></div>", unsafe_allow_html=True)

# ----------------- DATABASE SETUP -----------------
conn = sqlite3.connect('poultry_data.db', check_same_thread=False)
c = conn.cursor()

# Create table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS broiler_sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sale_date TEXT,
        customer_name TEXT,
        total_weight REAL,
        weight_per_bird REAL,
        bird_qty INTEGER,
        rate_per_kg REAL,
        order_amount REAL,
        paid_amount REAL,
        balance_amount REAL,
        mobile_no TEXT,
        village TEXT
    )
''')
conn.commit()

# Function to load data from Database
def load_data():
    return pd.read_sql_query("SELECT * FROM broiler_sales ORDER BY id DESC", conn)

# ----------------- TABS NAVIGATION -----------------
tab1, tab2, tab3 = st.tabs([
    "📝 New Sale / नवीन विक्री", 
    "📊 Customer Ledger / उधारी खातेवही", 
    "📈 Business Dashboard / व्यवसाय सारांश"
])

# ================= TAB 1: NEW SALE =================
with tab1:
    st.subheader("📝 Enter Sale Details / विक्रीची माहिती भरा")
    
    with st.form("sales_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            date = st.date_input("Date / तारीख", datetime.date.today())
            cust_name = st.text_input("Customer Name / ग्राहकाचे नाव *")
            mobile = st.text_input("Mobile No / मोबाईल नंबर")
            village = st.text_input("Village/Area / गाव किंवा क्षेत्र")
            st.success("🐓 Type / प्रकार: Broiler (ब्रॉयलर)")
            
        with col2:
            tot_wt = st.number_input("Total Weight - kg / एकूण वजन (किलो)", min_value=0.0, step=0.5, format="%.2f")
            wt_per_bird = st.number_input("Avg. Weight per Bird - kg / एका पक्षाचे वजन (किलो)", min_value=0.0, step=0.1, format="%.2f")
            
            # Automatic Bird Quantity Calculation
            bird_qty = round(tot_wt / wt_per_bird) if wt_per_bird > 0 else 0
            st.info(f"🐤 **Bird Quantity / पक्षांची संख्या: {bird_qty} Birds (नग)**")
            
            rate = st.number_input("Rate per Kg - ₹ / प्रति किलो दर (₹)", min_value=0.0, step=1.0, format="%.2f")
            
            # Order Amount Calculation
            order_amt = tot_wt * rate
            st.success(f"💰 **Total Bill Amount / एकूण बिल रक्कम: ₹ {order_amt:,.2f}**")
            
            paid_amt = st.number_input("Paid Amount - ₹ / जमा केलेली रक्कम (₹)", min_value=0.0, step=10.0, format="%.2f")
            balance = order_amt - paid_amt
            
            if balance > 0:
                st.warning(f"🔴 **Pending Balance / बाकी उधारी: ₹ {balance:,.2f}**")
            else:
                st.info(f"✅ **Full Paid / पूर्ण भरणा (No Balance)**")

        submit_btn = st.form_submit_button("💾 Save to Database / डेटाबेसमध्ये सेव्ह करा")
        
        if submit_btn:
            if cust_name.strip() != "":
                c.execute('''
                    INSERT INTO broiler_sales 
                    (sale_date, customer_name, total_weight, weight_per_bird, bird_qty, rate_per_kg, order_amount, paid_amount, balance_amount, mobile_no, village)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (str(date), cust_name, tot_wt, wt_per_bird, bird_qty, rate, order_amt, paid_amt, balance, mobile, village))
                conn.commit()
                st.balloons()
                st.success(f"✅ Sale saved permanently for {cust_name}! / {cust_name} यांची नोंद डेटाबेसमध्ये सेव्ह झाली!")
            else:
                st.error("❌ Please enter Customer Name! / कृपया ग्राहकाचे नाव टाका!")

# ================= TAB 2: LEDGER =================
with tab2:
    st.subheader("📊 Customer Sales & Balance Ledger / विक्री व उधारी खातेवही")
    
    df_sales = load_data()
    
    if not df_sales.empty:
        search_cust = st.text_input("🔍 Search Customer Name / ग्राहकाचे नाव शोधून पहा")
        
        df_display = df_sales
        if search_cust:
            df_display = df_display[df_display["customer_name"].str.contains(search_cust, case=False, na=False)]
            
        st.dataframe(df_display, use_container_width=True)
        
        csv_data = df_display.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="📥 Download Excel/CSV Report / एक्सेल रिपोर्ट डाऊनलोड करा",
            data=csv_data,
            file_name=f"Broiler_Sales_Database_{datetime.date.today()}.csv",
            mime="text/csv"
        )
    else:
        st.info("No sales recorded in database yet. / डेटाबेसमध्ये अद्याप कोणतीही विक्री नोंदवलेली नाही.")

# ================= TAB 3: DASHBOARD =================
with tab3:
    st.subheader("📈 Overall Business Dashboard / एकूण व्यवसाय सारांश")
    df_sales = load_data()
    
    if not df_sales.empty:
        col_a, col_b, col_c = st.columns(3)
        
        tot_sales = df_sales["order_amount"].sum()
        tot_paid = df_sales["paid_amount"].sum()
        tot_bal = df_sales["balance_amount"].sum()
        tot_birds = df_sales["bird_qty"].sum()
        tot_weight = df_sales["total_weight"].sum()
        
        col_a.metric("💵 Total Revenue / एकूण विक्री", f"₹ {tot_sales:,.2f}")
        col_b.metric("🟢 Total Paid / जमा रक्कम", f"₹ {tot_paid:,.2f}")
        col_c.metric("🔴 Outstanding / उधारी बाकी", f"₹ {tot_bal:,.2f}")
        
        st.divider()
        col_d, col_e = st.columns(2)
        col_d.metric("🐔 Total Birds Sold / विकलेले एकूण नग", f"{tot_birds:,} Birds")
        col_e.metric("⚖️ Total Weight Sold / विकलेले एकूण वजन", f"{tot_weight:,.2f} kg")
    else:
        st.info("No data available for dashboard. / डॅशबोर्ड पाहण्यासाठी पहिली विक्री सेव्ह करा.")
