<?php
$lifo = new \SplDoublyLinkedList();
$lifo->setIteratorMode(SplDoublyLinkedList::IT_MODE_LIFO);

$lifo->push("laranja");
$lifo->push("banana");
$lifo->push("limão");
$lifo->push("maça");
$lifo->push("uva");
$lifo->push("abacaxi");

foreach ($lifo as $value) {
    echo "$value\n";
}
?>