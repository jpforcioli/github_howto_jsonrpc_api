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

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/pm/config/_meta_fields/firewall/policy"
       }
     ],
     "session": "AcKWyixkN05yfGbv1qq4LEZXu9iFD5Bjl4ReKGxeGvBOkwb3t3g+DJ1AHTMu3mFlAeSit85Uu/d65zpB45A2Og=="
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": [
           {
             "importance": 1,
             "length": 20,
             "name": "owner"
           },
           {
             "importance": 0,
             "length": 20,
             "name": "ticket_id"
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

How to add a firewall policy Meta-fields?
+++++++++++++++++++++++++++++++++++++++++

We add firewall policy Meta-field ``test_001``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": {
           "importance": 1,
           "length": 20,
           "name": "test_001"
         },
         "url": "/pm/config/_meta_fields/firewall/policy"
       }
     ],
     "session": "uUAr5Po+6iYl0FfaU+eKpTOhw1Kv2Aj71p8lCxCR06OugC7JFMYwrzC/NSXKXyZPWrxqQ2bsp3NhB9DdZ/8KJA=="
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
         "url": "/pm/config/_meta_fields/firewall/policy"
       }
     ]
   }

How to get firewall policy Meta-fields for one firewall policy?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

We get the firewall policy Meta-fields for policy ID ``1`` from policy package
``default`` of our ADOM ``adom_dc3``:

**REQUEST:**

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
         "url": "/pm/config/adom/adom_dc3/pkg/default/firewall/policy/1"
       }
     ],
     "session": "JG5FUPBiUTRMtWTICPzRiLvGQ4o1SiimNxQjoHidKXm1ntOlgoKOD2nvRUEyECODZRzNw2iqqm5Jhu90b33ZFw=="
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": {
           "meta fields": {
             "owner": "jpforcioli",
             "test_001": "",
             "ticket_id": ""
           },
           "obj seq": 1,
           "oid": 4106,
           "policyid": 1
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/adom_dc3/pkg/default/firewall/policy/1"
       }
     ]
   }

How to set firewall policy Meta-fields for one firewall policy?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

We change the value of the firewall policy Meta-fields ``owner`` for policy ID
``1`` from policy package ``default`` of our ADOM ``adom_dc3``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "set",
     "params": [
       {
         "data": {
           "meta fields": {
             "owner": "aforcioli"
           }
         },
         "url": "/pm/config/adom/adom_dc3/pkg/default/firewall/policy/1"
       }
     ],
     "session": "6QK8r5TQqmOq9L8rREONhwZLrA/LWfgZI0CVplvIJ99R5EK1FFzvMtz5biRzb7wsUESXjsvcCU/BD0WWfbmYeg=="
   }

**RESPONSE:**

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
         "url": "/pm/config/adom/adom_dc3/pkg/default/firewall/policy/1"
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

How to set a device Meta-fields?
--------------------------------

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