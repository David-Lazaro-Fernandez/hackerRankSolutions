function DFS(node) {
    // Vamos a crear una pila y añadiremos nuestro nodo en la pila
    let s = new Stack(this.nodes.length);
    let explored = new Set();
    s.push(node);
 
    // Despues marcaremos nuestro nodo como explorato
    explored.add(node);
 
    // Haremos lo mismo hasta que nuestra pila se vacie
    while (!s.isEmpty()) {
       let t = s.pop();
 
    // Imprimimos cada uno de los nodos en la pila
       console.log(t);
    // 1. En el 
    // 1. En los bordes buscaremos por cada uno de los nodos con los que esta conectado nuestro nodo
    // 2. Despues filtraremos los nodos que ya han sido explorados
    // 3. Ahora marcaremos a cada uno de los nodos inexplorados como explorados y los añadiremos a nuestra pila
    this.edges[t]
    .filter(n => !explored.has(n))
    .forEach(n => {
       explored.add(n);
       s.push(n);
       });
    }
 }
 
 //Inicializamos nuestro Grafo
 let g = new Graph();
 //Añadimos los nodos
 g.addNode("A");
 g.addNode("B");
 g.addNode("C");
 g.addNode("D");
 g.addNode("E");
 g.addNode("F");
 g.addNode("G");
 //Añadimos cada una de las conexiones de nuestros nodos
 g.addEdge("A", "C");
 g.addEdge("A", "B");
 g.addEdge("A", "D");
 g.addEdge("D", "E");
 g.addEdge("E", "F");
 g.addEdge("B", "G");
 //Buscamos Realizamos la busqueda
 g.DFS("A");