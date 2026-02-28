<?php
class Conexion //class that manage database connection
{
    public static function StartUp() //method to start database connection
    {   
        //query to start database connection
        $pdo = new PDO('mysql:host=localhost;dbname=computacion1;charset=utf8', 'root', '1234');
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);	
        return $pdo;
    }
}
?>
