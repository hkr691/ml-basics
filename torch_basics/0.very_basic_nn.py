import torch
import torch.nn as nn
import torch.optim as optim

# Ensure reproducibility
torch.manual_seed(42)

# Data (Batch Size: 4, Features: 1)
distance = torch.tensor([[1.0], [2.0], [3.0], [4.0]], dtype=torch.float32)
time = torch.tensor([[6.96], [12.11], [16.77], [22.21]], dtype=torch.float32)

# Model
model = nn.Sequential(nn.Linear(in_features=1, out_features=1))

# Inspect initial parameters
print("Initial Weight:", model[0].weight.item())
print("Initial Bias:", model[0].bias.item())

# Loss and Optimizer
loss_function = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(500):
    optimizer.zero_grad()
    outputs = model(distance)
    loss = loss_function(outputs, time)
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch + 1}: Loss = {loss.item():.4f}")

# Inference
dist_to_pred = 7.0
with torch.no_grad():
    new_distance = torch.tensor([[dist_to_pred]], dtype=torch.float32)
    predicted_time = model(new_distance)
    print(f"\nPrediction for a {dist_to_pred}-mile delivery: {predicted_time.item():.2f} minutes")