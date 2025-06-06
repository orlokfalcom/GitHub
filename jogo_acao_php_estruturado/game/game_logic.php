<?php
include '../config/config.php';
include '../database/db.php';

if ($_SESSION['fase'] <= 5) {
    $_SESSION['vida'] -= $fases[$_SESSION['fase']]['dano'];
    $_SESSION['pontos'] += $fases[$_SESSION['fase']]['recompensa'];

    if ($_SESSION['vida'] > 0) {
        $_SESSION['fase']++;
    } else {
        echo "<h2>Game Over! Você perdeu todas as vidas.</h2>";
        session_destroy();
        exit();
    }
} else {
    echo "<h2>Parabéns! Você completou todas as fases!</h2>";
    session_destroy();
    exit();
}
?>
