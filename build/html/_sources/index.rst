.. _Home:

Accueil
=========

.. raw:: html

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        body {
            font-family: 'Roboto', sans-serif;
        }

        .jumbotron {
            background: linear-gradient(135deg, #2c3e50, #4ca1af);
            color: white;
            text-align: center;
            padding: 2rem 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }

        .card-deck {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }

        .card {
            flex: 1 1 300px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 15px;
            background-color: #f9f9f9;
            border-left: 5px solid #4ca1af;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .card:hover {
            transform: scale(1.03);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .card h4 {
            margin-top: 0;
            color: #2c3e50;
        }

    </style>

    <div class="jumbotron">
        <h1 class="display-4">Bienvenue sur ma page</h1>
        <p style="margin-top: 1rem;">Je m'appelle <strong>John GABARY</strong>, Actuaire diplômé et passionné par la <strong>modélisation prédictive</strong>, les <strong>statistiques appliquées</strong> et l'<strong>innovation actuarielle</strong>.</p>
        <p>Mon objectif : créer de la valeur durable à travers des modèles robustes, compréhensibles et utiles.</p>
    </div>

    <div class="card-deck">
        <div class="card">
            <div class="card-body">
                <h4 class="card-title">À propos de moi</h4>
                <p class="card-text">Découvrez mon parcours, mes valeurs et ma vision du métier d’actuaire.</p>
                <a href="about/index.html" class="btn">En savoir plus</a>
            </div>
        </div>

        <div class="card">
            <div class="card-body">
                <h4 class="card-title">Mon CV</h4>
                <p class="card-text">Accédez à l’ensemble de mes expériences, compétences techniques et certifications.</p>
                <a href="cv/index.html" class="btn">CV</a>
            </div>
        </div>

        <div class="card">
            <div class="card-body">
                <h4 class="card-title">Mes Projets</h4>
                <p class="card-text">Explorez des projets concrets en data science, tarification, prédiction de sinistres, etc.</p>
                <a href="projects/index.html" class="btn">Projets</a>
            </div>
        </div>
    </div>

.. toctree::
   :maxdepth: 2
   :caption: Contenu:

   about/index
   cv/index
   projects/index
   contact/index
