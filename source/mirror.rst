mirror
======

.. code-block:: python	

	def mirror(liste)

_________________________________________________________________

**Algorithm**
-------------

The mirror function build a mirror list from the given one.

=============== =========== ========================
**Parameters**    **Type**    **Description**
**liste**          list        The list to be treat
=============== =========== ========================

:Returns: list : The mirror list from the given parameter.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python

	res=liste[:]
	for i in range(1,len(liste)):
		res.append(liste[-i])
	res.append(liste[0])
	return res