# %%
import numpy as np
v1 = np.array([78.6, 0.0019, 0.64])
v2 = np.array([85.2, 0.0017, 0.71])

print(v1 + v2)
print(v2 - v1)
print(v1 * 2)
distance = np.sqrt(np.sum((v1 - v2)**2))
print(distance)
# %%
coefficients = np.array([-0.000017, 0.5, 0.0001])
features = np.array([78.6, 0.0019, 0.64])
print(np.dot(coefficients, features))

# %%
M = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(M.shape)
print(M.T)
print(M.T.shape)
print(M+M)
# %%
A = np.array([
    [1, 2], 
    [3, 4]
])
B = np.array([
    [5, 6], 
    [7, 8]
])
print(A @ B)
print(A * B)
# %%
X = np.array([
    [78.6, 0.64],
    [85.2, 0.71],
    [72.3, 0.58]
])
coefs = np.array([-0.00002, 0.001])
b = 0.003

y_pred = X @ coefs + b
print(y_pred)

# %%
def f(x):
    return x ** 2
x = 3
h = 0.0001

derivative = (f(x + h) - f(x)) / h

print(derivative)
# %%
def f(x):
    return (x - 5) ** 2
x = 0
learning_rate  = 0.1
h = 0.0001

for i in range(50):
    derivative = (f(x + h) - f(x)) / h

    x = x - learning_rate * derivative

    if i % 10 == 0:
        print(f"Шаг {i}: x = {x:.4f}, f(x) = {f(x):.6f}")

print(f"\nФинальное x: {x:.4f}")
print(f"Ожидаемое: 5.0")
# %%
