import streamlit as st
from src.appraisal_report.main import appraisal_report_screen

def main_dashboard():
    """
    Main dashboard with navigation to different screens.
    """
    st.set_page_config(
        page_title="CHAMP-LM Dashboard",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    if "screen" not in st.session_state:
        st.session_state.screen = "Home"

    def set_screen(screen_name):
        st.session_state.screen = screen_name

    st.sidebar.title("Navigation")
    st.sidebar.button("Home", on_click=set_screen, args=("Home",))
    st.sidebar.button("NFT Appraisal Report", on_click=set_screen, args=("NFT Appraisal Report",))

    if st.session_state.screen == "Home":
        home_screen()
    elif st.session_state.screen == "NFT Appraisal Report":
        appraisal_report_screen()

def home_screen():
    """
    Placeholder for the home screen.
    """
    st.title("Home Screen")
    st.write("Welcome to the main dashboard.")

if __name__ == "__main__":
    main_dashboard()
