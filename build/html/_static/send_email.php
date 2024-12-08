<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    $to = 'johngabary@gmail.com';
    $subject = 'Nouveau message de votre site personnel';
    $body = "Nom: $name\nEmail: $email\nMessage:\n$message";

    // Pour envoyer un email en utilisant PHP mail() function
    if (mail($to, $subject, $body)) {
        echo 'Votre message a été envoyé avec succès.';
    } else {
        echo 'Une erreur s\'est produite lors de l\'envoi de votre message. Veuillez réessayer.';
    }
} else {
    echo 'Méthode de requête non autorisée.';
}
?>
