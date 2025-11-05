import streamlit as st

def render_header(title):
    """
    Renders the header with a back button and a title.
    """
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        if st.button("← Back"):
            st.session_state.screen = "Home"
    with col2:
        st.header(title)
    with col3:
        pass


def render_main_score_card(score, recommendation, image_url):
    """
    Renders the main score card with a circular progress bar and NFT image.
    """
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image_url, width=100)

    with col2:
        # This is a simplified version of the circular progress bar.
        # A full implementation requires more complex SVG and CSS.
        score_card_html = f"""
        <div style="text-align: center;">
            <div style="position: relative; display: inline-block; width: 150px; height: 150px;">
                <svg width="150" height="150" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="40" fill="transparent" stroke="#363A3E" stroke-width="8"></circle>
                    <circle cx="50" cy="50" r="40" fill="transparent" stroke="#55B9A9" stroke-width="8" stroke-dasharray="251.2" stroke-dashoffset="{251.2 * (1 - score / 100)}" transform="rotate(-90 50 50)"></circle>
                </svg>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
                    <span style="font-size: 2rem; font-weight: 800;">{score}</span>
                    <span style="font-size: 0.8rem;">/ 100</span>
                </div>
            </div>
            <h2 style="font-size: 1.5rem; font-weight: 700; margin-top: 1rem;">Consensus Score</h2>
            <p style="color: #55B9A9; font-weight: 600;">{recommendation}</p>
        </div>
        """
        st.markdown(score_card_html, unsafe_allow_html=True)

def render_component_breakdown(components):
    """
    Renders the component breakdown accordion.
    """
    with st.expander("Component Breakdown", expanded=True):
        st.markdown('<p class="text-sm font-normal text-text-muted-dark pb-4 border-b border-border-light dark:border-border-dark">Detailed scores for each component used in the appraisal.</p>', unsafe_allow_html=True)
        for component in components:
            st.markdown(f"""
            <div style="margin-bottom: 1.5rem;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <p style="font-weight: 500;">{component['name']}</p>
                    <p style="font-size: 0.9rem; font-weight: 500;">{component['score']}/100</p>
                </div>
                <div class="progress-bar-container">
                    <div class="progress-bar" style="width: {component['score']}%;"></div>
                </div>
                <p style="font-size: 0.75rem; color: #9DA3B0;">Weight: {component['weight']}%</p>
            </div>
            """, unsafe_allow_html=True)

def render_validator_analysis(validators):
    """
    Renders the validator analysis accordion.
    """
    with st.expander("Validator Analysis", expanded=False):
        st.markdown('<p class="text-sm font-normal text-text-muted-dark pb-4 border-b border-border-light dark:border-border-dark">Analysis from individual AI validator models.</p>', unsafe_allow_html=True)
        for validator in validators:
            st.markdown(f"""
            <div class="validator-card" style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <h4 style="font-weight: 700;">{validator['name']} Analysis</h4>
                    <div>
                        <span style="font-weight: 700; color: #55B9A9; font-size: 1.2rem;">{validator['score']}</span>
                        <span style="font-size: 0.9rem; color: #9DA3B0;">/100</span>
                    </div>
                </div>
                <p style="font-size: 0.9rem; color: #9DA3B0;">{validator['analysis']}</p>
            </div>
            """, unsafe_allow_html=True)
