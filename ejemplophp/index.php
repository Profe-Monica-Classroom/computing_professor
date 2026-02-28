<?php
// Iniciamos la sesión para poder verificar usuarios
session_start();

require_once 'Model/conexion.php';

// Controlador por defecto es Login si no hay usuario logueado
if(!isset($_SESSION['user_id'])){
    $controller = 'login';
    
    // Si intentan acceder a otro controlador sin login, forzamos login
    if(isset($_REQUEST['c']) && strtolower($_REQUEST['c']) != 'login'){
         require_once "Controller/$controller.controller.php";
         $controller = ucwords($controller) . 'Controller';
         $controller = new $controller;
         $controller->Index();
         exit;
    }
} else {
    // Si ya está logueado, por defecto es Persona
    $controller = 'persona';
}

// Todo esta lógica es para el FrontController
if(!isset($_REQUEST['c']))
{
    require_once "Controller/$controller.controller.php";
    $controller = ucwords($controller) . 'Controller';
    $controller = new $controller;
    $controller->Index();    
}
else
{
    // Obtenemos el controlador a cargar
    $controller = strtolower($_REQUEST['c']);
    $accion = isset($_REQUEST['a']) ? $_REQUEST['a'] : 'Index';
    
    // Instanciamos el controlador
    require_once "Controller/$controller.controller.php";
    $controller = ucwords($controller) . 'Controller';
    $controller = new $controller;
    
    // Llama la accion
    call_user_func( array( $controller, $accion ) );
}
?>
