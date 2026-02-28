<?php
session_start();
ob_clean();

// Generar código aleatorio de 5 caracteres
$caracteres = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; // Evitamos O, 0, I, 1
$captcha_text = '';
for ($i = 0; $i < 5; $i++) {
    $captcha_text .= $caracteres[rand(0, strlen($caracteres) - 1)];
}

// Guardar en sesión para validar después
$_SESSION['captcha_text'] = $captcha_text;

// Crear la imagen
$width = 150;
$height = 50;
$image = imagecreatetruecolor($width, $height);

// Colores
$bg = imagecolorallocate($image, 255, 255, 255); // Blanco
$text_color = imagecolorallocate($image, 25, 119, 204); // Azul primario
$noise_color = imagecolorallocate($image, 200, 200, 200); // Gris para ruido

imagefilledrectangle($image, 0, 0, $width, $height, $bg);

// Agregar ruido (puntos aleatorios)
for ($i = 0; $i < 100; $i++) {
    imagesetpixel($image, rand(0, $width), rand(0, $height), $noise_color);
}

// Agregar lineas de interferencia
for ($i = 0; $i < 5; $i++) {
    imageline($image, 0, rand(0, $height), $width, rand(0, $height), $noise_color);
}

// Escribir el texto (usando fuentes internas de PHP para evitar dependencias de archivos .ttf externos)
// imagestring(imagen, fuente(1-5), x, y, texto, color)
$font_size = 5;
$x = 40;
$y = 15;
imagestring($image, $font_size, $x, $y, $captcha_text, $text_color);

// Enviar cabeceras y salida
header('Content-type: image/png');
imagepng($image);
imagedestroy($image);
?>
