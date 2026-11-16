import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import time

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="EcoRoute AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM DESIGN AND CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #F0FDF4;
    color: #1E293B;
}

/* Main Layout */

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main Headings */

h1 {
    color: #14532D !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #166534 !important;
    font-weight: 700 !important;
}

/* Paragraphs */

p, li {
    color: #334155 !important;
    line-height: 1.7;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #14532D,
        #052E16
    );
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #D1FAE5 !important;
}

/* Sidebar Navigation */

[data-testid="stSidebar"] label {
    color: white !important;
}

/* Hero Section */

.hero {
    background: linear-gradient(
        120deg,
        #14532D,
        #047857,
        #10B981
    );
    padding: 45px;
    border-radius: 24px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 10px 30px rgba(20,83,45,0.15);
}

.hero h1 {
    color: white !important;
    font-size: 43px;
}

.hero h2 {
    color: white !important;
    font-size: 26px;
}

.hero p {
    color: #ECFDF5 !important;
    font-size: 17px;
}

/* Cards */

.custom-card {
    background: #FFFFFF;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #BBF7D0;
    box-shadow: 0 5px 18px rgba(20,83,45,0.07);
    margin-bottom: 20px;
    transition: 0.2s ease;
}

.custom-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(20,83,45,0.13);
}

.custom-card h3 {
    color: #14532D !important;
    font-size: 21px;
    font-weight: 700;
}

.custom-card p {
    color: #334155 !important;
    font-size: 15px;
    font-weight: 500;
    line-height: 1.8;
}

.custom-card span {
    color: #047857 !important;
}

/* Metrics */

[data-testid="stMetric"] {
    background: white;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #BBF7D0;
    box-shadow: 0 4px 15px rgba(20,83,45,0.06);
}

[data-testid="stMetricLabel"] {
    color: #475569 !important;
}

[data-testid="stMetricValue"] {
    color: #14532D !important;
}

/* Buttons */

.stButton > button {
    background: linear-gradient(
        90deg,
        #059669,
        #10B981
    );
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 12px 22px;
    font-weight: 700;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background: #047857;
    color: white !important;
    transform: translateY(-2px);
}

/* Input Fields */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"],
.stTimeInput input {
    background: white !important;
    color: #1E293B !important;
    border-radius: 10px;
}

/* Input Labels */

.stTextInput label,
.stSelectbox label,
.stNumberInput label,
.stTimeInput label {
    color: #14532D !important;
    font-weight: 600 !important;
}

/* Captions */

[data-testid="stCaptionContainer"] p {
    color: #64748B !important;
    font-size: 12px;
}

/* Tables */

[data-testid="stTable"] {
    background: white;
    border-radius: 12px;
}

/* Divider */

hr {
    border-color: #D1FAE5;
}

/* Footer */

