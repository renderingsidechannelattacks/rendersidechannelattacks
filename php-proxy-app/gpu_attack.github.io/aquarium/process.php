<?php

    // $data=$_GET["data"];//from ajax
    // $data = isset($_POST['value']) ? $_POST['value'] : false;

    $json = file_get_contents('php://input');
    // Converts it into a PHP object
    $data = json_decode($json);

    echo $json;

    // echo $data->value;

    $str_arr = explode(",", $data->value);  
    echo 'filename: ' . $str_arr[0];

    $myfile = fopen("data/".$str_arr[0].".txt", "w") or die("Unable to open file!");
    fwrite($myfile, $data->value);
    fclose($myfile);


?>
