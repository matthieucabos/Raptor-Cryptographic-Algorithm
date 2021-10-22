multlist
========

.. code-block:: python

	def multlist(a,b)

_________________________________________________________________

**Algorithm**
-------------

Utils : A point by point list multiplier

=============== ================ =======================
**Parameters**   **Type**        **Description**
**a**           *int/float list*  The list to multiply
**b**           *int/float list*  The list to multiply
=============== ================ =======================

:Returns: **int / float list** : The computed point by point multiplication

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res = []
	if(len(a)!=len(b)):
		return []
	else:
		for i in range(0,len(a)):
			res.append(a[i]*b[i])
	return res