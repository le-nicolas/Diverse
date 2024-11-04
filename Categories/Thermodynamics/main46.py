import torch
import torch.nn as nn
import numpy as np

# Sample sequence data representing thermodynamic states (e.g., [Pressure, Volume, Temperature])
sequence_length = 10
input_size = 3  # P, V, T
output_size = 3  # P, V, T
batch_size = 1

# Sample Data: Sequence of thermodynamic states (Batch x Seq x Features)
data = torch.rand((batch_size, sequence_length, input_size))

# Define Transformer model
class TransformerModel(nn.Module):
    def __init__(self, input_size, output_size, num_heads=2, num_layers=2):
        super(TransformerModel, self).__init__()
        self.transformer_layer = nn.Transformer(input_size, num_heads, num_layers)
        self.fc_out = nn.Linear(input_size, output_size)

    def forward(self, src):
        # Pass data through the transformer layer
        transformer_output = self.transformer_layer(src, src)
        # Final output layer
        output = self.fc_out(transformer_output)
        return output

# Instantiate the model
model = TransformerModel(input_size, output_size)

# Predict the next thermodynamic state
output = model(data)
print("Predicted Thermodynamic States:\n", output)
