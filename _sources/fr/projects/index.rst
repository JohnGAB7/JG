.. _projects-fr:

Projets
===============

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
        .card h2 {
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
        <h1 class="display-4">Projets Réalisés</h1>
        <p>Exploration d'applications concrètes en actuariat, data science et statistique appliquée</p>
    </div>

    <div class="section">Applications Shiny</div>

    <div class="card">
        <h2>Analyse et Prédiction des Sinistres Automobiles</h2>
        <div class="mini-card">
            <ul>
                <li>Exploration interactive des données (âge, véhicule, puissance...)</li>
                <li>Modélisation GLM et GAM</li>
                <li>Visualisations interactives (Leaflet, corrélations)</li>
                <li>Évaluation : AIC, BIC, MAE, ROC</li>
                <li>Prédiction de fréquence des sinistres</li>
            </ul>
            <a href="https://johngab7.shinyapps.io/PredictCarCrash/" target="_blank" class="btn-primary">Voir l'application</a>
        </div>
        <img src="../../_static/log.png" alt="Insurance Analytics Logo" class="logosec">
    </div>

    <div class="card">
        <h2>Analyse des Taux de Mortalité</h2>
        <div class="mini-card">
            <ul>
                <li>Téléchargement HMD, nettoyage, détection des anomalies</li>
                <li>Visualisation et projection par Lee-Carter</li>
                <li>Export de tables de mortalité personnalisées</li>
            </ul>
            <a href="https://johngab7.shinyapps.io/MortalityApp/" target="_blank" class="btn-primary">Voir l'application</a>
        </div>
    </div>

    <div class="card">
        <h2>Convergence de l'Estimation par Maximum de Vraisemblance (MLE)</h2>
        <div class="mini-card">
            <p>Visualisation de la trajectoire de convergence pour différents modèles et scénarios.</p>
            <a href="https://johngab7.shinyapps.io/mle_convergence_in_r/" target="_blank" class="btn-primary">Voir l'application</a>
        </div>
    </div>

    <div class="card">
        <h2>Estimation GMM par Monte Carlo</h2>
        <div class="mini-card">
            <p>Simulation et visualisation de convergence GMM selon différents échantillons.</p>
            <a href="https://johngab7.shinyapps.io/monte_carlo_for_gmm_estimation/" target="_blank" class="btn-primary">Voir l'application</a>
        </div>
    </div>

    <div class="section">Projets Éducatifs</div>

    <div class="card">
        <h2>Actu-Basics</h2>
        <div class="mini-card">
            <p>Plateforme d'auto-apprentissage pour actuaires et data scientists débutants : concepts fondamentaux, modélisation, visualisation, pédagogie moderne.</p>
            <a href="https://johngab7.github.io/Actu_Basics/" target="_blank" class="btn-primary">Découvrir Actu-Basics</a>
        </div>
        <img src="../../_static/log.png" alt="Actu-Basics Logo" class="logosec">
    </div>
