import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import os
import pandas as pd

st.set_page_config(
    page_title="Dataset Overview - Hydration Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)


current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "..", "..", "dataset", "Daily_Water_Intake.csv")
df = pd.read_csv(csv_path)


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

html, body, [class*="css"] { font-family: 'Open Sans', sans-serif; }

.stApp { background: var(--bg); }
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header[data-testid="stAppHeader"] { display: none !important; }
header[data-testid="stHeader"]    { background: transparent !important; }
header[data-testid="stHeader"] button { color: var(--text) !important; }
.st-emotion-cache-12bp31y { color: var(--text) !important; }
[data-testid="collapsedControl"] { display: none !important; }

.block-container {
    padding-top: 3rem !important;
    padding-bottom: 0 !important;
    max-width: 1150px !important;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #023e6e 0%, #012a4a 100%) !important;
    border-right: none;
}
section[data-testid="stSidebar"] > div { padding: 2rem 1.5rem !important; }
.stSidebar .st-emotion-cache-12bp31y { color: var(--ocean-light) !important; }

.sidebar-title {
    font-family: 'Poppins', sans-serif;
    font-size: 2.2rem;
    color: white;
    margin-bottom: 0;
}
.sidebar-sub {
    font-family: 'Open Sans', sans-serif !important;
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.6;
    color: white;
    margin-bottom: 2rem;
}
.team-title {
    font-family: 'Open Sans', sans-serif !important;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.45;
    color: white;
    margin-bottom: 1rem;
}
.member {
    background: rgba(255,255,255,0.07);
    padding: 0.9rem;
    border-radius: 8px;
    margin-bottom: 0.7rem;
    border-left: 2px solid var(--sky);
}
.member-name {
    font-family: 'Open Sans', sans-serif !important;
    font-size: 0.9rem;
    color: white;
}
.member-id {
    font-family: 'Open Sans', sans-serif !important;
    font-size: 0.7rem;
    opacity: 0.55;
    color: white;
    margin-top: 4px;
}

.eyebrow {
    font-family: 'Open Sans', sans-serif !important;
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--ocean-mid);
    margin-bottom: 1rem;
}
.page-title {
    font-family: 'Poppins', sans-serif;
    font-size: 5.5rem;
    line-height: 0.92;
    font-weight: 300;
    color: var(--text);
    margin-bottom: 2.5rem;
}
.page-title em {
    font-family: 'Poppins', sans-serif;
    color: var(--ocean);
    font-style: italic;
}

.divider { width: 100%; height: 1px; background: var(--border); margin: 2rem 0; }

.section-label {
    font-family: 'Open Sans', sans-serif !important;
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

.info-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin-bottom: 2rem;
}
.info-cell {
    padding: 1.4rem 1.5rem 1.2rem;
    border-right: 1px solid var(--border);
}
.info-cell:last-child { border-right: none; }
.info-cell:nth-child(1) { background: var(--sky-light); }
.info-cell:nth-child(2) { background: var(--aqua-light); }
.info-cell:nth-child(3) { background: var(--ocean-light); }

.info-num {
    font-family: 'Poppins', sans-serif;
    font-size: 2.8rem;
    font-weight: 300;
    line-height: 1;
    margin-bottom: 5px;
}
.info-cell:nth-child(1) .info-num { color: var(--ocean); }
.info-cell:nth-child(2) .info-num { color: var(--aqua); }
.info-cell:nth-child(3) .info-num { color: var(--ocean-mid); }

.info-label {
    font-family: 'Open Sans', sans-serif !important;
    font-size: 0.78rem;
    color: var(--text);
}
.info-sub {
    font-family: 'Open Sans', sans-serif !important;
    font-size: 0.65rem;
    color: var(--muted);
    margin-top: 2px;
}

.stDataFrame, [data-testid="stDataFrame"] {
    border-radius: 10px !important;
    overflow: hidden !important;
    border: 1px solid var(--border) !important;
}

