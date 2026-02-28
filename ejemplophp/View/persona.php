<div class="d-flex justify-content-between align-items-center" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px;">
    <h1 class="page-header" style="margin: 0; padding-bottom: 10px;">Gestión de Personas (PHP)</h1>
    <a class="btn-clinic" href="?c=Persona&a=Crud" style="text-decoration: none;">+ Agregar Persona</a>
</div>

<div class="table-responsive">
    <table class="table table-hover">
        <thead>
            <tr>
                <th>Nombres y Apellidos</th>
                <th>Cédula</th>
                <th>F. Nacimiento</th>
                <th>Dirección</th>
                <th>Correo Electrónico</th>
                <th width="60"></th>
                <th width="60"></th>
            </tr>
        </thead>
        <tbody>
        <?php foreach($this->model->Listar() as $r): ?>
            <tr>
                <td><?php echo $r->nombres; ?></td>
                <td><?php echo $r->cedula; ?></td>
                <td><?php echo $r->fecha_nmto; ?></td>
                <td><?php echo $r->direccion; ?></td>
                <td><?php echo $r->email; ?></td>
                <td class="text-center">
                    <a href="?c=Persona&a=Crud&idpersona=<?php echo $r->idpersona; ?>" title="Editar" style="color: var(--primary);">
                        <i class="glyphicon glyphicon-pencil"></i>
                    </a>
                </td>
                <td class="text-center">
                    <a href="?c=Persona&a=Eliminar&idpersona=<?php echo $r->idpersona; ?>" title="Eliminar" style="color: #d9534f;" onclick="javascript:return confirm('¿Seguro de eliminar este registro?');">
                        <i class="glyphicon glyphicon-trash"></i>
                    </a>
                </td>
            </tr>
        <?php endforeach; ?>
        </tbody>
    </table> 
</div>
