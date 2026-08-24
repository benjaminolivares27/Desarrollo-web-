// --- PARTE 1: Manipulación del DOM en el Navegador ---

// Creación dinámica de un elemento de texto e inserción en el body
let inputDinamico = document.createElement("input"); 
inputDinamico.setAttribute("type","text"); 
inputDinamico.setAttribute("value", "PokeLeo TCG"); 
document.body.innerHTML = ""; 
document.body.appendChild(inputDinamico);

// Simulación de respuesta de API local
const payloadAPI = { 
  "status": 200, 
  "message": "Productos Obtenidos", 
  "data": [{"id":"1","nombre":"Mew ex"},{"id":"2","nombre":"Pikachu VMAX"}] 
};

// Creación dinámica de un combo selector (select) y sus opciones (option)
let selectDinamico = document.createElement("select"); 
selectDinamico.setAttribute("name","selectDinamico"); 

payloadAPI.data.forEach((elem) => { 
  let optNode = document.createElement("option"); 
  optNode.setAttribute("value", elem.id); 
  optNode.innerText = elem.nombre; 
  selectDinamico.appendChild(optNode); 
}); 

document.body.appendChild(selectDinamico);


// --- PARTE 2: Operaciones con Objetos y Propagación (Spread Operator) ---

const configObjeto = { propiedad1 : 1, propiedad2 : 2}; 
delete configObjeto.propiedad1; // Eliminar propiedad de forma directa
console.log(configObjeto); 

// Desempaquetado y ordenamiento usando el operador de propagación (...)
const objetoActualizado = { propiedad1: 3, ...configObjeto}; 
console.log(objetoActualizado); 

const metaData = { "tipo":"TCG"}; 

// Fusión de objetos usando Object.assign
const fusionObjetos = Object.assign({}, objetoActualizado, metaData); 
console.log(fusionObjetos); 

// Composición real de objetos jerárquicos
const objetoJerarquico = {objetoActualizado, metaData}; 
console.log(objetoJerarquico); 
console.log(objetoJerarquico.metaData); 

// Recorridos de propiedades usando for...in
for(let llave in objetoJerarquico){ 
  console.log(llave); 
} 

// Recorridos estructurados con Object.entries() y Object.values()
Object.entries(objetoJerarquico).forEach(([llave, valor]) => { 
  console.log(`key: ${llave}, value: ${valor.propiedad1}`); 
}); 

Object.values(objetoJerarquico).forEach(val => { 
  console.log(`value: ${val}`); 
}); 

// Desempaquetado de objetos anidados de forma iterativa
Object.entries(objetoJerarquico).forEach(([llave, valor]) => { 
  Object.entries(valor).forEach(([subLlave, subValor]) => { 
    console.log(`key: ${subLlave}, value: ${subValor}`); 
  }); 
});