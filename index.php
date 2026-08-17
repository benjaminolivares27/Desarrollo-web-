<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PokeLeo TCG - Inicio</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

    <!-- Menú de Navegación -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand fw-bold text-warning" href="index.php">PokeLeo TCG</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link active" href="index.php">Inicio</a></li>
                    <li class="nav-item"><a class="nav-link" href="empresa.php">Empresa</a></li>
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

    <!-- Carrusel / Banner Principal -->
    <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="banner.jpg" class="d-block w-100" alt="Banner PokeLeo TCG" style="height: 450px; object-fit: cover;">
                <div class="carousel-caption d-none d-md-block bg-dark bg-opacity-50 rounded p-3">
                    <h2>¡Bienvenido a PokeLeo TCG!</h2>
                    <p>Las mejores cartas coleccionables y competitivas del mercado.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Contenido Principal -->
    <div class="container my-5">
        <div class="text-center mb-5">
            <h1 class="fw-bold">Tu tienda de confianza para Pokémon TCG</h1>
            <p class="text-muted">Encuentra cartas sueltas, ediciones especiales y todo lo necesario para tu deck.</p>
        </div>
        <div class="row text-center">
            <div class="col-md-4 mb-4">
                <div class="card h-100 shadow-sm">
                    <div class="card-body">
                        <h3 class="card-title text-danger">Cartas Originales</h3>
                        <p class="card-text">Garantizamos 100% de autenticidad en cada una de nuestras piezas de colección.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card h-100 shadow-sm">
                    <div class="card-body">
                        <h3 class="card-title text-primary">Envíos Rápidos</h3>
                        <p class="card-text">Despachamos de forma segura para que tus cartas lleguen en perfecto estado.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card h-100 shadow-sm">
                    <div class="card-body">
                        <h3 class="card-title text-success">Comunidad</h3>
                        <p class="card-text">Asesoramiento personalizado para jugadores competitivos y coleccionistas.</p>
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

    <!-- Pie de página -->
    <footer class="bg-dark text-white text-center py-3">
        <p class="mb-0">&copy; 2026 PokeLeo TCG. Todos los derechos reservados.</p>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>