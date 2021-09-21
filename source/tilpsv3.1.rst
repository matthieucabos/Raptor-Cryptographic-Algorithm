tilps
=====

.. code-block:: python	

	def tilps(chaine)

_________________________________________________________________

**Algorithm**
-------------


The reverse method of the split function. From a given str list, we rebuild the full length string

=============== =========== =============================
**Parameters**    **Type**   **Description**
**chaine**       *str list*   The String slices as a list
=============== =========== =============================

:Returns: **str** : The full striing rebuilded from the slices list

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res = ''
	for i in range (0,len(chaine)):
		res+=chaine[i]
	return res