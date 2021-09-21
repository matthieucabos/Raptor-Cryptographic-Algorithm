cyclik_ascii_lvl3
=================

.. code-block:: python	

	def cyclik_ascii_lvl3(current)

_________________________________________________________________

**Algorithm**
-------------

Compute a cyclik ascii separators into Upper letters from A to L.
Get a third cyclic ascii set modulo length

============== =========== ===================================
**Parameters**   **Type**   **Description**
**current**     *str*        The current poncuation separator 
============== =========== ===================================

:Returns: **str** : The following separator from the defined 'sep' Set.

_________________________________________________________________

**Source Code**
---------------
 
.. code-block:: python

	sep=['A','B','C','D','E','F','G','H','I','J','K','L'] 		
	tmp=r.randint(0,11)
	res = sep[tmp]
	return res