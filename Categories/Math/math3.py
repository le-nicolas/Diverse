import random
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import numpy as np
from micrograd.engine import Value
from micrograd.nn import MLP
from sklearn.preprocessing import StandardScaler

# Set seeds for reproducibility
np.random.seed(1337)
random.seed(1337)

# Generate data
toy_size = np.random.rand(50) * 100
toy_complexity = np.random.rand(50) * 100
noise = 0.1 * np.random.randn(50)
toy_size += noise
toy_complexity += noise

# Combine and normalize data
X = np.column_stack((toy_size, toy_complexity))
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# Generate labels
colors = ['red' if size >= 60 or complexity >= 60 else 'blue' for size, complexity in zip(toy_size, toy_complexity)]
y = [1 if color == 'red' else -1 for color in colors]
y = np.array(y)

# Initialize model
model = MLP(2, [16, 16, 1])
print(model)
print("Number of parameters:", len(model.parameters()))

# Define loss function
def loss(batch_size=None):
    if batch_size is None:
        Xb, yb = X_normalized, y
    else:
        ri = np.random.permutation(X_normalized.shape[0])[:batch_size]
        Xb, yb = X_normalized[ri], y[ri]
    inputs = [list(map(Value, xrow)) for xrow in Xb]
    scores = list(map(model, inputs))
    losses = [(1 + -yi * scorei).relu() for yi, scorei in zip(yb, scores)]
    data_loss = sum(losses) * (1.0 / len(losses))
    alpha = 1e-4
    reg_loss = alpha * sum((p * p for p in model.parameters()))
    total_loss = data_loss + reg_loss
    accuracy = [(yi > 0) == (scorei.data > 0) for yi, scorei in zip(yb, scores)]
    return total_loss, sum(accuracy) / len(accuracy)

# Train model
epochs = 200
batch_size = 16
for epoch in range(epochs):
    total_loss, acc = loss(batch_size)
    model.zero_grad()
    total_loss.backward()
    learning_rate = 0.01  # Reduce the learning rate
    for p in model.parameters():
        p.data -= learning_rate * p.grad
    if epoch % 10 == 0:
        print(f"Epoch {epoch}: Loss = {total_loss.data:.4f}, Accuracy = {acc * 100:.2f}%")

# Visualize decision boundary
h = 0.25
x_min, x_max = X_normalized[:, 0].min() - 1, X_normalized[:, 0].max() + 1
y_min, y_max = X_normalized[:, 1].min() - 1, X_normalized[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Xmesh = np.c_[xx.ravel(), yy.ravel()]
Xmesh_normalized = scaler.transform(Xmesh)
inputs = [list(map(Value, xrow)) for xrow in Xmesh_normalized]
scores = list(map(model, inputs))
Z = np.array([s.data > 0 for s in scores])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)
plt.scatter(X_normalized[:, 0], X_normalized[:, 1], c=y, cmap=plt.cm.Spectral)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('Toy Size vs Toy Complexity')
plt.xlabel('Normalized Toy Size')
plt.ylabel('Normalized Toy Complexity')
plt.show()
