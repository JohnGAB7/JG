Bienvenue sur ma page personnelle
=================================

.. image:: _static/photo.png
   :width: 200px
   :align: right

Ici, vous découvrirez mon parcours académique et professionnel, mes compétences techniques, ainsi que mes projets passionnants dans le domaine des **sciences actuarielles**, des **statistiques**, et de la **programmation appliquée**.

Je suis passionné par la combinaison de la **programmation** et des **sciences actuarielles**. J'ai récemment terminé mon **Master en sciences actuarielles** à l'Université Libre de Bruxelles, où j'ai approfondi mes connaissances en modélisation, en gestion des risques, et en analyse de données.

Mon objectif est de fusionner les compétences en analyse de données et en programmation pour résoudre des problèmes complexes en actuariat, particulièrement dans les domaines de la **non-vie** et de la **modélisation financière**.

À propos de moi
---------------
Je suis un **Jeune Actuaire** passionné par l’analyse de données et la création de solutions innovantes dans le secteur de l’actuariat. Grâce à mes compétences en **R** et en **Python**, je suis capable de concevoir des modèles statistiques avancés et des outils de visualisation interactifs. Voici un résumé de mes compétences et technologies maîtrisées :

- **Data Science & Statistiques** : Connaissance en analyse de données avec Python (Pandas, NumPy, Scikit-learn) et R (ggplot2, Shiny).
- **Modélisation Actuarielle** : Prédiction des sinistres, tarification des risques, et modélisation de la solvabilité pour les assurances non-vie.
- **Machine Learning** : Développement de modèles prédictifs et d'algorithmes de classification et régression.
- **Automatisation et Reporting** : Utilisation de Power BI, Excel VBA, et Python pour automatiser les rapports et analyses.

Projets et Réalisations
------------------------
Voici quelques-uns de mes projets les plus significatifs dans le domaine des sciences actuarielles et des données :

- **Modélisation Actuarielle pour l'Assurance Non-Vie** : Développement d’un modèle prédictif pour évaluer les risques en assurance non-vie.
- **Analyse Prédictive des Risques Boursiers** : Création d'un modèle de prédiction des tendances boursières en utilisant des techniques de machine learning.
- **Dashboard Interactif avec R Shiny** : Un tableau de bord interactif pour visualiser les données financières et actuarielles.

Chaque projet présente une opportunité de démontrer mes capacités en programmation et en gestion des risques dans des scénarios réels.

Accédez à mes projets sur `GitHub <https://johngab7.github.io/Actu_Basics/>`_ pour voir le code source de ces applications et bien d'autres.

Liens vers mes autres ressources
--------------------------------
- `Mon profil GitHub <https://github.com/JohnGAB7>`_
- `Mon profil LinkedIn <https://www.linkedin.com/in/johngabary>`_
- `Applications R Shiny <https://johngab7.shinyapps.io/mle_convergence_in_r/>`_
- `Télécharger mon CV (PDF) <_static/CV_John_GABARY.pdf>`_

Contactez-moi
-------------
Pour toute question ou demande de collaboration, n'hésitez pas à me contacter via le formulaire ci-dessous :

.. raw:: html

    <style>
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
    </style>

    <form action="https://formspree.io/f/mldekjld" method="POST" class="contact-form">
        <label for="firstname">Prénom:</label><br>
        <input type="text" id="firstname" name="firstname" required><br>
        <label for="lastname">Nom:</label><br>
        <input type="text" id="lastname" name="lastname" required><br>
        <label for="email">Adresse Email:</label><br>
        <input type="email" id="email" name="email" required><br>
        <label for="phone">Téléphone:</label><br>
        <input type="tel" id="phone" name="phone" required><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" required></textarea><br>
        <button type="submit">Envoyer</button>
        <div class="hidden" id="success-message">
            <p>Votre message a été envoyé avec succès !</p>
        </div>
        <div class="hidden" id="error-message">
            <p>Une erreur s'est produite lors de l'envoi de votre message. Veuillez réessayer.</p>
        </div>
    </form>

.. raw:: html

    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const form = document.querySelector(".contact-form");
            const successMessage = document.getElementById("success-message");
            const errorMessage = document.getElementById("error-message");

            form.addEventListener("submit", function (event) {
                event.preventDefault();
                const formData = new FormData(form);

                fetch(form.action, {
                    method: form.method,
                    body: formData,
                    headers: {
                        'Accept': 'application/json'
                    }
                }).then(response => {
                    if (response.ok) {
                        form.reset();
                        successMessage.classList.remove("hidden");
                        errorMessage.classList.add("hidden");
                    } else {
                        successMessage.classList.add("hidden");
                        errorMessage.classList.remove("hidden");
                    }
                }).catch(error => {
                    successMessage.classList.add("hidden");
                    errorMessage.classList.remove("hidden");
                });
            });
        });
    </script>
