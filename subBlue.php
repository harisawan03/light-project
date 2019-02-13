<?php
$f = fopen("/var/www/html/color.txt", "w");
fwrite($f, "c.subBlue()");
fclose($f);
?>