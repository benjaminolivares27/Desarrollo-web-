document.addEventListener("DOMContentLoaded", () => {
    // Ejemplo de consumo del API Gateway
    fetch("http://localhost:8000/api/clientes")
        .then(response => response.json())
        .then(data => {
            const lista = document.getElementById("listaClientes");
            if (lista && Array.isArray(data)) {
                data.forEach(cliente => {
                    const item = document.createElement("li");
                    item.className = "list-group-item";
                    item.textContent = `${cliente.nombre} - ${cliente.correo}`;
                    lista.appendChild(item);
                });
            }
        })
        .catch(error => console.error("Error al conectar con el Gateway:", error));
});