<!DOCTYPE html>
<html lang="es">
<head>
    <title>Clas-Med - PHP</title>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700" rel="stylesheet">

    <!-- Styles -->
    <link rel="stylesheet" href="assets/css/bootstrap.min.css" />
    <link rel="stylesheet" href="assets/js/jquery-ui/jquery-ui.min.css" />
    <link rel="stylesheet" href="assets/css/style.css" />
    
    <script src="http://code.jquery.com/jquery-1.11.2.min.js"></script>
</head>
<body>
    <!-- Top Bar -->
    <div id="topbar" class="d-flex align-items-center fixed-top" style="display: flex; align-items: center; justify-content: space-between; padding: 0 50px;">
        <div class="contact-info">
            <i class="glyphicon glyphicon-envelope"></i> <a href="mailto:contacto@unexpo.edu.ve">contacto@unexpo.edu.ve</a>
            <i class="glyphicon glyphicon-phone" style="margin-left: 15px;"></i> +58 212 555 1234
        </div>
        <div class="social-links">
            PHP Version - UNEXPO
        </div>
    </div>

    <div class="container" style="margin-top: 60px;">
        <!-- Navbar -->
        <nav class="navbar navbar-default">
            <div class="container-fluid">
                <div class="navbar-header">
                    <a class="navbar-brand" href="?c=Persona">Clas-Med</a>
                </div>
                
                <?php if(isset($_SESSION['username'])): ?>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">Bienvenido, <strong><?php echo $_SESSION['username']; ?></strong></a></li>
                    <li><a href="?c=Login&a=Salir" class="btn btn-danger navbar-btn" style="color:white; margin-left:15px; border-radius: 20px; padding: 5px 15px;">Salir</a></li>
                </ul>
                <?php endif; ?>
            </div>
        </nav>

        <!-- Start Card Container -->
        <div class="clinic-card">