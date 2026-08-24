// Simulación de respuesta API de inventario TCG
const apiInventario = { 
  "status": 200, 
  "message" : "Productos obtenidos correctamente", 
  "data": [ 
    { "id": 1, "nombre": "Protector de Cartas", "precio": 3500 }, 
    { "id": 2, "nombre": "Deck Box Oficial", "precio": 8900 } 
  ] 
};

// Recorrido de arreglo con foreach y función flecha
apiInventario.data.forEach((item) => { 
  console.log(`${item.nombre} - $${item.precio}`); 
});

// Pruebas de tipos de datos en memoria (Null y Objetos)
let datoNulo = null; 
console.log(typeof(datoNulo)); 
datoNulo = { "tienda": "PokeLeo TCG"}; 
console.log(typeof(datoNulo.tienda)); 

// Pruebas de NaN (Not a Number) e Infinity
let valorMatematico = NaN; 
console.log(typeof(valorMatematico)); 
valorMatematico = 1/0; 
console.log(typeof(valorMatematico)); 
console.log(valorMatematico); 
valorMatematico = 1/datoNulo; 
console.log(typeof(valorMatematico)); 
console.log(valorMatematico); 

// Pruebas de Undefined e instancias
let variableVacia; 
console.log(typeof(variableVacia)); 
console.log(variableVacia instanceof Object);
console.log(null instanceof Object); 

// Captura segura de errores con bloque try-catch
try { 
  valorMatematico = valorMatematico + variableInexistente; 
} catch (errorGenerado) { 
  console.log(`Error ${errorGenerado}`); 
}