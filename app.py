# =========================================================
# INDIA COVID-19 DASHBOARD
# MAP + HOSPITAL BEDS + OXYGEN LEVEL
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
# CSS
# =========================================================

st.markdown("""
<style>

.stApp{
background:#020f3a;
color:white;
}

header{
visibility:hidden;
}

[data-testid="stToolbar"]{
display:none;
}

.block-container{
padding-top:0rem;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
background:linear-gradient(#0a0066,#6a00ff);
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
# SIDEBAR
# =========================================================

st.sidebar.markdown("""
<div class='sidebar-title'>
🦠 COVID-19
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("## INDIA DASHBOARD")

# =========================================================
# DATA
# =========================================================

df = pd.DataFrame({

"State":[
"Maharashtra","Kerala","Karnataka","Tamil Nadu",
"Delhi","Uttar Pradesh","Bihar","Rajasthan"
],

"lat":[
19.7515,10.8505,15.3173,11.1271,
28.7041,26.8467,25.0961,27.0238
],

"lon":[
75.7139,76.2711,75.7139,78.6569,
77.1025,80.9462,85.3131,74.2179
],

"Cases":[
8232964,7012255,4309996,3690213,
2120755,2300455,1125110,1407557
],

"Recovered":[
7850215,6824620,4258851,3956618,
2201212,2333251,1055000,1332417
],

"Deaths":[
73892,7599,27027,25720,
11134,12092,12500,2728
],

"Active":[
441013,34512,23938,7875,
902,1603,6200,5612
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

# =========================================================
# HEADER
# =========================================================

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

# =========================================================
# TOTAL
# =========================================================

total_cases = df["Cases"].sum()
recovered = df["Recovered"].sum()
deaths = df["Deaths"].sum()
active = df["Active"].sum()

# =========================================================
# CARDS
# =========================================================

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

# =========================================================
# MAP VISUALIZATION
# =========================================================

st.markdown("## 🗺 INDIA COVID MAP")

map_fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    size="Cases",
    color="Cases",
    hover_name="State",
    hover_data=["Beds","Oxygen"],
    zoom=3.5,
    height=500,
    color_continuous_scale="Turbo"
)

map_fig.update_layout(
    mapbox_style="carto-darkmatter",
    paper_bgcolor="#020f3a",
    font_color="white",
    margin={"r":0,"t":0,"l":0,"b":0}
)

st.plotly_chart(map_fig, use_container_width=True)

# =========================================================
# HOSPITAL BEDS CHART
# =========================================================

st.markdown("## 🏥 HOSPITAL BEDS AVAILABLE")

bed_fig = px.bar(
    df,
    x="State",
    y="Beds",
    color="Beds",
    title="State Wise Hospital Beds",
    color_continuous_scale="Turbo"
)

bed_fig.update_layout(
    paper_bgcolor="#22388f",
    plot_bgcolor="#22388f",
    font_color="white",
    height=500
)

st.plotly_chart(bed_fig, use_container_width=True)

# =========================================================
# OXYGEN LEVEL CHART
# =========================================================

st.markdown("## 🫁 OXYGEN AVAILABILITY")

oxygen_fig = px.line(
    df,
    x="State",
    y="Oxygen",
    markers=True,
    title="State Wise Oxygen Availability"
)

oxygen_fig.update_layout(
    paper_bgcolor="#22388f",
    plot_bgcolor="#22388f",
    font_color="white",
    height=500
)

st.plotly_chart(oxygen_fig, use_container_width=True)

# =========================================================
# TABLE
# =========================================================

st.dataframe(
    df.style.background_gradient(cmap="cool"),
    use_container_width=True
)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class='footer'>
Developed By Shivam Kumar
</div>
""", unsafe_allow_html=True)
