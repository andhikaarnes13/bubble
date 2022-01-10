<?php
$angka1=$_POST['angka1'];
$angka2=$_POST['angka2'];
$angka3=$_POST['angka3'];
$angka4=$_POST['angka4'];

$numbers = array($angka1, $angka2, $angka3, $angka4);
sort($numbers);

$arrlength = count($numbers);
for($x = 0; $x < $arrlength; $x++) {
    echo $numbers[$x];
  echo "<br>";
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <a href="../dsc/">mau ke dsc?</a>
  <a href="index.php">kembali</a>
</body>
</html>