Hello, bienvenue sur ma page personnelle
=======================================================

.. raw:: html

    <style>
        .block {
            margin-bottom: 40px;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            transition: transform 1s, box-shadow 1s;
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
                transform: translate3d(0, 40px, 0);
                opacity: 0;
            }
            to {
                transform: translate3d(0, 0, 0);
                opacity: 1;
            }
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
            background-color: #007bff;
        }

        .contact-form .hidden {
            display: none;
        }

        .typing-container {
            width: 100%;
            text-align: center;
            font-size: 1em;
            font-weight: bold;
        }

        .typing {
            display: inline-block;
            white-space: nowrap;
            overflow: hidden;
            border-right: .20em black;
            animation: typing 12s steps(140, end), blink-caret .75s step-end infinite;
        }

        .typing-slow {
            display: inline-block;
            white-space: nowrap;
            overflow: hidden;
            border-right: .20em black;
            animation: typing-slow 4s steps(40, end), blink-caret .75s step-end infinite;
        }

        .delay-1 {
            animation-delay: 0s;
        }

        .delay-2 {
            animation-delay: 2.5s;
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
             to { width: 100%; } }

        @keyframes blink-caret {
            from, to { border-color: transparent; }
            50% { border-color: white; }
        }
    </style>

    <div class="typing-container">
        <div class="typing-slow">
            Je suis <strong>John GABARY,</strong> actuaire junior par la combinaison de la programmation et des sciences actuarielles.          
        </div>
    </div>

    <div class="typing-container">
        <div class="typing animated delay-2">
            Ici, vous découvrirez mon parcours académique et professionnel ainsi que mes projets en actuariat et en statistiques.
        </div>
    </div>
