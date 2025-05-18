.. _contact-index:

Contact
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
        }

        .contact-form {
            max-width: 600px;
            margin: auto;
            padding: 2rem;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            animation: fadeInUp 1s ease-in-out;
        }

        .contact-form label {
            display: block;
            margin: 1rem 0 0.3rem;
            font-weight: 600;
            color: #333;
        }

        .contact-form input,
        .contact-form textarea {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 1rem;
            resize: vertical;
        }

        .contact-form input:focus,
        .contact-form textarea:focus {
            outline: none;
            border-color: #4ca1af;
            box-shadow: 0 0 5px rgba(76, 161, 175, 0.5);
        }

        .contact-form button {
            margin-top: 1.5rem;
            background-color: #4ca1af;
            border: none;
            color: white;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .contact-form button:hover {
            background-color: #3b8a9e;
        }

        .form-feedback {
            margin-top: 1rem;
            display: none;
            font-size: 0.95rem;
            text-align: center;
        }

        .form-feedback.success {
            color: #28a745;
        }

        .form-feedback.error {
            color: #dc3545;
        }

        .footer-message {
            text-align: center;
            margin-top: 3rem;
            font-size: 1.2rem;
            color: #555;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>

    <div class="jumbotron">
        <p>Pour toute question ou demande de collaboration, n'hésitez pas à me contacter via le formulaire ci-dessous :</p>
    </div>

    <form action="https://formspree.io/f/mldekjld" method="POST" class="contact-form" aria-label="Formulaire de contact">
        <label for="firstname">Prénom</label>
        <input type="text" id="firstname" name="firstname" placeholder="John" required>

        <label for="lastname">Nom</label>
        <input type="text" id="lastname" name="lastname" placeholder="Doe" required>

        <label for="email">Adresse email</label>
        <input type="email" id="email" name="email" placeholder="john.doe@example.com" required>

        <label for="phone">Téléphone</label>
        <input type="tel" id="phone" name="phone" placeholder="+33 6 12 34 56 78" required>

        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" placeholder="Votre message ici..." required></textarea>

        <button type="submit">Envoyer</button>

        <div id="success-message" class="form-feedback success">Votre message a été envoyé avec succès !</div>
        <div id="error-message" class="form-feedback error">Une erreur est survenue. Veuillez réessayer.</div>

        <small class="form-text text-muted" style="display:block; margin-top:1rem; text-align:center;">
            Vos informations resteront strictement confidentielles.
        </small>
    </form>

.. raw:: html

    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const form = document.querySelector(".contact-form");
            const successMessage = document.getElementById("success-message");
            const errorMessage = document.getElementById("error-message");

            form.addEventListener("submit", function (event) {
                event.preventDefault();
                successMessage.style.display = "none";
                errorMessage.style.display = "none";

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
                        successMessage.style.display = "block";
                    } else {
                        errorMessage.style.display = "block";
                    }
                }).catch(() => {
                    errorMessage.style.display = "block";
                });
            });
        });
    </script>



.. raw:: html

    <!-- Ajouter dans le fichier HTML (ou bloc raw dans Sphinx) -->
    <div class="likebtn-wrapper" data-theme="custom" data-ef="bounce" data-lang="fr" data-identifier="page_contact"></div>
    <script src="https://w.likebtn.com/js/w/widget.js" async></script>
    <!-- LikeBtn.com BEGIN -->
    <span class="likebtn-wrapper" data-identifier="item_1"></span>
    <script>(function(d,e,s){if(d.getElementById("likebtn_wjs"))return;a=d.createElement(e);m=d.getElementsByTagName(e)[0];a.async=1;a.id="likebtn_wjs";a.src=s;m.parentNode.insertBefore(a, m)})(document,"script","//w.likebtn.com/js/w/widget.js");</script>
    <!-- LikeBtn.com END -->

    <div class="footer-message">
        Merci de votre visite !
    </div>
