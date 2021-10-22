vec_poids
=========

.. code-block:: python

	def vec_poids(int_chaine)

_________________________________________________________________

**Algorithm**
-------------

Compute the vectorial cumulated weight of the list.

=============== ========== ===========================
**Parameters**   **Type**   **Description**
**int_chaine**  *int list*  The integer list to treat
=============== ========== ===========================

:Returns: **int list** : The computed accumulated weigth integer list

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res = []
	res.append(int_chaine[0])
	for i in range(1,len(int_chaine)):
		res.append(res[i-1]+int_chaine[i])
	return res
