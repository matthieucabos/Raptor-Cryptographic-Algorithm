equa_2_nd
=========

.. code-block:: python

	def equa_2_nd(a,b,c)

_________________________________________________________________

**Algorithm**
-------------

Utils : An 2nd order equation solver

============== ============= ===================
**Parameters**  **Type**     **Description**
**a**          *int / float*  The a coefficient
**b**          *int / float*  The b coefficient
**c**          *int / float*  The c coefficient
============== ============= ===================

:Returns: **int / float** : The solved equation positive root

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res = 0
	racine1 = 0.0
	racine2 = 0.0
	delta = b**2-4*a*c 
	if(delta>0):
		racine1 = (-b+m.sqrt(delta))/2*a
		racine2 = (-b-m.sqrt(delta))/2*a
	if(racine1>0):
		res = int(racine1)
	else:
		res = int(racine2)
	return res