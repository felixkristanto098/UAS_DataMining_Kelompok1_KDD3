import streamlit as st

st.set_page_config(
    page_title="prediksi dehidrasi harian",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# STYLING (CSS KUSTOM)
# =====================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300&family=DM+Mono:wght@300;400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Mystery+Quest&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Londrina+Shadow&display=swap');


:root {
    --ocean: #0b4f7a;
    --ocean-dark: #072f4e;
    --ocean-light: #e4f4fc;
    --sky: #38a8d4;
    --sky-light: #eaf7fd;
    --aqua: #0e9e8e;
    --aqua-light: #e3f7f5;
    --text: #0d1f2d;
    --muted: #4a6577;
    --bg: #f5fbff;
    --border: rgba(11,79,122,0.10);
}


.stApp {
    background: var(--bg);
}


.hero, .eyebrow, .title, .desc, .pills, .pill, .divider,
.overview-grid, .overview-title, .overview-text, .stats, .card,
.card-label, .card-sub, .sidebar-title, .sidebar-sub, .team-title,
.member, .member-name, .member-id {
    font-family: 'Open Sans', sans-serif !important;
}


#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

.st-emotion-cache-12bp31y{
    color: var(--text) !important;
}
.stSidebar .st-emotion-cache-12bp31y{
    color: var(--ocean-light) !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}
header[data-testid="stHeader"] button {
    color: var(--text) !important;
}


.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 1150px !important;
}


section[data-testid="stSidebar"] {
    background: var(--ocean-dark) !important;
    border-right: none;
}

section[data-testid="stSidebar"] > div {
    padding: 2rem 1.5rem !important;
}

.sidebar-title, .sidebar-sub, .team-title, .member, .member-name, .member-id {
    color: white !important;
}

.sidebar-title {
    font-family: 'Londrina Shadow', sans-serif !important;
    font-size: 2.2rem;
    margin-bottom: 0;
}

.sidebar-sub {
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.6;
    margin-bottom: 2rem;
}

.team-title {
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.45;
    margin-bottom: 1rem;
}

.member {
    background: rgba(255,255,255,0.06);
    padding: 0.9rem;
    border-radius: 8px;
    margin-bottom: 0.7rem;
    border-left: 2px solid var(--sky);
}

.member-name { font-size: 0.9rem; }
.member-id { font-size: 0.7rem; opacity: 0.55; margin-top: 4px; }


.hero { margin-top: 1rem; }

.eyebrow {
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    color: var(--sky);
    margin-bottom: 1rem;
}

.title {
    font-family: 'Londrina Shadow', sans-serif !important;
    font-size: 5.5rem;
    line-height: 0.92;
    font-weight: 300;
    color: var(--text);
}

.title em {
    font-family: 'Londrina Shadow', sans-serif !important;
    color: var(--ocean);
    font-style: italic;
}

.desc {
    margin-top: 2rem;
    max-width: 520px;
    line-height: 2;
    font-size: 0.9rem;
    color: var(--muted);
}

.pills { display: flex; gap: 10px; margin-top: 2rem; flex-wrap: wrap; }
.pill {
    background: var(--ocean-light);
    color: var(--ocean) !important;
    padding: 8px 14px;
    border-radius: 5px;
    font-size: 0.75rem;
    border: 1px solid rgba(11,79,122,0.15);
}

.divider { width: 100%; height: 1px; background: var(--border); margin: 1.2rem 0; }


.overview-grid {
    display: grid;
    grid-template-columns: 180px 1fr;
    gap: 2rem;
    align-items: start;
}

.overview-title {
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #7fa8c0;
}

.overview-text { line-height: 2; color: var(--muted); font-size: 0.9rem; }


.stats { margin-top: 3rem; display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.card { padding: 1.6rem; border-radius: 10px; border: 1px solid var(--border); }
.card:nth-child(1) { background: var(--ocean-light); }
.card:nth-child(2) { background: var(--sky-light); }
.card:nth-child(3) { background: var(--aqua-light); }

.card-number {
    font-family: 'Londrina Shadow', sans-serif !important;
    font-size: 3.5rem;
    line-height: 1;
    margin-bottom: 0.5rem;
}
.card-label { font-size: 1rem; color: var(--text); }
.card-sub { font-size: 0.8rem; color: var(--muted); margin-top: 0.3rem; }


@media (max-width: 900px){
    .title { font-size: 3.8rem; }
    .overview-grid { grid-template-columns: 1fr; gap: 0.5rem; }
    .stats { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# KONTEN SIDEBAR
# =====================================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-title"></div>
    <div class="sidebar-sub">hydration prediction</div>

    <div class="team-title">Team</div>

    <div class="member">
        <div class="member-name">Abil Faroj Nur Yahya</div>
        <div class="member-id">24051214072</div>
    </div>

    <div class="member">
        <div class="member-name">Felix Kristanto</div>
        <div class="member-id">24051214098</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# KONTEN UTAMA
# =====================================================
st.markdown("""
<div class="hero">
    <div class="title">
        Prediksi Dehidrasi <br>
        <em>Menggunakan Machine Learning.</em>
    </div>
    <div class="desc">
            Sistem prediksi hidrasi berbasis machine learning yang membantu
            menganalisis status hidrasi dan kebutuhan konsumsi air harian
            berdasarkan karakteristik individu, tingkat aktivitas fisik,
            kondisi cuaca, serta pola konsumsi air.
            </div>
    <div class="pills">
            <div class="pill">XGBoost Classifier</div>
            <div class="pill">LightGBM Regressor</div>
            <div class="pill">SHAP Explainable AI</div>
    </div>
</div>

<div class="divider"></div>

<div class="overview-grid">
    <div class="overview-title">Project Overview</div>
            <div class="overview-text">
            Proyek ini mengimplementasikan dua pendekatan machine learning
            untuk mendukung analisis hidrasi harian. Skenario pertama menggunakan
            XGBoost Classifier untuk mengklasifikasikan status hidrasi pengguna
            menjadi Good atau Poor berdasarkan
            profil individu dan konsumsi air. Skenario kedua menggunakan
            LightGBM Regressor untuk memperkirakan kebutuhan konsumsi air harian
            ketika data konsumsi air belum tersedia. Hasil klasifikasi pada
            skenario pertama dijelaskan menggunakan metode SHAP (SHapley Additive
            exPlanations) sehingga faktor-faktor yang memengaruhi prediksi dapat
            dipahami secara transparan.
            </div>
</div>

<div class="stats">
    <div class="card">
        <div class="card-number" style="color:#0b4f7a;">6</div>
        <div class="card-label">Input Features</div>
        <div class="card-sub">age, weight, gender, activity, weather, water intake</div>
    </div>
    <div class="card">
        <div class="card-number" style="color:#38a8d4;">2</div>
        <div class="card-label">Prediction Models</div>
        <div class="card-sub">XGBoost Classification + LightGBM Regression</div>
    </div>
<div class="card">
        <div class="card-number" style="color:#0e9e8e;">CRISP-DM</div>
        <div class="card-label">Framework</div>
        <div class="card-sub">data mining</div>
    </div>
</div>
""", unsafe_allow_html=True)