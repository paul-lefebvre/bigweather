<?php
$mysqli = new mysqli("localhost", "root", "", "bigweather");

/* Vérification de la connexion */
if ($mysqli->connect_errno) {
    printf("Échec de la connexion : %s\n", $mysqli->connect_error);
    exit();
}
       

?>