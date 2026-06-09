import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import os
import shap

st.set_page_config(
    page_title="Prediction - Hydration",
    layout="wide",
    initial_sidebar_state="expanded"
)

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir   = os.path.join(current_dir, "..", "..", "model")

try:
    pre_s1        = joblib.load(os.path.join(model_dir, "preprocessor_s1.pkl"))
    pre_s2        = joblib.load(os.path.join(model_dir, "preprocessor_s2.pkl"))
    classifier_s1 = joblib.load(os.path.join(model_dir, "classifier_s1.pkl"))
    regressor_s2  = joblib.load(os.path.join(model_dir, "regressor_s2.pkl"))
    models_loaded = True
except Exception as e:
    models_loaded = False
    load_error    = str(e)

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
    --text:        #012a4a;
    --muted:       #2c7da0;
    --bg:          #f0fbff;
    --border:      rgba(0,119,182,0.12);
}

.stMainBlockContainer p {color: var(--text);}
.st-emotion-cache-1lads1q p {color: var(--sky-light) !important;}

.stApp { background: var(--bg); }
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent !important; }
.block-container { padding-top: 3rem !important; padding-bottom: 0 !important; max-width: 1150px !important; }

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #023e6e 0%, #012a4a 100%) !important;
    border-right: none;
}
section[data-testid="stSidebar"] > div { padding: 2rem 1.5rem !important; }
.sidebar-title { font-family: 'Poppins', sans-serif; font-size: 2.2rem; color: white; margin-bottom: 0; }
.sidebar-sub   { font-family: 'Open Sans', sans-serif !important; font-size: 0.7rem; letter-spacing: 0.18em; text-transform: uppercase; opacity: 0.6; color: white; margin-bottom: 2rem; }
.team-title    { font-family: 'Open Sans', sans-serif !important; font-size: 0.65rem; letter-spacing: 0.18em; text-transform: uppercase; opacity: 0.45; color: white; margin-bottom: 1rem; }
.member        { background: rgba(255,255,255,0.07); padding: 0.9rem; border-radius: 8px; margin-bottom: 0.7rem; border-left: 2px solid var(--sky); }
.member-name   { font-family: 'Open Sans', sans-serif !important; font-size: 0.9rem; color: white; }
.member-id     { font-family: 'Open Sans', sans-serif !important; font-size: 0.7rem; opacity: 0.55; color: white; margin-top: 4px; }

.eyebrow    { font-family: 'Open Sans', sans-serif !important; font-size: 0.7rem; letter-spacing: 0.25em; text-transform: uppercase; color: var(--ocean-mid); margin-bottom: 1rem; }
.page-title { font-family: 'Poppins', sans-serif; font-size: 5.5rem; line-height: 0.92; font-weight: 300; color: var(--text); margin-bottom: 2rem; }
.page-title em { font-family: 'Poppins', sans-serif; color: var(--ocean); font-style: italic; }
.divider    { width:100%; height:1px; background:var(--border); margin:2rem 0; }
.section-label {
    font-family: 'Open Sans', sans-serif !important; font-size: 0.65rem; letter-spacing: 0.22em;
    text-transform: uppercase; color: var(--aqua); margin-bottom: 1.25rem;
    display: flex; align-items: center; gap: 10px;
}
.section-label::before { content:''; display:inline-block; width:16px; height:1px; background:var(--ocean-mid); flex-shrink:0; }

.scenario-badge { display:inline-flex; align-items:center; gap:8px; padding:6px 14px; border-radius:20px; font-family:'Roboto',monospace !important; font-size:0.72rem; letter-spacing:0.08em; margin-bottom:1.5rem; }
.scenario-badge.s1 { background:var(--sky-light);  color:var(--ocean);     border:1px solid rgba(0,150,199,0.2); }
.scenario-badge.s2 { background:var(--aqua-light); color:var(--ocean-mid); border:1px solid rgba(0,180,216,0.2); }
.st-emotion-cache-12bp31y{
    color: var(--text) !important;
}
.stSidebar .st-emotion-cache-12bp31y{
    color: var(--ocean-light) !important;
}
.slider-group-label { font-family:'Roboto',monospace !important; font-size:0.6rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--text) !important; margin-bottom:1rem; padding-bottom:0.5rem; border-bottom:1px solid var(--border); }
div[data-testid="stSlider"] label p { font-family:'Roboto',monospace !important; font-size:0.78rem !important; color:var(--text) !important; }

