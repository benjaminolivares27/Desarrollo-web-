const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema } = require('graphql');
const cors = require('cors');

// 1. Definimos el esquema de GraphQL para la tienda orgánica
const schema = buildSchema(`
  type Producto {
    id: ID!
    nombre: String!
    precio: Float!
    categoria: String!
    stock: Int!
  }

  type Query {
    getProductos: [Producto]
    getProductoById(id: ID!): Producto
    getProductosByCategory(categoria: String!): [Producto]
  }
`);

// 2. Datos de prueba en memoria (simulando la base de datos para la entrega)
const productosData = [
  { id: "1", nombre: "Tomate Orgánico", precio: 1500, categoria: "Verduras", stock: 25 },
  { id: "2", nombre: "Lechuga Hidropónica", precio: 1200, categoria: "Verduras", stock: 15 },
  { id: "3", nombre: "Manzana Fuji Orgánica", precio: 2000, categoria: "Frutas", stock: 40 },
  { id: "4", nombre: "Miel de Abeja Pura", precio: 6500, categoria: "Despensa", stock: 10 }
];

// 3. Los resolvers que devuelven los datos exactos que el cliente solicita
const root = {
  getProductos: () => {
    return productosData;
  },
  getProductoById: ({ id }) => {
    return productosData.find(p => p.id === id);
  },
  getProductosByCategory: ({ categoria }) => {
    return productosData.filter(p => p.categoria.toLowerCase() === categoria.toLowerCase());
  }
};

const app = express();
app.use(cors());

// 4. Configuramos la interfaz de GraphQL
app.use('/graphql', graphqlHTTP({
  schema: schema,
  rootValue: root,
  graphiql: true, // Habilita la interfaz visual en el navegador
}));

const PORT = 8090;
app.listen(PORT, () => {
  console.log(`Servidor GraphQL listo en http://localhost:${PORT}/graphql`);
});