@media (max-width: 900px) {
    .page-title  { font-size: 3.8rem; }
    .info-strip  { grid-template-columns: 1fr; }
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


st.markdown("""
<div class="eyebrow">Dataset · Overview</div>
<div class="page-title">Hydration<br><em>Dataset.</em></div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-label">01 · Informasi Dataset</div>', unsafe_allow_html=True)

missing_total = int(df.isnull().sum().sum())
st.markdown(f"""
<div class="info-strip">
    <div class="info-cell">
        <div class="info-num">{df.shape[0]:,}</div>
        <div class="info-label">Records</div>
        <div class="info-sub">hydration observations</div>
    </div>
    <div class="info-cell">
        <div class="info-num">{df.shape[1]}</div>
        <div class="info-label">Features</div>
        <div class="info-sub">prediction variables</div>
    </div>
    <div class="info-cell">
        <div class="info-num">{missing_total}</div>
        <div class="info-label">Missing Values</div>
        <div class="info-sub">data quality check</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-label" style="margin-top:1.5rem;">Preview Data</div>',
            unsafe_allow_html=True)
st.dataframe(df.head(), use_container_width=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">02 · Statistik Dataset</div>', unsafe_allow_html=True)
st.dataframe(df.describe(), use_container_width=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">03 · Missing Value</div>', unsafe_allow_html=True)

missing_df = df.isnull().sum().reset_index()
missing_df.columns = ["Feature", "Missing Count"]
st.dataframe(missing_df, use_container_width=True, hide_index=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


st.markdown('<div class="section-label">04 · Visualisasi Data</div>', unsafe_allow_html=True)


def style_ax(ax, fig):
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f0fbff')
    ax.tick_params(colors='#2c7da0', labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor('#caf0f8')
    ax.yaxis.grid(True, color='#e0f7fc', linewidth=0.8)
    ax.set_axisbelow(True)

col1, col2 = st.columns(2, gap="large")


with col1:
    st.markdown(
        '<span style="font-family:DM Mono,monospace;font-size:0.78rem;color:#012a4a;">'
        ' Distribusi Hydration Level</span>',
        unsafe_allow_html=True
    )
    fig1, ax1 = plt.subplots(figsize=(5, 3.5))
    style_ax(ax1, fig1)
    counts = df['Hydration Level'].value_counts().sort_index()
    colors_hl = ["#0077b6" if c == "Good" else "#48cae4" for c in counts.index]
    bars = ax1.bar(counts.index, counts.values, color=colors_hl, width=0.5, edgecolor='none')
    for bar, val in zip(bars, counts.values):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + counts.values.max() * 0.02,
                 str(val), ha='center', va='bottom', fontsize=8,
                 color='#2c7da0', fontfamily='monospace')
    ax1.set_xlabel("Hydration Level", fontsize=8, color='#2c7da0', fontfamily='monospace')
    ax1.set_ylabel("Jumlah Data",     fontsize=8, color='#2c7da0', fontfamily='monospace')
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)


with col2:
    st.markdown(
        '<span style="font-family:DM Mono,monospace;font-size:0.78rem;color:#012a4a;">'
        ' Distribusi Daily Water Intake</span>',
        unsafe_allow_html=True
    )
    fig2, ax2 = plt.subplots(figsize=(5, 3.5))
    style_ax(ax2, fig2)
    ax2.hist(df['Daily Water Intake (liters)'], bins=25,
             color='#0096c7', edgecolor='none', alpha=0.85)
    ax2.set_xlabel("Daily Water Intake (liters)", fontsize=8,
                   color='#2c7da0', fontfamily='monospace')
    ax2.set_ylabel("Frekuensi", fontsize=8, color='#2c7da0', fontfamily='monospace')
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)


col3, col4 = st.columns(2, gap="large")

with col3:
    st.markdown(
        '<span style="font-family:DM Mono,monospace;font-size:0.78rem;color:#012a4a;">'
        ' Physical Activity Level</span>',
        unsafe_allow_html=True
    )
    fig3, ax3 = plt.subplots(figsize=(5, 3.5))
    style_ax(ax3, fig3)
    act_counts = df['Physical Activity Level'].value_counts()
    activity_colors = ['#023e6e', '#0077b6', '#48cae4']
    ax3.bar(act_counts.index, act_counts.values,
            color=activity_colors[:len(act_counts)], width=0.5, edgecolor='none')
    for i, (idx, val) in enumerate(act_counts.items()):
        ax3.text(i, val + act_counts.values.max() * 0.02, str(val),
                 ha='center', va='bottom', fontsize=8,
                 color='#2c7da0', fontfamily='monospace')
    ax3.set_xlabel("Activity Level", fontsize=8, color='#2c7da0', fontfamily='monospace')
    ax3.set_ylabel("Jumlah Data",    fontsize=8, color='#2c7da0', fontfamily='monospace')
    plt.tight_layout()
    st.pyplot(fig3)
    plt.close(fig3)

with col4:
    st.markdown(
        '<span style="font-family:DM Mono,monospace;font-size:0.78rem;color:#012a4a;">'
        ' Distribusi Weather</span>',
        unsafe_allow_html=True
    )
    fig4, ax4 = plt.subplots(figsize=(5, 3.5))
    style_ax(ax4, fig4)
    wx_counts = df['Weather'].value_counts()
    wx_colors = ['#00b4d8', '#0096c7', '#0077b6']
    ax4.bar(wx_counts.index, wx_counts.values,
            color=wx_colors[:len(wx_counts)], width=0.5, edgecolor='none')
    for i, (idx, val) in enumerate(wx_counts.items()):
        ax4.text(i, val + wx_counts.values.max() * 0.02, str(val),
                 ha='center', va='bottom', fontsize=8,
                 color='#2c7da0', fontfamily='monospace')
    ax4.set_xlabel("Weather",     fontsize=8, color='#2c7da0', fontfamily='monospace')
    ax4.set_ylabel("Jumlah Data", fontsize=8, color='#2c7da0', fontfamily='monospace')
    plt.tight_layout()
    st.pyplot(fig4)
    plt.close(fig4)


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<span style="font-family:DM Mono,monospace;font-size:0.78rem;color:#012a4a;">'
    ' Distribusi Intake per Hydration Level</span>',
    unsafe_allow_html=True
)
fig5, ax5 = plt.subplots(figsize=(10, 3.8))
style_ax(ax5, fig5)
for lbl, color in [('Good', '#0077b6'), ('Poor', '#48cae4')]:
    subset = df[df['Hydration Level'] == lbl]['Daily Water Intake (liters)']
    ax5.hist(subset, bins=30, alpha=0.65, label=lbl, color=color, edgecolor='none')
ax5.set_xlabel("Daily Water Intake (liters)", fontsize=8, color='#2c7da0', fontfamily='monospace')
ax5.set_ylabel("Frekuensi",                   fontsize=8, color='#2c7da0', fontfamily='monospace')
ax5.legend(fontsize=8)
plt.tight_layout()
st.pyplot(fig5)
plt.close(fig5)


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<span style="font-family:DM Mono,monospace;font-size:0.78rem;color:#012a4a;">'
    ' Boxplot Intake per Activity Level</span>',
    unsafe_allow_html=True
)
fig6, ax6 = plt.subplots(figsize=(10, 3.8))
style_ax(ax6, fig6)
order = ['Low', 'Moderate', 'High']
data_by_act = [df[df['Physical Activity Level'] == lvl]['Daily Water Intake (liters)'].dropna()
               for lvl in order]
