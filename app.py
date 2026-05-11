# =========================================================
# INDIA COVID-19 ADVANCED DASHBOARD
# Developed By Shivam Kumar
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="India COVID Dashboard",
    page_icon="🦠",
    layout="wide"
)

# =========================================================
# LOADING
# =========================================================

with st.spinner("Loading India COVID Dashboard..."):
    time.sleep(2)

# =========================================================
# SESSION
# =========================================================

if "login" not in st.session_state:
    st.session_state.login = False

# =========================================================
# LOGIN DATA
# =========================================================

USERNAME = "shivam"
PASSWORD = "1234"

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* MAIN */

.stApp{
background:#020f3a;
color:white;
}

/* REMOVE WHITE BAR */

header{
visibility:hidden;
}

[data-testid="stToolbar"]{
display:none;
}

.block-container{
padding-top:0rem;
}

/* LOGIN TITLE */

.title{
text-align:center;
font-size:70px;
font-weight:bold;
color:#00e5ff;
text-shadow:0px 0px 20px #00e5ff;
margin-top:10px;
}

/* LOGIN BOX */

.login-box{
background:#142b75;
padding:40px;
border-radius:25px;
border:3px solid #00e5ff;
box-shadow:0px 0px 30px #00e5ff;
margin-top:20px;
}

/* INPUT */

label{
color:#00e5ff !important;
font-size:22px !important;
font-weight:bold !important;
}

div[data-baseweb="input"]{
background:#142b75 !important;
border:2px solid #00e5ff !important;
border-radius:15px !important;
}

div[data-baseweb="input"] input{
background:transparent !important;
color:white !important;
font-size:22px !important;
text-align:center !important;
}

/* BUTTON */

.stButton>button{
width:100%;
height:55px;
font-size:22px;
font-weight:bold;
background:#00e5ff;
color:black;
border:none;
border-radius:14px;
margin-top:15px;
transition:0.4s;
}

