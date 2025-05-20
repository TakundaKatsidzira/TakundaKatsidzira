Sequence Game Documentation
===========================

Welcome to the Sequence Game documentation!

Contents:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   board
   cpu_agent
   game
   player
   utils

Installation
------------

Run:

.. code-block:: bash

    pip install -r requirements.txt
    python setup.py install

Usage
-----

Run the game CLI:

.. code-block:: bash

    python scripts/play_sequence.py --players 2 --cpu 1

Testing
-------

Run tests with:

.. code-block:: bash

    pytest tests/

