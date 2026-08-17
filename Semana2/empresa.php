<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PokeLeo TCG - Empresa</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

    <!-- Menú -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand fw-bold text-warning" href="index.php">PokeLeo TCG</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="index.php">Inicio</a></li>
                    <li class="nav-item"><a class="nav-link active" href="empresa.php">Empresa</a></li>
                    <li class="nav-item"><a class="nav-link" href="productos.php">Productos</a></li>
                    <li class="nav-item"><a class="nav-link" href="servicios.php">Servicios</a></li>
                    <li class="nav-item"><a class="nav-link" href="contacto.php">Contacto</a></li>
                    <li class="nav-item">
                        <button class="btn btn-outline-warning ms-2" data-bs-toggle="modal" data-bs-target="#loginModal">Iniciar Sesión</button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Contenido Empresa -->
    <div class="container my-5">
        <div class="row align-items-center">
            <div class="col-md-6">
                <h1 class="fw-bold mb-4">¿Quiénes Somos?</h1>
                <p class="lead">En <strong>PokeLeo TCG</strong> somos apasionados del juego de cartas coleccionables de Pokémon. Nacimos con la misión de acercar las mejores cartas y rarezas tanto a jugadores competitivos como a coleccionistas.</p>
                <p>Nos esforzamos por mantener un catálogo actualizado, ofreciendo piezas icónicas, atención personalizada y un espacio seguro para todos los fanáticos del universo Pokémon.</p>
            </div>
            <div class="col-md-6">
                <img src="banner.jpg" class="img-fluid rounded shadow" alt="PokeLeo TCG Negocio">
            </div>
        </div>
    </div>

    <!-- Modal de Inicio de Sesión -->
    <div class="modal fade" id="loginModal" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Acceso a PokeLeo TCG</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <form>
                        <div class="mb-3">
                            <label class="form-label">Correo Electrónico</label>
                            <input type="email" class="form-control" placeholder="tu@correo.com">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Contraseña</label>
                            <input type="password" class="form-control" placeholder="Contraseña">
                        </div>
                        <button type="submit" class="btn btn-warning w-100">Ingresar</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <footer class="bg-dark text-white text-center py-3 mt-auto">
        <p class="mb-0">&copy; 2026 PokeLeo TCG. Todos los derechos reservados.</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>