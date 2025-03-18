<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST" && !empty($_POST["nome"])) {
    $_SESSION['jogador'] = $_POST["nome"];
    header("Location: index.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro do Jogador</title>
    <link rel="stylesheet" href="../assets/styles.css">
</head>
<body>
    <div class="register-container">
        <h1>Digite seu nome para jogar</h1>
        <form method="post">
            <input type="text" name="nome" required placeholder="Nome do jogador">
            <button type="submit" class="btn">Começar Jogo</button>
        </form>
    </div>
</body>
</html>
