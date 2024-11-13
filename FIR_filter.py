import numpy as np
import matplotlib.pyplot as plt
fir_coef = np.array([0.2,0.2,0.2,0.2,0.2])

fs = 500
t = np.linspace(0,1,fs,endpoint = False)
phase = np.sin(2*np.pi*10*t)+np.random.randn(len(t))
filtered_phase = np.convolve(fir_coef,phase, mode='same')
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(t, phase,label = 'original signal')

plt.legend()

plt.subplot(2,1,2)
plt.plot(t,filtered_phase,label = 'filtered signal')
plt.legend()
plt.tight_layout()
plt.show()

