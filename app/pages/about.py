import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="About - Hydration Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)


current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(
    current_dir, "..", "..", "dataset", "Daily_Water_Intake.csv"
)

try:
    df = pd.read_csv(csv_path)
    jumlah_data = df.shape[0]
    jumlah_fitur = df.shape[1] - 1
    target_col = [c for c in df.columns if "hydration" in c.lower() or "status" in c.lower() or "dehydrat" in c.lower()]
    jumlah_kelas = df[target_col[0]].nunique() if target_col else "-"
except Exception:
    jumlah_data = 1500
    jumlah_fitur = 10
    jumlah_kelas = 3

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300&family=DM+Mono:wght@300;400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Mystery+Quest&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Londrina+Shadow&display=swap');

:root {
    --ocean:       #0077b6;
    --ocean-dark:  #023e6e;
    --ocean-mid:   #0096c7;
    --ocean-light: #caf0f8;
    --sky:         #48cae4;
    --sky-light:   #e0f7fc;
    --aqua:        #00b4d8;
    --aqua-light:  #d0f4f9;
    --foam:        #90e0ef;
    --text:        #012a4a;
    --muted:       #2c7da0;
    --bg:          #f0fbff;
    --border:      rgba(0,119,182,0.12);
}


.stApp { background: var(--bg); }

#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }

header[data-testid="stHeader"] { background: transparent !important; }
header[data-testid="stHeader"] button { color: var(--text) !important; }

.block-container {
    padding-top: 3rem !important;
    padding-bottom: 0 !important;
    max-width: 1150px !important;
}


.page-header, .eyebrow, .page-title, .divider, .section-label,
.method-cards, .method-card, .method-tag, .method-name, .method-body,
.info-table, .info-row, .info-key, .info-val, .dataset-stats, .ds-cell,
.ds-num, .ds-label, .ds-sub, .framework-block, .fw-step, .fw-num, .fw-name,
.fw-sub, .sidebar-title, .sidebar-sub, .team-title, .member, .member-name,
.member-id, .source-link {
    font-family: 'DM Mono', monospace !important;
}


section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #023e6e 0%, #012a4a 100%) !important;
    border-right: none;
}
section[data-testid="stSidebar"] > div { padding: 2rem 1.5rem !important; }

.sidebar-title, .sidebar-sub, .team-title, .member, .member-name, .member-id {
    color: white !important;
}

.sidebar-title {
    font-family: 'Poppins', sans-serif;
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
    background: rgba(255,255,255,0.07);
    padding: 0.9rem;
    border-radius: 8px;
    margin-bottom: 0.7rem;
    border-left: 2px solid var(--sky);
}
.member-name { font-size: 0.9rem; }
.member-id   { font-size: 0.7rem; opacity: 0.55; margin-top: 4px; }


.page-header { margin-top: 0.5rem; margin-bottom: 2.5rem; }

.eyebrow {
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    color: var(--ocean-mid);
    margin-bottom: 1rem;
    text-transform: uppercase;
}

.page-title {
    font-family: 'Poppins', sans-serif;
    font-size: 5.5rem;
    line-height: 0.92;
    font-weight: 300;
    color: var(--text);
}
.page-title em {
    font-family: 'Poppins', sans-serif;
    color: var(--ocean);
    font-style: italic;
}


.divider { width:100%; height:1px; background:var(--border); margin:2rem 0; }


.section-label {
    font-size: 0.65rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--aqua);
    margin-bottom: 1.25rem;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-label::before {
    content: '';
    display: inline-block;
    width: 16px;
    height: 1px;
    background: var(--ocean-mid);
    flex-shrink: 0;
}


.method-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 0.5rem;
}
.method-card {
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid var(--border);
}
.method-card:nth-child(1) { background: var(--sky-light); }
.method-card:nth-child(2) { background: var(--aqua-light); }

