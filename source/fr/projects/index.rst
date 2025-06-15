.. _projects-fr:

Projets
===========

.. raw:: html

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        body {
            background-color: #0F2B36;
            color: #DDFCF8;
            font-family: 'Segoe UI', sans-serif;
        }

        .jumbotron {
            background: linear-gradient(135deg, #0F2B36, #2DB6A0);
            color:  #DDFCF8;
            text-align: center;
            padding: 2.5rem 2rem;
            border-radius: 20px;
            margin-bottom: 3rem;
            box-shadow: 0 8px 18px rgba(0,0,0,0.3);
        }

        .section {
            font-weight: 700;
            text-align: center;
            margin: 2.5rem 0 1.5rem;
            font-size: 1.9rem;
            color: #62F2C5;
            text-transform: uppercase;
        }

        .card {
            border-radius: 15px;
            background-color: #10333F;
            padding: 25px;
            margin-bottom: 2rem;
            box-shadow: 0 5px 18px rgba(0,0,0,0.25);
            border-left: 6px solid #2DB6A0;
            color:  #DDFCF8;
            transition: transform 0.3s, box-shadow 0.3s;
            position: relative;
        }

        .card:hover {
            transform: scale(1.01);
            box-shadow: 0 12px 28px rgba(0,0,0,0.35);
        }

        .card h2 {
            color: #62F2C5;
            margin-top: 0;
        }

        .mini-card {
            background-color: #0F2B36;
            border-radius: 10px;
            padding: 1rem 1.2rem;
            margin-top: 1rem;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
        }

        .mini-card ul {
            padding-left: 20px;
            margin: 0.5rem 0;
        }

        .mini-card ul li {
            margin-bottom: 5px;
            font-size: 1.05rem;
        }

        .mini-card p {
            font-size: 1.05rem;
            margin-bottom: 1rem;
        }

        .logosec {
            width: 50px;
            height: 50px;
            position: absolute;
            top: 15px;
            right: 15px;
        }

        .btn-primary {
            display: inline-block;
            margin-top: 1rem;
            background-color: #2DB6A0;
            border: none;
            padding: 0.6rem 1.2rem;
            color: #0F2B36;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.3s;
        }

        .btn-primary:hover {
            background-color: #62F2C5;
        }
    </style>

    <div class="jumbotron">
        <h1 class="display-4">Mes projets</h1>
        <p>Applications concrètes en actuariat, data science et modélisation statistique</p>
    </div>

    <div class="section">Applications Shiny</div>

    <div class="card">
        <h2>Prédiction de Sinistres Auto</h2>
        <div class="mini-card">
            <ul>
                <li>Exploration interactive des variables (âge conducteur, puissance véhicule...)</li>
                <li>Modélisation avec GLM et GAM</li>
                <li>Visualisations dynamiques (Leaflet, matrices de corrélation)</li>
                <li>Évaluation des modèles : AIC, BIC, MAE, courbe ROC</li>
                <li>Prédiction de la fréquence de sinistres</li>
            </ul>
            <a href="https://johngab7.shinyapps.io/PredictCarCrash/" target="_blank" class="btn-primary">Ouvrir l'application</a>
        </div>
        <img src="../../../../_static/log.png" alt="Logo analytique" class="logosec">
    </div>

    <div class="card">
        <h2>Analyse de la Mortalité</h2>
        <div class="mini-card">
            <ul>
                <li>Sélection des pays et import depuis la base HMD</li>
                <li>Détection des valeurs manquantes</li>
                <li>Projection avec le modèle de Lee-Carter</li>
                <li>Export personnalisé des tables de mortalité</li>
            </ul>
            <a href="https://johngab7.shinyapps.io/MortalityApp/" target="_blank" class="btn-primary">Ouvrir l'application</a>
        </div>
    </div>

    <div class="card">
        <h2>Convergence du Maximum de Vraisemblance</h2>
        <div class="mini-card">
            <p>Visualisation des trajectoires de convergence, des paramètres estimés et des performances selon différents scénarios.</p>
            <a href="https://johngab7.shinyapps.io/mle_convergence_in_r/" target="_blank" class="btn-primary">Ouvrir l'application</a>
        </div>
    </div>

    <div class="card">
        <h2>Simulation Monte Carlo pour GMM</h2>
        <div class="mini-card">
            <p>Exploration du comportement de l'estimateur GMM selon les tailles d'échantillons et contextes simulés.</p>
            <a href="https://johngab7.shinyapps.io/monte_carlo_for_gmm_estimation/" target="_blank" class="btn-primary">Ouvrir l'application</a>
        </div>
    </div>

    <div class="section">Projets Éducatifs</div>

    <div class="card">
        <h2>Actu-Basics</h2>
        <div class="mini-card">
            <p>Une plateforme d’apprentissage pour maîtriser les bases de l’actuariat, des statistiques et de la data science. Un enseignement visuel au service de la rigueur technique.</p>
            <a href="https://johngab7.github.io/Actu_Basics/" target="_blank" class="btn-primary">Explorer Actu-Basics</a>
        </div>
        <img src="../../../../_static/log.png" alt="Logo Actu-Basics" class="logosec">
    </div>

        <div class="section">Vidéo d’introduction à Actu-Basics</div>
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); max-width: 100%; margin-bottom: 3rem;">
        <video controls style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
            <source src="../../_static/actubasics_intro.mp4" type="video/mp4">
            Votre navigateur ne prend pas en charge la balise vidéo.
        </video>
    </div>

