slurp2
======

.. code-block:: python

	def slurp2(chaine)

_________________________________________________________________

**Algorithm**
-------------

This method is similar of the slurp method. It defined a second level of crypting management.

=============== ========== ==================================
**Parameters**   **Type**   **Description**
**chaine**       *str*         The raw string crypted message
=============== ========== ==================================

:Returns: **str list** : The list of crypted terms rebuilded from the raw string.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	tmp=''
	res = []
	sep=[":",";","<","=",">","?","@"]
	for elem in chaine:
		if(not elem in sep):
			tmp+=str(elem)
		else:
			res.append(tmp)
			tmp=''
		if(elem==''):
			break
	res.append(tmp)
	return res