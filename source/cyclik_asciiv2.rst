cyclik_ascii
============

.. code-block:: python

	def cyclik_ascii(current)

_________________________________________________________________

**Algorithm**
-------------

Compute a cyclik ascii separators into ponctuation signs

============== =========== ===================================
**Parameters**   **Type**   **Description**
**current**     *str*       The current poncuation separator 
============== =========== ===================================

:Returns: **str** : The following separator from the defined 'sep' Set.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	sep=['!','"','#','$','%','&','(',')','*','+',',','-','.','/']
	tmp=((sep.index(current)+1)%13)
	res =sep[tmp]
	return res