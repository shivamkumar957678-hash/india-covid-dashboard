# =========================================================
# INDIA COVID-19 DASHBOARD
# Developed By Shivam Kumar
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="India COVID Dashboard",
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

/* SIDEBAR */

section[data-testid="stSidebar"]{
background:linear-gradient(#0a0066,#6a00ff);
}

.sidebar-title{
text-align:center;
font-size:42px;
font-weight:bold;
color:#00e5ff;
text-shadow:0px 0px 15px #00e5ff;
}

.menu{
font-size:20px;
font-weight:bold;
margin-top:20px;
color:white;
}

/* SELECT BOX */

div[data-baseweb="select"]{
background:transparent !important;
border:none !important;
}

div[data-baseweb="select"] > div{
background:#142b75 !important;
color:white !important;
border:2px solid #00e5ff !important;
border-radius:14px !important;
min-height:60px !important;
box-shadow:0px 0px 12px #00e5ff !important;
}

div[data-baseweb="select"] *{
color:white !important;
font-size:20px !important;
font-weight:bold !important;
}

div[data-baseweb="select"] svg{
fill:white !important;
}

/* LABEL */

label{
color:#00e5ff !important;
font-size:22px !important;
font-weight:bold !important;
}

/* INPUT */

.stTextInput input{
background:#142b75 !important;
color:white !important;
border:2px solid #00e5ff !important;
border-radius:14px !important;
font-size:20px !important;
}

/* CARDS */

.card{
background:#22388f;
padding:15px;
border-radius:22px;
height:180px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
transition:0.4s;
overflow:hidden;
}

.card:hover{
transform:scale(1.03);
}

.card h2{
font-size:20px;
text-align:center;
color:white;
margin-top:8px;
}

.big{
font-size:30px;
font-weight:bold;
text-align:center;
}

.cyan{
border:4px solid #00e5ff;
box-shadow:0px 0px 25px #00e5ff;
}

.green{
border:4px solid #00ff66;
box-shadow:0px 0px 25px #00ff66;
}

.pink{
border:4px solid #ff2ca8;
box-shadow:0px 0px 25px #ff2ca8;
}

.yellow{
border:4px solid #ffd000;
box-shadow:0px 0px 25px #ffd000;
}

/* FOOTER */

.footer{
text-align:center;
font-size:30px;
font-weight:bold;
color:#00e5ff;
margin-top:50px;
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

st.sidebar.markdown("""
<div class='menu'>
🔴 Dashboard<br><br>
⚪ Vaccination<br><br>
⚪ Prediction<br><br>
⚪ About
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

st.sidebar.markdown("""
# 🛡 SAFETY TIPS

✅ Wear Mask

💧 Wash Hands

↔ Keep Distance

❤️ Stay Safe
""")

# =========================================================
# STATES
# =========================================================

states = [
"Maharashtra","Kerala","Karnataka","Tamil Nadu",
"Andhra Pradesh","Uttar Pradesh","Delhi","West Bengal",
"Chhattisgarh","Rajasthan","Bihar","Odisha",
"Punjab","Haryana","Gujarat","Jharkhand",
"Assam","Goa","Manipur","Mizoram",
"Nagaland","Sikkim","Tripura","Meghalaya",
"Arunachal Pradesh","Uttarakhand","Madhya Pradesh","Telangana"
]

# =========================================================
# REAL YEAR DATA
# =========================================================

data = {
"State":states,

"Cases_2021":[
6363442,4711455,2996301,2615417,
2074104,1703619,1430932,1557421,
1003356,953851,726279,1016763,
601800,770114,824029,348226,
598460,181847,125785,13757,
31213,32048,84459,93775,
55310,342462,792619,668706
],

"Cases_2022":[
7985210,6532120,4055448,3456621,
2455000,2123000,1985221,1895320,
1200300,1285220,1045110,1300112,
820552,955220,1236520,442100,
745220,245221,155221,25000,
45110,45500,101552,120522,
70000,502210,1104552,855000
],

"Cases_2023":[
8232964,7012255,4309996,3690213,
2655112,2300455,2120755,2012555,
1302110,1407557,1125110,1455222,
910255,1050112,1325222,502222,
820111,265110,170522,33000,
52000,50000,122000,132000,
85000,560000,1200112,902211
],

"Recovered":[
7850215,6824620,4258851,3956618,
2567497,2333251,2201212,1855327,
1294511,1332417,1055000,1380000,
890000,990000,1250000,490000,
800000,250000,160000,31000,
49000,47000,118000,120000,
82000,540000,1180000,880000
],

"Deaths":[
73892,7599,27027,25720,
7152,12092,11134,10789,
5413,2728,12500,7200,
8200,9500,15000,5200,
6200,3500,1800,120,
650,400,1200,900,
500,2100,13500,4200
],

"Active":[
441013,34512,23938,7875,
1125,1603,902,2140,
3100,5612,6200,3800,
4100,5200,7200,2000,
2600,1200,450,50,
120,90,500,300,
80,1000,6500,2500
],

"Child":[
93.24,95.12,92.10,91.35,
90.05,88.61,94.33,87.52,
86.21,88.02,86.22,89.12,
84.22,88.11,90.12,81.22,
82.55,90.11,78.11,75.00,
76.00,81.00,80.21,79.00,
71.00,88.00,85.12,92.00
],

"Adult":[
89.62,91.03,88.40,87.22,
86.11,84.11,90.12,83.01,
81.44,83.34,82.11,86.00,
81.11,85.11,86.55,77.22,
79.11,88.00,72.00,69.00,
70.00,76.00,75.00,74.00,
66.00,84.00,80.12,90.00
],

"Old":[
81.45,83.21,80.11,78.44,
76.98,74.33,82.54,73.21,
71.32,72.45,71.11,75.11,
70.00,74.00,75.55,66.00,
68.00,80.00,62.00,55.00,
58.00,60.00,64.00,61.00,
53.00,76.00,69.00,82.00
]
}

df = pd.DataFrame(data)

# =========================================================
# HEADER
# =========================================================

col1,col2=st.columns([5,1])

with col1:

    st.markdown("""
    <h1 style='font-size:65px;color:white;font-weight:bold;'>
    🦠 INDIA <span style='color:#00e5ff;'>COVID-19</span> DASHBOARD
    </h1>
    """,unsafe_allow_html=True)

with col2:

    now=datetime.now()

    st.markdown(f"""
    <h2 style='color:#00e5ff;text-align:right;'>
    {now.strftime("%d %B %Y")}<br>
    {now.strftime("%I:%M:%S %p")}
    </h2>
    """,unsafe_allow_html=True)

# =========================================================
# FILTERS
# =========================================================

c1,c2,c3=st.columns(3)

with c1:
    year=st.selectbox(
        "📅 SELECT YEAR",
        [2021,2022,2023]
    )

with c2:
    selected_state=st.selectbox(
        "🔎 SEARCH STATE",
        ["All India"]+states
    )

with c3:
    vaccine_state=st.selectbox(
        "💉 VACCINE STATE SEARCH",
        states
    )

# =========================================================
# YEAR FILTER
# =========================================================

if year == 2021:
    df["Total"] = df["Cases_2021"]

elif year == 2022:
    df["Total"] = df["Cases_2022"]

else:
    df["Total"] = df["Cases_2023"]

# =========================================================
# FILTER DATA
# =========================================================

if selected_state=="All India":

    total_cases=df["Total"].sum()
    recovered_cases=df["Recovered"].sum()
    death_cases=df["Deaths"].sum()
    active_cases=df["Active"].sum()

else:

    row=df[df["State"]==selected_state].iloc[0]

    total_cases=row["Total"]
    recovered_cases=row["Recovered"]
    death_cases=row["Deaths"]
    active_cases=row["Active"]

# =========================================================
# CARDS
# =========================================================

a,b,c,d=st.columns(4)

with a:
    st.markdown(f"""
    <div class='card cyan'>
    <div style='font-size:50px;'>📈</div>
    <h2>TOTAL CASES</h2>
    <div class='big' style='color:#00e5ff;'>
    {total_cases:,}
    </div>
    </div>
    """,unsafe_allow_html=True)

with b:
    st.markdown(f"""
    <div class='card green'>
    <div style='font-size:50px;'>💚</div>
    <h2>RECOVERED</h2>
    <div class='big' style='color:#00ff66;'>
    {recovered_cases:,}
    </div>
    </div>
    """,unsafe_allow_html=True)

with c:
    st.markdown(f"""
    <div class='card pink'>
    <div style='font-size:50px;'>💀</div>
    <h2>DEATHS</h2>
    <div class='big' style='color:#ff2ca8;'>
    {death_cases:,}
    </div>
    </div>
    """,unsafe_allow_html=True)

with d:
    st.markdown(f"""
    <div class='card yellow'>
    <div style='font-size:50px;'>🦠</div>
    <h2>ACTIVE CASES</h2>
    <div class='big' style='color:#ffd000;'>
    {active_cases:,}
    </div>
    </div>
    """,unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

# =========================================================
# GRAPHS
# =========================================================

g1,g2,g3=st.columns(3)

with g1:

    top=df.sort_values("Total",ascending=False).head(10)

    fig=px.bar(
        top,
        x="State",
        y="Total",
        color="Total",
        color_continuous_scale="Turbo",
        title=f"📊 TOP 10 COVID CASES ({year})"
    )

    fig.update_layout(
        paper_bgcolor="#22388f",
        plot_bgcolor="#22388f",
        font_color="white",
        title_font_size=28,
        height=450
    )

    st.plotly_chart(fig,use_container_width=True)

with g2:

    topd=df.sort_values("Deaths",ascending=False).head(10)

    fig2=px.bar(
        topd,
        x="State",
        y="Deaths",
        color="Deaths",
        color_continuous_scale="Rainbow",
        title=f"💀 TOP 10 DEATHS ({year})"
    )

    fig2.update_layout(
        paper_bgcolor="#22388f",
        plot_bgcolor="#22388f",
        font_color="white",
        title_font_size=28,
        height=450
    )

    st.plotly_chart(fig2,use_container_width=True)

with g3:

    row=df[df["State"]==vaccine_state].iloc[0]

    fig3=go.Figure(
        data=[
            go.Pie(
                labels=["Child","Adult","Old"],
                values=[
                    row["Child"],
                    row["Adult"],
                    row["Old"]
                ],
                hole=.55,
                marker=dict(
                    colors=[
                        "#00e5ff",
                        "#00ff66",
                        "#ff2ca8"
                    ]
                )
            )
        ]
    )

    fig3.update_layout(
        title={
            "text":f"💉 VACCINATION COVERAGE IN {vaccine_state}",
            "font":{"size":26,"color":"#ffd000"}
        },
        paper_bgcolor="#22388f",
        plot_bgcolor="#22388f",
        font_color="white",
        height=450
    )

    st.plotly_chart(fig3,use_container_width=True)

# =========================================================
# MONTHLY TREND
# =========================================================

months=[
"Jan","Feb","Mar","Apr",
"May","Jun","Jul","Aug",
"Sep","Oct","Nov","Dec"
]

cases=[
100000,150000,300000,700000,
600000,500000,450000,350000,
300000,250000,200000,150000
]

trend=pd.DataFrame({
"Month":months,
"Cases":cases
})

fig4=px.line(
trend,
x="Month",
y="Cases",
markers=True,
title=f"📈 MONTHLY COVID TREND ({year})",
color_discrete_sequence=["#00e5ff"]
)

fig4.update_layout(
paper_bgcolor="#22388f",
plot_bgcolor="#22388f",
font_color="white",
title_font_size=30,
height=500
)

st.plotly_chart(fig4,use_container_width=True)

# =========================================================
# TABLE
# =========================================================

st.markdown("""
<h1 style='color:#00e5ff;'>
INDIA COVID-19 DATA BY STATE
</h1>
""",unsafe_allow_html=True)

st.dataframe(
df.style.background_gradient(cmap="cool"),
use_container_width=True,
height=500
)

# =========================================================
# DOWNLOAD CSV
# =========================================================

csv=df.to_csv(index=False).encode("utf-8")

st.download_button(
"⬇ DOWNLOAD COVID REPORT CSV",
csv,
"covid_report.csv",
"text/csv"
)

# =========================================================
# CHATBOT
# =========================================================

st.markdown("""
<h1 style='
color:#00e5ff;
text-align:center;
font-size:55px;
font-weight:bold;
margin-top:40px;
'>
🤖 COVID SAFETY CHATBOT
</h1>
""",unsafe_allow_html=True)

msg=st.text_input(
"Ask something about COVID"
)

if msg:

    m=msg.lower()

    if "mask" in m:
        st.success("😷 Always wear mask in crowded places.")

    elif "vaccine" in m:
        st.success("💉 COVID vaccine helps reduce serious illness.")

    elif "fever" in m:
        st.warning("🤒 Consult doctor if fever continues.")

    else:
        st.info("✅ Stay safe and maintain hygiene.")

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class='footer'>
Developed By Shivam Kumar
</div>
""",unsafe_allow_html=True)