.stButton>button:hover{
transform:scale(1.03);
background:#00c3ff;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
background:linear-gradient(#050033,#6a00ff);
animation: glow 3s infinite;
}

@keyframes glow{
0%{box-shadow:0px 0px 10px #00e5ff;}
50%{box-shadow:0px 0px 30px #00e5ff;}
100%{box-shadow:0px 0px 10px #00e5ff;}
}

.sidebar-title{
text-align:center;
font-size:40px;
font-weight:bold;
color:#00e5ff;
text-shadow:0px 0px 15px #00e5ff;
}

/* CARDS */

.card{
background:#22388f;
padding:15px;
border-radius:20px;
height:170px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
margin-top:10px;
transition:0.4s;
}

.card:hover{
transform:scale(1.05);
}

.card h2{
font-size:20px;
color:white;
}

.big{
font-size:32px;
font-weight:bold;
}

.cyan{
border:4px solid #00e5ff;
box-shadow:0px 0px 20px #00e5ff;
}

.green{
border:4px solid #00ff66;
box-shadow:0px 0px 20px #00ff66;
}

.pink{
border:4px solid #ff2ca8;
box-shadow:0px 0px 20px #ff2ca8;
}

.yellow{
border:4px solid #ffd000;
box-shadow:0px 0px 20px #ffd000;
}

/* MOBILE */

@media screen and (max-width:768px){

.title{
font-size:35px !important;
}

.card{
height:auto !important;
}

}

/* FOOTER */

.footer{
text-align:center;
font-size:30px;
font-weight:bold;
color:#00e5ff;
margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOGIN PAGE
# =========================================================

if st.session_state.login == False:

    st.markdown("""
    <div class='title'>
    🦠 INDIA COVID-19 LOGIN
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3 = st.columns([1,2,1])

    with c2:

        st.markdown("<div class='login-box'>", unsafe_allow_html=True)

        username = st.text_input(
            "👤 Username",
            placeholder="Enter Username"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter Password"
        )

        if st.button("LOGIN"):

            if username == USERNAME and password == PASSWORD:

                st.session_state.login = True
                st.rerun()

            else:
                st.error("❌ Wrong Username or Password")

        if st.button("Forgot Password"):
            st.info("👤 Username : shivam")
            st.info("🔒 Password : 1234")

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# DASHBOARD
# =========================================================

else:

    st.sidebar.markdown("""
    <div class='sidebar-title'>
    🦠 COVID-19
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("## INDIA DASHBOARD")

    # =====================================================
    # REAL STYLE DATA
    # =====================================================

    df = pd.DataFrame({

    "State":[
    "Maharashtra","Kerala","Karnataka","Tamil Nadu",
    "Delhi","Uttar Pradesh","Gujarat","Rajasthan"
    ],

    "Cases":[
    8232964,7012255,4309996,3690213,
    2120755,2300455,1325222,1407557
    ],

    "Recovered":[
    7850215,6824620,4258851,3956618,
    2201212,2333251,1250000,1332417
    ],

    "Deaths":[
    73892,7599,27027,25720,
    11134,12092,15000,2728
    ],

    "Active":[
    441013,34512,23938,7875,
    902,1603,7200,5612
    ],

    "Beds":[
    120000,85000,90000,80000,
    65000,95000,72000,70000
    ],

    "Oxygen":[
    88,92,90,87,
    85,91,89,86
    ]

    })

    # =====================================================
    # HEADER
    # =====================================================

    col1,col2 = st.columns([5,1])

    with col1:

        st.markdown("""
        <h1 style='font-size:60px;color:white;font-weight:bold;'>
        🦠 INDIA <span style='color:#00e5ff;'>COVID-19</span> DASHBOARD
        </h1>
        """, unsafe_allow_html=True)

    with col2:

        now = datetime.now()

        st.markdown(f"""
        <h3 style='color:#00e5ff;text-align:right;'>
        📅 {now.strftime("%d %B %Y")}<br>
        ⏰ {now.strftime("%I:%M:%S %p")}
        </h3>
        """, unsafe_allow_html=True)

    # =====================================================
    # CARDS
    # =====================================================

    total_cases = df["Cases"].sum()
    recovered = df["Recovered"].sum()
    deaths = df["Deaths"].sum()
    active = df["Active"].sum()

    a,b,c,d = st.columns(4)

    with a:
        st.markdown(f"""
        <div class='card cyan'>
        <h2>📈 TOTAL CASES</h2>
        <div class='big'>{total_cases:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown(f"""
        <div class='card green'>
        <h2>💚 RECOVERED</h2>
        <div class='big'>{recovered:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown(f"""
        <div class='card pink'>
        <h2>💀 DEATHS</h2>
        <div class='big'>{deaths:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with d:
        st.markdown(f"""
        <div class='card yellow'>
        <h2>🦠 ACTIVE</h2>
        <div class='big'>{active:,}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # HOSPITAL BEDS CHART
    # =====================================================

    bed_fig = px.bar(
        df,
        x="State",
        y="Beds",
        color="Beds",
        title="🏥 Hospital Beds Availability",
        color_continuous_scale="Turbo"
    )

    st.plotly_chart(bed_fig, use_container_width=True)

    # =====================================================
    # OXYGEN CHART
    # =====================================================

    oxygen_fig = px.line(
        df,
        x="State",
        y="Oxygen",
        markers=True,
        title="🫁 Oxygen Level Monitoring"
    )

    st.plotly_chart(oxygen_fig, use_container_width=True)

    # =====================================================
    # NEWS SECTION
    # =====================================================

    st.markdown("## 📰 COVID NEWS")

    st.info("India vaccination coverage increased successfully.")
    st.info("COVID active cases reduced in multiple states.")
    st.info("Government released updated health guidelines.")

    # =====================================================
    # ADMIN PANEL
    # =====================================================

    st.markdown("## ⚙️ ADMIN PANEL")

    admin_name = st.text_input("Admin Name")
    admin_password = st.text_input(
        "Admin Password",
        type="password"
    )

    if st.button("Admin Login"):

        if admin_name == "admin" and admin_password == "admin123":
            st.success("✅ Admin Login Successful")
        else:
            st.error("❌ Wrong Admin Credentials")

    # =====================================================
    # USER SIGNUP
    # =====================================================

    st.markdown("## 👤 USER SIGNUP")

    new_user = st.text_input("Create Username")
    new_pass = st.text_input(
        "Create Password",
        type="password"
    )

    if st.button("Signup"):
        st.success(f"✅ User {new_user} Registered Successfully")

    # =====================================================
    # VOICE ASSISTANT
    # =====================================================

    st.markdown("## 🎤 VOICE ASSISTANT")

    voice_text = st.text_input("Ask About COVID")

    if st.button("Speak"):
        st.success(f"🤖 Response: {voice_text}")

    # =====================================================
    # TABLE
    # =====================================================

    st.dataframe(
        df.style.background_gradient(cmap="cool"),
        use_container_width=True
    )

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("""
    <div class='footer'>
    Developed By Shivam Kumar
    </div>
    """, unsafe_allow_html=True)
