Contactez-moi 📞
--------------------------

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

        /* Animation styles */
        .animated {
            animation-duration: 60s;
            animation-fill-mode: both;
        }

        .fadeInUp {
            animation-name: fadeInUp;
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
    </style>

    <form action="https://formspree.io/f/mldekjld" method="POST" class="contact-form animated fadeInUp">
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

            function reveal() {
                var reveals = document.querySelectorAll(".animated");
                for (var i = 0; i < reveals.length; i++) {
                    var windowHeight = window.innerHeight;
                    var elementTop = reveals[i].getBoundingClientRect().top;
                    var elementVisible = 150;
                    if (elementTop < windowHeight - elementVisible) {
                        reveals[i].classList.add("active");
                    } else {
                        reveals[i].classList.remove("active");
                    }
                }
            }

            window.addEventListener("scroll", reveal);
            reveal(); // To check the scroll position on page load
        });
    </script>

Retour d'expérience et Contributions
------------------------------------
Si vous avez des suggestions ou souhaitez contribuer à ce site, vous pouvez créer une pull request ou ouvrir une issue sur `GitHub <https://johngab7.github.io/Actu_Basics/>`_.

Merci de votre visite !
