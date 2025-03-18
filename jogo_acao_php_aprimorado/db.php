<?php
$host = 'localhost';
$user = 'root';
$password = '';
$dbname = 'jogo_acao';

$conn = new mysqli($host, $user, $password, $dbname);

if ($conn->connect_error) {
    die("Erro na conexão com o banco de dados: " . $conn->connect_error);
}
?>
