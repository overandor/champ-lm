import streamlit as st
from src.appraisal_report.styles import get_styles
from src.appraisal_report.components import (
    render_header,
    render_main_score_card,
    render_component_breakdown,
    render_validator_analysis,
)

def appraisal_report_screen():
    """
    Renders the NFT Appraisal Report screen.
    """
    # Inject custom CSS
    st.markdown(get_styles(), unsafe_allow_html=True)

    # Mock data based on the design reference
    main_score = 90
    recommendation = "Highly Recommended"
    nft_image_url = "https://lh3.googleusercontent.com/aida-public/AB6AXuCEjk_rANW6i-O05pCNOZhQQ94Akt0sZcRbnGGCQR1bYBKfv25bUfJM1mCzcUwCtiYv9qHNFFYQ9UX_mCYk6cP-OsWDn-uPaXe_79G3wbv2GevNssBlWqVVWYJOdF7eEVH3NUnDI5CA-XJKsHRiVJaOMqLM12CdktPO22JElsPTvaBU8BM3e2I3npNTLy3m1KLd4TWbIyDcnu_dWUQ5pdVzrnAxpoUTuFyk8szcIhiahzuqGurkyL2Id7Gc1tOrQiJpd57d-gegndE"
    components = [
        {"name": "Rarity", "score": 95, "weight": 40},
        {"name": "Artist Reputation", "score": 92, "weight": 25},
        {"name": "Historical Performance", "score": 85, "weight": 20},
        {"name": "Social Sentiment", "score": 88, "weight": 15},
    ]
    validators = [
        {
            "name": "Llama3",
            "score": 92,
            "analysis": "Emphasizes strong rarity signals and positive historical sales data as key value drivers.",
        },
        {
            "name": "Mixtral",
            "score": 88,
            "analysis": "Notes high social engagement but cautions on recent market volatility affecting short-term value.",
        },
    ]

    # Render the screen components
    render_header("CryptoPunk #7804")
    render_main_score_card(main_score, recommendation, nft_image_url)
    render_component_breakdown(components)
    render_validator_analysis(validators)

if __name__ == "__main__":
    appraisal_report_screen()
