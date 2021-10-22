vec_1_poids
===========

.. code-block:: python

	def vec_1_poids(vec_poids)

_________________________________________________________________

**Algorithm**
-------------

Compute the inverse of the vectorial cumulated weigth computation.

=============== ========== ===============================
**Parameters**   **Type**   **Description**
**vec_poids**   *int list*   The weigth as an integer list
=============== ========== ===============================

:Returns: **int list** : The computed list containing the inverse operation of vec_poids method 

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res=[]
	for i in range (0,len(vec_poids)):
		res.append(1/vec_poids[i])
	return res