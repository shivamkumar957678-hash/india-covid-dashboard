# =========================================================
# INDIA COVID-19 DASHBOARD
# FINAL ADVANCED VERSION
# Developed By Shivam Kumar
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="India COVID Dashboard",
    page_icon="🦠",
    layout="wide"
)

# =========================================================
# LOGIN SESSION
# =========================================================

if "login" not in st.session_state:
    st.session_state.login = False

USERNAME = "shivam"
PASSWORD = "1234"

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp{
background:#020f3a;
color:white;
}

/* REMOVE WHITE HEADER */

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
font-size:65px;
font-weight:bold;
color:#00e5ff;
margin-top:10px;
text-shadow:0px 0px 20px #00e5ff;
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

/* LABEL */

label{
color:#00e5ff !important;
font-size:22px !important;
font-weight:bold !important;
}

/* INPUT */

div[data-baseweb="input"]{
background:#142b75 !important;
border:2px solid #00e5ff !important;
border-radius:15px !important;
box-shadow:0px 0px 10px #00e5ff !important;
}

div[data-baseweb="input"] input{
background:transparent !important;
color:white !important;
font-size:20px !important;
font-weight:bold !important;
text-align:center !important;
}

/* BUTTON */

.stButton>button{
width:100%;
height:50px;
font-size:20px;
font-weight:bold;
background:#00e5ff;
color:black;
border:none;
border-radius:12px;
margin-top:10px;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
background:linear-gradient(#0a0066,#6a00ff);
}

.sidebar-title{
text-align:center;
font-size:35px;
font-weight:bold;
color:#00e5ff;
text-shadow:0px 0px 15px #00e5ff;
}

/* CARDS */

.card{
background:#22388f;
padding:15px;
border-radius:20px;
height:160px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
margin-top:10px;
}

.card h2{
font-size:18px;
color:white;
}

.big{
font-size:30px;
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

/* FOOTER */

.footer{
text-align:center;
font-size:28px;
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
    # DATA
    # =====================================================

    df = pd.DataFrame({

    "State":[
    "Maharashtra","Kerala","Karnataka","Tamil Nadu",
    "Delhi","Uttar Pradesh","Bihar","Rajasthan",
    "Punjab","Haryana","Gujarat","Madhya Pradesh"
    ],

    "Cases":[
    8232964,7012255,4309996,3690213,
    2120755,2300455,1125110,1407557,
    910255,1050112,1325222,1200112
    ],

    "Recovered":[
    7850215,6824620,4258851,3956618,
    2201212,2333251,1055000,1332417,
    890000,990000,1250000,1180000
    ],

    "Deaths":[
    73892,7599,27027,25720,
    11134,12092,12500,2728,
    8200,9500,15000,13500
    ],

    "Active":[
    441013,34512,23938,7875,
    902,1603,6200,5612,
    4100,5200,7200,6500
    ]
    })

    # =====================================================
    # HEADER
    # =====================================================

    col1,col2 = st.columns([5,1])

    with col1:

        st.markdown("""
        <h1 style='font-size:55px;color:white;font-weight:bold;'>
        🦠 INDIA COVID-19 DASHBOARD
        </h1>
        """, unsafe_allow_html=True)

    with col2:

        now = datetime.now()

        st.markdown(f"""
        <h4 style='color:#00e5ff;text-align:right;'>
        📅 {now.strftime("%d %B %Y")}<br>
        ⏰ {now.strftime("%I:%M:%S %p")}
        </h4>
        """, unsafe_allow_html=True)

    # =====================================================
    # YEAR
    # =====================================================

    year = st.selectbox(
        "📅 SELECT YEAR",
        [2021,2022,2023]
    )

    # =====================================================
    # TOTAL
    # =====================================================

    total_cases = df["Cases"].sum()
    recovered = df["Recovered"].sum()
    deaths = df["Deaths"].sum()
    active = df["Active"].sum()

    # =====================================================
    # CARDS
    # =====================================================

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
    # VACCINE
    # =====================================================

    st.markdown("## 💉 VACCINE STATUS")

    vaccine_state = st.selectbox(
        "🔍 Vaccine State Search",
        df["State"]
    )

    v1,v2,v3 = st.columns(3)

    with v1:
        st.markdown("""
        <div class='card cyan'>
        <h2>👶 CHILD</h2>
        <div class='big'>72%</div>
        </div>
        """, unsafe_allow_html=True)

    with v2:
        st.markdown("""
        <div class='card green'>
        <h2>🧑 ADULT</h2>
        <div class='big'>91%</div>
        </div>
        """, unsafe_allow_html=True)

    with v3:
        st.markdown("""
        <div class='card pink'>
        <h2>👴 OLD AGE</h2>
        <div class='big'>84%</div>
        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # CHATBOT
    # =====================================================

    st.markdown("## 🤖 COVID CHATBOT")

    question = st.text_input(
        "Ask something about COVID"
    )

    if st.button("ASK"):

        if "symptom" in question.lower():
            st.success("Common symptoms are fever and cough.")

        elif "vaccine" in question.lower():
            st.success("Vaccination helps reduce infection risk.")

        else:
            st.success("Stay safe and wear mask.")

    # =====================================================
    # CASE GRAPH
    # =====================================================

    fig = px.bar(
        df,
        x="State",
        y="Cases",
        color="Cases",
        title=f"📊 TOP COVID CASES ({year})",
        color_continuous_scale="Turbo"
    )

    fig.update_layout(
        paper_bgcolor="#22388f",
        plot_bgcolor="#22388f",
        font_color="white",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    # =====================================================
    # EXTRA DATA
    # =====================================================

    extra_df = pd.DataFrame({

    "State":[
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar",
    "Chhattisgarh","Goa","Gujarat","Haryana",
    "Himachal Pradesh","Jharkhand","Karnataka","Kerala",
    "Madhya Pradesh","Maharashtra","Manipur","Meghalaya",
    "Mizoram","Nagaland","Odisha","Punjab",
    "Rajasthan","Sikkim","Tamil Nadu","Telangana",
    "Tripura","Uttar Pradesh","Uttarakhand","West Bengal"
    ],

    "lat":[
    15.9129,28.2180,26.2006,25.0961,
    21.2787,15.2993,22.2587,29.0588,
    31.1048,23.6102,15.3173,10.8505,
    22.9734,19.7515,24.6637,25.4670,
    23.1645,26.1584,20.9517,31.1471,
    27.0238,27.5330,11.1271,18.1124,
    23.9408,26.8467,30.0668,22.9868
    ],

    "lon":[
    79.7400,94.7278,92.9376,85.3131,
    81.8661,74.1240,71.1924,76.0856,
    77.1734,85.2799,75.7139,76.2711,
    78.6569,75.7139,93.9063,91.3662,
    92.9376,94.5624,85.0985,75.3412,
    74.2179,88.5122,78.6569,79.0193,
    91.9882,80.9462,79.0193,87.8550
    ],

    "Beds":[
    85000,12000,35000,90000,
    42000,10000,75000,50000,
    25000,30000,95000,88000,
    70000,120000,12000,15000,
    10000,11000,60000,45000,
    68000,8000,85000,65000,
    12000,110000,20000,78000
    ],

    "Oxygen":[
    91,88,90,89,
    87,92,90,88,
    86,87,93,94,
    89,95,85,84,
    83,82,90,88,
    89,86,92,91,
    85,94,87,90
    ],

    "Cases":[
    2345678,123456,987654,1125110,
    765432,223344,1325222,1050112,
    456789,567890,4309996,7012255,
    1200112,8232964,223344,112233,
    99887,88776,998877,910255,
    1407557,77665,3690213,998877,
    66554,2300455,223344,1500112
    ]
    })

    # =====================================================
    # MAP
    # =====================================================

    st.markdown("## 🗺 INDIA COVID MAP")

    map_fig = px.scatter_mapbox(
        extra_df,
        lat="lat",
        lon="lon",
        size="Cases",
        color="Cases",
        hover_name="State",
        hover_data=["Beds","Oxygen"],
        zoom=3.5,
        height=600,
        color_continuous_scale="Turbo"
    )

    map_fig.update_layout(
        mapbox_style="carto-darkmatter",
        paper_bgcolor="#22388f",
        font_color="white"
    )

    st.plotly_chart(map_fig, use_container_width=True)

    # =====================================================
    # BEDS
    # =====================================================

    st.markdown("## 🏥 HOSPITAL BEDS")

    beds_fig = px.bar(
        extra_df,
        x="State",
        y="Beds",
        color="Beds",
        color_continuous_scale="Turbo"
    )

    beds_fig.update_layout(
        paper_bgcolor="#22388f",
        plot_bgcolor="#22388f",
        font_color="white",
        height=600
    )

    st.plotly_chart(beds_fig, use_container_width=True)

    # =====================================================
    # OXYGEN
    # =====================================================

    st.markdown("## 🫁 OXYGEN AVAILABILITY")

    oxygen_fig = px.line(
        extra_df,
        x="State",
        y="Oxygen",
        markers=True
    )

    oxygen_fig.update_layout(
        paper_bgcolor="#22388f",
        plot_bgcolor="#22388f",
        font_color="white",
        height=600
    )

    st.plotly_chart(oxygen_fig, use_container_width=True)

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
