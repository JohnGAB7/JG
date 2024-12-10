Hello 👋! 
============
Bienvenue sur la page de **John GABARY**
=======================================================

.. raw:: html

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap'); 
        
        body { 
            font-family: 'Menlo', monospace;
            background-color: #f4f4f9; 
            color: #333; 
            margin: 0; 
            padding: 0;
            text-align: center; 
        }

        .block {
            margin-bottom: 40px;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            transition: transform 1s, box-shadow 1s;
            overflow: hidden;
            text-overflow: ellipsis;
            word-wrap: break-word;
            hyphens: auto;
        }

        .block:hover {
            transform: translateY(-10px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }

        .contact-info {
            text-align: center;
            margin-bottom: 40px;
        }

        .contact-info p {
            margin: 5px 0;
        }

        .animated {
            animation-duration: 60s;
            animation-fill-mode: both;
        }

        .fadeIn {
            animation-name: fadeIn;
        }

        .fadeInUp {
            animation-name: fadeInUp;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        @keyframes fadeInUp {
            from {
                transform: scale(0.5);
                opacity: 0;
            }
            to {
                transform: scale(1);
                opacity: 1;
            }
        }

        .text { 
            opacity: 0; 
            animation: fadeIn 10s both; 
            font-size: 1em; 
            color: #333; 
            transition: color 1s;
            text-align: center;
        }

        .skills-container, .languages-container, .interests-container,
        .education-container, .experience-container {
            margin-top: 20px;
        }

        .skill-card, .language-card, .interest-card,
        .education-card, .experience-card {
            background-color: #f7f7f7;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
            text-align: center;
            transition: all 0.3s ease;
        }

        .skill-card h3, .language-card h3, .interest-card h3,
        .education-card h3, .experience-card h3 {
            margin-top: 0;
        }

        .skills-container, .languages-container, .interests-container,
        .education-container, .experience-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }

        .skill-card, .language-card, .interest-card, .education-card, .experience-card {
            flex: 1 1 calc(50% - 20px);
            margin: 10px;
        }

        .contact-form {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-color: #f7f7f7;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .contact-form input,
        .contact-form textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .contact-form button {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .contact-form button:hover {
            background-color: #0056b3;
        }

        .contact-form .hidden {
            display: none;
        }

        .typing-container {
            width: 100%;
            text-align: center;
            font-size: 1em;
            font-family: 'Menlo', monospace;
        }

        .typing {
            display: inline-block;
            white-space: nowrap;
            overflow: hidden;
            border-right: .20em;
            animation: typing 12s steps(140, end), blink-caret 1s step-end infinite;
        }

        .typing-slow {
            display: inline-block;
            white-space: nowrap;
            overflow: hidden;
            border-right: .20em;
            animation: typing-slow 8s steps(40, end), blink-caret 0.75s step-end infinite;
        }

        .delay-1 {
            animation-delay: 0s;
        }

        .delay-2 {
            animation-delay: 1s;
        }

        .delay-3 {
            animation-delay: 5s;
        }

        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }

        @keyframes typing-slow { 
            from { width: 0; }
            to { width: 100%; } 
        }

        @keyframes blink-caret {
            from, to { border-color: transparent; }
            50% { border-color: white; }
        }

        @media only screen and (max-width: 600px) {
            .skills-container, .languages-container, .interests-container,
            .education-container, .experience-container {
                flex-direction: column;
            }

            .skill-card, .language-card, .interest-card, .education-card, .experience-card {
                flex: 1 1 100%;
            }

            .block {
                padding: 10px;
                overflow: visible;
            }

            .contact-form {
                padding: 10px;
            }

            .typing-container, .text {
                font-size: 0.9em;
            }
        }
    </style>

    <div class="block">
        <div class="typing-slow">
            <strong>Actuaire junior</strong>, spécialisé en modélisation statistique et gestion des risques.
        </div>
    </div>

    <div class="typing-container">
        <div class="text">
            Diplômé en sciences actuarielles de l'Université Libre de Bruxelles 🎓, je combine expertise quantitative et programmation pour résoudre des problématiques complexes en actuariat non-vie et finance.

            Gravissant les échelons de la réussite 🚀, je suis déterminé à exceller dans le domaine de l'actuariat.
        </div>
    </div>

    <div class="typing-container">
        <div class="text delay-2">
            Découvrez ici mon parcours académique et mes réalisations professionnelles. 🌟
        </div>
    </div>

.. toctree::
   :maxdepth: 1
   :caption: Voir :

   formation_academique
   experiences_professionnelles
   competences

.. include:: contact.rst
