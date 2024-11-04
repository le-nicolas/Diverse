const brain = require('brain.js');
const net = new brain.NeuralNetwork();

// Train the network
net.train([
  { input: [0, 0], output: [0] },
  { input: [0, 1], output: [1] },
  { input: [1, 0], output: [1] },
  { input: [1, 1], output: [0] }
]);

// Test the network
const testCases = [
  { input: [0, 0], expected: 0 },
  { input: [0, 1], expected: 1 },
  { input: [1, 0], expected: 1 },
  { input: [1, 1], expected: 0 }
];

testCases.forEach((testCase) => {
  const output = net.run(testCase.input);
  console.log(`Input: ${testCase.input}, Predicted: ${output}, Expected: ${testCase.expected}`);
});
