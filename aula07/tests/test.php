<?php
// tests/test.php

// Teste simples: checar se 2 + 2 é 4
$result = 2 + 2;
if ($result === 4) {
    echo "Teste passou: 2 + 2 é igual a 4\n";
    exit(0);
} else {
    echo "Teste falhou\n";
    exit(1);
}

