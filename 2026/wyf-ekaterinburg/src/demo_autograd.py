"""
Sorix Autograd & Neural Network Demonstration
Prepared for WYF-2026 (Ekaterinburg, Russia)
Official website: https://sorix.mitchellmirano.com
"""

import numpy as np

try:
    from sorix import tensor, save, load
    from sorix.nn import Sequential, Linear, ReLU, MSELoss
    from sorix.optim import SGD
    SORIX_AVAILABLE = True
except ImportError:
    SORIX_AVAILABLE = False


def run_autograd_demo():
    print("=" * 60)
    print("1. Sorix Autograd Engine Demo")
    print("=" * 60)
    if not SORIX_AVAILABLE:
        print("Sorix is not installed. Install via: pip install sorix")
        return

    # Create tensors with gradient tracking
    x = tensor([2.0], requires_grad=True)
    w = tensor([3.0], requires_grad=True)
    b = tensor([1.0], requires_grad=True)

    # Forward computation: y = w * x + b
    y = w * x + b

    # Backpropagation via dynamic computational graph
    y.backward()

    print(f"Forward output: y = {y.data}")
    print(f"Gradient dy/dx (w): {x.grad} (Expected: 3.0)")
    print(f"Gradient dy/dw (x): {w.grad} (Expected: 2.0)")
    print(f"Gradient dy/db (1): {b.grad} (Expected: 1.0)")


def run_nn_training_demo():
    print("\n" + "=" * 60)
    print("2. Multi-Layer Perceptron Training with Sorix")
    print("=" * 60)
    if not SORIX_AVAILABLE:
        return

    # Synthetic non-linear regression data: y = 2x^2 - x + 1
    X_raw = np.linspace(-1, 1, 100).reshape(-1, 1)
    y_raw = 2 * (X_raw ** 2) - X_raw + 1 + 0.05 * np.random.randn(*X_raw.shape)

    X_t, y_t = tensor(X_raw), tensor(y_raw)

    # Define architecture
    model = Sequential(
        Linear(1, 16),
        ReLU(),
        Linear(16, 16),
        ReLU(),
        Linear(16, 1)
    )

    criterion = MSELoss()
    optimizer = SGD(model.parameters(), lr=0.05)

    print("Training Sorix model for 500 epochs...")
    for epoch in range(500):
        y_pred = model(X_t)
        loss = criterion(y_pred, y_t)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f"Epoch [{epoch + 1}/500], Loss: {loss.item():.5f}")

    # Persistence
    save(model, "sorix_model.sor")
    print("Model serialized to 'sorix_model.sor'")

    # Inference with loaded model
    loaded_model = load("sorix_model.sor")
    test_input = tensor([[0.5]])
    prediction = loaded_model(test_input)
    print(f"Inference on x=0.5: {prediction.item():.4f} (Actual ~1.0000)")


if __name__ == "__main__":
    run_autograd_demo()
    run_nn_training_demo()
