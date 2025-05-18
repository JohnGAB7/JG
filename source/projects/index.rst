.. _projects-index:

Projets
=========

.. raw:: html

    <style>
        .jumbotron {
            background: linear-gradient(135deg, #2c3e50, #4ca1af);
            color: white;
            text-align: center;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            word-wrap: break-word;
        }
        .section {
            font-weight: bold;
            text-align: center;
            margin: 2rem 0 1rem;
            font-size: 2rem;
            color: #333;
        }
        .card {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
            padding: 1.5rem;
            background-color: #f9f9f9;
            border-left: 5px solid #4ca1af;
            position: relative;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover {
            transform: scale(1.03);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        .card h4 {
            margin-top: 0;
            color: #4ca1af;
        }
        .mini-card {
            background-color: #fff;
            border-radius: 10px;
            padding: 1rem;
            margin-top: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .mini-card ul {
            padding-left: 20px;
            margin: 0.5rem 0;
        }
        .mini-card ul li {
            margin-bottom: 5px;
        }
        .logosec {
            width: 50px;
            height: 50px;
            position: absolute;
            top: 10px;
            right: 10px;
        }
        .btn-primary {
            background-color: #4ca1af;
            border: none;
            padding: 0.5rem 1rem;
            color: white;
            border-radius: 5px;
            text-decoration: none;
        }
        .btn-primary:hover {
            background-color: #3b8a9e;
        }
    </style>

    <div class="jumbotron">
        <p class="display-4 typing-slow">Anciens</p>
    </div>

    <div class="card">
        <h4>Applications Shiny</h4>
        <div class="mini-card">
            <h5>Analyse et Prédiction des Sinistres Automobiles</h5>
            <ul>
                <li>Exploration interactive des données (âge conducteur, véhicule, puissance, etc.)</li>
                <li>Modélisation GLM et GAM</li>
                <li>Visualisations interactives (Leaflet, corrélations)</li>
                <li>Évaluation des modèles : AIC, BIC, MAE, courbes ROC</li>
                <li>Prédiction de fréquence et visualisation des résultats</li>
            </ul>
            <a href="https://johngab7.shinyapps.io/PredictCarCrash/" target="_blank" class="btn btn-primary">Accéder à l'application</a>
        </div>
        <img src="../_static/log.png" alt="Insurance Analytics Logo" class="logosec">
    </div>

    <div class="card">
        <div class="mini-card">
            <h5>Analyse des Taux de Mortalité</h5>
            <ul>
                <li>Sélection de pays et téléchargement depuis la base HMD</li>
                <li>Détection des valeurs manquantes</li>
                <li>Calcul et visualisation des taux de mortalité</li>
                <li>Projection via le modèle Lee-Carter</li>
                <li>Exportation de tables de mortalité</li>
            </ul>
            <a href="https://johngab7.shinyapps.io/MortalityApp/" target="_blank" class="btn btn-primary">Accéder à l'application</a>
        </div>
    </div>

    <div class="card">
        <div class="mini-card">
            <h5>Convergence de l’Estimation par Maximum de Vraisemblance (MLE)</h5>
            <p>Visualisez les trajectoires de convergence, les paramètres estimés et les performances statistiques à travers divers modèles et scénarios.</p>
            <a href="https://johngab7.shinyapps.io/mle_convergence_in_r/" target="_blank" class="btn btn-primary">Accéder à l'application</a>
        </div>
    </div>

    <div class="card">
        <div class="mini-card">
            <h5>Estimation GMM par Monte Carlo</h5>
            <p>Simulez des processus pour comprendre la convergence de GMM dans différents contextes d’estimation et tailles d’échantillons.</p>
            <a href="https://johngab7.shinyapps.io/monte_carlo_for_gmm_estimation/" target="_blank" class="btn btn-primary">Accéder à l'application</a>
        </div>
    </div>

    <div class="jumbotron">
        <p class="display-4 typing-slow">Nouveaux</p>
    </div>

    <div class="card">
        <h4>Auto Apprentissage</h4>
        <div class="mini-card">
            <h5>Actu-Basics</h5>
            <p>Plateforme de ressources pour apprendre les bases de l’actuariat, des statistiques et de l’analyse des données.</p>
            <a href="https://johngab7.github.io/Actu_Basics/" target="_blank" class="btn btn-primary">Accéder au projet Actu-Basics</a>
        </div>
        <img src="../_static/log.png" alt="Actu-Basic Logo" class="logosec">
    </div>
