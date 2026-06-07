import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="Visualization - Hydration Prediction",
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
    font-family: 'Londrina Shadow', sans-serif !important;
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
    font-family: 'Londrina Shadow', sans-serif !important;
    font-size: 5.5rem;
    line-height: 0.92;
    font-weight: 300;
    color: var(--text);
    margin-bottom: 2.5rem;
}
.page-title em {
    font-family: 'Londrina Shadow', sans-serif !important;
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

.chart-desc {
    font-family: 'Open Sans', sans-serif !important;
    font-size: 0.75rem;
    color: var(--muted);
    line-height: 1.8;
    max-width: 680px;
    margin-bottom: 1.25rem;
}

.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid var(--border) !important;
    gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Open Sans', sans-serif !important;
    font-size: 0.68rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
    padding: 0.6rem 1.25rem !important;
    background: transparent !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
}
.stTabs [aria-selected="true"] {
    color: var(--ocean) !important;
    border-bottom: 2px solid var(--ocean) !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab-panel"] {
    padding-top: 1.5rem !important;
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
<div class="eyebrow">Visualization · Analysis</div>
<div class="page-title">Data<br><em>Visualization.</em></div>
""", unsafe_allow_html=True)

def styled_fig(w=10, h=5):
    fig, ax = plt.subplots(figsize=(w, h))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f0fbff')
    ax.tick_params(colors='#2c7da0', labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor('#caf0f8')
    ax.yaxis.grid(True, color='#e0f7fc', linewidth=0.7, linestyle='--')
    ax.set_axisbelow(True)
    return fig, ax

cmap_ocean = matplotlib.colors.LinearSegmentedColormap.from_list(
    "ocean_cmap", ["#023e6e", "#caf0f8", "#0096c7"]
)

OCEAN_PALETTE = ["#023e6e", "#0077b6", "#0096c7", "#00b4d8", "#48cae4", "#90e0ef", "#caf0f8"]


tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Heatmap",
    "Histogram",
    "Distribusi Label",
    "Boxplot",
    "Perbandingan Kategori",
])

with tab1:
    st.markdown('<div class="section-label">Correlation Heatmap</div>', unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f0fbff')
    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        fmt=".2f",
        cmap=cmap_ocean,
        ax=ax,
        annot_kws={"size": 9, "color": "#012a4a"},
        linewidths=0.5,
        linecolor="#e0f7fc",
        cbar_kws={"shrink": 0.8}
    )
    ax.tick_params(colors='#2c7da0', labelsize=8)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with tab2:
    st.markdown('<div class="section-label">Distribusi Fitur</div>', unsafe_allow_html=True)

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    cat_cols     = ['Gender', 'Physical Activity Level', 'Weather']
    all_cols     = numeric_cols + cat_cols
    default_idx  = all_cols.index('Daily Water Intake (liters)') \
                   if 'Daily Water Intake (liters)' in all_cols else 0
    selected_col = st.selectbox("Pilih fitur", all_cols, index=default_idx)

    if selected_col in numeric_cols:
        fig, ax = styled_fig(8, 4)
        sns.histplot(
            df[selected_col], kde=True, ax=ax,
            color='#0096c7', edgecolor='none', alpha=0.8,
            line_kws={"color": "#023e6e", "linewidth": 1.8}
        )
        ax.set_xlabel(selected_col, fontsize=9, color='#2c7da0', fontfamily='monospace')
        ax.set_ylabel("Frekuensi",  fontsize=9, color='#2c7da0', fontfamily='monospace')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)
    else:
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        for ax in axes:
            ax.set_facecolor('#f0fbff')
        fig.patch.set_facecolor('#ffffff')

        counts = df[selected_col].value_counts()
        colors_cat = OCEAN_PALETTE[:len(counts)]
        axes[0].bar(counts.index, counts.values, color=colors_cat, width=0.5, edgecolor='none')
        for i, (idx, val) in enumerate(counts.items()):
            axes[0].text(i, val + counts.values.max() * 0.02, str(val),
                         ha='center', fontsize=9, color='#2c7da0', fontfamily='monospace')
        axes[0].set_xlabel(selected_col, fontsize=9, color='#2c7da0', fontfamily='monospace')
        axes[0].set_ylabel("Jumlah Data", fontsize=9, color='#2c7da0', fontfamily='monospace')
        axes[0].set_title("Distribusi Total", fontsize=9, color='#2c7da0', fontfamily='monospace')
        axes[0].tick_params(colors='#2c7da0', labelsize=8)
        for spine in axes[0].spines.values(): spine.set_edgecolor('#caf0f8')
        axes[0].yaxis.grid(True, color='#e0f7fc', linewidth=0.7, linestyle='--')
        axes[0].set_axisbelow(True)

        ct = pd.crosstab(df[selected_col], df['Hydration Level'], normalize='index') * 100
        x  = range(len(ct))
        w  = 0.35
        if 'Good' in ct.columns:
            axes[1].bar([i - w/2 for i in x], ct['Good'], width=w,
                        color='#0077b6', edgecolor='none', label='Good')
        if 'Poor' in ct.columns:
            axes[1].bar([i + w/2 for i in x], ct['Poor'], width=w,
                        color='#48cae4', edgecolor='none', label='Poor')
        axes[1].set_xticks(list(x))
        axes[1].set_xticklabels(ct.index, fontsize=8, color='#2c7da0', fontfamily='monospace')
        axes[1].set_xlabel(selected_col, fontsize=9, color='#2c7da0', fontfamily='monospace')
        axes[1].set_ylabel("Persentase (%)", fontsize=9, color='#2c7da0', fontfamily='monospace')
        axes[1].set_title("% Good vs Poor per Kategori",
                          fontsize=9, color='#2c7da0', fontfamily='monospace')
        axes[1].tick_params(colors='#2c7da0', labelsize=8)
        for spine in axes[1].spines.values(): spine.set_edgecolor('#caf0f8')
        axes[1].yaxis.grid(True, color='#e0f7fc', linewidth=0.7, linestyle='--')
        axes[1].set_axisbelow(True)
        axes[1].legend(fontsize=8, framealpha=0.4)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

with tab3:
    st.markdown('<div class="section-label">Distribusi Hydration Level</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="chart-desc">
        Sebaran label target <strong>Hydration Level</strong> (Good / Poor)
        yang digunakan pada model klasifikasi. Termasuk proporsi per kelas.
    </p>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        counts = df['Hydration Level'].value_counts().sort_index()
        bar_colors = [('#0077b6' if lbl == 'Good' else '#48cae4') for lbl in counts.index]
        fig, ax = styled_fig(5, 4)
        bars = ax.bar(counts.index, counts.values,
                      color=bar_colors, width=0.5, edgecolor='none')
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + counts.values.max() * 0.02,
                    str(int(bar.get_height())),
                    ha='center', fontsize=9, color='#2c7da0', fontfamily='monospace')
        ax.set_xlabel("Hydration Level", fontsize=9, color='#2c7da0', fontfamily='monospace')
        ax.set_ylabel("Jumlah Data",     fontsize=9, color='#2c7da0', fontfamily='monospace')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    with col_b:
        good = (df['Hydration Level'] == 'Good').sum()
        poor = len(df) - good
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        fig2.patch.set_facecolor('#ffffff')
        ax2.pie(
            [poor, good],
            labels=["Poor", "Good"],
            colors=["#48cae4", "#0077b6"],
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops={"edgecolor": "#ffffff", "linewidth": 2},
            textprops={"fontsize": 9, "color": "#012a4a", "fontfamily": "monospace"}
        )
        ax2.set_title("Good vs Poor Hydration", fontsize=9,
                      color='#2c7da0', fontfamily='monospace', pad=12)
        plt.tight_layout()
        st.pyplot(fig2)
        plt.close(fig2)

with tab4:
    st.markdown('<div class="section-label">Boxplot Fitur Numerik per Kategori</div>',
                unsafe_allow_html=True)
    st.markdown("""
    <p class="chart-desc">
        Distribusi fitur numerik dikelompokkan berdasarkan variabel kategorikal pilihan.
        Berguna untuk melihat perbedaan pola antar kelompok (status hidrasi, aktivitas, cuaca, gender).
    </p>
    """, unsafe_allow_html=True)

    col_box1, col_box2 = st.columns(2, gap="large")
    with col_box1:
        numeric_cols2 = df.select_dtypes(include='number').columns.tolist()
        default_box   = numeric_cols2.index('Daily Water Intake (liters)') \
                        if 'Daily Water Intake (liters)' in numeric_cols2 else 0
        box_col = st.selectbox("Fitur numerik (sumbu Y)", numeric_cols2,
                               index=default_box, key="box_y")
    with col_box2:
        group_col = st.selectbox("Kelompokkan berdasarkan", 
                                 ["Hydration Level", "Physical Activity Level", "Weather", "Gender"],
                                 key="box_group")

    group_configs = {
        "Hydration Level":        {"order": ["Good", "Poor"],
                                   "palette": {"Good": "#0077b6", "Poor": "#48cae4"}},
        "Physical Activity Level":{"order": ["Low", "Moderate", "High"],
                                   "palette": {"Low": "#023e6e", "Moderate": "#0077b6", "High": "#48cae4"}},
        "Weather":                {"order": ["Cold", "Normal", "Hot"],
                                   "palette": {"Cold": "#90e0ef", "Normal": "#0096c7", "Hot": "#023e6e"}},
        "Gender":                 {"order": ["Male", "Female"],
                                   "palette": {"Male": "#0077b6", "Female": "#48cae4"}},
    }
    cfg = group_configs[group_col]

    fig, ax = styled_fig(9, 4.5)
    sns.boxplot(
        data=df, x=group_col, y=box_col, ax=ax,
        hue=group_col,
        palette=cfg["palette"],
        order=cfg["order"],
        legend=False,
        linewidth=0.9,
        flierprops={"marker": "o", "markersize": 3,
                    "markerfacecolor": "#0096c7", "alpha": 0.5}
    )
    ax.set_xlabel(group_col, fontsize=9, color='#2c7da0', fontfamily='monospace')
    ax.set_ylabel(box_col,   fontsize=9, color='#2c7da0', fontfamily='monospace')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with tab5:
    st.markdown('<div class="section-label">Perbandingan Fitur Kategorikal</div>',
                unsafe_allow_html=True)
    st.markdown("""
    <p class="chart-desc">
        Persentase Good vs Poor per kategori fitur. Membantu memahami pengaruh
        gender, aktivitas, dan cuaca terhadap status hidrasi.
    </p>
    """, unsafe_allow_html=True)

    cat_feature = st.selectbox(
        "Pilih fitur kategorikal",
        ["Gender", "Physical Activity Level", "Weather"],
        key="cat_select"
    )

    col_c, col_d = st.columns(2, gap="large")

    with col_c:
        # Stacked bar: % Good vs Poor per kategori
        ct = pd.crosstab(df[cat_feature], df['Hydration Level'], normalize='index') * 100
        fig, ax = styled_fig(5, 4)
        bottom = [0] * len(ct)
        colors_stack = {"Good": "#0077b6", "Poor": "#48cae4"}
        for label in ["Good", "Poor"]:
            if label in ct.columns:
                vals = ct[label].values
                bars = ax.bar(ct.index, vals, bottom=bottom,
                              color=colors_stack[label], width=0.5,
                              edgecolor='none', label=label)
                for bar, val, bot in zip(bars, vals, bottom):
                    if val > 6:
                        ax.text(bar.get_x() + bar.get_width() / 2,
                                bot + val / 2,
                                f"{val:.0f}%",
                                ha='center', va='center',
                                fontsize=8, color='white', fontfamily='monospace')
                bottom = [b + v for b, v in zip(bottom, vals)]
        ax.set_ylim(0, 115)
        ax.set_xlabel(cat_feature,  fontsize=9, color='#2c7da0', fontfamily='monospace')
        ax.set_ylabel("Persentase (%)", fontsize=9, color='#2c7da0', fontfamily='monospace')
        ax.legend(fontsize=8, framealpha=0.5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    with col_d:
        mean_df = df.groupby([cat_feature, 'Hydration Level'])['Daily Water Intake (liters)'].mean().unstack()
        fig, ax = styled_fig(5, 4)
        x      = range(len(mean_df))
        width  = 0.35
        labels = mean_df.index.tolist()
        if 'Good' in mean_df.columns:
            ax.bar([i - width/2 for i in x], mean_df['Good'],
                   width=width, color='#0077b6', edgecolor='none', label='Good')
        if 'Poor' in mean_df.columns:
            ax.bar([i + width/2 for i in x], mean_df['Poor'],
                   width=width, color='#48cae4', edgecolor='none', label='Poor')
        ax.set_xticks(list(x))
        ax.set_xticklabels(labels, fontsize=8, color='#2c7da0', fontfamily='monospace')
        ax.set_xlabel(cat_feature, fontsize=9, color='#2c7da0', fontfamily='monospace')
        ax.set_ylabel("Rata-rata Intake (L)", fontsize=9, color='#2c7da0', fontfamily='monospace')
        ax.legend(fontsize=8, framealpha=0.5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)
