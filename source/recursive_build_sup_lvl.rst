recursive_build_sup_lvl
=======================

.. code-block:: python	

	def recursive_build_sup_lvl(table_base,current,lvl)

_________________________________________________________________

**Algorithm**
-------------

The recursive_build_sup_lvl method is used to manage recursivity of the algorithm. 
I mean i have wrote the iterative version of the recursive function. So you can easely use it and control it.

=============== ============ ========================================
**Parameters**    **Type**    **Description**
**table_base**  *str list*   my first step Base table array as list
**current**     *str list*   my current Base table array as list
**lvl**         *int*        Define the level of recursivity
=============== ============ ========================================

:Returns: **(list,int) Tuple** : The (Base Table builded, Index of depth) Couple of informations.

_________________________________________________________________

**Source Code**
---------------

.. code-block:: python	

	res   = []
	break_ind = 0
	for i in table_base:	
		try :
			res.extend(recursive_build_sup_lvl_safe_mode(current,i))
		except:
			break_ind=1
			break
	return (res,break_ind)