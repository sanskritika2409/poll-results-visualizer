import streamlit as st

# ---------------- LOGIN ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🔐 Login to Dashboard")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state.logged_in = True
        else:
            st.error("Invalid Credentials")

if not st.session_state.logged_in:
    login()
    st.stop() 
import streamlit as st
import pandas as pd
import plotly.express as px
from data_loader import load_data
from preprocessing import clean_data
from analysis import summary_stats

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Poll Insights Dashboard", layout="wide")

# -----------------------------
# LOAD DATA
# -----------------------------
df = load_data()
df = clean_data(df)

stats = summary_stats(df)

# -----------------------------
# HEADER (GLASSMORPHISM STYLE)
# -----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .title {
        font-size:40px;
        font-weight:bold;
        color:#00d4ff;
        text-align:center;
    }
    .card {
        padding:20px;
        border-radius:15px;
        background: rgba(255,255,255,0.05);
        box-shadow: 0 4px 30px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
        text-align:center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📊 Poll Results Visualizer Dashboard</div>", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🎛 Filters")

tool_filter = st.sidebar.multiselect(
    "Select Tools",
    df["Preferred_Tool"].unique(),
    default=df["Preferred_Tool"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

df = df[
    (df["Preferred_Tool"].isin(tool_filter)) &
    (df["Gender"].isin(gender_filter))
]

# -----------------------------
# KPI CARDS (ANIMATED STYLE)
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class='card'>
        <h3>📌 Total Responses</h3>
        <h2>{len(df)}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='card'>
        <h3>⭐ Avg Satisfaction</h3>
        <h2>{round(df['Satisfaction'].mean(),2)}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='card'>
        <h3>🏆 Top Tool</h3>
        <h2>{df['Preferred_Tool'].mode()[0]}</h2>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# CHART 1 - TOOL DISTRIBUTION
# -----------------------------
st.subheader("📊 Tool Preference Analysis")

tool_counts = df["Preferred_Tool"].value_counts()

fig = px.bar(
    x=tool_counts.index,
    y=tool_counts.values,
    labels={"x": "Tools", "y": "Votes"},
    title="Most Preferred Tools"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# CHART 2 - SATISFACTION
# -----------------------------
st.subheader("😊 Satisfaction Distribution")
fig2 = px.histogram(df, x="Satisfaction", color="Gender", barmode="group")
st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# CHART 3 - REGION INSIGHTS
# -----------------------------
st.subheader("🌍 Region Analysis")
fig3 = px.pie(df, names="Region", title="Region-wise Response Share")
st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# DOWNLOAD REPORT BUTTON
# -----------------------------
csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="poll_results.csv",
    mime="text/csv"
)
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=5000, key="refresh")
st.write(df.columns)