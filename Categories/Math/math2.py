import random
import numpy as np
import matplotlib.pyplot as plt
from micrograd.engine import Value
from micrograd.nn import Neuron, Layer, MLP
# Import the necessary library
from sklearn.preprocessing import StandardScaler

# Create a StandardScaler object
scaler = StandardScaler()

np.random.seed(1337)
random.seed(1337)

# Generate 20 samples for toy_size and toy_complexity
toy_size = np.random.rand(50) * 100  # Toy sizes between 0 and 20
toy_complexity = np.random.rand(50) * 100  # Toy complexities between 0 and 20

# Add 0.1 noise to the data
noise = 0.1 * np.random.randn(50)  # Generate noise
toy_size += noise  # Add noise to toy_size
toy_complexity += noise  # Add noise to toy_complexity

# Combine toy_size and toy_complexity into a single 2D numpy array
X = np.column_stack((toy_size, toy_complexity))
# Fit the scaler to the data and transform the data
X_normalized = scaler.fit_transform(X)

# Create a color array and convert it to numerical labels
colors = ['red' if size >= 60 or complexity >= 60 else 'blue' for size, complexity in zip(toy_size, toy_complexity)]
color_map = {'red': 1, 'blue': 0}
color_values = [color_map[color] for color in colors]

# Generate labels based on a boundary condition
labels = np.where(toy_size > 60, 'blue', 'red')

# convert labels to numerical values
y = [1 if color == 'red' else 0 for color in colors]

y = [value*2 - 1 for value in y] # make y be -1 or 1

y = np.array(y) # convert y to a numpy array for proper indexing


# Create a scatter plot
#plt.scatter(toy_size, toy_complexity, color=colors)

# Add a specific point
#plt.scatter(60, 60, color='red')


# Set the title and labels
#plt.title('Toy Size vs Toy Complexity')
#plt.xlabel('Toy Size')
#plt.ylabel('Toy Complexity')


# initialize a model 
model = MLP(2, [16, 16, 1]) # 2-layer neural network
print(model)
print("number of parameters", len(model.parameters()))

# loss function
def loss(batch_size=None):
    
    # inline DataLoader :)
    if batch_size is None:
        Xb, yb = X_normalized, y
    else:
        ri = np.random.permutation(X_normalized.shape[0])[:(batch_size)]
        Xb, yb = X_normalized[ri], y[ri]
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

total_loss, acc = loss()
print(total_loss, acc)


# optimization
epochs = 10 # increase the number of iterations
batch_size = 3 # use mini-batch training
for epoch in range(epochs):
    total_loss, acc = loss(batch_size)
    
    model.zero_grad()
    total_loss.backward()
 
    learning_rate = 0.05 - 0.9 * epoch / 1000 # adjust the learning rate
    for p in model.parameters():
        p.data -= learning_rate * p.grad
  
    
    if epoch % 10 == 0:
        print(f"epoch {epoch} loss {total_loss.data}, accuracy {acc*100}%")

# visualize decision boundary

h = 0.25
x_min, x_max = X_normalized[:, 0].min() - 1, X_normalized[:, 0].max() + 1
y_min, y_max = X_normalized[:, 1].min() - 1, X_normalized[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Xmesh = np.c_[xx.ravel(), yy.ravel()]
Xmesh_normalized = scaler.transform(Xmesh) #normalize the meshgrid
inputs = [list(map(Value, xrow)) for xrow in Xmesh_normalized]
scores = list(map(model, inputs))
Z = np.array([s.data > 0 for s in scores])
Z = Z.reshape(xx.shape)

fig = plt.figure()
plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)
plt.scatter(X_normalized[:, 0], X_normalized[:, 1], c=color_values, cmap=plt.cm.Spectral)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('Toy Size vs Toy Complexity')
plt.xlabel('Normalized Toy Size')
plt.ylabel('Normalized Toy Complexity')
plt.show()