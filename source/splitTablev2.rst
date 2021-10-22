splitTable
==========

.. code-block:: python

	def splitTable(table)

_________________________________________________________________

**Algorithm**
-------------

Split a string as array from the given separator.

=============== =========== ====================
**Parameters**    **Type**    **Description**
**table**        *string*      The list to split
=============== =========== ====================

:Returns: **list**  : The splitted list

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	local_list=table.split('\n')
	res_list=[]
	for i in range (0,len(local_list)):
		res_list.append(local_list[i])
	return res_list