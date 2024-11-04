const brain = require('brain.js');

// Define the input data (xs) and output targets (ys)
const xs = [
  [2.0, 3.0, -1.0],
  [3.0, -1.0, 0.5],
  [0.5, 1.0, 1.0],
  [1.0, 1.0, -1.0],
];
const ys = [1.0, -1.0, -1.0, 1.0];

// Normalize the input data
const normalize = (data, mean, std) => data.map(x => (x - mean) / std);

// Flatten the xs array and calculate mean and standard deviation
const flattenedXs = xs.flat();
const mean = flattenedXs.reduce((acc, val) => acc + val, 0) / flattenedXs.length;
const std = Math.sqrt(flattenedXs.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / flattenedXs.length);

// Apply normalization to each input array in xs
const normalizedData = xs.map(arr => normalize(arr, mean, std));

// Split data into training and testing sets
const trainSize = Math.floor(xs.length * 0.75);
const testSize = xs.length - trainSize;

const trainingData = normalizedData.slice(0, trainSize).map((input, index) => ({
  input: input,
  output: [ys[index]]
}));
const testingData = normalizedData.slice(trainSize).map((input, index) => ({
  input: input,
  expected: ys[trainSize + index]
}));

// Create a new neural network
const net = new brain.NeuralNetwork({
  hiddenLayers: [5, 5] // Example: Two hidden layers with 5 neurons each
});

// Train the network
net.train(trainingData, {
  iterations: 50000, // Increase the number of iterations
  log: true,         // Enable logging
  logPeriod: 1000,   // Log every 1000 iterations
  learningRate: 0.005 // Adjust the learning rate
});

// Test the network on the testing set
let totalError = 0;
testingData.forEach((testCase) => {
  const output = net.run(testCase.input);
  const error = Math.abs(output[0] - testCase.expected);
  totalError += error;
  console.log(`Input: ${testCase.input}, Predicted: ${output}, Expected: ${testCase.expected}, Error: ${error}`);
});

const averageError = totalError / testingData.length;
console.log(`Average Testing Error: ${averageError}`);
