<?php
header('Content-Type: text/html;charset=UTF-8');

$ear= $_POST['num1'];
$lhand = $_POST['num2'];  
$rhand = $_POST['num3'];
$mouth = $_POST['num4'];   
echo $ear."<br>"; 
echo $lhand . "<br>";
echo $rhand . "<br>";
echo $mouth . "<br>";
echo "以傳送";

$link=mysql_connect("localhost","root","abc123") or die("連接失敗");
mysql_select_db("webdata",$link);

mysql_query("ALTER TABLE  `value` CHANGE  `ear`  `ear` INT( 11 ) NOT NULL DEFAULT  '$ear'");
mysql_query("ALTER TABLE  `value` CHANGE  `lhand`  `lhand` INT( 11 ) NOT NULL DEFAULT  '$lhand'");
mysql_query("ALTER TABLE  `value` CHANGE  `rhand`  `rhand` INT( 11 ) NOT NULL DEFAULT  '$rhand'");
mysql_query("ALTER TABLE  `value` CHANGE  `mouth`  `mouth` INT( 11 ) NOT NULL DEFAULT  '$mouth'");

echo "資料寫入成功";
?>
