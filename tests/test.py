import numpy as np
import ulia.routines as rt
import matplotlib.pyplot as plt
import time

t = np.arange(0, 800)/50
r = 0.5 * np.cos(2*np.pi*1.85*t)
s = 0.2 * np.sin(2*np.pi*1.85*t)

start_time = time.time()
lia = rt.ULIA(r.size, 50, 2.5, 2, 0.2)
lia.execute(r, s)
print(f'runtime: {time.time() - start_time}')

print(t.shape)
print(np.mean(lia.x[200:500]))
print(np.mean(lia.y[200:500]))

fig0 = plt.figure('raw')
plt.plot(t, r, label='reference')
plt.plot(t, s, label='signal')
plt.grid()
plt.legend()

fig1 = plt.figure('pll')
plt.plot(t, np.real(lia.avco), label='real')
plt.plot(t, np.imag(lia.avco), label='imag')
plt.grid()
plt.legend()

fig2 = plt.figure('demod')
plt.plot(t, lia.x, label='real')
plt.plot(t, lia.y, label='real')
plt.grid()
plt.legend()

plt.show()

