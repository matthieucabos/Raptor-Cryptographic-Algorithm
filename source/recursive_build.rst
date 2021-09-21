recursive_build
===============

.. code-block:: python	

	def recursive_build(table_base)

_________________________________________________________________

**Algorithm**
-------------

This function recursively build a full Base Table from an existing one.
You can pass the first step table as already builded recursive table.

=============== =========== ============================
**Parameters**    **Type**   **Description**
**table_base**   *list*        Base Table array as list
=============== =========== ============================

:Returns: **str list** : The recursively builded Base Table

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	res = []
	# //*2
	for i in table_base:
		for j in table_base:
			res.append(i+j)

	return res
