<h1 class="page-header">
    <?php echo $alm->idpersona != null ? $alm->nombres : 'Nuevo Registro'; ?>
</h1>

<nav aria-label="breadcrumb">
  <ol class="breadcrumb" style="background: var(--bg-light); padding: 10px 15px;">
    <li><a href="?c=Persona" style="color: var(--primary);">Gestión</a></li>
    <li class="active" style="margin-left: 10px;"><?php echo $alm->idpersona != null ? $alm->nombres : 'Nueva Persona'; ?></li>
  </ol>
</nav>

<form action="?c=Persona&a=Guardar" method="post" enctype="multipart/form-data" id="frm-persona" style="max-width: 800px; margin: 30px 0;">
    <input type="hidden" name="idpersona" value="<?php echo $alm->idpersona; ?>" />
    
    <div class="row">
        <div class="col-md-12">
            <div class="form-group" style="margin-bottom: 20px;">
                <label style="font-weight: 600; color: var(--text-dark);">Nombre Completo</label>
                <input type="text" name="Nombres" value="<?php echo $alm->nombres; ?>" class="form-control" placeholder="Ingrese nombre y apellido" required />
            </div>
        </div>
    </div>
    
    <div class="row">
        <div class="col-md-6">
            <div class="form-group" style="margin-bottom: 20px;">
                <label style="font-weight: 600; color: var(--text-dark);">Cédula de Identidad</label>
                <input type="text" name="Cedula" value="<?php echo $alm->cedula; ?>" class="form-control" placeholder="V-0000000" required />
            </div>
        </div>
        <div class="col-md-6">
            <div class="form-group" style="margin-bottom: 20px;">
                <label style="font-weight: 600; color: var(--text-dark);">Fecha de Nacimiento</label>
                <input type="date" name="FechaNacimiento" value="<?php echo $alm->fecha_nmto; ?>" class="form-control" required />
            </div>
        </div>
    </div>
    
    <div class="form-group" style="margin-bottom: 20px;">
        <label style="font-weight: 600; color: var(--text-dark);">Dirección de Habitación</label>
        <textarea name="direccion" class="form-control" rows="2" placeholder="Dirección completa" required><?php echo $alm->direccion; ?></textarea>
    </div>
    
    <div class="form-group" style="margin-bottom: 20px;">
        <label style="font-weight: 600; color: var(--text-dark);">Correo Electrónico</label>
        <input type="email" name="correo" value="<?php echo $alm->email; ?>" class="form-control" placeholder="ejemplo@correo.com" required />
    </div>
    
    <hr style="border-top: 1px solid #d9e1ec; margin-top: 30px;" />
    
    <div class="text-right" style="display: flex; justify-content: flex-end; gap: 10px;">
        <a href="?c=Persona" class="btn btn-default" style="border-radius: 50px; padding: 10px 30px;">Cancelar</a>
        <button type="submit" class="btn-clinic">Guardar Registro</button>
    </div>
</form>

<script>
    $(document).ready(function(){
        $("#frm-persona").submit(function(){
            return $(this).validate();
        });
    })
</script>