.stButton > button { width:100%; background:linear-gradient(135deg,var(--ocean-dark),var(--ocean)) !important; color:white !important; border:none !important; border-radius:8px !important; padding:0.85rem 1rem !important; font-family:'Roboto',monospace !important; font-size:0.8rem !important; letter-spacing:0.1em !important; text-transform:uppercase !important; transition:opacity 0.2s !important; margin-top:0.5rem !important; }
.stButton > button:hover { opacity:0.85 !important; }

.result-card  { padding:1.6rem 1.4rem 1.4rem; border-radius:12px; border:1px solid var(--border); margin-bottom:1rem; }
.result-card.hydrated { background:var(--sky-light);   border-color:rgba(72,202,228,0.25); }
.result-card.poor     { background:#fff0e8;             border-color:rgba(220,100,50,0.18); }
.result-card.reg      { background:var(--aqua-light);  border-color:rgba(0,180,216,0.2);  }
.result-card.info     { background:var(--ocean-light); border-color:rgba(0,119,182,0.15); }
.result-tag   { font-family:'Roboto',monospace !important; font-size:0.58rem; letter-spacing:0.16em; text-transform:uppercase; margin-bottom:0.5rem; }
.hydrated .result-tag { color:var(--ocean); }
.poor .result-tag     { color:#c0552a; }
.reg .result-tag      { color:var(--aqua); }
.info .result-tag     { color:var(--ocean-mid); }
.result-value { font-family:'Cormorant Garamond',serif !important; font-size:2.4rem; font-weight:300; line-height:1.1; margin-bottom:6px; }
.hydrated .result-value { color:var(--ocean); }
.poor .result-value     { color:#c0552a; }
.reg .result-value      { color:var(--aqua); }
.info .result-value     { color:var(--ocean-mid); }
.result-sub { font-family:'Roboto',monospace !important; font-size:0.72rem; color:var(--muted); }

.prob-wrap { margin-bottom:0.6rem; }
.prob-label-row { display:flex; justify-content:space-between; font-size:0.68rem; color:var(--muted); margin-bottom:4px; font-family:'Roboto',monospace; }
.prob-bar-bg   { background:var(--ocean-light); border-radius:4px; height:8px; overflow:hidden; }
.prob-bar-fill { height:100%; border-radius:4px; transition:width 0.4s ease; }

.input-table { border:1px solid var(--border); border-radius:10px; overflow:hidden; }
.input-row   { display:grid; grid-template-columns:1fr 1fr; }
.input-row + .input-row { border-top:1px solid var(--border); }
.input-key   { padding:0.55rem 1rem; font-size:0.65rem; letter-spacing:0.05em; color:var(--muted); background:var(--ocean-light); border-right:1px solid var(--border); font-family:'Roboto',monospace; }
.input-val   { padding:0.55rem 1rem; font-size:0.72rem; color:var(--text); background:#fff; font-family:'Roboto',monospace; }

.shap-info { background:var(--sky-light); border:1px solid rgba(0,150,199,0.2); border-radius:8px; padding:0.9rem 1.1rem; font-family:'Roboto',monospace !important; font-size:0.72rem; color:var(--ocean-dark); margin-bottom:1.2rem; line-height:1.6; }
.shap-note { background:var(--ocean-light); border:1px solid rgba(0,119,182,0.15); border-radius:8px; padding:0.8rem 1rem; font-family:'Roboto',monospace !important; font-size:0.68rem; color:var(--muted); margin-top:1rem; line-height:1.6; }
.shap-badge { display:inline-block; padding:3px 10px; border-radius:4px; font-family:'Roboto',monospace !important; font-size:0.62rem; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.8rem; }
.shap-badge.s1 { background:var(--sky-light); color:var(--ocean); border:1px solid rgba(0,119,182,0.2); }

.reg-info-box { background:var(--aqua-light); border:1px solid rgba(0,180,216,0.25); border-radius:10px; padding:1rem 1.2rem; font-family:'Roboto',monospace !important; font-size:0.75rem; color:var(--ocean-dark); margin-bottom:1.5rem; line-height:1.8; }

.wave-footer { position:relative; width:100vw; left:50%; transform:translateX(-50%); overflow:hidden; line-height:0; margin-top:3rem; }
.wave-footer svg { display:block; width:100%; }
.wave-footer .wave-layer-1 { animation:wave-move 7s ease-in-out infinite alternate; }
.wave-footer .wave-layer-2 { animation:wave-move 5s ease-in-out infinite alternate-reverse; }
.wave-footer .wave-layer-3 { animation:wave-move 9s ease-in-out infinite alternate; }
@keyframes wave-move { 0%{transform:translateX(0);} 100%{transform:translateX(-3%);} }
.wave-footer .wave-text { position:absolute; bottom:22px; left:50%; transform:translateX(-50%); font-family:'Roboto',monospace; font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:rgba(255,255,255,0.55); white-space:nowrap; }

div[data-testid="stRadio"] label { font-family:'Roboto',monospace !important; font-size:0.8rem !important; color:var(--text) !important; }
@media (max-width:900px) { .page-title{font-size:3.8rem;} }
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

st.markdown("""
<div class="eyebrow">Prediction · Analysis</div>
<div class="page-title">Hydration<br><em>Analysis.</em></div>
""", unsafe_allow_html=True)



def get_feature_names(preprocessor):
    try:
        raw = preprocessor.get_feature_names_out()
        return [n.split("__", 1)[-1] for n in raw]
    except Exception:
        pass
    names = []
    for name, trans, cols in preprocessor.transformers_:
        if name == "remainder":
            continue
        if hasattr(trans, "get_feature_names_out"):
            try:
                sub = trans.get_feature_names_out(cols if isinstance(cols, list) else list(cols))
                names.extend([s.split("__", 1)[-1] for s in sub])
                continue
            except Exception:
                pass
        names.extend(cols if isinstance(cols, list) else list(cols))
    return names


def compute_shap_classifier(preprocessor, classifier, X_input_df):
    X_tr = preprocessor.transform(X_input_df)
    feat  = get_feature_names(preprocessor)
    if hasattr(X_tr, "toarray"):
        X_tr = X_tr.toarray()
    X_tr = np.array(X_tr, dtype=np.float64)
    if X_tr.ndim == 1:
        X_tr = X_tr.reshape(1, -1)

    explainer = shap.TreeExplainer(classifier)
    shap_out  = explainer.shap_values(X_tr)
    sv        = np.array(shap_out)

    if sv.ndim == 3:
        sv = sv[0, :, 1] if sv.shape[2] > 1 else sv[0, :, 0]
    elif isinstance(shap_out, list):
        arr = np.array(shap_out[1] if len(shap_out) > 1 else shap_out[0])
        sv  = arr[0] if arr.ndim == 2 else arr
    else:
        sv = sv[0]

    exp_val = explainer.expected_value
    if isinstance(exp_val, (list, np.ndarray)):
        ev_arr  = np.array(exp_val).ravel()
        exp_val = float(ev_arr[1] if len(ev_arr) > 1 else ev_arr[0])
    else:
        exp_val = float(exp_val)

    sv = sv.reshape(-1)
    n  = min(len(sv), len(feat))

    df = pd.DataFrame({
        "Feature": feat[:n],
        "SHAP Value": sv[:n]
    })


    def collapse_feature(name):

        # Weather
        if "Weather" in name:
            return "Weather"

        if "Gender" in name:
            return "Gender"

        if "Physical Activity Level" in name:
            return "Physical Activity Level"

        if "Daily Water Intake" in name:
            return "Daily Water Intake"

        return name

    df["Feature"] = df["Feature"].apply(collapse_feature)

    
    df = (
        df.groupby("Feature", as_index=False)
        ["SHAP Value"]
        .sum()
    )

    df["Abs"] = df["SHAP Value"].abs()

    df = (
        df.sort_values("Abs", ascending=True)
        .reset_index(drop=True)
    )

    return df, exp_val


def render_shap_classifier(shap_df, expected_value):

    fig, ax = plt.subplots(figsize=(8, max(4, len(shap_df) * 0.5)))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f0fbff')
    colors_s = ["#0077b6" if x > 0 else "#c0552a" for x in shap_df["SHAP Value"]]
    bars = ax.barh(shap_df["Feature"], shap_df["SHAP Value"],
                   color=colors_s, edgecolor='none', height=0.55)
    for bar, val in zip(bars, shap_df["SHAP Value"]):
        xpos   = bar.get_width()
        ha     = "left" if xpos >= 0 else "right"
        offset = 0.002 if xpos >= 0 else -0.002
        ax.text(xpos + offset, bar.get_y() + bar.get_height() / 2,
                f"{val:+.4f}", va='center', ha=ha,
                fontsize=7.5, color='#012a4a', fontfamily='monospace')
    ax.axvline(0, color='#90e0ef', linewidth=1.5)
    ax.set_xlabel("SHAP Impact (log-odds)  (→ Good  |  ← Poor)",
                  fontsize=8, color='#2c7da0', fontfamily='monospace')
    ax.set_title(f"Baseline E[f(x)] = {expected_value:.4f}",
                 fontsize=8, color='#2c7da0', fontfamily='monospace', pad=8)
    ax.tick_params(colors='#2c7da0', labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor('#caf0f8')
    ax.xaxis.grid(True, color='#e0f7fc', linewidth=0.7)
    ax.set_axisbelow(True)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    pos_df = shap_df[shap_df["SHAP Value"] > 0].sort_values("SHAP Value", ascending=False)
    neg_df = shap_df[shap_df["SHAP Value"] < 0].sort_values("SHAP Value")
    col_p, col_n = st.columns(2, gap="large")
    with col_p:
        st.markdown('<div class="section-label"> Mendukung Good (Terhidrasi)</div>', unsafe_allow_html=True)
        if len(pos_df):
            rows = "".join(
                f'<div class="input-row">'
                f'<div class="input-key"> {r["Feature"]}</div>'
                f'<div class="input-val" style="color:#0077b6;font-weight:500;">+{r["SHAP Value"]:.4f}</div>'
                f'</div>' for _, r in pos_df.iterrows()
            )
            st.markdown(f'<div class="input-table">{rows}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<span style="font-size:0.75rem;color:var(--muted);">Tidak ada kontribusi positif</span>',
                        unsafe_allow_html=True)
    with col_n:
        st.markdown('<div class="section-label"> Mendukung Poor (Dehidrasi)</div>', unsafe_allow_html=True)
        if len(neg_df):
            rows = "".join(
                f'<div class="input-row">'
                f'<div class="input-key"> {r["Feature"]}</div>'
                f'<div class="input-val" style="color:#c0552a;font-weight:500;">{r["SHAP Value"]:.4f}</div>'
                f'</div>' for _, r in neg_df.iterrows()
            )
            st.markdown(f'<div class="input-table">{rows}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<span style="font-size:0.75rem;color:var(--muted);">Tidak ada kontribusi negatif</span>',
                        unsafe_allow_html=True)


st.markdown('<div class="section-label">01 · Pilih Skenario</div>', unsafe_allow_html=True)

scenario   = st.radio("", ["Dengan Input Water Intake",
                            "Tanpa Input Water Intake"],
                       horizontal=True, label_visibility="collapsed")
use_intake = "Skenario 1" in scenario

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">02 · Input Data Individu</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown('<div class="slider-group-label">Profil Fisik</div>', unsafe_allow_html=True)
    age    = st.slider("Age (tahun)",  10,   80,   25)
    weight = st.slider("Weight (kg)", 30.0, 150.0, 65.0, step=0.5)
    gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
with col2:
    st.markdown('<div class="slider-group-label">Aktivitas & Lingkungan</div>', unsafe_allow_html=True)
    activity = st.selectbox("Physical Activity Level", ["Low", "Moderate", "High"])
    weather  = st.selectbox("Weather Condition",       ["Cold", "Normal", "Hot"])
    if use_intake:
        st.markdown('<div class="slider-group-label" style="margin-top:1rem;">Konsumsi Air</div>',
                    unsafe_allow_html=True)
        water_intake = st.slider("Daily Water Intake (liter)", 0.5, 6.0, 2.0, step=0.1)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
predict_btn = st.button("Analyze Hydration Status")

if predict_btn:

    if not models_loaded:
        st.error(f"Model gagal dimuat: {load_error}")
        st.stop()

    base_data = {
        "Age":                     age,
        "Weight (kg)":             weight,
        "Gender":                  gender,
        "Physical Activity Level": activity,
        "Weather":                 weather,
    }

    if use_intake:
        df_cls = pd.DataFrame([{**base_data, "Daily Water Intake (liters)": water_intake}])
        df_cls = df_cls[["Age", "Weight (kg)", "Daily Water Intake (liters)",
                          "Gender", "Physical Activity Level", "Weather"]]

        X_tr      = pre_s1.transform(df_cls)
        pred_y    = classifier_s1.predict(X_tr)[0]
        prob      = classifier_s1.predict_proba(X_tr)[0]
        classes   = classifier_s1.classes_

        is_good       = int(pred_y) == 1
        display_label = "Good"     if is_good else "Poor"
        quality_icon  = ""       if is_good else ""
        card_class    = "hydrated" if is_good else "poor"
        idx_good      = list(classes).index(1) if 1 in classes else 1
        prob_good     = float(prob[idx_good])
        prob_poor     = 1.0 - prob_good

        st.markdown('<div class="section-label">03 · Hasil Prediksi</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="result-card {card_class}">
            <div class="result-tag">Hydration Status · Skenario 1 · XGBoost Classifier</div>
            <div class="result-value">{quality_icon} {display_label}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-label">04 · Probabilitas Klasifikasi</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="prob-wrap">
            <div class="prob-label-row"><span> Good (Terhidrasi)</span><span>{prob_good:.1%}</span></div>
            <div class="prob-bar-bg"><div class="prob-bar-fill" style="width:{prob_good*100:.1f}%; background:var(--ocean);"></div></div>
        </div>
        <div class="prob-wrap">
            <div class="prob-label-row"><span>⚠️ Poor (Dehidrasi)</span><span>{prob_poor:.1%}</span></div>
            <div class="prob-bar-bg"><div class="prob-bar-fill" style="width:{prob_poor*100:.1f}%; background:#c0552a;"></div></div>
        </div>
        """, unsafe_allow_html=True)

        fig, ax = plt.subplots(figsize=(6, 3))
        fig.patch.set_facecolor('#ffffff')
        ax.set_facecolor('#f0fbff')
        ax.bar(["Good", "Poor"], [prob_good, prob_poor],
               color=["#0077b6", "#c0552a"], width=0.4, edgecolor='none')
        ax.set_ylim(0, 1.15)
        for i, v in enumerate([prob_good, prob_poor]):
            ax.text(i, v + 0.04, f"{v:.2f}", ha='center', fontsize=9,
                    color='#2c7da0', fontfamily='monospace')
        ax.tick_params(colors='#2c7da0', labelsize=8)
        for spine in ax.spines.values(): spine.set_edgecolor('#caf0f8')
        ax.yaxis.grid(True, color='#caf0f8', linewidth=0.8)
        ax.set_axisbelow(True)
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        st.markdown('<div class="section-label">05 · SHAP — Explainable AI</div>', unsafe_allow_html=True)
        try:
            shap_df, exp_val = compute_shap_classifier(pre_s1, classifier_s1, df_cls)
            render_shap_classifier(shap_df, exp_val)
        except Exception as e:
            st.markdown(
                f'<div style="font-family:Roboto,monospace;font-size:0.75rem;color:#c0552a;'
                f'background:#fff0e8;padding:1rem;border-radius:8px;border:1px solid rgba(192,85,42,0.2);">'
                f'⚠️ SHAP tidak dapat dijalankan: {e}</div>',
                unsafe_allow_html=True
            )

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        st.markdown('<div class="section-label">06 · Input Data Summary</div>', unsafe_allow_html=True)
        summary = {
            "Age":                     f"{age} tahun",
            "Gender":                  gender,
            "Weight":                  f"{weight} kg",
            "Physical Activity Level": activity,
            "Weather":                 weather,
            "Daily Water Intake":      f"{water_intake:.1f} L",
            "Skenario":                "Klasifikasi",
            "Algoritma":               "XGBoost",
            "Prediksi":                f"{quality_icon} {display_label}",
            "Prob. Good":              f"{prob_good:.1%}",
            "Prob. Poor":              f"{prob_poor:.1%}",
        }


    else:
        df_reg = pd.DataFrame([base_data])
        df_reg = df_reg[["Age", "Weight (kg)", "Gender", "Physical Activity Level", "Weather"]]

        X_tr        = pre_s2.transform(df_reg)
        pred_intake = float(regressor_s2.predict(X_tr)[0])

        st.markdown('<div class="section-label">03 · Hasil Prediksi</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="result-card reg">
            <div class="result-tag">Estimasi Kebutuhan Air · Skenario 2 · LightGBM Regressor</div>
            <div class="result-value"> {pred_intake:.2f} L</div>
            <div class="result-sub">prediksi daily water intake yang direkomendasikan per hari</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        st.markdown('<div class="section-label">04 · Input Data Summary</div>', unsafe_allow_html=True)
        summary = {
            "Age":                     f"{age} tahun",
            "Gender":                  gender,
            "Weight":                  f"{weight} kg",
            "Physical Activity Level": activity,
            "Weather":                 weather,
            "Daily Water Intake":      "(tidak diinput)",
            "Skenario":                "Regresi",
            "Algoritma":               "LightGBM",
            "Estimasi Kebutuhan Air":  f"{pred_intake:.2f} L / hari",
        }

    rows_html = "".join(
        f'<div class="input-row">'
        f'<div class="input-key">{k}</div>'
        f'<div class="input-val">{v}</div>'
        f'</div>'
        for k, v in summary.items()
    )
    st.markdown(f'<div class="input-table">{rows_html}</div>', unsafe_allow_html=True)

