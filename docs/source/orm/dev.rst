ORM documentation: generic aiida.orm
====================================

.. toctree::
   :maxdepth: 3

This section describes the aiida object-relational mapping.

Some generic methods of the module aiida.orm.utils

.. automodule:: aiida.orm.utils
   :members:
   :special-members: __init__

Computer
++++++++
.. automodule:: aiida.orm.implementation.general.computer
   :members:

Node
++++
.. automodule:: aiida.orm.implementation.general.node
   :members:
   :private-members:
   :special-members:


.. automodule:: aiida.orm.node
   :members:

.. autoclass:: aiida.orm.node.Node

Workflow
++++++++
.. automodule:: aiida.orm.implementation.general.workflow
   :members:


Code
++++
.. automodule:: aiida.orm.implementation.general.code
   :members:
   :special-members: __init__




ORM documentation: Data
=======================

.. automodule:: aiida.orm.data
   :members:

.. _my-ref-to-structure:

Structure
+++++++++
.. automodule:: aiida.orm.data.structure
   :members:
   :special-members: __init__

Folder
++++++
.. automodule:: aiida.orm.data.folder
   :members:

Singlefile
++++++++++
.. automodule:: aiida.orm.data.singlefile
   :members:

Upf
+++
.. automodule:: aiida.orm.data.upf
   :members:

Cif
+++
.. automodule:: aiida.orm.data.cif
   :members:

Parameter
+++++++++
.. automodule:: aiida.orm.data.parameter
   :members:

Remote
++++++
.. automodule:: aiida.orm.data.remote
   :members:

OrbitalData
+++++++++++
.. automodule:: aiida.orm.data.orbital
   :members:

ArrayData
+++++++++
.. automodule:: aiida.orm.data.array
   :members:

ArrayData subclasses
--------------------
The following are Data classes inheriting from ArrayData.

KpointsData
...........
.. automodule:: aiida.orm.data.array.kpoints
   :members:

BandsData
.........
.. automodule:: aiida.orm.data.array.bands
   :members:

ProjectionData
..............
.. automodule:: aiida.orm.data.array.projection
   :members:

TrajectoryData
..............
.. automodule:: aiida.orm.data.array.trajectory
   :members:

XyData
..............
.. automodule:: aiida.orm.data.array.xy
   :members:


ORM documentation: Calculations
===============================

.. automodule:: aiida.orm.implementation.general.calculation
   :members:
   :special-members: __init__

.. automodule:: aiida.orm.calculation.inline
   :members:
   :special-members: __init__

.. automodule:: aiida.orm.implementation.general.calculation.job
   :members:
   :special-members: __init__

.. automodule:: aiida.orm.implementation.general.calculation.inline
   :members:
   :special-members: __init__

.. automodule:: aiida.orm.calculation
   :members:
   :special-members: __init__

Quantum ESPRESSO
++++++++++++++++

Quantum Espresso - pw.x
-----------------------
.. automodule:: aiida.orm.calculation.job.quantumespresso.pw
   :members:

.. automodule:: aiida.orm.calculation.job.quantumespresso.helpers
   :members:

.. NOTE: NEXT TWO PACKAGES NOT YET MERGED
.. Quantum Espresso - Dos
.. ----------------------
.. .. automodule:: aiida.orm.calculation.job.quantumespresso.dos
..    :members:
..    :special-members: __init__

.. Quantum Espresso - Projwfc
.. --------------------------
.. .. automodule:: aiida.orm.calculation.job.quantumespresso.projwfc
..    :members:
..    :special-members: __init__

Quantum Espresso - PW immigrant
-------------------------------
.. automodule:: aiida.orm.calculation.job.quantumespresso.pwimmigrant
   :members:
   :special-members: __init__

.. NOTE: Wannier90 plugin not yet merged
.. Wannier90  - Wannier90
.. ++++++++++++++++++++++
.. .. automodule:: aiida.orm.calculation.job.wannier90
..    :members:
..    :special-members: __init__

TemplateReplacer
++++++++++++++++
.. automodule:: aiida.orm.calculation.job.simpleplugins.templatereplacer
   :members:
