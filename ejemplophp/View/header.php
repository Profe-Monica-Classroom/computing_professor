<!DOCTYPE html>
<html lang="es">
<head>
    <title>Ejemplo CRUD - PHP</title>
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
    <div id="topbar" class="d-flex align-items-center fixed-top" style="display: flex; align-items: center; justify-content: space-between; padding: 0 50px;">
        <div class="contact-info">
            <i class="glyphicon glyphicon-envelope"></i> <a href="mailto:mtahan@unexpo.edu.ve">mtahan@unexpo.edu.ve</a>
            <i class="glyphicon glyphicon-phone" style="margin-left: 15px;"></i> +58 xxx xxx xxxx
        </div>
        <div class="social-links">
            Ejemplo CRUD - PHP
        </div>
    </div>

    <!-- Navbar -->
    <nav class="navbar navbar-default" style="margin-top: 40px;">
        <div class="container">
            <div class="navbar-header">
                <a class="navbar-brand" href="?c=Persona">Registro de Personas</a>
            </div>
            
            <?php if(isset($_SESSION['username'])): ?>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#">Bienvenido, <strong><?php echo $_SESSION['username']; ?></strong></a></li>
                <li><a href="?c=Login&a=Salir" class="btn btn-danger navbar-btn" style="color:white; margin-left:15px; border-radius: 20px; padding: 5px 15px;">Salir</a></li>
            </ul>
            <?php endif; ?>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="hero" style="overflow: hidden; position: relative;">
        <img src="assets/img/hero-bg.png" alt="Banner" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1;">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(25, 119, 204, 0.6); z-index: 2;"></div>
        <div class="container" style="position: relative; z-index: 3;">
            <h1>Registro de Personas</h1>
            <p>Computación 1. UNEXPO - Núcleo Guarenas. Sección 37. Prof. Mónica Tahan</p>
        </div>
    </section>

    <div class="container main-content-area">
        <!-- Start Card Container -->
        <div class="clinic-card">