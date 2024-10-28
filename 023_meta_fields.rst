Meta-fields Management
======================

TODO
----

Seen in #0450247.

The list of |fmg_api| URLs for Meta-fields management:

- ``pm/config/_meta_fields/firewall/address``
- ``pm/config/_meta_fields/firewall/addrgrp``
- ``pm/config/_meta_fields/firewall/service/custom``
- ``pm/config/_meta_fields/firewall/service/group``
- ``pm/config/_meta_fields/firewall/policy``
- ``pm/config/_meta_fields/firewall/central-snat-map``
- ``dvmdb/_meta_fields/device``
- ``dvmdb/_meta_fields/group``
- ``dvmdb/_meta_fields/adom``
- ``cli/global/_meta_fields/system/admin/user``

Firewall Policy Meta-fields
---------------------------

How to get firewall policy Meta-fields?
+++++++++++++++++++++++++++++++++++++++

The following example shows how to get the Meta-fields created for firewall policies:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/_meta_fields/firewall/policy"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json         
      
         {
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "importance": 1,
                   "length": 20,
                   "name": "mf_001"
                 },
                 {
                   "importance": 0,
                   "length": 20,
                   "name": "mf_002"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/_meta_fields/firewall/policy"
             }
           ]
         }

      .. note::

         - In this output, you can see that two Meta-fields have been defined 
           for firewall policies: ``mf_001`` and ``mf_002``
      
How to add one firewall policy Meta-field?
++++++++++++++++++++++++++++++++++++++++++

The following example shows how to add the ``mf_003`` for firewall policies:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "importance": 1,
                 "length": 20,
                 "name": "mf_003"
               },
               "url": "/pm/config/_meta_fields/firewall/policy"
             }
           ],
           "session": "{{session}}"
         }
  
   .. tab-item:: RESPONSE

      .. code-block:: json         

         {
           "id": 3,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/_meta_fields/firewall/policy"
             }
           ]
         }

How to get firewall policy Meta-fields for one firewall policy?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to get the firewall policy Meta-fields for the 
firewall policy with ``policyid`` ``1`` from the ``pkg_001`` Policy Package in 
the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "fields": [
                 "policyid"
               ],
               "loadsub": 0,
               "option": [
                 "get meta"
               ],
               "url": "/pm/config/adom/demo/pkg/pkg_001/firewall/policy/1"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "meta fields": {
                   "mf_001": "value_001",
                   "mf_002": "value_002",
                   "mf_003": "value_003"
                 },
                 "obj seq": 1,
                 "oid": 4106,
                 "policyid": 1
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/pkg/pkg_001/firewall/policy/1"
             }
           ]
         }

How to set a firewall policy Meta-fields?
+++++++++++++++++++++++++++++++++++++++++

The following example shows how to set one firewall policy Meta-field for the firewall policy with ``policyid`` ``1`` in the ``pkg_001`` Policy Package from the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "set",
           "params": [
             {
               "data": {
                 "meta fields": {
                   "mf_003": "value_003"
                 }
               },
               "url": "/pm/config/adom/demo/pkg/pkg_001/firewall/policy/1"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json      

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "policyid": 1
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/pkg/pkg_001/firewall/policy/1"
             }
           ]
         }

Device Meta-fields
------------------

How to create a device Meta-fields?
+++++++++++++++++++++++++++++++++++

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": {
           "importance": "optional",
           "length": 20,
           "name": "foo_000253",
           "status": "enable"
         },
         "url": "/dvmdb/_meta_fields/device"
       }
     ],
     "session": "xRxXrczUh7LBIdT4K1K9WoH0vNBFtGjmS+RR1x/IGzQDNdgIYvJVt7wbxmyAn24jY2kTbZOQaJ/QfAFcFP5lPA=="
   }

**RESPONSE:**

.. code-block:: json
    
   {
     "id": 3,
     "result": [
       {
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/_meta_fields/device"
       }
     ]
   }

How to set a device Meta-field?
-------------------------------

The following example shows how to set a value to the ``mf_001`` Meta-field for 
the ``dev_001`` device in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "set",
           "params": [
             {
               "data": {
                 "meta fields": {
                   "mf_001": "value_001"
                 }
               },
               "url": "/dvmdb/adom/demo/device/dev_001"
             }
           ],
           "session": "{{session}}"
         }
      

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "name": "dev_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/device/dev_001"
             }
           ]
         }

How to set multiple device Meta-field?
--------------------------------------

The following example shows how to set values to the ``mf_001``, ``mf_002`` and ``mf_003`` Meta-fields for the ``dev_001`` device in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "set",
           "params": [
             {
               "data": {
                 "meta fields": {
                   "mf_001": "value_001",
                   "mf_002": "value_002",
                   "mf_003": "value_003",
                 }
               },
               "url": "/dvmdb/adom/demo/device/dev_001"
             }
           ],
           "session": "{{session}}"
         }
      

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "name": "dev_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/device/dev_001"
             }
           ]
         }          