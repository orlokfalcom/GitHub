<?php
session_start();

if (!isset($_SESSION['fase'])) {
    $_SESSION['fase'] = 1;
    $_SESSION['vida'] = 100;
    $_SESSION['pontos'] = 0;
}

$fases = [
    1 => ['inimigos' => 2, 'dano' => 10, 'recompensa' => 50],
    2 => ['inimigos' => 3, 'dano' => 15, 'recompensa' => 70],
    3 => ['inimigos' => 4, 'dano' => 20, 'recompensa' => 100],
    4 => ['inimigos' => 5, 'dano' => 25, 'recompensa' => 150],
    5 => ['inimigos' => 6, 'dano' => 30, 'recompensa' => 200]
];
?>