.method-tag {
    font-size: 0.6rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.method-card .method-tag { color: var(--ocean); }
.method-name {
    font-family: 'Poppins', sans-serif;
    font-size: 1.5rem;
    font-weight: 400;
    line-height: 1.2;
    margin-bottom: 0.75rem;
}
.method-card .method-name{ color: var(--ocean-dark); }

.method-body { font-size: 0.8rem; line-height: 1.85; color: var(--muted); }
.method-body strong { color: var(--text); font-weight: 400; }


.info-table {
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 1rem;
}
.info-row {
    display: grid;
    grid-template-columns: 140px 1fr;
}
.info-row + .info-row { border-top: 1px solid var(--border); }
.info-key {
    padding: 0.8rem 1rem;
    font-size: 0.65rem;
    letter-spacing: 0.08em;
    color: var(--muted);
    background: var(--ocean-light);
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
}
.info-val {
    padding: 0.8rem 1rem;
    font-size: 0.8rem;
    color: var(--text);
    background: #fff;
    display: flex;
    align-items: center;
    line-height: 1.6;
}


.dataset-stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin-top: 1rem;
}
.ds-cell {
    padding: 1.2rem 1.2rem 1rem;
    border-right: 1px solid var(--border);
}
.ds-cell:last-child { border-right: none; }
.ds-cell:nth-child(1) { background: var(--sky-light); }
.ds-cell:nth-child(2) { background: var(--aqua-light); }
.ds-cell:nth-child(3) { background: var(--ocean-light); }

.ds-num {
    font-family: 'Poppins', sans-serif;
    font-size: 2.4rem;
    font-weight: 300;
    line-height: 1;
    margin-bottom: 4px;
}
.ds-cell:nth-child(1) .ds-num { color: var(--ocean); }
.ds-cell:nth-child(2) .ds-num { color: var(--aqua); }
.ds-cell:nth-child(3) .ds-num { color: var(--ocean-mid); }
.ds-label { font-size: 0.72rem; color: var(--text); }
.ds-sub   { font-size: 0.65rem; color: var(--muted); margin-top: 2px; }


.framework-block {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}
.fw-step {
    padding: 1.2rem 1.2rem 1rem;
    border-radius: 10px;
    border: 1px solid var(--border);
    background: #fff;
}
.fw-num {
    font-family: 'Poppins', sans-serif;
    font-size: 2rem;
    font-weight: 300;
    color: var(--ocean-mid);
    line-height: 1;
    margin-bottom: 6px;
}
.fw-name { font-size: 0.8rem; color: var(--text); line-height: 1.5; }
.fw-sub  { font-size: 0.65rem; color: var(--muted); margin-top: 4px; }

.source-link {
    display: inline-block;
    font-size: 0.72rem;
    color: var(--ocean-mid) !important;
    border-bottom: 1px solid rgba(0,150,199,0.35);
    padding-bottom: 1px;
    margin-top: 0.75rem;
    text-decoration: none;
}


.wave-footer {
    position: relative;
    width: 100vw;
    left: 50%;
    transform: translateX(-50%);
    overflow: hidden;
    line-height: 0;
}

.wave-footer svg {
    display: block;
    width: 100%;
}

.st-emotion-cache-12bp31y{
    color: var(--text) !important;
}
.stSidebar .st-emotion-cache-12bp31y{
    color: var(--ocean-light) !important;
}

.wave-footer .wave-text {
    position: absolute;
    bottom: 22px;
    left: 50%;
    transform: translateX(-50%);
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.55);
    white-space: nowrap;
}

