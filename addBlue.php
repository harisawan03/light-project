<?php
$f = fopen("/var/www/html/color.txt", "w");
fwrite($f, "c.addBlue()");
fclose($f);
?>