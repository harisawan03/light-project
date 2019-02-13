<?php
$f = fopen("/var/www/html/color.txt", "w");
fwrite($f, "c.subGreen()");
fclose($f);
?>