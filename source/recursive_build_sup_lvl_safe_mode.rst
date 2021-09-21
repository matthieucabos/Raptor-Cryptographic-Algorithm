recursive_build_sup_lvl_safe_mode
=================================

.. code-block:: python	

	def recursive_build_sup_lvl_safe_mode(current,indice)

_________________________________________________________________

**Algorithm**
-------------

The variable indeice correspond to the pow index of the current recursive build.
The current argument contain the current Base Tale array as list.
Using once again the Horner's scheme, we can build each sup level without be limited by internal constraints.

=============== ========== ============================
**Parameters**   **Type**   **Description**
**current**      *list*     The current table to treat
**indice**       *int*      The pow indice
=============== ========== ============================

:Returns: **list** : A list containing the next level builded Base Table

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	res = []
	#//
	for i in current:
		# try:
		res.append(str(indice)+str(i))
		# except:
			# print("break in method : recursive_build_sup_lvl_safe_mode")
			# break
	return res
