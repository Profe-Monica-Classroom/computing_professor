<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
    <h3 style="margin: 0; color: var(--primary); font-weight: 700;">Listado de Personas</h3>
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
