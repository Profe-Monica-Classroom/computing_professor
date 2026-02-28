<?php
class Persona //class that manage person data
{
	private $pdo;
    
    public $idpersona; //person id
    public $nombres; //person name
    public $cedula; //person id card
    public $fecha_nmto; //person birth date
    public $direccion; //person address
    public $email; //person email

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

	//method to list all persons
	public function Listar()
	{
		try
		{
			$result = array();

			$stm = $this->pdo->prepare("SELECT * FROM persona");
			$stm->execute();

			return $stm->fetchAll(PDO::FETCH_OBJ);
		}
		catch(Exception $e)
		{
			die($e->getMessage());
		}
	}

	//method to get a person by id
	public function getting($idpersona)
	{
		try 
		{
			//query to get a person by id
			$stm = $this->pdo
			          ->prepare("SELECT * FROM persona WHERE idpersona = ?");
			          

			$stm->execute(array($idpersona));
			return $stm->fetch(PDO::FETCH_OBJ);
		} catch (Exception $e) 
		{
			die($e->getMessage());
		}
	}

	public function Eliminar($idpersona)
	{
		try 
		{
			//query to delete a person
			$stm = $this->pdo
			            ->prepare("DELETE FROM persona WHERE idpersona = ?");			          

			$stm->execute(array($idpersona));
		} catch (Exception $e) 
		{
			die($e->getMessage());
		}
	}

	//method to update a person
	public function Actualizar($data)
	{
		try 
		{
			//query to update a person
			$sql = "UPDATE persona SET 
						nombres          = ?, 
						cedula        = ?,
                        fecha_nmto        = ?,
						direccion            = ?, 
						email = ?
				    WHERE idpersona = ?";

			$this->pdo->prepare($sql)
			     ->execute(
				    array(
                        $data->nombres, 
                        $data->cedula,
                        $data->fecha_nmto,
                        $data->direccion,
                        $data->email,
                        $data->idpersona
					)
				);
		} catch (Exception $e) 
		{
			die($e->getMessage());
		}
	}
	//method to register a new person	
	public function Registrar($data)
	{
		try 
		{
			//query to register a new person
		$sql = "INSERT INTO `persona` (nombres,cedula,fecha_nmto,direccion,email) 
		        VALUES (?, ?, ?, ?, ?)";

		$this->pdo->prepare($sql)
		     ->execute(
				array(
                    $data->nombres, 
                    $data->cedula,
                    $data->fecha_nmto,
                    $data->direccion,
                    $data->email                    
                )
			);
		} catch (Exception $e) 
		{
			die($e->getMessage());
		}
	}
}
?>
