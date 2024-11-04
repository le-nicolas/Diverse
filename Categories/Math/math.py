import random
import numpy as np
import matplotlib.pyplot as plt
from micrograd.engine import Value
from micrograd.nn import Neuron, Layer, MLP
import pandas as pd
# Your plotting commands here

# Generate random data
#toy_size = np.random.rand(50) * 100  # Toy sizes between 0 and 100
#toy_complexity = np.random.rand(50) * 100  # Toy complexities between 0 and 100

# Generate 100 samples for toy_size and toy_complexity
toy_size = np.random.rand(100) * 100  # Toy sizes between 0 and 100
toy_complexity = np.random.rand(100) * 100  # Toy complexities between 0 and 100

# Add 0.1 noise to the data
noise = 0.1 * np.random.randn(100)  # Generate noise
toy_size += noise  # Add noise to toy_size
toy_complexity += noise  # Add noise to toy_complexity

#create a color array
colors = ['red' if size >= 60 or complexity >= 60 else 'blue' for size, complexity in zip(toy_size, toy_complexity)]



# Create a scatter plot
plt.scatter(toy_size, toy_complexity, color=colors)

# Add a specific point
#plt.scatter(60, 60, color='red')


# Set the title and labels
plt.title('Toy Size vs Toy Complexity')
plt.xlabel('Toy Size')
plt.ylabel('Toy Complexity')


# Save the plot
#plt.savefig('plot.png')

# Show the plot
#plt.show()

#I need to store the coordinates of x and y.
#i need the data to be handled as numpy arrays

# initialize a model 
model = MLP(2, [16, 16, 1]) # 2-layer neural network
print(model)
print("number of parameters", len(model.parameters()))

# loss function
def loss(toy_size, toy_complexity, batch_size=None):
    # Ensure toy_size and toy_complexity are 1D numpy arrays
    toy_size = np.array([toy_size]) if np.isscalar(toy_size) else toy_size
    toy_complexity = np.array([toy_complexity]) if np.isscalar(toy_complexity) else toy_complexity

    # inline DataLoader :)
    if batch_size is None:
        Xb, yb = toy_size, toy_complexity
    else:
        ri = np.random.permutation(toy_size.shape[0])[:batch_size]
        Xb, yb = toy_size[ri], toy_complexity[ri]
    inputs = [list(map(Value, xrow)) for xrow in Xb]
    
    # forward the model to get scores
    scores = list(map(model, inputs))
    
    # svm "max-margin" loss
    losses = [(1 + -yi*scorei).relu() for yi, scorei in zip(yb, scores)]
    data_loss = sum(losses) * (1.0 / len(losses))
    # L2 regularization
    alpha = 1e-4
    reg_loss = alpha * sum((p*p for p in model.parameters()))
    total_loss = data_loss + reg_loss
    
    # also get accuracy
    accuracy = [(yi > 0) == (scorei.data > 0) for yi, scorei in zip(yb, scores)]
    return total_loss, sum(accuracy) / len(accuracy)

total_loss, acc = loss(toy_size, toy_complexity)
print(total_loss, acc)


# optimization
for k in range(100):
    
    # forward
    total_loss, acc = loss()
    
    # backward
    model.zero_grad()
    total_loss.backward()
    
    # update (sgd)
    learning_rate = 1.0 - 0.9*k/100
    for p in model.parameters():
        p.data -= learning_rate * p.grad
    
    if k % 1 == 0:
        print(f"step {k} loss {total_loss.data}, accuracy {acc*100}%")


# visualize decision boundary

h = 0.25
x_min, x_max = toy_size[:, 0].min() - 1, toy_size[:, 0].max() + 1
y_min, y_max = toy_size[:, 1].min() - 1, toy_size[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Xmesh = np.c_[xx.ravel(), yy.ravel()]
inputs = [list(map(Value, xrow)) for xrow in Xmesh]
scores = list(map(model, inputs))
Z = np.array([s.data > 0 for s in scores])
Z = Z.reshape(xx.shape)

fig = plt.figure()
plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)
plt.scatter(toy_size[:, 0], toy_size[:, 1], c=toy_complexity, s=40, cmap=plt.cm.Spectral)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())


