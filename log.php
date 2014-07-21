<?php
$data = 
	time() . "\t" .
	$_SERVER['REMOTE_ADDR'] . "\t" .
	$_GET['href'] . "\n";
file_put_contents('.log', $data, FILE_APPEND | LOCK_EX);
?>