
import streamlit as st

from conversions import convert_units


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="ConvertIQ | Unit Converter",
    page_icon="🔄",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================



dark_mode = st.session_state.get("dark_mode", False)

st.markdown("""
<style>

/* MAKE ONLY CATEGORY LABEL BOLD */

.st-key-category [data-testid="stWidgetLabel"] p {
    font-weight: 800 !important;
    font-size: 16px !important;
    color: #101d50 !important;
}

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);


/* ================================================
   GLOBAL BACKGROUND
================================================ */

.stApp {
    background:
        radial-gradient(
            ellipse at 100% 0%,
            rgba(125, 140, 255, 0.16),
            transparent 35%
        ),
        radial-gradient(
            ellipse at 0% 100%,
            rgba(147, 130, 255, 0.12),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #f4f5ff,
            #edf3ff,
            #f8f9ff
        );

    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1400px;
    padding: 2rem !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stToolbar"] {
    background: transparent !important;
}


/* ================================================
   TYPOGRAPHY
================================================ */

h1, h2, h3 {
    color: #101d50 !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 800 !important;
}

.stApp p {
    color: #43517f;
}

.stApp label {
    color: #26345f !important;
    font-weight: 600 !important;
}


/* ================================================
   BRAND LOGO
================================================ */

.brand-icon {
    width: 68px;
    height: 68px;

    border-radius: 20px;

    background: linear-gradient(
        135deg,
        #2685ff,
        #6426e9
    );

    display: flex;
    align-items: center;
    justify-content: center;

    position: relative;

    box-shadow:
        0 10px 25px rgba(79, 70, 229, 0.22);
}

.brand-ring {
    width: 37px;
    height: 37px;

    border: 5px solid white;
    border-right-color: transparent;

    border-radius: 50%;

    position: absolute;

    transform: rotate(-35deg);
}

.brand-arrow-top,
.brand-arrow-bottom {
    position: absolute;

    color: white;

    font-size: 25px;
    font-weight: 900;

    line-height: 1;
}

.brand-arrow-top {
    top: 7px;
    right: 9px;
}

.brand-arrow-bottom {
    bottom: 7px;
    left: 9px;
}


/* BRAND TEXT */

.brand-title {
    font-size: 40px;
    font-weight: 800;

    color: #101d50;

    letter-spacing: -1.5px;
}

.brand-title span {
    color: #652ce8;
}

.brand-subtitle {
    font-size: 15px;
    color: #647398;
    margin-top: 4px;
}


/* ================================================
   EQUAL HEIGHT CARDS
================================================ */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.88) !important;

    border: 1px solid #d0d9f5 !important;

    border-radius: 20px !important;

    padding: 22px !important;

    box-sizing: border-box;

    height: auto !important;
    overflow: visible !important;

    box-shadow:
        0 10px 28px rgba(35,55,120,0.07);
}

/* One shared frame for both workspace sections */
.st-key-main-workspace [data-testid="stVerticalBlockBorderWrapper"] {
    min-height: 440px !important;
    height: auto !important;
    overflow: visible !important;
}

.st-key-main-workspace [data-testid="stVerticalBlockBorderWrapper"] > div {
    overflow: visible !important;
}

/* A subtle divider between the converter and explore sections */
@media (min-width: 700px) {
    .st-key-main-workspace [data-testid="stHorizontalBlock"] > div:first-child {
        border-right: 1px solid #d0d9f5;
        padding-right: 1.4rem;
    }
}

div[data-testid="stVerticalBlockBorderWrapper"] h1,
div[data-testid="stVerticalBlockBorderWrapper"] h2,
div[data-testid="stVerticalBlockBorderWrapper"] h3 {
    color: #101d50 !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] p {
    color: #4a5887 !important;
}


/* ================================================
   CATEGORY SELECTOR
================================================ */

.stSelectbox div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.95) !important;

    border: 1px solid #c4cff0 !important;

    border-radius: 11px !important;

    min-height: 48px;
}

.stSelectbox div[data-baseweb="select"] span {
    color: #172554 !important;
}


/* ================================================
   INPUT FIELDS
================================================ */

.stSelectbox label,
.stNumberInput label {
    color: #172554 !important;

    font-size: 14px !important;

    font-weight: 600 !important;
}

.stSelectbox div[data-baseweb="select"] > div,
.stNumberInput div[data-baseweb="input"] {
    background: #ffffff !important;

    border: 1px solid #c4cdec !important;

    border-radius: 11px !important;

    min-height: 48px;
}

.stSelectbox div[data-baseweb="select"] span,
.stNumberInput input {
    color: #172554 !important;

    font-size: 15px !important;
}


/* ================================================
   CONVERT BUTTON
================================================ */

.stButton > button {
    width: 100%;

    min-height: 54px;

    background: linear-gradient(
        100deg,
        #2387ff,
        #6724ed
    ) !important;

    border: none !important;

    border-radius: 12px !important;

    color: white !important;

    font-size: 17px !important;

    font-weight: 700 !important;

    box-shadow:
        0 7px 18px rgba(79,70,229,0.18);

    transition: all 0.2s ease;
}

.stButton > button p,
.stButton > button span {
    color: white !important;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 25px rgba(79,70,229,0.25);
}


/* ================================================
   HERO PANEL
================================================ */

.hero-art {
    height: 290px;
    width: 100%;

    border-radius: 20px;

    position: relative;

    overflow: hidden;

    display: flex;

    align-items: center;
    justify-content: center;

    margin-top: 16px;

    isolation: isolate;
}

.hero-content {
    text-align: center;

    color: white;

    z-index: 2;

    position: relative;
}


/* UNIT ICON CONTAINER */

.unit-icon {
    width: 112px;
    height: 112px;

    border-radius: 27px;

    background: rgba(255,255,255,0.20);

    border: 1px solid rgba(255,255,255,0.38);

    display: flex;

    align-items: center;
    justify-content: center;

    margin: 0 auto 18px;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.10);
}


/* ================================================
   LENGTH ICON - RULER
================================================ */

.ruler-shape {
    width: 67px;
    height: 27px;

    background: #ffffff;

    border-radius: 6px;

    transform: rotate(-42deg);

    position: relative;

    box-shadow:
        0 7px 12px rgba(0,0,0,0.18);

    background-image:
        repeating-linear-gradient(
            90deg,
            transparent 0px,
            transparent 7px,
            #647bdb 7px,
            #647bdb 9px,
            transparent 9px,
            transparent 13px
        );

    background-size: 100% 12px;

    background-repeat: no-repeat;

    background-position: top;
}


/* ================================================
   WEIGHT ICON - SCALE
================================================ */

.scale-shape {
    width: 65px;
    height: 65px;

    position: relative;
}

.scale-base {
    position: absolute;

    bottom: 4px;
    left: 5px;

    width: 55px;
    height: 12px;

    background: white;

    border-radius: 5px;
}

.scale-neck {
    position: absolute;

    top: 15px;
    left: 29px;

    width: 7px;
    height: 32px;

    background: white;

    border-radius: 4px;
}

.scale-top {
    position: absolute;

    top: 7px;
    left: 15px;

    width: 35px;
    height: 8px;

    background: white;

    border-radius: 5px;
}

.scale-pan {
    position: absolute;

    top: 25px;

    width: 20px;
    height: 12px;

    border: 3px solid white;

    border-top: none;

    border-radius: 0 0 12px 12px;
}

.scale-pan.left {
    left: 0;
}

.scale-pan.right {
    right: 0;
}


/* ================================================
   TEMPERATURE ICON - THERMOMETER
================================================ */

.thermometer-shape {
    width: 25px;
    height: 72px;

    border: 5px solid white;

    border-radius: 18px;

    position: relative;
}

.thermometer-shape::before {
    content: "";

    position: absolute;

    width: 18px;
    height: 18px;

    background: white;

    border-radius: 50%;

    bottom: -10px;
    left: -1px;
}

.thermometer-shape::after {
    content: "";

    position: absolute;

    width: 7px;
    height: 37px;

    background: white;

    border-radius: 5px;

    bottom: 5px;
    left: 4px;
}


/* ================================================
   VOLUME ICON - BEAKER
================================================ */

.beaker-shape {
    width: 57px;
    height: 66px;

    position: relative;

    border: 4px solid white;

    border-top: none;

    border-radius: 5px 5px 17px 17px;

    clip-path: polygon(
        15% 0,
        85% 0,
        85% 20%,
        100% 100%,
        0 100%,
        15% 20%
    );

    background: rgba(255,255,255,0.12);
}

.beaker-shape::after {
    content: "";

    position: absolute;

    bottom: 8px;
    left: 4px;

    width: 42px;
    height: 19px;

    background: rgba(255,255,255,0.65);

    border-radius: 3px 3px 12px 12px;
}


/* ================================================
   HERO TEXT
================================================ */

.hero-symbol {
    font-size: 32px;

    font-weight: 800;

    letter-spacing: 2px;

    color: white;
}

.hero-caption {
    font-size: 15px;

    margin-top: 10px;

    color: white;
}


/* ================================================
   HERO DECORATIONS
================================================ */

.hero-decoration {
    position: absolute;

    border-radius: 50%;

    background: rgba(255,255,255,0.13);
}

.decoration-one {
    width: 190px;
    height: 190px;

    top: -85px;
    right: -35px;
}

.decoration-two {
    width: 150px;
    height: 150px;

    bottom: -90px;
    left: -35px;
}


/* ================================================
   CATEGORY GRADIENTS
================================================ */

.hero-art.length {
    background: linear-gradient(
        120deg,
        #14b8f5,
        #3477fa,
        #6538ef
    );
}

.hero-art.weight {
    background: linear-gradient(
        120deg,
        #8b5cf6,
        #6366f1,
        #4338ca
    );
}

.hero-art.temperature {
    background: linear-gradient(
        120deg,
        #f97316,
        #ef4444,
        #a855f7
    );
}

.hero-art.volume {
    background: linear-gradient(
        120deg,
        #06b6d4,
        #0d9488,
        #2563eb
    );
}


/* ================================================
   FOOTER
================================================ */

.feature-icon {
    width: 54px;
    height: 54px;

    border-radius: 50%;

    background: #e4edff;

    color: #2563eb;

    display: flex;

    align-items: center;
    justify-content: center;

    font-size: 30px;
    font-weight: 900;
}

.feature-icon-simple {
    width: 64px !important;
    height: 64px !important;
    font-size: 39px !important;
    }

.feature-title {
    color: #101d50;

    font-size: 19px;

    font-weight: 800;
}

.feature-description {
    color: #647398;

    font-size: 13px;
}

hr {
    border-color: #cbd5f3 !important;
}

</style>
""", unsafe_allow_html=True)


