<?php
$f = fopen("/var/www/html/color.txt", "w");
fwrite($f, "color()");
fclose($f);
?>