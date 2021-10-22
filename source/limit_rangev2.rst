limit_range
===========

.. code-block:: python

	def limit_range(Range,base)

_________________________________________________________________

**Algorithm**
-------------

Utils method : A method to limit the Base range

============== =========== ========================
**Parameters**   **Type**   **Description**
**Range**       *int*        The range as a limit
**base**        *int*        The current Base index
============== =========== ========================

:Returns: **int** : The limited by range res.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res=0
	if(Range>base**2):
		res=base**2
	else:
		res=Range 
	return res