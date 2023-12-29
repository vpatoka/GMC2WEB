<?php

$fp = fopen('GMCdata/gmc.csv', 'a+');
fputcsv($fp, $_REQUEST);
fclose($fp);

file_put_contents("GMCdata/gmc.log", print_r($_REQUEST, true));
echo "OK.ERR0";

?>
