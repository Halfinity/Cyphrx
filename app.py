"""
CYPHRX :: cyber ops terminal — Streamlit wrapper.

Run with:
    streamlit run app.py

This module is a thin Streamlit shell around the original single-file HTML
application (cyphrx.html). The original markup, CSS, and JavaScript are
loaded verbatim and rendered inside a Streamlit HTML component, so all
existing behavior — boot animation, command palette, localStorage progress,
mobile drawers, RSS intel feed, etc. — is preserved exactly as-is.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
# Streamlit-specific: configure the host page before any other Streamlit call.
# `layout="wide"` gives the embedded terminal the full browser width, and
# collapsing the sidebar prevents Streamlit's own UI from competing with the
# in-app sidebar that the original HTML already provides.
st.set_page_config(
    page_title="CYPHRX :: cyber ops terminal",
    page_icon="🔺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Strip Streamlit's default chrome so the terminal fills the viewport
# ---------------------------------------------------------------------------
# Streamlit-specific: by default Streamlit adds page padding, a top header,
# the hamburger menu, and a footer. The original app is designed to occupy
# the full viewport, so we hide those elements and zero out the container
# padding. This is purely cosmetic glue — no original code is touched.
st.markdown(
    """
    <style>
      /* Match the terminal's deep-black background so any sliver of host
         page peeking through stays on-theme. */
      .stApp { background: #050505; }

      /* Edge-to-edge component: remove default Streamlit padding/margins. */
      .block-container,
      [data-testid="stAppViewContainer"] > .main > .block-container {
        padding: 0 !important;
        max-width: 100% !important;
      }
      [data-testid="stAppViewContainer"] { background: #050505; }

      /* Hide Streamlit chrome that would otherwise overlap the terminal UI. */
      header[data-testid="stHeader"] { display: none !important; }
      [data-testid="stToolbar"]      { display: none !important; }
      #MainMenu                       { visibility: hidden; }
      footer                          { visibility: hidden; }

      /* The component renders inside an iframe — drop its default border. */
      iframe { border: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Load the original HTML application (unchanged) and embed it
# ---------------------------------------------------------------------------
# The original file is kept verbatim alongside this script. We read it as
# UTF-8 text and hand it to Streamlit's HTML component, which renders it
# inside a sandboxed iframe. Because the iframe has its own document, all
# of the original JavaScript (DOMContentLoaded handlers, localStorage,
# fetch() calls to api.rss2json.com, keyboard shortcuts, etc.) continues
# to run exactly as it does when the .html file is opened directly.
HTML_PATH = Path(__file__).parent / "cyphrx.html"
html_source = HTML_PATH.read_text(encoding="utf-8")

# `height` is the iframe's pixel height. The original layout uses `100vh`
# internally, which inside an iframe resolves to this value. 900px gives a
# comfortable terminal-sized canvas on most laptops; `scrolling=True` lets
# users on shorter displays still reach the lower content.
components.html(html_source, height=900, scrolling=True)
