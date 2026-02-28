<?php
require_once 'Model/usuario.php';

class LoginController{
    
    private $model;
    
    public function __CONSTRUCT(){
        $this->model = new Usuario();
    }
    
    public function Index(){
        require_once 'View/login.php';
    }
    
    public function Iniciar(){
        // Validar Captcha de Imagen (sensible a mayúsculas o normalizado)
        if(!isset($_REQUEST['captcha_input']) || strtoupper($_REQUEST['captcha_input']) != $_SESSION['captcha_text']){
            header('Location: index.php?error=captcha');
            return;
        }

        $usuario = $this->model->Entrar($_REQUEST['usuario'], $_REQUEST['password']);

        
        if($usuario){
            $_SESSION['user_id'] = $usuario->idusuario;
            $_SESSION['username'] = $usuario->usuario;
            header('Location: index.php?c=Persona');
        } else {
            header('Location: index.php?error=1');
        }
    }

    public function Registro(){
        require_once 'View/usuario-registro.php';
    }

    public function GuardarRegistro(){
        // Validar Captcha de Imagen
        if(!isset($_REQUEST['captcha_input']) || strtoupper($_REQUEST['captcha_input']) != $_SESSION['captcha_text']){
            header('Location: index.php?c=Login&a=Registro&error=captcha');
            return;
        }

        $usuario = $_REQUEST['usuario'];

        $password = $_REQUEST['password'];
        $confirm = $_REQUEST['confirm_password'];

        if($password != $confirm){
            header('Location: index.php?c=Login&a=Registro&error=pass');
            return;
        }

        if($this->model->Registrar($usuario, $password)){
            header('Location: index.php?success=reg');
        } else {
            header('Location: index.php?c=Login&a=Registro&error=exist');
        }
    }

    
    public function Salir(){
        session_destroy();
        header('Location: index.php');
    }
}
?>