bp = ax6.boxplot(data_by_act, labels=order, patch_artist=True,
                 medianprops=dict(color='white', linewidth=2),
                 whiskerprops=dict(color='#2c7da0'),
                 capprops=dict(color='#2c7da0'),
                 flierprops=dict(marker='o', color='#2c7da0', markersize=4, alpha=0.5))
box_colors = ['#023e6e', '#0077b6', '#48cae4']
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)
ax6.set_xlabel("Physical Activity Level",    fontsize=8, color='#2c7da0', fontfamily='monospace')
ax6.set_ylabel("Daily Water Intake (liters)", fontsize=8, color='#2c7da0', fontfamily='monospace')
plt.tight_layout()
st.pyplot(fig6)
plt.close(fig6)


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<span style="font-family:DM Mono,monospace;font-size:0.78rem;color:#012a4a;">'
    ' Correlation Heatmap (Fitur Numerik)</span>',
    unsafe_allow_html=True
)
fig7, ax7 = plt.subplots(figsize=(10, 4))
fig7.patch.set_facecolor('#ffffff')
cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
    "ocean_cmap", ["#023e6e", "#caf0f8", "#0096c7"]
)
sns.heatmap(
    df.corr(numeric_only=True),
    ax=ax7,
    cmap=cmap,
    annot=True,
    fmt=".2f",
    annot_kws={"size": 8, "color": "#012a4a"},
    linewidths=0.5,
    linecolor="#e0f7fc",
    cbar_kws={"shrink": 0.8}
)
ax7.tick_params(colors='#2c7da0', labelsize=8)
plt.tight_layout()
st.pyplot(fig7)
plt.close(fig7)