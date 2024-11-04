// Import Brain.js
const brain = require('brain.js');

// Prepare the training data
const trainingData = [
    { input: [2.0, 3.0, -1.0], output: [1.0] },
    { input: [3.0, -1.0, 0.5], output: [-1.0] },
    { input: [0.5, 1.0, 1.0], output: [-1.0] },
    { input: [1.0, 1.0, -1.0], output: [1.0] }
  ];

// normalize the function
const normalize = (data) => data.map(x => (x - mean) / std);
const mean = xs.flat().reduce((acc, val) => acc + val, 0) / xs.flat().length;
const std = Math.sqrt(xs.flat().reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / xs.flat().length);
const normalizedData = xs.map(arr => normalize(arr));

// Create a new neural network
const net = new brain.NeuralNetwork({
  hiddenLayers: [5, 5] // Optional: Define hidden layers configuration
  // 2 hidden layees with 5 neurons each
});



// Train the network
net.train(trainingData, {
  iterations: 20000,   // The maximum number of iterations to train the network
  log: true,           // Print the error rate to the console
  logPeriod: 1000,     // The number of iterations between logging
  learningRate: 0.01   // Learning rate
});



// Test the network
const testCases = [
    { input: normalizedData[0], expected: 1.0 },
    { input: normalizedData[1], expected: -1.0 },
    { input: normalizedData[2], expected: -1.0 },
    { input: normalizedData[3], expected: 1.0 }
  ];

testCases.forEach((testCase) => {
  const output = net.run(testCase.input);
  console.log(`Input: ${testCase.input}, Predicted: ${output}, Expected: ${testCase.expected}`);
});
