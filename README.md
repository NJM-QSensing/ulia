# Universal Software Lock-In Amplifier (ULIA)
An effective algorithm to emulate a Lock-In Amplifier.

## Installation
To install `ulia` you can use `pip` or `setuptools`.

### Using `pip`
`ulia` package can be installed directly from PyPI using `pip` (`pip3`).

```bash
$ pip3 install ulia
```

### Using `setuptools`
It can also be installed directly from this repository.

```bash
$ git clone https://gitlab.com/UhlDaniel/ulia.git
$ cd ulia
$ python3 setup.py install
```

### Dependencies
This package depends on:
 - Numpy
 - Scipy
 - Numba

## Usage

```python
import numpy as np
import ulia


modulation_frequency = 5000.0
sampling_rate = 200000.0

t = np.arange(0, 0.3*sampling_rate) / sampling_rate
signal = np.cos(2*np.pi*t*modulation_frequency)
reference = np.cos(2*np.pi*t*modulation_frequency)

lia = ulia.ULIA(signal.size, sampling_rate, 0.03, 2, 0.2)
lia.load_data(reference, signal)
lia.execute()

x = np.mean(lia.x[int(0.3*lia.x.size):int(0.9*lia.x.size)])
y = np.mean(lia.y[int(0.3*lia.y.size):int(0.9*lia.y.size)])

print(x - 1j * y)
```
