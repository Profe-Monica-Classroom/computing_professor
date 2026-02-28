<?php require_once 'View/header.php'; ?>

<div class="container" style="background: white; padding: 40px; border-radius: 10px; margin-top: -50px; position: relative; z-index: 10; box-shadow: 0 5px 25px rgba(0,0,0,0.1);">
    <div class="row">
        <div class="col-md-6 col-md-offset-3">
            <div class="text-center" style="margin-bottom: 30px;">
                <h2 style="color: var(--primary); font-weight: 700;">Iniciar Sesión</h2>
                <p style="color: #777;">Accede al sistema con tus credenciales</p>
            </div>

            <?php if(isset($_REQUEST['error'])): ?>
                <div class="alert alert-danger" style="font-size: 14px; border-radius: 5px;">
                    <?php 
                        if($_REQUEST['error'] == 'captcha') echo "CAPTCHA incorrecto. Inténtalo de nuevo.";
                        else echo "Usuario o contraseña incorrectos";
                    ?>
                </div>
            <?php endif; ?>

            <?php if(isset($_REQUEST['success'])): ?>
                <div class="alert alert-success" style="font-size: 14px; border-radius: 5px;">
                    Registro exitoso. Ya puedes entrar.
                </div>
            <?php endif; ?>

            <form action="?c=Login&a=Iniciar" method="post">
                <div class="form-group" style="margin-bottom: 20px;">
                    <label style="color: var(--text-dark);">Usuario</label>
                    <input type="text" name="usuario" class="form-control" placeholder="Nombre de usuario" required />
                </div>
                <div class="form-group" style="margin-bottom: 25px;">
                    <label style="color: var(--text-dark);">Contraseña</label>
                    <input type="password" name="password" class="form-control" placeholder="Clave de acceso" required />
                </div>

                <!-- CAPTCHA de Imagen Moderno -->
                <div class="form-group" style="margin-bottom: 25px; background: #f8f9fa; padding: 15px; border-radius: 8px; border: 1px solid #dee2e6;">
                    <label style="color: var(--primary); font-weight: 700; display: block; margin-bottom: 10px;">Código de Verificación</label>
                    <div class="text-center" style="margin-bottom: 15px;">
                        <!-- Forzamos recarga con un parámetro aleatorio para evitar cache -->
                        <img src="assets/captcha.php?r=<?php echo rand(); ?>" alt="Captcha" style="border-radius: 4px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); width: 100%; max-width: 150px;">
                        <br><small style="color: #777;">(Escribe el código de la imagen)</small>
                    </div>
                    <input type="text" name="captcha_input" class="form-control" placeholder="Escribe el código" required 
                           style="text-transform: uppercase; text-align: center; font-weight: 700; letter-spacing: 2px;"/>
                </div>
                
                <button type="submit" class="btn-clinic btn-block" style="width: 100%; height: 45px; font-size: 16px;">Entrar al Sistema</button>

                <p class="text-center" style="margin-top: 20px; font-size: 14px;">
                    ¿No tienes cuenta? <a href="?c=Login&a=Registro" style="color: var(--primary); font-weight: 600;">Regístrate aquí</a>
                </p>

                <p class="text-center" style="margin-top: 20px; font-size: 12px; color: #777;">
                    Indique aquí sus credenciales de acceso<br>
                    <strong>Nota: (admin/1234) para este demo.</strong><br>
                    <strong>UNEXPO - Computación 1. Sección 37</strong>
                </p>
            </form>
        </div>
    </div>
</div>

<?php require_once 'View/footer.php'; ?>

