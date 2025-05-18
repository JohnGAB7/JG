.. _cv-index:

CV
==========

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
        .card h5 {
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
        .skill-logo img {
            background-color:rgb(250, 250, 250); /* Couleur pour les compétences interpersonnelles */
            color: white;
            width: 60px;
            height: auto;
            margin: 10px;
        }
        .skill-logo {
            background-color: white;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 10px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
        }
        .skill-logo img {
            max-width: 60%;
            max-height: 60%;
        }

    </style>


.. raw:: html

    <div class="section">🎓 Formation Académique</div>

    <div class="card">
        <h5>Master en Actuariat</h5>
        <p class="institution">Université Libre de Bruxelles</p>
        <p class="date">2024</p>
        <div class="achievements">
            <div class="mini-card">
                <h6>Cours principaux</h6>
                <ul>
                    <li>Probabilités et Statistiques</li>
                    <li>Assurance Vie et Non-Vie</li>
                    <li>Mathématiques Financières</li>
                    <li>Gestion des Risques, ALM, Réassurance</li>
                    <li>Analyse de Données, Modélisation Stochastique</li>
                    <li>Économétrie, Projet de Mémoire</li>
                </ul>
            </div>
        </div>
        <img src="../_static/ulb.png" alt="ULB Logo" class="logosec">
    </div>

    <div class="card">
        <h5>Maîtrise en Économie Mathématique</h5>
        <p class="institution">Université de Dschang</p>
        <p class="date">2021</p>
        <div class="achievements">
            <div class="mini-card">
                <h6>Cours principaux</h6>
                <ul>
                    <li>Séries Chronologiques, Modélisation Économique</li>
                    <li>Économétrie Avancée, Macro/Microéconomie Dynamique</li>
                    <li>Analyse de Bases de Données, Théorie des Jeux</li>
                    <li>Recherche Opérationnelle, Projet de Mémoire</li>
                </ul>
            </div>
        </div>
        <img src="../_static/uds.png" alt="Université de Dschang Logo" class="logosec">
    </div>

    <div class="card">
        <h5>Licence en Économie Mathématique</h5>
        <p class="institution">Université de Dschang</p>
        <p class="date">2020</p>
        <div class="achievements">
            <div class="mini-card">
                <h6>Cours principaux</h6>
                <ul>
                    <li>Statistiques, Probabilités, Économétrie</li>
                    <li>Mathématiques Financières, Recherche Opérationnelle</li>
                    <li>Microéconomie, Macrodynamique</li>
                    <li>Projet de Mémoire</li>
                </ul>
            </div>
        </div>
        <img src="../_static/uds.png" alt="Université de Dschang Logo" class="logosec">
    </div>

    <div class="card">
        <h5>Technicien Supérieur de la Statistique</h5>
        <p class="institution">Institut Sous-Régional de Statistique et d’Économie Appliquée</p>
        <p class="date">2019</p>
        <div class="achievements">
            <div class="mini-card">
                <h6>Cours principaux</h6>
                <ul>
                    <li>Statistiques Descriptives, Probabilités</li>
                    <li>Microéconomie, Macroéconomie</li>
                    <li>Économétrie, Analyse de Données</li>
                    <li>Mathématiques Financières, Projet de Fin d'Études</li>
                </ul>
            </div>
        </div>
        <img src="../_static/issea.png" alt="ISSEA Logo" class="logosec">
    </div>

.. raw:: html

    <div class="section">💼 Expériences Professionnelles</div>

    <div class="card">
        <h5>Consultant Actuaire Junior</h5>
        <p class="institution">Act-Unity s.a/n.v</p>
        <p class="date">Août 2024 - Présent</p>
        <div class="achievements">
            <div class="mini-card">
                <ul>
                    <li>Renouvellement et tarification des plans d’assurance groupe.</li>
                    <li>Analyses actuarielles de régimes à cotisations définies (DC) et prestations définies (DB).</li>
                </ul>
            </div>
        </div>
        <img src="../_static/act.png" alt="Logo Act-Unity" class="logosec">
    </div>

    <div class="card">
        <h5>Stagiaire en Actuariat</h5>
        <p class="institution">Europ Assistance Belgique</p>
        <p class="date">Décembre 2023 - Juillet 2024</p>
        <div class="achievements">
            <div class="mini-card">
                <ul>
                    <li>Développement de tableaux de bord Power BI et Excel, réduisant le temps de reporting de 30 %.</li>
                    <li>Construction de modèles GLM avec AKUR8 pour l’analyse des coûts de sinistres (amélioration de la tarification de 20 %).</li>
                    <li>Analyses de sensibilité sur scénarios tarifaires, augmentant les marges opérationnelles de 12 %.</li>
                </ul>
            </div>
        </div>
        <img src="../_static/europas.png" alt="Logo Europ Assistance" class="logosec">
    </div>

    <div class="card">
        <h5>Technicien Supérieur de la Statistique</h5>
        <p class="institution">Ministère de l’Habitat et du Développement Urbain</p>
        <p class="date">Octobre 2020 - Août 2021</p>
        <div class="achievements">
            <div class="mini-card">
                <ul>
                    <li>Suivi et évaluation des projets d’urbanisme.</li>
                    <li>Production de statistiques sectorielles pour la planification.</li>
                </ul>
            </div>
        </div>
        <img src="../_static/minhdu.png" alt="Logo Ministère de l’Habitat et du Développement Urbain" class="logosec">
    </div>

    <div class="card">
        <h5>Stagiaire en Statistique</h5>
        <p class="institution">Cameroon Policy Analysis and Research Center</p>
        <p class="date">Février 2019 - Mai 2019</p>
        <div class="achievements">
            <div class="mini-card">
                <ul>
                    <li>Analyse de la performance budgétaire.</li>
                    <li>Élaboration d’indicateurs pour le suivi de projets.</li>
                </ul>
            </div>
        </div>
        <img src="../_static/camercap.png" alt="Logo Cameroon Policy Analysis and Research Center" class="logosec">
    </div>

.. raw:: html

    <div class="section">🛠️ Compétences</div>

    <div class="card">
        <h5>Compétences Techniques</h5>
        <div class="achievements">
            <div class="mini-card">
                <ul>
                    <li><strong>Langages</strong> : Python, R, SQL, VBA, SAS</li>
                    <li><strong>BI & Visualisation</strong> : Power BI, Tableau, Excel (Power Query)</li>
                    <li><strong>Modélisation</strong> : GLM, GAM, Forêts aléatoires, Gradient Boosting</li>
                    <li><strong>Actuariat</strong> : Tarification Auto/Non-Vie, rentabilité, segmentation, reporting</li>
                    <li><strong>Certification en cours</strong> : Data Science avec Python et R</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="card">
        <h5>Compétences Interpersonnelles</h5>
        <div class="achievements">
            <div class="mini-card">
                <ul>
                    <li>Communication claire</li>
                    <li>Esprit d’équipe</li>
                    <li>Résolution de problèmes</li>
                    <li>Leadership et initiative</li>
                </ul>
            </div>
        </div>
    </div>

.. raw:: html


    <div class="skills-container">
        <!-- Logos des logiciels / outils techniques maîtrisés -->
        <div class="skill-logo technical">
            <img src="../_static/python.png" alt="Python" title="Python">
        </div>
        <div class="skill-logo technical">
            <img src="../_static/rr.jpg" alt="R" title="R">
        </div>
        <div class="skill-logo technical">
            <img src="../_static/sql.png" alt="SQL" title="SQL">
        </div>
        <div class="skill-logo technical">
            <img src="../_static/sas.png" alt="SAS" title="SAS">
        </div>
        <div class="skill-logo technical">
            <img src="../_static/powerbi.png" alt="Power BI" title="Power BI">
        </div>
        <div class="skill-logo technical">
            <img src="../_static/excel.png" alt="Excel" title="Excel">
        </div>
        <div class="skill-logo technical">
            <img src="../_static/akur8.png" alt="AKUR8" title="AKUR8">
        </div>
    </div>

    <div class="skills-container">
        <!-- Compétences Interpersonnelles -->
        <div class="skill-circle interpersonal">
            <span>Communication efficace</span>
            <div class="emoji">🗣️</div>
        </div>
        <div class="skill-circle interpersonal">
            <span>Travail en équipe</span>
            <div class="emoji">🤝</div>
        </div>
        <div class="skill-circle interpersonal">
            <span>Résolution de problèmes</span>
            <div class="emoji">🧩</div>
        </div>
        <div class="skill-circle interpersonal">
            <span>Leadership</span>
            <div class="emoji">🌟</div>
        </div>
    </div>



.. raw:: html

    <div class="section">Projets Académiques Réalisés</div>
    <div class="card">
        <h5>Avril 2022 : Assurance Vie</h5>
        <div class="achievements">
            <div class="mini-card">
                <ul>
                    <li>Analyse et estimation des taux de mortalité pour une cohorte d'assurés sous contrat de rente viagère temporaire.</li>
                    <li>Utilisation des données de la Human Mortality Database pour estimer, projeter et diagnostiquer la mortalité.</li>
                    <li>Évaluation de l'impact sur la tarification et la solvabilité de l'assureur.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="card">
        <h5>Juin 2023 : Gestion Actif-Passif en assurance vie</h5>
        <div class="achievements">
            <div class="mini-card">
                <ul>
                    <li>Modélisation, évaluation des fonds propres.</li>
                    <li>Analyse du risque de taux d'intérêt.</li>
                    <li>Optimisation de l'allocation des actifs avec R.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="card">
        <h5>Avril 2023 : Modèles Financiers en assurance vie</h5>
        <div class="achievements">
            <div class="mini-card">
                <ul>
                    <li>Évaluation de contrats d'assurance-vie en utilisant des modèles stochastiques de taux d'intérêt et de mortalité.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="card">
        <h5>Janvier 2023 : Modélisation Sinistres en assurance automobile</h5>
        <div class="achievements">
            <div class="mini-card">
                <ul>
                    <li>Modélisation de la fréquence de sinistre d'un portefeuille automobile en utilisant les techniques avancées de machine learning.</li>
                </ul>
            </div>
        </div>
    </div>

.. raw:: html

    <div class="section">Projets en Cours</div>
    <div class="card">
        <div class="achievements">
            <div class="mini-card">
            <p class="card-textt typing-slow delay-3">Explorez mes projets réalisés et en cours.</p>
            <p class="card-text"></p>
            <a href="projects.html" class="btn btn-primary">Voir mes projets</a>
            </div>
        </div>
    </div>

.. raw:: html

    <div class="footer-message">
    <label for="cv-select">CV:</label>
    <select id="cv-select" onchange="window.location.href = this.value;">
        <option value="">--</option>
        <option value="../_static/cv_fr.pdf">🇫🇷 Français</option>
        <option value="../_static/cv_en.pdf">🇬🇧 English</option>
    </select>
    </div>

