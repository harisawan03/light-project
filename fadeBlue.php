<?php
$f = fopen("/var/www/html/color.txt", "w");
fwrite($f, "fadeBlue()");
fclose($f);
?>