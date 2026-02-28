<?php
class Usuario //class tu manage system user
{
    private $pdo;
    
    public $idusuario; //system user id
    public $usuario; //system user name
    public $password; //system user password

    //constructor of class
    public function __CONSTRUCT()
    {
        try
        {
            $this->pdo = Conexion::StartUp();     
        }
        catch(Exception $e)
        {
            die($e->getMessage());
        }
    }

    //method to login
    public function Entrar($usuario, $password)
    {
        try 
        {
            //query to login
            $stm = $this->pdo
                      ->prepare("SELECT * FROM usuario WHERE usuario = ? AND password = ?");
                      

            $stm->execute(array($usuario, $password));
            
            return $stm->fetch(PDO::FETCH_OBJ);
        } catch (Exception $e) 
        {
            die($e->getMessage());
        }
    }

    public function Registrar($usuario, $password)
    {
        try 
        {
            //query to check if user exists
            $stmCheck = $this->pdo->prepare("SELECT idusuario FROM usuario WHERE usuario = ?");
            $stmCheck->execute(array($usuario));
            if($stmCheck->fetch()){
                return false; // User already exists
            }

            //query to register new user
            $sql = "INSERT INTO usuario (usuario, password) VALUES (?, ?)";
            $this->pdo->prepare($sql)->execute(array($usuario, $password));
            return true;
        } catch (Exception $e) 
        {
            die($e->getMessage());
        }
    }

}
?>