@media (max-width: 900px) {
    .page-title { font-size: 3.8rem; }
    .method-cards, .framework-block, .dataset-stats { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

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

st.markdown(f"""
<div class="page-header">
    <div class="eyebrow">About Project</div>
    <div class="page-title">
        Project<br>
        <em>Overview.</em>
    </div>
</div>

<div class="divider"></div>

<div class="section-label">01 · Prediction Models</div>

<div class="method-cards">
    <div class="method-card">
        <div class="method-tag">Scenario 1</div>
        <div class="method-name">XGBoost Classification</div>
        <div class="method-body">
            Mengklasifikasikan status hidrasi pengguna menjadi
            <strong>Good Hydration</strong> atau
            <strong>Poor Hydration</strong>
            berdasarkan usia, berat badan, gender,
            tingkat aktivitas fisik, kondisi cuaca,
            dan konsumsi air harian.
        </div>
    </div>
    <div class="method-card">
        <div class="method-tag">Scenario 2</div>
        <div class="method-name">LightGBM Regression</div>
        <div class="method-body">
            Memperkirakan kebutuhan konsumsi air harian
            berdasarkan karakteristik individu,
            aktivitas fisik, dan kondisi cuaca
            ketika data konsumsi air aktual belum tersedia.
        </div>
    </div>
    
</div>
<div class="divider"></div>

<div class="section-label">02 · Explainable AI</div>

<div class="method-card" style="background:var(--ocean-light);">
    <div class="method-tag">Interpretability</div>
    <div class="method-name">
        SHAP (SHapley Additive Explanations)
    </div>
    <div class="method-body">
        SHAP digunakan untuk menjelaskan kontribusi setiap fitur
        terhadap hasil prediksi model XGBoost.
        Pendekatan ini memungkinkan pengguna memahami faktor-faktor
        yang mendukung atau mengurangi kemungkinan terjadinya
        kondisi hidrasi yang baik.
    </div>
</div>

<div class="divider"></div>

<div class="section-label">03 · Dataset</div>
<div class="info-table">
    <div class="info-row">
        <div class="info-key">Dataset</div>
        <div class="info-val">Daily Water Intake & Hydration Patterns Dataset</div>
    </div>
    <div class="info-row">
        <div class="info-key">Sumber</div>
        <div class="info-val">Kaggle — sonalshinde123/daily-water-intake-and-hydration-patterns-dataset</div>
    </div>
</div>

<div class="dataset-stats">
    <div class="ds-cell">
        <div class="ds-num">{jumlah_data}</div>
        <div class="ds-label">Jumlah Data</div>
        <div class="ds-sub">total rows</div>
    </div>
    <div class="ds-cell">
        <div class="ds-num">{jumlah_fitur}</div>
        <div class="ds-label">Jumlah Fitur</div>
        <div class="ds-sub">prediction variables</div>
    </div>
    <div class="ds-cell">
        <div class="ds-num">{jumlah_kelas}</div>
        <div class="ds-label">Kelas</div>
        <div class="ds-sub">hydration status labels</div>
    </div>
</div>

<a class="source-link"
   href="https://www.kaggle.com/datasets/sonalshinde123/daily-water-intake-and-hydration-patterns-dataset"
   target="_blank">
    ↗ Lihat dataset di Kaggle
</a>

<div class="divider"></div>

<div class="section-label">04 · Framework</div>
<div class="framework-block">
    <div class="fw-step">
        <div class="fw-num">01</div>
        <div class="fw-name">Business Understanding</div>
        <div class="fw-sub">Memahami tujuan proyek</div>
    </div>
    <div class="fw-step">
        <div class="fw-num">02</div>
        <div class="fw-name">Data Understanding</div>
        <div class="fw-sub">Eksplorasi & analisis data</div>
    </div>
    <div class="fw-step">
        <div class="fw-num">03</div>
        <div class="fw-name">Data Preparation</div>
        <div class="fw-sub">Pembersihan & transformasi</div>
    </div>
    <div class="fw-step">
        <div class="fw-num">04</div>
        <div class="fw-name">Modeling</div>
        <div class="fw-sub">
        XGBoost Classification + LightGBM Regression
        </div>
    </div>
    <div class="fw-step">
        <div class="fw-num">05</div>
        <div class="fw-name">Evaluation</div>
        <div class="fw-sub">Pengukuran performa model</div>
    </div>
    <div class="fw-step">
        <div class="fw-num">06</div>
        <div class="fw-name">Deployment</div>
        <div class="fw-sub">Streamlit web application</div>
    </div>
</div>
""", unsafe_allow_html=True)