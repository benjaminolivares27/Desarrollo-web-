<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PokeLeo TCG - Servicios</title>
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
                    <li class="nav-item"><a class="nav-link" href="empresa.php">Empresa</a></li>
                    <li class="nav-item"><a class="nav-link" href="productos.php">Productos</a></li>
                    <li class="nav-item"><a class="nav-link active" href="servicios.php">Servicios</a></li>
                    <li class="nav-item"><a class="nav-link" href="contacto.php">Contacto</a></li>
                    <li class="nav-item">
                        <button class="btn btn-outline-warning ms-2" data-bs-toggle="modal" data-bs-target="#loginModal">Iniciar Sesión</button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Contenido Servicios -->
    <div class="container my-5">
        <h1 class="text-center fw-bold mb-4">Nuestros Servicios</h1>
        <p class="text-center text-muted mb-5">Más allá de la venta de cartas, te ofrecemos soporte integral para tu hobby.</p>

        <div class="row">
            <div class="col-md-4 mb-4">
                <div class="card h-100 shadow-sm text-center p-3">
                    <div class="card-body">
                        <h3 class="card-title text-warning">Tasación y Evaluación</h3>
                        <p class="card-text">Revisamos el estado de tus cartas y te orientamos sobre su valor real de mercado actual.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card h-100 shadow-sm text-center p-3">
                    <div class="card-body">
                        <h3 class="card-title text-warning">Torneos y Ligas</h3>
                        <p class="card-text">Organizamos encuentros competitivos presenciales y online para probar tus mazos.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card h-100 shadow-sm text-center p-3">
                    <div class="card-body">
                        <h3 class="card-title text-warning">Asesoría de Mazos</h3>
                        <p class="card-text">Te ayudamos a optimizar tu baraja competitiva (Deckbuilding) para los torneos oficiales.</p>
                    </div>
                </div>
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

    <footer class="bg-dark text-white text-center py-3">
        <p class="mb-0">&copy; 2026 PokeLeo TCG. Todos los derechos reservados.</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>