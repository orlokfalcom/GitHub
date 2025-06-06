<?php
session_start();
include '../config/config.php';
include '../database/db.php';
include '../game/game_logic.php';

if (!isset($_SESSION['jogador'])) {
    header("Location: register.php");
    exit();
}

$jogador = $_SESSION['jogador'];
?>

<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jogo de Ação em PHP</title>
    <link rel="stylesheet" href="../assets/styles.css">
</head>
<body>
    <div class="game-container">
        <h1>Jogo de Ação</h1>
        <p>Jogador: <strong><?php echo htmlspecialchars($jogador); ?></strong></p>
        <p>Fase: <span class="fase"><?php echo $_SESSION['fase']; ?></span></p>
        <p>Vida: <span class="vida"><?php echo $_SESSION['vida']; ?></span></p>
        <p>Pontos: <span class="pontos"><?php echo $_SESSION['pontos']; ?></span></p>
        
        <form method="post" action="next_phase.php">
            <button type="submit" class="btn">Avançar para a próxima fase</button>
        </form>
    </div>
</body>
</html>
