def get_styles():
    """
    Returns the CSS styles for the NFT Appraisal Report screen.
    """
    return """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');

    :root {
      --primary: #55B9A9;
      --background-dark: #1A1C1E;
      --text-dark: #E0E5EC;
      --text-muted-dark: #9DA3B0;
      --surface-dark: #24282C;
      --border-dark: #363A3E;
      --neo-dark-box-shadow: 5px 5px 10px #131516, -5px -5px 10px #212326;
      --neo-inset-dark-box-shadow: inset 5px 5px 10px #131516, inset -5px -5px 10px #212326;
    }

    body, .stApp {
        background-color: var(--background-dark);
        color: var(--text-dark);
        font-family: 'Inter', sans-serif;
    }

    .material-symbols-outlined {
        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    }

    .header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem;
        position: sticky;
        top: 0;
        background-color: var(--background-dark);
        z-index: 10;
    }

    .back-button {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 2.5rem;
        width: 2.5rem;
        border-radius: 9999px;
        box-shadow: var(--neo-dark-box-shadow);
        transition: all 0.2s;
        border: none;
        background-color: transparent;
        color: var(--text-dark);
    }

    .back-button:active {
        box-shadow: var(--neo-inset-dark-box-shadow);
    }

    .main-score-card {
        padding: 1.5rem;
        border-radius: 1.5rem;
        box-shadow: var(--neo-dark-box-shadow);
        margin-top: 1rem;
    }

    .accordion {
        border-radius: 0.75rem;
        box-shadow: var(--neo-dark-box-shadow);
        margin-top: 2rem;
    }

    .progress-bar-container {
        height: 0.5rem;
        width: 100%;
        border-radius: 9999px;
        box-shadow: var(--neo-inset-dark-box-shadow);
    }

    .progress-bar {
        height: 0.5rem;
        border-radius: 9999px;
        background-color: var(--primary);
    }

    .validator-card {
        padding: 1rem;
        border-radius: 0.75rem;
        box-shadow: var(--neo-inset-dark-box-shadow);
    }
</style>
"""
