<?php
$f = fopen("/var/www/html/color.txt", "w");
fwrite($f, "c.off()");
fclose($f);
?>