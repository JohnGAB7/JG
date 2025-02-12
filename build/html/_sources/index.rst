.. _Home:

.. raw:: html

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap'); 

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

        .card {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            padding: 15px;
            background-color: #f9f9f9;
            border-left: 5px solid #4ca1af;
            position: relative;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
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
            animation: typing 12s steps(40, end), blink-caret 1s step-end infinite;
        }

        .typing-slow {
            display: inline-block;
            white-space: nowrap;
            overflow: hidden;
            border-right: .20em;
            animation: typing-slow 8s steps(40, end), blink-caret 0.75s step-end infinite;
        }

        .delay-1 {
            animation-delay: 6s;
        }

        .delay-2 {
            animation-delay: 12s;
        }

        .delay-3 {
            animation-delay: 16s;
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
        }
    </style>
    

   <div class="jumbotron" style="background: linear-gradient(135deg, #2c3e50, #4ca1af); color: white; text-align: center; padding: 2rem 2rem; border-radius: 20px; margin-bottom: 2rem; word-wrap: break-word; overflow-wrap: break-word;">
    <h1 class="display-4">Bienvenue sur ma page</h1>
   </div>

   <div class="jumbotron" style="background: linear-gradient(135deg, #2c3e50, #4ca1af); color: white; text-align: center; padding: 2rem 1rem; border-radius: 15px; margin-bottom: 2rem;">
     <hr class="my-4">
     <p></p>
     <div class="card-deck">
   <div class="card">
     <div class="card-body">
       <h4 class="card-title">À propos de moi</h4>
       <p class="card-text"></p>
       <p class="card-text">Je suis <strong>John GABARY</strong>, <strong>Actuaire</strong> passioné par la modélisation statistique et actuarielle.</p>
       <p class="card-text"></p>
       <a href="about/index.html" class="btn btn-primary">En savoir plus</a>
     </div>
   </div>
   <div class="card">
     <div class="card-body">
       <h4 class="card-title">Mon CV</h4>
       <p class="card-text">Découvrez mon parcours académique et professionnel.</p>
        <p class="card-text"></p>
       <a href="cv/index.html" class="btn btn-primary">Voir mon CV</a>
     </div>
   </div>
   <div class="card">
     <div class="card-body">
       <h4 class="card-title">Mes Projets</h4>
       <p class="card-text">Explorez mes projets réalisés et en cours.</p>
        <p class="card-text"></p>
       <a href="projects/index.html" class="btn btn-primary">Voir mes projets</a>
     </div>
   </div>


   
.. toctree::
   :maxdepth: 2
   :caption: Contenu:

   about/index
   cv/index
   projects/index
   contact/index
