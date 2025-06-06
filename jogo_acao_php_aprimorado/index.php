<?php
session_start();
include 'config.php';
include 'game_logic.php';
?>

<!DOCTYPE html>
<html>
<head>
    <title>Jogo de Ação em PHP</title>
</head>
<body>
    <h1>Jogo de Ação</h1>
    <p>Fase: <?php echo $_SESSION['fase']; ?></p>
    <p>Vida: <?php echo $_SESSION['vida']; ?></p>
    <p>Pontos: <?php echo $_SESSION['pontos']; ?></p>
    
    <form method="post" action="next_phase.php">
        <button type="submit">Avançar para a próxima fase</button>
    </form>
</body>
</html>
