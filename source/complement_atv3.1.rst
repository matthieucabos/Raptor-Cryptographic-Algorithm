complement_at
=============

.. code-block:: python	

	def complement_at(x,base=2)

_________________________________________________________________

**Algorithm**
-------------

Get the direct Base complemented value from the original x value.
The Base must be inferior or equal to 10.

=============== ============ ===============================
**Parameters**    **Type**   **Description**
**x**            *int*        The value to be complemented
**base**         *int*        The current base
=============== ============ ===============================

:Returns: **int** : The complemented value as an integer

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	return (base-1-x)