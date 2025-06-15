.. _contact-index:

Contact
=========

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
            color: #DDFCF8;
            text-align: center;
            padding: 2.5rem 2rem;
            border-radius: 20px;
            margin-bottom: 2.5rem;
            box-shadow: 0 6px 16px rgba(0,0,0,0.25);
        }

        .contact-form {
            max-width: 600px;
            margin: auto;
            padding: 2rem;
            background-color: #10333F;
            border-radius: 15px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
            color: #DDFCF8;
            border-left: 6px solid #2DB6A0;
        }

        .contact-form label {
            display: block;
            margin: 1rem 0 0.3rem;
            font-weight: bold;
            color: #62F2C5;
        }

        .contact-form input,
        .contact-form textarea {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #2DB6A0;
            border-radius: 6px;
            font-size: 1rem;
            background-color: #0F2B36;
            color: #DDFCF8;
        }

        .contact-form input:focus,
        .contact-form textarea:focus {
            outline: none;
            border-color: #62F2C5;
            box-shadow: 0 0 6px rgba(98, 242, 197, 0.5);
        }

        .contact-form button {
            margin-top: 1.5rem;
            background-color: #2DB6A0;
            border: none;
            color: #0F2B36;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .contact-form button:hover {
            background-color: #62F2C5;
        }

        .form-feedback {
            margin-top: 1rem;
            display: none;
            font-size: 1rem;
            text-align: center;
        }

        .form-feedback.success {
            color: #62F2C5;
        }

        .form-feedback.error {
            color: #ff4d4f;
        }

        .footer-message {
            text-align: center;
            margin-top: 3rem;
            font-size: 1.1rem;
            color: #DDFCF8;
            padding-bottom: 80px;
        }
    </style>

    <div class="jumbotron">
        <p style="font-size: 1.25rem;">📬 If you have any questions, ideas, or collaboration proposals, feel free to reach out below:</p>
    </div>

    <form action="https://formspree.io/f/mldekjld" method="POST" class="contact-form" aria-label="Contact Form">
        <label for="firstname">First Name</label>
        <input type="text" id="firstname" name="firstname" placeholder="John" required>

        <label for="lastname">Last Name</label>
        <input type="text" id="lastname" name="lastname" placeholder="Doe" required>

        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="john.doe@example.com" required>

        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="+32 465 000 000" required>

        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" placeholder="Your message here..." required></textarea>

        <button type="submit">Send</button>

        <div id="success-message" class="form-feedback success">✅ Your message has been sent successfully!</div>
        <div id="error-message" class="form-feedback error">❌ An error occurred. Please try again.</div>

        <small style="display:block; margin-top:1rem; text-align:center; color:#DDFCF8;">
            🔒 Your information will remain strictly confidential.
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

    <div class="likebtn-wrapper" data-theme="custom" data-ef="bounce" data-lang="en" data-identifier="page_contact"></div>
    <script src="https://w.likebtn.com/js/w/widget.js" async></script>
    <div class="footer-message">
        Thank you for visiting! Feel free to connect anytime.
    </div>
