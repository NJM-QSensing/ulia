Universal Software Lock-In Amplifier (ULIA)
===========================================

.. image:: https://gitlab.com/UhlDaniel/ulia/-/jobs/artifacts/master/raw/license.svg?job=badges
        :target: https://gitlab.com/UhlDaniel/ulia/-/blob/master/LICENSE

.. image:: https://gitlab.com/UhlDaniel/ulia/-/jobs/artifacts/master/raw/pypi.svg?job=pypi
        :target: https://pypi.org/project/ulia/

.. image:: https://img.shields.io/badge/DOI-10.1063%2F5.0059740-blue
        :target: https://aip.scitation.org/doi/10.1063/5.0059740


An effective algorithm to emulate a Lock-In Amplifier.


Quickstart
==========

Installation
------------

To install `ulia` you can use `pip`.


`ulia` package can be installed directly from PyPI using `pip` (`pip3`).

.. code-block:: console

  $ pip install git+https://gitlab.com/UhlDaniel/ulia.git

or

.. code-block:: console

  $ pip install ulia


Dependencies
------------

This package depends on:

 - Numpy
 - Scipy
 - Numba



Usage
-----

A simple example on how to utilize the ULIA.

.. code-block:: python

  >>> import numpy as np
  >>> import ulia


  >>> modulation_frequency = 5000.0
  >>> sampling_rate = 200000.0

  >>> t = np.arange(0, 0.3*sampling_rate) / sampling_rate
  >>> signal = np.cos(2*np.pi*t*modulation_frequency)
  >>> reference = np.cos(2*np.pi*t*modulation_frequency)

  >>> lia = ulia.ULIA(signal.size, sampling_rate, 0.03, 2, 0.2)
  >>> lia.load_data(reference, signal)
  >>> lia.execute()


  Ignore the first 30% and last 10% of data due to filter artefacts.
  >>> x = np.mean(lia.x[int(0.3*lia.x.size):int(0.9*lia.x.size)])
  >>> y = np.mean(lia.y[int(0.3*lia.y.size):int(0.9*lia.y.size)])

  >>> print(x + 1j * y)



Links
=====

 * `ULIA on PyPi <https://pypi.org/project/ulia/>`_
 * `Publication <https://doi.org/10.1063/5.0059740>`_
