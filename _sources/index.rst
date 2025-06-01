.. _Home:

Bienvenue / Welcome
========================

.. raw:: html

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f2f5;
        }
        .lang-switch {
            text-align: center;
            margin: 2rem 0;
        }
        .lang-switch select {
            padding: 0.6rem 1rem;
            font-size: 1rem;
            border-radius: 5px;
            border: 1px solid #ccc;
            background-color: #4ca1af;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }
        .lang-switch option {
            color: black;
        }
    </style>

    <div class="lang-switch">
        <label for="lang-select" style="font-weight: bold; margin-right: 0.5rem;">🌍 Veuillez choisir votre langue / Please select your language :</label>
        <select id="lang-select" onchange="window.location.href = this.value;">
            <option disabled selected>-- Sélectionnez / Select --</option>
            <option value="fr/index.html">🇫🇷 Français</option>
            <option value="en/index.html">🇬🇧 English</option>
        </select>
    </div>
    
    
.. raw:: html

    <div style="text-align:center; margin-top:3rem;">
        <img src="_static/language-hero.png" alt="Language selection hero" style="max-width: 100%; border-radius: 15px;">
    </div>

