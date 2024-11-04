// Import Brain.js
const brain = require('brain.js');

// Create a new neural network
const net = new brain.NeuralNetwork();

// Train the network with the XOR dataset
net.train([
  { input: [0, 0], output: [0] },
  { input: [0, 1], output: [1] },
  { input: [1, 0], output: [1] },
  { input: [1, 1], output: [0] }
]);

// Test the network
console.log(net.run([0, 0])); // Should output a value close to 0
console.log(net.run([0, 1])); // Should output a value close to 1
console.log(net.run([1, 0])); // Should output a value close to 1
console.log(net.run([1, 1])); // Should output a value close to 0