.footer {
    text-align: center;
    padding: 30px;
    color: #64748B;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SAMPLE RIDE DATA
# ==========================================

rides = [
    {
        "driver": "Student A",
        "area": "North",
        "destination": "JECRC University",
        "time": time(8, 30),
        "seats": 2
    },
    {
        "driver": "Student B",
        "area": "North",
        "destination": "JECRC University",
        "time": time(8, 40),
        "seats": 3
    },
    {
        "driver": "Student C",
        "area": "East",
        "destination": "JECRC University",
        "time": time(9, 0),
        "seats": 2
    },
    {
        "driver": "Student D",
        "area": "South",
        "destination": "JECRC University",
        "time": time(8, 35),
        "seats": 1
    }
]


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown("""
<h1 style="color:white!important;">
🌿 EcoRoute AI
</h1>
<p style="color:#BBF7D0!important;">
SMART CAMPUS MOBILITY
</p>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "EXPLORE",
    [
        "Home",
        "Find a Carpool",
        "Shuttle Planner",
        "Green Suggestions",
        "Impact Dashboard"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
<p style="color:#D1FAE5!important;font-size:13px;">
ONE CAMPUS.<br>
SMARTER JOURNEYS.<br>
A GREENER TOMORROW.
</p>
""", unsafe_allow_html=True)


# ==========================================
# HOME PAGE
# ==========================================

if page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>🌿 EcoRoute AI</h1>
        <h2>Move Smart. Travel Green.</h2>
        <p>
        Your intelligent campus mobility companion.
        Discover shared journeys and sustainable
        transportation options.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Your Mobility, Simplified")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="custom-card">
            <h3>🚗 Smart Carpool</h3>
            <p>
            Discover potential travel matches
            based on your journey details.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="custom-card">
            <h3>🚌 Shuttle Planner</h3>
            <p>
            Explore illustrative campus
            shuttle routes and schedules.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="custom-card">
            <h3>🌱 Green Choices</h3>
            <p>
            Discover sustainable ways
            to travel around campus.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Why EcoRoute AI?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="custom-card">
            <h3>🌍 Sustainable Mobility</h3>
            <p>
            Encourage shared journeys,
            reduce unnecessary solo trips
            and promote greener travel habits.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="custom-card">
            <h3>🔒 Privacy First</h3>
            <p>
            Designed around broad travel areas,
            voluntary participation and
            user-controlled coordination.
            </p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# CARPOOL PAGE
# ==========================================

elif page == "Find a Carpool":

    st.title("🚗 Find Your Carpool")

    st.write(
        "Let's find a smarter way to reach your destination."
    )

    with st.container(border=True):

        st.subheader("Plan Your Journey")

        col1, col2 = st.columns(2)

        with col1:

            area = st.selectbox(
                "Starting Area",
                ["North", "South", "East", "West", "Central"]
            )

            destination = st.selectbox(
                "Destination",
                ["JECRC University"]
            )

        with col2:

            departure = st.time_input(
                "Departure Time",
                value=time(8, 30)
            )

            seats_required = st.number_input(
                "Seats Required",
                min_value=1,
                max_value=6,
                value=1
            )

        search = st.button(
            "🔍 Find My Carpool",
            use_container_width=True
        )

    if search:

        matches = []

        for ride in rides:

            ride_minutes = (
                ride["time"].hour * 60
                + ride["time"].minute
            )

            requested_minutes = (
                departure.hour * 60
                + departure.minute
            )

            difference = abs(
                ride_minutes - requested_minutes
            )

            if (
                ride["area"] == area
                and ride["destination"] == destination
                and difference <= 15
                and ride["seats"] >= seats_required
            ):

                matches.append(ride)

        st.markdown("---")

        st.subheader("Your Potential Matches")

        if matches:

            st.success(
                f"Found {len(matches)} potential match(es)!"
            )

            for ride in matches:

                st.markdown(f"""
                <div class="custom-card">
                    <h3>🚘 {ride['driver']}</h3>
                    <p>📍 Starting Area: {ride['area']}</p>
                    <p>🎯 Destination: {ride['destination']}</p>
                    <p>🕒 Departure:
                    {ride['time'].strftime('%I:%M %p')}</p>
                    <p>💺 Available Seats: {ride['seats']}</p>
                    <span>● Potential Match</span>
                </div>
                """, unsafe_allow_html=True)

                st.caption(
                    "Fictional sample record. "
                    "No real driver or confirmed ride is involved."
                )

        else:

            st.warning(
                "No compatible sample rides found. "
                "Try another area or time."
            )


# ==========================================
# SHUTTLE PLANNER
# ==========================================

elif page == "Shuttle Planner":

    st.title("🚌 Campus Shuttle Planner")

    st.write(
        "Explore illustrative transportation routes."
    )

    routes = [
        ("Route A", "North → University", "8:00 AM"),
        ("Route B", "South → University", "8:15 AM"),
        ("Route C", "East → University", "8:30 AM")
    ]

    for name, stops, schedule in routes:

        st.markdown(f"""
        <div class="custom-card">
            <h3>🚌 {name}</h3>
            <p>📍 {stops}</p>
            <p>🕒 Sample Departure: {schedule}</p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "These routes and timings are illustrative, "
        "not verified university shuttle information."
    )


# ==========================================
# GREEN SUGGESTIONS
# ==========================================

elif page == "Green Suggestions":

    st.title("🌱 Green Travel Suggestions")

    st.write(
        "Choose a travel option that suits your journey."
    )

    options = [
        ("🚶", "Walking",
         "Consider walking for short journeys."),

        ("🚲", "Cycling",
         "Explore cycling where safe and practical."),

        ("🚗", "Carpooling",
         "Share available seats with compatible travellers."),

        ("🚌", "Shared Transport",
         "Consider public or campus transport.")
    ]

    for icon, title, description in options:

        st.markdown(f"""
        <div class="custom-card">
            <h3>{icon} {title}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# IMPACT DASHBOARD
# ==========================================

elif page == "Impact Dashboard":

    st.title("📊 Sustainability Dashboard")

    st.write(
        "Explore illustrative mobility impact indicators."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Sample Shared Journeys",
        "12"
    )

    col2.metric(
        "Potential Trips Avoided",
        "8"
    )

    col3.metric(
        "Estimated CO₂ Savings",
        "5.2 kg"
    )

    st.markdown("---")

    st.subheader("Weekly Mobility Overview")

    data = pd.DataFrame({
        "Day": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
        ],
        "Shared Journeys": [5, 8, 6, 10, 12]
    })

    fig = px.bar(
        data,
        x="Day",
        y="Shared Journeys",
        title="Illustrative Shared Journeys",
        color_discrete_sequence=["#10B981"]
    )

    fig.update_layout(
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        font=dict(
            color="#14532D",
            family="Inter"
        ),
        xaxis_title="Day",
        yaxis_title="Number of Journeys"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.info(
        "All dashboard values are fictional demonstration "
        "data, not measured campus results."
    )


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    🌿 EcoRoute AI
    <br>
    Smart Mobility for a Greener Tomorrow
    <br><br>
    RE-SPIRE'26 | Prototype V1
</div>
""", unsafe_allow_html=True)