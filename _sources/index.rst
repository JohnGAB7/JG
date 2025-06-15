.. _Home:

Welcome / Bienvenue 👋
==============================

.. raw:: html

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {
            background-color: #0F2B36;
            color: #DDFCF8;
            font-family: 'Segoe UI', sans-serif;
        }

    h1, h2 {
        color: #62F2C5;
        text-align: center;
        margin-top: 3rem;
        margin-bottom: 1rem;
    }

    .lang-switch {
        text-align: center;
        margin: 4rem 0 2rem;
    }

    .lang-switch label {
        font-weight: bold;
        font-size: 1.3rem;
        color: #B5F3E9;
        margin-bottom: 1rem;
        display: inline-block;
    }

    .lang-switch select {
        padding: 0.7rem 1.2rem;
        font-size: 1rem;
        border-radius: 8px;
        border: none;
        background-color: #62F2C5;
        color: #DDFCF8;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .lang-switch select:hover {
        background-color: #62F2C5;
        color: #0F2B36;
    }

    .lang-switch option {
        color: #0F2B36;
        background-color: #62F2C5;
    }

    .hero-img {
        display: block;
        margin: 3rem auto 4rem;
        max-width: 95%;
        border-radius: 18px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }

    </style>

.. raw:: html

    <div class="lang-switch">
        <label for="lang-select">🌍 Please select your language / Veuillez choisir votre langue :</label><br>
        <select id="lang-select" onchange="window.location.href = this.value;">
            <option disabled selected>-- Select --</option>
            <option value="fr/index.html">🇫🇷 Français</option>
            <option value="en/index.html">🇬🇧 English</option>
        </select>
    </div>

    <div class="hero-img">
        <img src="_static/language-hero.png" alt="Welcome illustration" />
    </div>

.. toctree::
   :hidden:
   :maxdepth: 2

   fr/index
   en/index
