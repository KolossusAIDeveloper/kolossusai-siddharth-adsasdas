import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="adsasdas", page_icon="✨", layout="wide")

# Theme persistence via localStorage
components.html("""
<script>
(function() {
  const KEY = 'adsasdas-theme';
  const saved = localStorage.getItem(KEY);
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const theme = saved || (prefersDark ? 'dark' : 'light');
  window.__adsasdas_theme = theme;
  window.parent.postMessage({type: 'adsasdas-theme-init', theme}, '*');
})();
</script>
""", height=0)

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

THEMES = {
    "dark": {
        "bg": "#0f1117",
        "surface": "#1e2130",
        "border": "#2d3250",
        "text_primary": "#f0f2f6",
        "text_secondary": "#a0a8c0",
        "accent": "#4f8ef7",
        "accent_hover": "#3a7ae8",
        "card_bg": "#1e2130",
        "toggle_bg": "#2d3250",
        "toggle_icon": "☀️",
        "toggle_label": "Light mode",
    },
    "light": {
        "bg": "#f5f7fa",
        "surface": "#ffffff",
        "border": "#d1d9e0",
        "text_primary": "#1a1f36",
        "text_secondary": "#5a6380",
        "accent": "#2563eb",
        "accent_hover": "#1d4ed8",
        "card_bg": "#ffffff",
        "toggle_bg": "#e8eaf0",
        "toggle_icon": "🌙",
        "toggle_label": "Dark mode",
    },
}

t = THEMES[st.session_state.theme]

st.markdown(f"""
<style>
  [data-testid="stAppViewContainer"] {{
    background-color: {t['bg']};
  }}
  [data-testid="stHeader"] {{
    background-color: {t['bg']};
  }}
  [data-testid="stSidebar"] {{
    background-color: {t['surface']};
  }}
  .block-container {{
    padding-top: 1.5rem;
  }}
  * {{
    color: {t['text_primary']};
  }}
  .app-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1.5rem;
    background: {t['surface']};
    border: 1px solid {t['border']};
    border-radius: 12px;
    margin-bottom: 2rem;
  }}
  .app-title {{
    font-size: 1.6rem;
    font-weight: 700;
    color: {t['text_primary']};
    margin: 0;
  }}
  .app-subtitle {{
    font-size: 0.9rem;
    color: {t['text_secondary']};
    margin: 0;
  }}
  .card {{
    background: {t['card_bg']};
    border: 1px solid {t['border']};
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
  }}
  .card-title {{
    font-size: 1rem;
    font-weight: 600;
    color: {t['text_secondary']};
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.5rem;
  }}
  .card-value {{
    font-size: 2.2rem;
    font-weight: 700;
    color: {t['accent']};
  }}
  .card-desc {{
    font-size: 0.85rem;
    color: {t['text_secondary']};
    margin-top: 0.3rem;
  }}
  .stButton > button {{
    background: {t['accent']};
    color: #ffffff !important;
    border: none;
    border-radius: 8px;
    padding: 0.4rem 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
  }}
  .stButton > button:hover {{
    background: {t['accent_hover']};
  }}
  p, h1, h2, h3, h4, label, span, div {{
    color: {t['text_primary']};
  }}
  .section-heading {{
    font-size: 1.2rem;
    font-weight: 600;
    color: {t['text_primary']};
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid {t['border']};
  }}
</style>
""", unsafe_allow_html=True)

# Header row
col_title, col_toggle = st.columns([5, 1])
with col_title:
    st.markdown(f"""
    <div style="padding: 0.5rem 0;">
      <div class="app-title">adsasdas</div>
      <div class="app-subtitle">Your dashboard · {st.session_state.theme.capitalize()} mode</div>
    </div>
    """, unsafe_allow_html=True)

with col_toggle:
    label = t["toggle_icon"] + " " + t["toggle_label"]
    if st.button(label, key="theme_toggle"):
        new_theme = "light" if st.session_state.theme == "dark" else "dark"
        st.session_state.theme = new_theme
        # Persist to localStorage
        components.html(f"""
        <script>
          localStorage.setItem('adsasdas-theme', '{new_theme}');
        </script>
        """, height=0)
        st.rerun()

st.markdown("---")

# Stat cards
c1, c2, c3, c4 = st.columns(4)
cards = [
    ("Total Items", "1,284", "Updated just now"),
    ("Active", "342", "+12% this week"),
    ("Pending", "57", "Needs attention"),
    ("Completed", "885", "All time"),
]
for col, (title, value, desc) in zip([c1, c2, c3, c4], cards):
    with col:
        st.markdown(f"""
        <div class="card">
          <div class="card-title">{title}</div>
          <div class="card-value">{value}</div>
          <div class="card-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown(f'<div class="section-heading">Overview</div>', unsafe_allow_html=True)

left, right = st.columns([2, 1])
with left:
    st.markdown(f"""
    <div class="card">
      <div class="card-title">Welcome to adsasdas</div>
      <p style="color:{t['text_secondary']}; line-height:1.7; margin-top:0.5rem;">
        This is your central workspace. Use the dashboard to track activity,
        monitor metrics, and manage your data — all in one place.
        Switch between light and dark mode using the toggle in the header.
      </p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown(f"""
    <div class="card">
      <div class="card-title">Quick Actions</div>
      <p style="color:{t['text_secondary']}; font-size:0.85rem;">Get started with common tasks.</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("New Item", key="new_item")
    st.button("View Report", key="view_report")
    st.button("Settings", key="settings_btn")