# Apply dark-theme overrides when the header toggle is enabled.
if dark_mode:
    st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(ellipse at 100% 0%, rgba(99,102,241,0.16), transparent 35%),
                    linear-gradient(135deg, #0b1020, #111a32, #101827) !important;
        color: #edf2ff !important;
    }
    h1, h2, h3,
    .brand-title,
    .feature-title,
    .stApp p,
    .stApp label,
    .brand-subtitle,
    .feature-description {
        color: #edf2ff !important;
    }
    .brand-subtitle,
    .feature-description {
        color: #b7c3e3 !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(25, 36, 62, 0.96) !important;
        border: 1px solid #354568 !important;
        box-shadow: 0 10px 28px rgba(0,0,0,0.20) !important;
    }
    .st-key-main-workspace [data-testid="stHorizontalBlock"] > div:first-child {
        border-right-color: #354568 !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] h1,
    div[data-testid="stVerticalBlockBorderWrapper"] h2,
    div[data-testid="stVerticalBlockBorderWrapper"] h3 {
        color: #f2f5ff !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] p {
        color: #c1cbea !important;
    }
    .stSelectbox div[data-baseweb="select"] > div,
    .stNumberInput div[data-baseweb="input"],
    .stTextInput div[data-baseweb="input"] {
        background: #182541 !important;
        border: 1px solid #526487 !important;
    }
    .stSelectbox div[data-baseweb="select"] span,
    .stNumberInput input,
    .stTextInput input,
    [data-testid="stNumberInput"] input,
    [data-testid="stTextInput"] input {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        opacity: 1 !important;
        caret-color: #ffffff !important;
    }

    /* Make the entered number and its placeholder clearly distinguishable */
    [data-testid="stNumberInput"] input::placeholder,
    [data-testid="stTextInput"] input::placeholder {
        color: #aebbd6 !important;
        -webkit-text-fill-color: #aebbd6 !important;
        opacity: 1 !important;
    }
    .stSelectbox [data-testid="stWidgetLabel"] *,
    .stNumberInput [data-testid="stWidgetLabel"] *,
    [data-testid="stToggle"] label,
    [data-testid="stToggle"] p {
        color: #edf2ff !important;
    }
    [data-baseweb="popover"] *,
    [role="listbox"] *,
    [role="option"] {
        color: #172554 !important;
    }
    /* Conversion result / success message: force readable contrast */
    [data-testid="stAlert"],
    [data-testid="stAlert"] *,
    [data-baseweb="notification"],
    [data-baseweb="notification"] * {
        background-color: transparent;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        opacity: 1 !important;
    }

    [data-testid="stAlert"],
    [data-baseweb="notification"] {
        background: #173d35 !important;
        border: 1px solid #39866f !important;
        border-radius: 10px !important;
    }

    [data-testid="stAlert"] svg,
    [data-baseweb="notification"] svg {
        fill: #9df2ce !important;
        color: #9df2ce !important;
    }

    /* Ensure the number input's live value is visible against its field */
    [data-testid="stNumberInput"] input,
    [data-testid="stNumberInput"] input:focus {
        background: #182541 !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        opacity: 1 !important;
        caret-color: #ffffff !important;
    }
    .feature-icon {
        background: #26385f !important;
        color: #8eb4ff !important;
    }
    hr {
        border-color: #354568 !important;
    }
    [data-testid="stDivider"] {
        border-color: #354568 !important;
    }
    /* Keep the category label readable in dark mode */
    .st-key-category [data-testid="stWidgetLabel"],
    .st-key-category [data-testid="stWidgetLabel"] p,
    .st-key-category label,
    .st-key-category label p {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        font-weight: 800 !important;
    }
    </style>
    """, unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

header1, header2, header3 = st.columns(
    [0.65, 8.35, 1.0],
    vertical_alignment="center",
    gap="small"
)

with header1:

    st.markdown("""
    <div class="brand-icon">
        <div class="brand-ring"></div>
        <div class="brand-arrow-top">↗</div>
        <div class="brand-arrow-bottom">↙</div>
    </div>
    """, unsafe_allow_html=True)

with header2:

    st.markdown("""
    <div class="brand-title">
        Convert<span>IQ</span>
    </div>

    <div class="brand-subtitle">
        Your Everyday Unit Converter
    </div>
    """, unsafe_allow_html=True)

with header3:
    st.toggle("Dark mode", key="dark_mode")


st.divider()


# ==================================================
# CATEGORY SELECTION
# ==================================================

categories = [
    "Length",
    "Weight",
    "Temperature",
    "Volume"
]

category = st.selectbox(
    "Choose conversion category",
    categories,
    key="category"
)


# ==================================================
# CATEGORY INFORMATION
# ==================================================

hero_descriptions = {
    "Length": "Convert between kilometres, metres and more.",
    "Weight": "Convert between kilograms, grams and more.",
    "Temperature": "Convert between Celsius, Fahrenheit and Kelvin.",
    "Volume": "Convert between litres, millilitres and more."
}

hero_symbols = {
    "Length": "km  ↔  m",
    "Weight": "kg  ↔  g",
    "Temperature": "°C  ↔  °F",
    "Volume": "L  ↔  mL"
}

hero_icons = {
    "Length": '<div class="ruler-shape"></div>',

    "Weight": """
        <div class="scale-shape">
            <div class="scale-top"></div>
            <div class="scale-neck"></div>
            <div class="scale-pan left"></div>
            <div class="scale-pan right"></div>
            <div class="scale-base"></div>
        </div>
    """,

    "Temperature": '<div class="thermometer-shape"></div>',

    "Volume": '<div class="beaker-shape"></div>'
}


# ==================================================
# MAIN WORKSPACE - ONE SHARED RECTANGLE
# ==================================================

with st.container(
    border=True,
    key="main-workspace"
):

    left_col, right_col = st.columns(
        [1.1, 0.9],
        gap="large"
    )

    # ==================================================
    # LEFT SECTION - CONVERTER
    # ==================================================

    with left_col:

        st.subheader("Unit Converter")

        unit_options = {
            "Length": ["Kilometers", "Meters"],
            "Weight": ["Kilograms", "Grams"],
            "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
            "Volume": ["Litres", "Millilitres"],
        }

        units = unit_options[category]

        col1, col2 = st.columns(2)

        with col1:
            from_unit = st.selectbox(
                "From",
                units,
                key="from_unit"
            )

        with col2:
            to_unit = st.selectbox(
                "To",
                units,
                key="to_unit"
            )

        # Temperature can be negative; the other categories cannot.
        minimum_value = None if category == "Temperature" else 0.0

        value = st.number_input(
            "Enter Value",
            min_value=minimum_value,
            value=0.0,
            step=1.0,
            key="input_value"
        )

        if st.button(
            "↔  Convert",
            use_container_width=True
        ):
            try:
                st.session_state["conversion_result"] = {
                    "category": category,
                    "value": value,
                    "from_unit": from_unit,
                    "to_unit": to_unit,
                    "result": convert_units(
                        category,
                        value,
                        from_unit,
                        to_unit
                    ),
                    "error": None,
                }

            except ValueError as error:
                st.session_state["conversion_result"] = {
                    "category": category,
                    "value": value,
                    "from_unit": from_unit,
                    "to_unit": to_unit,
                    "result": None,
                    "error": str(error),
                }

        # Render the most recent result on every rerun, including theme changes.
        saved_result = st.session_state.get("conversion_result")

        if saved_result and saved_result["category"] == category:
            if saved_result["error"]:
                st.error(saved_result["error"])
            else:
                st.success(
                    f'{saved_result["value"]:g} {saved_result["from_unit"]} '
                    f'= {saved_result["result"]:,.4f} {saved_result["to_unit"]}'
                )


    # ==================================================
    # RIGHT SECTION - EXPLORE
    # ==================================================

    with right_col:

        st.subheader(
            f"Explore {category}"
        )

        st.write(
            hero_descriptions[category]
        )

        hero_html = f"""
        <div class="hero-art {category.lower()}">

            <div class="hero-decoration decoration-one"></div>

            <div class="hero-decoration decoration-two"></div>

            <div class="hero-content">

                <div class="unit-icon">
                    {hero_icons[category]}
                </div>

                <div class="hero-symbol">
                    {hero_symbols[category]}
                </div>

                <div class="hero-caption">
                    {category} Conversion
                </div>

            </div>

        </div>
        """

        st.html(hero_html)


# ==================================================
# FOOTER
# ==================================================

st.divider()

footer1, footer2, footer3 = st.columns(3)

features = [
    ("◎", "Simple", "Easy to use, for everyone."),
    ("➤", "Fast", "Instant conversion results."),
    ("▱", "Expandable", "More units coming soon.")
]

for col, feature in zip(
    [footer1, footer2, footer3],
    features
):

    icon, title, description = feature

    with col:

        icon_col, text_col = st.columns(
            [0.65, 3.35],
            vertical_alignment="center",
            gap="small"
        )

        with icon_col:

            st.markdown(
                f'<div class="feature-icon">{icon}</div>',
                unsafe_allow_html=True
            )

        with text_col:

            st.markdown(
                f'<div class="feature-title">{title}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="feature-description">{description}</div>',
                unsafe_allow_html=True
            )
