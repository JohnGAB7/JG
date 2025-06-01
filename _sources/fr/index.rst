.. _fr-index:

Accueil
=========

.. raw:: html

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f2f5;
        }

        .jumbotron {
            background: linear-gradient(135deg, #2c3e50, #4ca1af);
            color: white;
            text-align: center;
            padding: 3rem 2rem;
            border-radius: 20px;
            margin-bottom: 3rem;
        }

        .jumbotron h1 {
            font-size: 2.8rem;
            margin-bottom: 1rem;
        }

        .jumbotron p {
            font-size: 1.1rem;
            margin: 0.5rem auto;
            max-width: 800px;
        }

        .card-deck {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
            padding: 0 2rem 2rem;
        }

        .card {
            flex: 1 1 280px;
            border-radius: 15px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
            background-color: #ffffff;
            transition: transform 0.3s, box-shadow 0.3s;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }

        .card-title {
            font-size: 1.4rem;
            color: #2c3e50;
            margin-bottom: 0.8rem;
        }

        .card-text {
            font-size: 1rem;
            color: #555;
            flex-grow: 1;
        }

        .btnn {
            display: inline-block;
            margin-top: 1.5rem;
            padding: 0.6rem 1.2rem;
            background-color: #4ca1af;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.3s;
            text-align: center;
        }

        .btnn:hover {
            background-color: #2c3e50;
        }
    </style>

    <div class="jumbotron">
    <h1 class="display-4">Bienvenue</h1>
    <p>Je suis <strong>John GABARY</strong>, Actuaire diplômé, passionné par l'<strong>actuariat moderne</strong>, la <strong>data science</strong> et la <strong>conception de modèles explicables et accessibles</strong>.</p>
    <p>Ma mission : <em>construire des ponts entre la théorie mathématique, la programmation, et la prise de décision.</em></p>
    <p>À travers mes projets, je combine rigueur statistique, outils numériques et créativité pour créer des modèles explicables, performants et à impact durable.</p>
    </div>


    <div class="card-deck">
        <div class="card">
            <div class="card-body">
                <h4 class="card-title">À propos de moi</h4>
                <p class="card-text">Mon parcours, mes engagements, et ma vision d’un actuariat utile, accessible et tourné vers l’avenir.</p>
                <a href="about/index.html" class="btnn">En savoir plus</a>
            </div>
        </div>

        <div class="card">
            <div class="card-body">
                <h4 class="card-title">Mon CV</h4>
                <p class="card-text">Formations, expériences, compétences et certifications rassemblées ici.</p>
                <a href="cv/index.html" class="btnn">Explorer</a>
            </div>
        </div>

        <div class="card">
            <div class="card-body">
                <h4 class="card-title">Mes Projets</h4>
                <p class="card-text">Projets concrets en actuariat, machine learning, modélisation pédagogique et développement Python.</p>
                <a href="projects/index.html" class="btnn">Découvrir</a>
            </div>
        </div>

        <div class="card">
            <div class="card-body">
                <h4 class="card-title">Me contacter</h4>
                <p class="card-text">Une idée, une collaboration ou une question ? Je suis à votre écoute.</p>
                <a href="contact/index.html" class="btnn">Contact</a>
            </div>
        </div>
    </div>


.. toctree::
   :maxdepth: 2
   :caption: Navigation

   about/index
   cv/index
   projects/index
   contact/index


