.. _projects-index:

🚀 Projets
===============
.. raw:: html

    <style>
        .jumbotron {
        background: linear-gradient(135deg, #2c3e50, #4ca1af);
        color: white;
        text-align: center;
        padding: 2rem 1rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        transition: transform 0.3s, box-shadow 0.3s;
        }
        .section {
            font-weight: bold;
            text-align: center;
            margin: 2rem 0;
            font-size: 2rem;
            color: #333333;
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
        .card h4 {
            margin-top: 0;
            color: #4ca1af;
        }
        .date {
            font-style: italic;
            color: #4a5c76;#4ca1af;
        }
        .institution {
            font-style: italic;
            color: #597b89;
        }
        .achievements {
            margin-top: 5px;
            color: #333;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .mini-card {
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 10px;
            flex: 1 1 calc(50% - 10px);
            box-sizing: border-box;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .mini-card ul {
            padding-left: 20px;
        }
        .mini-card ul li {
            list-style-type: disc;
            margin-bottom: 5px;
        }
        .logosec {
            width: 60px;
            height: 60px;
            position: absolute;
            top: 10px;
            right: 10px;
        }
                .typing-slow {
            display: inline-block;
            white-space: nowrap;
            overflow: hidden;
            border-right: .20em;
            animation: typing-slow 8s steps(40, end), blink-caret 0.75s step-end infinite;
        }

        .delay-1 {
            animation-delay: 8s;
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
        .skills-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        margin: 2rem 0;
        }
        .skill-circle {
            width: 160px;
            height: 160px;
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }
        .skill-circle:hover {
            transform: scale(1.1);
        }
        .skill-circle span {
            padding: 10px;
            font-size: 16px;
        }
        .emoji {
            font-size: 24px;
            margin-top: 5px;
        }
        .technical {
            background-color: #4ca1af; /* Couleur pour les compétences techniques */
            color: white;
        }
        .interpersonal {
            background-color: #2c3e50; /* Couleur pour les compétences interpersonnelles */
            color: white;
        }
    </style>

    <div class="jumbotron" style="background: linear-gradient(135deg, #2c3e50, #4ca1af); color: white; text-align: center; padding: 2rem 2rem; border-radius: 15px; margin-bottom: 2rem; word-wrap: break-word; overflow-wrap: break-word;">
    <p class="card-text display-4 typing-slow">Anciens</p>
    </div>

.. raw:: html

    <div class="section"></div>
    <div class="card">
        <h4>Applications Shiny</h4>
        <div class="achievements">
            <div class="mini-card">
            <h5>Convergence de l'Estimation par Maximum de Vraisemblance (MLE)</h5>
            <p>Explorez le comportement de la convergence de l'Estimation par Maximum de Vraisemblance (MLE) dans divers scénarios statistiques. Visualisez les trajectoires de convergence, les estimations des paramètres et les statistiques associées. Plongez dans différents modèles et observez les performances de MLE dans différents contextes. <a href="https://johngab7.shinyapps.io/mle_convergence_in_r/">Accéder à l'Application de Convergence MLE</a></p>
            </div>
            <div class="mini-card">
            <h5>Estimation GMM par Monte Carlo</h5>
            <p>Cette application se concentre sur la convergence de l'estimation par la Méthode des Moments Généralisés (GMM) à travers des simulations Monte Carlo. Examinez les performances de GMM dans différentes conditions, y compris les tailles d'échantillon et les valeurs des paramètres réels. Visualisez les résultats des estimations et obtenez des insights sur l'efficacité de GMM dans l'estimation des paramètres du modèle. <a href="https://johngab7.shinyapps.io/monte_carlo_for_gmm_estimation/">Accéder à l'Application d'Estimation GMM par Monte Carlo</a></p>
            </div>
        </div>
        <img src="../_static/log.png" alt="ULB Logo" class="logosec">
    </div>
.. raw:: html

    <div class="jumbotron" style="background: linear-gradient(135deg, #2c3e50, #4ca1af); color: white; text-align: center; padding: 2rem 2rem; border-radius: 15px; margin-bottom: 2rem; word-wrap: break-word; overflow-wrap: break-word;">
    <p class="card-text display-4 typing-slow">Nouveaux</p>
    </div>

    <div class="section"></div>
    <div class="card">
        <h4>Auto Apprentissage</h4>
        <div class="achievements">
            <div class="mini-card">
            <h5>Actu-Basics</h5>
            <p>Actu-Basics est un projet visant à fournir des ressources pour apprendre et comprendre les bases de l'actuariat, des statistiques et de l'analyse des données. <a href="https://johngab7.github.io/Actu_Basics/">Accéder au projet Actu-Basics</a></p>
            </div>
        </div>
        <img src="../_static/log.png" alt="ULB Logo" class="logosec">
    </div>

