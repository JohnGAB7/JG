Contactez-moi 📞
====================

.. raw:: html

    <div class="jumbotron">
        <p>Pour toute question ou demande de collaboration, n'hésitez pas à me contacter via le formulaire ci-dessous :</p>
    </div>

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

        .contact-form input::placeholder,
        .contact-form textarea::placeholder {
            color: #999;
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
            animation-duration: 1s;
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

        .footer-message {
            text-align: center;
            margin-top: 50px;
            font-size: 1.2em;
            color: #555;
        }
    </style>

    <form action="https://formspree.io/f/mldekjld" method="POST" class="contact-form animated fadeInUp">
        <label for="firstname">Prénom:</label><br>
        <input type="text" id="firstname" name="firstname" placeholder="John" required><br>
        <label for="lastname">Nom:</label><br>
        <input type="text" id="lastname" name="lastname" placeholder="Doe" required><br>
        <label for="email">Adresse Email:</label><br>
        <input type="email" id="email" name="email" placeholder="john.doe@example.com" required><br>
        <label for="phone">Téléphone:</label><br>
        <input type="tel" id="phone" name="phone" placeholder="+33 6 12 34 56 78" required><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" placeholder="Votre message ici..." required></textarea><br>
        <button type="submit">Envoyer</button>
        <div class="hidden" id="success-message">
            <p>Votre message a été envoyé avec succès !</p>
        </div>
        <div class="hidden" id="error-message">
            <p>Une erreur s'est produite lors de l'envoi de votre message. Veuillez réessayer.</p>
        </div>
        <small id="emailHelp" class="form-text text-muted">Nous ne partagerons jamais votre email avec quelqu'un d'autre.</small>
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

.. raw:: html

    <div class="footer-message">
        Merci de votre visite !
    </div>