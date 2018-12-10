import numpy as np
import MPS as MPS
import matplotlib.pyplot as plt

d = 2
n = 6
epsilon = 1e-20
spins = tuple(np.ones(n, dtype=int) * d)

psi = np.random.randn(*spins)
psi /= np.linalg.norm(psi)
print('Psi0 = ', np.reshape(psi, (d, d ** (n - 1))))

norm_of_psi_t = 0
error = 0
k = d ** 10


mps = MPS.matrix_product_state(psi, k)
psi_t = np.tensordot(mps[0], mps[1], (len(np.shape(mps[0])) - 1, 0))
print('u0 shape - ', mps[0].shape)
print('s0 shape - ', mps[1].shape)

ju = 1
js = 1
for i in range(2, 2 * n - 1):
    psi_t = np.tensordot(psi_t, mps[i], (len(np.shape(psi_t)) - 1, 0))
    if not np.mod(i, 2):
        print('u' + str(ju) + ' shape - ', mps[i].shape)
        ju += 1
    if np.mod(i, 2):
        print('s' + str(js) + ' shape - ', mps[i].shape)
        js += 1

norm_of_psi = np.linalg.norm(psi)
norm_of_psi_t = (np.linalg.norm(psi_t))
error = (np.linalg.norm(psi - psi_t))

print('error = ', error)
