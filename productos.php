<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PokeLeo TCG - Productos</title>
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
                    <li class="nav-item"><a class="nav-link active" href="productos.php">Productos</a></li>
                    <li class="nav-item"><a class="nav-link" href="servicios.php">Servicios</a></li>
                    <li class="nav-item"><a class="nav-link" href="contacto.php">Contacto</a></li>
                    <li class="nav-item">
                        <button class="btn btn-outline-warning ms-2" data-bs-toggle="modal" data-bs-target="#loginModal">Iniciar Sesión</button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Catálogo de Productos -->
    <div class="container my-5">
        <h1 class="text-center fw-bold mb-4">Cartas Destacadas en Stock</h1>
        <p class="text-center text-muted mb-5">Explora nuestras cartas disponibles con alta rareza.</p>

        <div class="row">
            <!-- Producto 1: Mew ex -->
            <div class="col-md-3 mb-4">
                <div class="card h-100 shadow-sm">
                    <img src="534919_in_1000x1000.jpg" class="card-img-top p-2" alt="Mew ex" style="height: 320px; object-fit: contain;">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">Mew ex</h5>
                        <p class="card-text text-muted">Carta Pokémon EX - Edición Especial.</p>
                        <span class="fw-bold text-success mb-3">$14.990</span>
                        <button class="btn btn-dark mt-auto">Comprar</button>
                    </div>
                </div>
            </div>

            <!-- Producto 2: Pikachu VMAX -->
            <div class="col-md-3 mb-4">
                <div class="card h-100 shadow-sm">
                    <img src="SWSHP_LA_SWSH062.png" class="card-img-top p-2" alt="Pikachu VMAX" style="height: 320px; object-fit: contain;">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">Pikachu VMAX</h5>
                        <p class="card-text text-muted">Gigamax - Edición Aniversario.</p>
                        <span class="fw-bold text-success mb-3">$24.990</span>
                        <button class="btn btn-dark mt-auto">Comprar</button>
                    </div>
                </div>
            </div>

            <!-- Producto 3: Espeon V -->
            <div class="col-md-3 mb-4">
                <div class="card h-100 shadow-sm">
                    <img src="246689_in_1000x1000.jpg" class="card-img-top p-2" alt="Espeon V" style="height: 320px; object-fit: contain;">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">Espeon V</h5>
                        <p class="card-text text-muted">Full Art Alternate Art - Biblioteca.</p>
                        <span class="fw-bold text-success mb-3">$32.990</span>
                        <button class="btn btn-dark mt-auto">Comprar</button>
                    </div>
                </div>
            </div>

            <!-- Producto 4: Gengar VMAX -->
            <div class="col-md-3 mb-4">
                <div class="card h-100 shadow-sm">
                    <img src="271_hires.png" class="card-img-top p-2" alt="Gengar VMAX" style="height: 320px; object-fit: contain;">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">Gengar VMAX</h5>
                        <p class="card-text text-muted">Gigantamax Alternate Art - Colección.</p>
                        <span class="fw-bold text-success mb-3">$45.990</span>
                        <button class="btn btn-dark mt-auto">Comprar</button>
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