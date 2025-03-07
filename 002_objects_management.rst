Objects Management
==================

This section is about managing the objects that can be targetted using the
following |json_rpc_u|:

.. code-block:: text

   /pm/config/adom/{adom}/obj/{path_to_object}
   /pm/config/global/obj/{path_to_object}

How to reference objects when names have special characters?
------------------------------------------------------------

It is required to escape the special character using the ``\\`` (double
back-slash) notation.

For instance to update the ``Net_10.0.0.0/18`` (where ``/`` is the special
character) located in the ``root`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block::

        {
          "id": 4,
          "method": "update",
          "params": [
            {
              "url": "pm/config/adom/root/obj/firewall/address/Net_10.0.0.0\\/18",
              "data": {
                "subnet": "10.0.0.0/255.255.255.0",
              }
            }
          ],
          "session": "{{session}}",
        }

Metadata
--------

Metadata object has been introduced in FortiManager 7.2.0 to replace the Meta
fields.

How to add a metadata?
++++++++++++++++++++++

The following example shows how to add the ``md_001`` metadata in the ``demo`` ADOM, using ``0`` as default value:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "name": "md_001",
                 "value": "0"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable"
             }
           ],
           "session": "{{session}}"
         }
      
      .. warning::
    
         - The ``value`` attribute has to be set with a ``string``!

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "name": "md_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable"
             }
           ]
         }

How to delete a metadata?
+++++++++++++++++++++++++

The following example shows how to delete the ``md_001`` metadata in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "delete",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001"
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
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001"
             }
           ]
         }

How to rename a metadata?
+++++++++++++++++++++++++

The following example shows how to rename the ``md_001`` metadata to ``md_002``
in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "set",
           "params": [
             {
               "data": {
                 "name": "md_002"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001"
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
                 "name": "md_002"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001"
             }
           ]
         }

      .. warning::

         Objects and CLI Templates defined with the ``md_001`` metadata         
         will not be updated and will continue referring to the now 
         non-existent ``md_001`` metadata.

         However, managed devices mapped to the ``md_001`` metadata will be
         updated to reference the renamed ``md_002`` metadata.

How to assign a metadata to devices?
++++++++++++++++++++++++++++++++++++

For a single device
___________________

The following example shows how to add a per-device mapping to the ``md_001`` 
metadata for the ``dev_001`` device in the ``demo`` ADOM; its value will be 
``1``.

.. tab-set:: 
  
   .. tab-item:: REQUEST

      .. code-block:: json
    
         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": [
                 {
                   "_scope": [
                     {
                       "name": "dev_001",
                       "vdom": "global"
                     }
                   ],
                   "value": "1"
                 }
               ],
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001/dynamic_mapping"
             }
           ],
           "session": "{{session}}"
         }
    
      .. warning::
 
         - The ``value`` attribute has to be set with a ``string``!

   .. tab-item:: RESPONSE
 
      .. code-block:: json      
   
         {
           "id": 3,
           "result": [
             {
               "data": {
                 "_scope": null
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001/dynamic_mapping"
             }
           ]
         }
 
For multiple devices
____________________

The following example shows how to add per-device mapping to the ``md_001`` 
metadata for the ``dev_001`` and ``dev_002`` devices in the ``demo`` ADOM; its value will be ``1`` and ``2`` respectively:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
  
         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": [
                 {
                   "_scope": [
                     {
                       "name": "dev_001",
                       "vdom": "global"
                     }
                   ],
                   "value": "1"
                 },
                 {
                   "_scope": [
                     {
                       "name": "dev_002",
                       "vdom": "global"
                     }
                   ],
                   "value": "2"
                 }
               ],
               "url": "/pm/config/adom/demo/obj/fmg/variable/site_id/dynamic_mapping"
             }
           ],
           "session": "{{session}}"
         }
 
      .. warning::
 
         - The ``value`` attribute has to be set with a ``string``!
 
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
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001/dynamic_mapping"
             }
           ]
         }
  
How to assign metadatas at Model Device creation time?
++++++++++++++++++++++++++++++++++++++++++++++++++++++

It can be exposed by using the following FortiManager CLI debug command:

.. code-block:: text

   diagnose debug service dvmcmd 255
   diagnose debug
   
.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "client": "gui json:23235",
           "id": "57337fc8-5029-4458-b100-18cddddb707b",
           "keep_session_idle": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "add-dev-list": [
                   {
                     "_platform": "FortiGate-VM64-KVM",
                     "adm_pass": "******",
                     "adm_usr": "admin",
                     "desc": "Model device",
                     "device action": "add_model",
                     "device blueprint": "BRANCHES",
                     "extra commands": [
                       {
                         "id": 1,
                         "method": "set",
                         "params": [
                           {
                             "data": {
                               "_scope": {
                                 "name": "BRANCH_03",
                                 "vdom": "global",
                                 "vdom_oid": 1
                               },
                               "value": "10.200.1.3"
                             },
                             "url": "pm/config/adom/DEMO/obj/fmg/variable/BGP_LOOPBACK/dynamic_mapping"
                           }
                         ]
                       },
                       {
                         "id": 1,
                         "method": "set",
                         "params": [
                           {
                             "data": {
                               "_scope": {
                                 "name": "BRANCH_03",
                                 "vdom": "global",
                                 "vdom_oid": 1
                               },
                               "value": ""
                             },
                             "url": "pm/config/adom/DEMO/obj/fmg/variable/INET1_IP/dynamic_mapping"
                           }
                         ]
                       },
                       {
                         "id": 1,
                         "method": "set",
                         "params": [
                           {
                             "data": {
                               "_scope": {
                                 "name": "BRANCH_03",
                                 "vdom": "global",
                                 "vdom_oid": 1
                               },
                               "value": ""
                             },
                             "url": "pm/config/adom/DEMO/obj/fmg/variable/INET2_IP/dynamic_mapping"
                           }
                         ]
                       },
                       {
                         "id": 1,
                         "method": "set",
                         "params": [
                           {
                             "data": {
                               "_scope": {
                                 "name": "BRANCH_03",
                                 "vdom": "global",
                                 "vdom_oid": 1
                               },
                               "value": "10.71.144.1/24"
                             },
                             "url": "pm/config/adom/DEMO/obj/fmg/variable/MPLS_IP/dynamic_mapping"
                           }
                         ]
                       },
                       {
                         "id": 1,
                         "method": "set",
                         "params": [
                           {
                             "data": {
                               "_scope": {
                                 "name": "BRANCH_03",
                                 "vdom": "global",
                                 "vdom_oid": 1
                               },
                               "value": "10.0.3.1/24"
                             },
                             "url": "pm/config/adom/DEMO/obj/fmg/variable/LAN_IP/dynamic_mapping"
                           }
                         ]
                       },
                       {
                         "id": 1,
                         "method": "set",
                         "params": [
                           {
                             "data": {
                               "_scope": {
                                 "name": "BRANCH_03",
                                 "vdom": "global",
                                 "vdom_oid": 1
                               },
                               "value": "10.0.31.1/24"
                             },
                             "url": "pm/config/adom/DEMO/obj/fmg/variable/VLAN1_IP/dynamic_mapping"
                           }
                         ]
                       },
                       {
                         "id": 1,
                         "method": "set",
                         "params": [
                           {
                             "data": {
                               "_scope": {
                                 "name": "BRANCH_03",
                                 "vdom": "global",
                                 "vdom_oid": 1
                               },
                               "value": "10.0.32.1/24"
                             },
                             "url": "pm/config/adom/DEMO/obj/fmg/variable/VLAN2_IP/dynamic_mapping"
                           }
                         ]
                       },
                       {
                         "id": 1,
                         "method": "set",
                         "params": [
                           {
                             "data": {
                               "_scope": {
                                 "name": "BRANCH_03",
                                 "vdom": "global",
                                 "vdom_oid": 1
                               },
                               "value": "10.0.33.1/24"
                             },
                             "url": "pm/config/adom/DEMO/obj/fmg/variable/VLAN3_IP/dynamic_mapping"
                           }
                         ]
                       },
                       {
                         "id": 1,
                         "method": "set",
                         "params": [
                           {
                             "data": {
                               "_scope": {
                                 "name": "BRANCH_03",
                                 "vdom": "global",
                                 "vdom_oid": 1
                               },
                               "value": "172.16.31.42/24"
                             },
                             "url": "pm/config/adom/DEMO/obj/fmg/variable/OOB/dynamic_mapping"
                           }
                         ]
                       },
                       {
                         "id": 1,
                         "method": "set",
                         "params": [
                           {
                             "data": {
                               "_scope": {
                                 "name": "BRANCH_03",
                                 "vdom": "global",
                                 "vdom_oid": 1
                               },
                               "value": "140"
                             },
                             "url": "pm/config/adom/DEMO/obj/fmg/variable/VLAN_BASE/dynamic_mapping"
                           }
                         ]
                       }
                     ],
                     "faz.perm": 15,
                     "faz.quota": 0,
                     "groups": [
                       "BRANCHES"
                     ],
                     "is_vm": true,
                     "mgmt_mode": 3,
                     "mr": 2,
                     "name": "BRANCH_03",
                     "os_type": 0,
                     "os_ver": 7,
                     "sn": "FGVM08TM23000464"
                   }
                 ],
                 "adom": "DEMO",
                 "flags": [
                   "create_task",
                   "nonblocking",
                   "log_dev"
                 ]
               },
               "target start": 2,
               "url": "/dvm/cmd/add/dev-list"
             }
           ],
           "session": 52098
         }

You'll find additional details along with another alternative in section :ref:`How to add a Model HA Cluster with Device Blueprint and Metadata?`.

How to unassign a metadata?
+++++++++++++++++++++++++++

The following example shows how to delete per-device mapping of the ``md_001`` metadata for the ``dev_001`` device in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
    
         {
           "id": 3,
           "method": "delete",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001/dynamic_mapping/dev_001/global"
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
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001/dynamic_mapping/dev_001/global"
             }
           ]
         }

How to replace assigned device with another one?
++++++++++++++++++++++++++++++++++++++++++++++++

The ``demo`` ADOM has the ``md_001`` metadata assigned to the ``dev_001`` device
with value ``1``:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001/dynamic_mapping/dev_001/global"
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
                 "_scope": [
                   {
                     "name": "dev_001",
                     "vdom": "global"
                   }
                 ],
                 "oid": 3989,
                 "value": "1"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001/dynamic_mapping/dev_001/global"
             }
           ]
         }

The following example shows how to replace this per-device mapping with a new one for the ``dev_002`` device:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "set",
           "params": [
             {
               "data": [
                 {
                   "name": "dev_002",
                   "vdom": "global"
                 }
               ],
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001/dynamic_mapping/dev_001/global/_scope"
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
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001/dynamic_mapping/dev_001/global/_scope"
             }
           ]
         }

You can double check: both ``value`` and ``oid`` are still with same value as
before the replace operation:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001/dynamic_mapping/dev_002/root"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: REQUEST

      .. code-block:: json 
      
         {
           "id": 3,
           "result": [
             {
               "data": {
                 "_scope": [
                   {
                     "name": "dev_002",
                     "vdom": "global"
                   }
                 ],
                 "oid": 3989,
                 "value": "1"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable/md_001/dynamic_mapping/dev_002/root"
             }
           ]
         }

How to get the metadata values for a specific device?
+++++++++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to get all the metadata values for the ``dev_001`` device in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "fields": [
                 "name"
               ],
               "sub fetch": {
                 "dynamic_mapping": {
                   "fields": [
                     "value"
                   ],
                   "scope member": [
                     {
                       "name": "dev_001",
                       "vdom": "global"
                     }
                   ],
                   "subfetch count": [
                     "==",
                     1
                   ]
                 }
               },
               "subfetch filter": 1,
               "url": "/pm/config/adom/demo/obj/fmg/variable"
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
                   "dynamic_mapping": [
                     {
                       "_scope": [
                         {
                           "name": "dev_001",
                           "vdom": "global"
                         }
                       ],
                       "oid": 5453,
                       "value": "001_003"
                     }
                   ],
                   "name": "md_001",
                   "oid": 5450
                 },
                 {
                   "dynamic_mapping": [
                     {
                       "_scope": [
                         {
                           "name": "dev_001",
                           "vdom": "global"
                         }
                       ],
                       "oid": 5457,
                       "value": "002_003"
                     }
                   ],
                   "name": "md_002",
                   "oid": 5454
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable"
             }
           ]
         }

How to get the value of a metadata for a specific device/vdom?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to get the value of the ``var_001`` metadata 
for the ``dev_001`` mnanaged device and its global scope, from the ``demo`` 
ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/fmg/variable/var_001/dynamic_mapping/dev_001/global"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "_scope": [
                   {
                     "name": "dev_001",
                     "vdom": "global"
                   }
                 ],
                 "oid": 3934,
                 "value": "1"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable/var_001/dynamic_mapping/dev_001/global"
             }
           ]
         }

The following example shows how to the value of the ``var_001`` metadata for the ``dev_002`` managed device and, this time, its ``root`` VDOM, from the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/fmg/variable/var_001/dynamic_mapping/dev_002/root"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

   .. tab-item:: RESPONSE

      .. code-block:: json      

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "_scope": [
                   {
                     "name": "dev_002",
                     "vdom": "root"
                   }
                 ],
                 "oid": 3745,
                 "value": "2"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable/var_001/dynamic_mapping/dev_002/root"
             }
           ]
         }   

How to set multiple metadatas for one device?
+++++++++++++++++++++++++++++++++++++++++++++

It is possible to use a single |fmg_api| request.

The following example set the ``var_001`` and ``var_002`` metadata variables from the ``demo`` ADOM for the ``dev_001`` managed device:

.. tab-set::
   
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "_scope": [
                   {
                     "name": "dev_001",
                     "vdom": "global"
                   }
                 ],
                 "value": "var_001_dev_001"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable/var_001/dynamic_mapping"
             },
             {
               "data": {
                 "_scope": [
                   {
                     "name": "dev_001",
                     "vdom": "global"
                   }
                 ],
                 "value": "var_002_dev_001"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable/var_002/dynamic_mapping"
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
                 "_scope": [
                   {
                     "name": "dev_001",
                     "vdom": "global"
                   }
                 ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable/var_001/dynamic_mapping"
             },
             {
               "data": {
                 "_scope": [
                   {
                     "name": "dev_001",
                     "vdom": "global"
                   }
                 ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/fmg/variable/var_002/dynamic_mapping"
             }
           ]
         }
      
      .. note::
      
         - Of course, existing per-device mappings for the ``var_001`` and 
           ``var_002`` metadata variables are preserved.

How to assign a global metadata?
++++++++++++++++++++++++++++++++

Here the *assign* is in the sense to copy the global metadatas defined in the
Global ADOM into specific *normal* ADOMs.

Global ADOM is having the global metadata ``g_hostname``.

The following example shows how to assign the `g_hostname` global metadata to the ``root``, ``adom_001`` and ``adom_002`` ADOMs:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "global",
                 "category": 3200,
                 "flags": "none",
                 "objs": [
                   "g_hostname"
                 ],
                 "scope": [
                   {
                     "adom": "root"
                   },
                   {
                     "adom": "adom_001"
                   },
                   {
                     "adom": "adom_002"
                   }
                 ],
                 "target": [
                   {
                     "adom": "root"
                   },
                   {
                     "adom": "adom_001"
                   },
                   {
                     "adom": "adom_002"
                   }
                 ]
               },
               "url": "/securityconsole/assign/objs"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - The ``category`` attribute is the number of the table ``fmg 
           variable``

         - You can get this number by issuing following command:

           .. code-block:: text

              execute fmpolicy print-adom-object Global ?

           In the output, you will see this line:

           .. code-block:: text

              [...]
              3200	"fmg variable"
              [...]

   .. tab-item:: RESPONSE

      .. code-block:: json
  
         {
           "id": 3,
           "result": [
             {
               "data": {
                 "task": 54
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/securityconsole/assign/objs"
             }
           ]
         }

How to get the assignement status for global metadatas?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

Caught in #1123231.

The following example shows how to get the assignment status for the
global metadatas in the ``Global`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/global/_objstatus/fmg/variable"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

      .. note::

         ``_objstatus`` keyword in the ``url`` attribute is the method to object
         assignement status for the global metadatas.

   .. tab-item:: RESPONSE

      .. code-block: json

         {
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "device": "demo_001",
                   "objects": [
                     {
                       "category": 3200,
                       "copied_timestamp": 1740385389,
                       "latest_timestamp": 1740385324,
                       "name": "g_var_001",
                       "status": 0
                     },
                     {
                       "category": 3200,
                       "copied_timestamp": 1740385975,
                       "latest_timestamp": 1739523189,
                       "name": "g_var_002",
                       "status": 0
                     }
                   ],
                   "vdom": ""
                 },
                 {
                   "device": "demo_002",
                   "objects": [
                     {
                       "category": 3200,
                       "copied_timestamp": 1740386024,
                       "latest_timestamp": 1739523189,
                       "name": "g_var_002",
                       "status": 0
                     }
                   ],
                   "vdom": ""
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/global/_objstatus/fmg/variable"
             }
           ]
         }

      .. note::

         This output shows that:

         - Global medata ``g_var_001`` is assigned to the ``demo_001`` ADOM.
         - Global metadata ``g_var_002`` is assign to the ``demo_001`` and 
           ``demo_002`` ADOMs.
         
How to Export/Import metadatas?
+++++++++++++++++++++++++++++++

The FortiManager GUI allows you to export and import metadatas in either CSV or 
JSON format.

However, the CSV export/import process still relies on JSON format:

- During CSV export, FortiManager first generates the data in JSON format, then 
  it converts it to CSV before saving the file to your disk

- During CSV import, FortiManager reads your CSV file, converts it to JSON 
  format, and then adds the metadatas to the ADOM database

Direct CSV export/import cannot be performed via the FortiManager API. You will need to handle the conversion between CSV and JSON formats manually for both the export and import operations.

In the two next sections, you will export/import the following CSV file:

.. code-block:: text

   variable_name,default_value,description,device,VDOM,mapped_value
   var_001,1,Variable #001,dev_001,,1_1
   var_001,1,Variable #001,dev_002,root,1_2
   var_002,2,Variable #002,,,

Where in the case of the import operation:

- Metadata ``var_001`` will be created with ``1`` as default value and will 
  have two per-device mappings:

- `1_1` value will be set to the *global* scope of the ``dev_001`` device 
  because the ``vdom`` value is empty

- However, `1_2` value will be set to the ``root`` VDOM of the ``dev_002`` 
  device

- Metadata ``var_002`` will be created with ``2`` as default value

Export
______

The following example shows how to export in JSON format all your metadatas for the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "url": "/pm/config/adom/demo/_fmgvar/export"
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
                 "data": "{ \"adom\": \"demo\", \"variables\": [ { \"name\": \"var_001\", \"description\": \"Variable #001\", \"value\": \"1\", \"mapping\": [ { \"device\": \"dev_001\", \"vdom\": \"\", \"value\": \"1_1\" }, { \"device\": \"dev_002\", \"vdom\": \"root\", \"value\": \"1_2\" } ] }, { \"name\": \"var_002\", \"description\": \"Variable #002\", \"value\": \"2\" } ] }"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/_fmgvar/export"
             }
           ]
         }

      .. note::

         - the returned ``data`` attribute (the second one) is a 
           string!

Import
______

Caught in #1032303.

The following example shows how to import metadatas in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json    

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": "{'adom': 'dc_jani', 'variables': [{'name': 'var_001', 'description': 'Variable #001', 'value': '1', 'mapping': [{'value': '1_1', 'device': 'dev_001', 'vdom': ''}, {'value': '1_2', 'device': 'dev_002', 'vdom': 'root'}]}, {'name': 'var_002', 'description': 'Variable #002', 'value': '2'}]}",
               "url": "/pm/config/adom/demo/_fmgvar/import"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - the ``data`` attribute has to be a string!

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
               "url": "/pm/config/adom/demo/_fmgvar/import"
             }
           ]
         }

Firewall Address
----------------

How to add a IP Range firewall address?
+++++++++++++++++++++++++++++++++++++++

The following example shows how to add the ``iprange_001`` firewall address in
the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "color": 4,
                 "comment": "IP range #001",
                 "end-ip": "10.0.0.100",
                 "name": "iprange_001",
                 "start-ip": "10.0.0.1",
                 "type": "iprange"
               },
               "url": "/pm/config/adom/demo/obj/firewall/address"
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
                 "name": "iprange_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/firewall/address"
             }
           ]
         }


How to add a FQDN firewall address?
+++++++++++++++++++++++++++++++++++

To add FQDN ``www.foobar.com`` in ADOM ``adom_70_001``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": {
           "color": 2,
           "fqdn": "www.foobar.com",
           "name": "fqdn_001",
           "type": "fqdn"
         },
         "url": "/pm/config/adom/adom_70_001/obj/firewall/address"
       }
     ],
     "session": "FhdDcem5V4cjJZeGggJ36dn5fME4nxr4rkA0zojtu+c31+wGhWl2zhhhE2hyP/MAXWQQzNE1yUgQOrJ3eTH7SQ=="
   }

**RESPONSE:**

.. code-block:: json 

   {
     "id": 3,
     "result": [
       {
         "data": {
           "name": "fqdn_001"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/adom_70_001/obj/firewall/address"
       }
     ]
   }

Firewall Address Groups
-----------------------

How to add a single member?
+++++++++++++++++++++++++++

We add firewall address ``host_004`` in the existing address group ``foobar``
from ADOM ``adom_dc2``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": [
           "host_004"
         ],
         "url": "/pm/config/adom/adom_dc2/obj/firewall/addrgrp/foobar/member"
       }
     ],
     "session": "mZMkY72ZIYcs8QInB0h5CUILmCKWCesbvxXJ3P/t+JSrzBh32BV/HvCU7BNMp4GLe8/5vO1qNAoRlsSytXUlTw=="
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
         "url": "/pm/config/adom/adom_dc2/obj/firewall/addrgrp/foobar/member"
       }
     ]
   }

How to delete a single member?
++++++++++++++++++++++++++++++

We delete firewall address ``host_004`` from the existing address group ``foobar``
from ADOM ``adom_dc2``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "delete",
     "params": [
       {
         "data": [
           "host_004"
         ],
         "url": "/pm/config/adom/adom_dc2/obj/firewall/addrgrp/foobar/member"
       }
     ],
     "session": "5uNGBXEMc+cNXjSlx6RuyxE623Nul3hGTCEgeA7pONsNhMMEL1lxCUG7q2TVfnhD0BZiwMg+CgKpWuVY2k0oew=="
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
         "url": "/pm/config/adom/adom_dc2/obj/firewall/addrgrp/foobar/member"
       }
     ]
   }

How to delete all members?
++++++++++++++++++++++++++

.. note::

   - You can delete all members because since FortiOS 7.2.0 (Internal Reference 
     #0769154), you can operate an empty ``firewall addrgrp`` object

Using the ``unset`` method
__________________________

The following example shows how to delete all members from othe ``grp_001`` 
firewall addrgrp in the ``demo`` ADOM using the ``unset`` ``method``:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "unset",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/firewall/addrgrp/grp_001/member"
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
               "url": "/pm/config/adom/demo/obj/firewall/addrgrp/grp_001/member"
             }
           ]
         }

Using the ``unset attrs``
_________________________

The following example shows how to delete all members from othe ``grp_001`` 
firewall addrgrp in the ``demo`` ADOM using the ``unset attrs`` described in :ref:`How to unset a specific attribute?`:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "set",
           "params": [
             {
               "data": {
                 "unset attrs": [
                   "member"
                 ]
               },
               "url": "/pm/config/adom/demo/obj/firewall/addrgrp/grp_001"
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
                 "name": "grp_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/firewall/addrgrp/grp_001"
             }
           ]
         }           

How to get firewall addrgrp members along with their details?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The following example demonstrates how to use the ``expand datasrc`` attribute
to obtain the full details of the members of the ``addrgrp_001`` address group
in the ``demo`` ADOM:

We're getting the member elements of our ``addrgrp_001`` address group:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "params": [
             {
               "expand datasrc": [
                 {
                   "datasrc": [
                     {
                       "fields": [
                         "name",
                         "subnet"
                       ],
                       "obj type": "firewall address"
                     },
                     {
                       "fields": [
                         "name",
                         "member"
                       ],
                       "obj type": "firewall addrgrp"
                     }
                   ],
                   "name": "member"
                 }
               ],
               "filter": [
                 "name",
                 "==",
                 "addrgrp_001"
               ],
               "url": "/pm/config/adom/demo/obj/firewall/addrgrp"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 1,
           "result": [
             {
               "data": [
                 {
                   "allow-routing": "disable",
                   "color": 0,
                   "comment": "",
                   "dynamic_mapping": null,
                   "exclude": "disable",
                   "exclude-member": [],
                   "member": [
                     {
                       "name": "host_005",
                       "obj type": "firewall address",
                       "subnet": [
                         "10.0.0.5",
                         "255.255.255.255"
                       ]
                     },
                     {
                       "name": "host_006",
                       "obj type": "firewall address",
                       "subnet": [
                         "10.0.0.6",
                         "255.255.255.255"
                       ]
                     },
                     {
                       "member": [
                         "host_001",
                         "host_002"
                       ],
                       "name": "addrgrp_002",
                       "obj type": "firewall addrgrp"
                     },
                     {
                       "member": [
                         "host_003",
                         "host_004"
                       ],
                       "name": "addrgrp_003",
                       "obj type": "firewall addrgrp"
                     }
                   ],
                   "name": "addrgrp_001",
                   "tagging": null,
                   "uuid": "c5097fe2-cbf3-51ea-94c7-4543af3302a3",
                   "visibility": "enable"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/firewall/addrgrp"
             }
           ]
         }
      
Wildcard FQDN
-------------

How to add a wildcard FQDN?
+++++++++++++++++++++++++++

To add wilcard FQDN ``*.foobar.*`` to ADOM ``adom_70_001``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": {
           "color": 3,
           "name": "w_fqdn_001",
           "wildcard-fqdn": "*.foobar.*",
         },
         "url": "/pm/config/adom/adom_70_001/obj/firewall/wildcard-fqdn/custom"
       }
     ],
     "session": "/CPDFD77zdvbfmX5tI0OwZ6mEha6Zcfsn1qPaITMmr43uysUgPlNBK5TgUIXFYQcoQXwF0w2oh1XcKRUnB2BMg=="
   }

**RESPONSE:**

.. code-block:: json 

   {
     "id": 3,
     "result": [
       {
         "data": {
           "name": "w_fqdn_001"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/adom_70_001/obj/firewall/wildcard-fqdn/custom"
       }
     ]
   }

Objects Operations
------------------

Objects default values
++++++++++++++++++++++

How to get the default values for a firewall address?
_____________________________________________________

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "get",
     "params": [
       {
         "object template": 1,
         "url": "/pm/config/adom/DB/obj/firewall/address"
       }
     ],
     "session": "HKERCCqx6ximKXlkWN7lxWIgqagVqpj0xXiJtFtYrpiLIL7X3nCuIdlnZw83N+N3JO95oUOOCIwE+emXMuLvcPvKXNHsVYSN",
     "verbose": 1
   }


How to bulk add objects?
++++++++++++++++++++++++

You have two methods:

- ``params`` multi-plexing
- ``data`` multi-plexing

``params`` multi-plexing
________________________

**REQUEST:**

.. code-block::

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "add",
     "params": [
       {
         "data": {
           "name": "test_004",
           "subnet": [
             "10.0.0.4",
             "255.255.255.0"
           ]
         },
         "url": "/pm/config/adom/DEMO_008/obj/firewall/address"
       },
       {
         "data": {
           "name": "test_005",
           "subnet": [
             "10.0.0.5",
             "255.255.255.0"
           ]
         },
         "url": "/pm/config/adom/DEMO_008/obj/firewall/address"
       },
       {
         "data": {
           "name": "test_006",
           "subnet": [
             "10.0.0.6",
             "255.255.255.0"
           ]
         },
         "url": "/pm/config/adom/DEMO_008/obj/firewall/address"
       }
     ],
     "session": "H4bqANWVw4+9ChxkRYdNfdtu4kE+5emeSojgay0fOghSwAPaFuzoBSZHjcvWc6l3TanYih4q9QktzVvLNTdpzA==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block::

   {
     "id": 1,
     "result": [
       {
         "data": {
           "name": "test_004"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/DEMO_008/obj/firewall/address"
       },
       {
         "data": {
           "name": "test_005"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/DEMO_008/obj/firewall/address"
       },
       {
         "data": {
           "name": "test_006"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/DEMO_008/obj/firewall/address"
       }
     ]
   }


``data`` multi-plexing
______________________

**REQUEST:**

.. code-block::

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "add",
     "params": [
       {
         "data": [
           {
             "name": "test_001",
             "subnet": [
               "10.0.0.1",
               "255.255.255.0"
             ]
           },
           {
             "name": "test_002",
             "subnet": [
               "10.0.0.2",
               "255.255.255.0"
             ]
           },
           {
             "name": "test_003",
             "subnet": [
               "10.0.0.3",
               "255.255.255.0"
             ]
           }
         ],
         "url": "/pm/config/adom/DEMO_008/obj/firewall/address"
       }
     ],
     "session": "31rAPPvgsYtaqwXnlwKZJrJQHff1V5hbfwj9lB62868KC1n73fF739Z+wTP+J5CoTxjKSWE8TqY7mTHyFovW7w==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block::

   {
     "id": 1,
     "result": [
       {
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/DEMO_008/obj/firewall/address"
       }
     ]
   }

How to get CLI configuration of a new object?
+++++++++++++++++++++++++++++++++++++++++++++

This is a new feature from FortiManager 7.6.0 (#0954842).

The following example shows how to get the CLI configuration for the ``host_001`` firewall address which is going to be created in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "color": 4,
                 "name": "host_001",
                 "subnet": "10.0.0.1/32"
               },
               "option": [
                 "cli config"
               ],
               "url": "/pm/config/adom/demo/obj/firewall/address"
             }
           ],
           "session": "{{seession}}"
         }
        
      .. note::

         - The ``cli config`` is asking FortiManager to just generate the CLI
           configuration that could have been used to create this object
         
   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "cli config": "config firewall address\nedit \"host_001\"\nset uuid 01dc1d34-4275-51ef-365b-135128a140a9\nset color 4\nset subnet 10.0.0.1 255.255.255.255\n\nnext\nend\n"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/firewall/address"
             }
           ]
         }

      .. note::

         - The ``host_001`` isn't created!
         - FortiManager just returned its CLI configuration
         - ``cli config`` option work also with the ``update`` method or more
           recently, starting with FortiManager 7.6.1 with the ``get`` method
           (caught in #1057509)

           In the case of the ``get`` method, the ``cli config`` option can be
           used when getting an object or a sub-table of an object. But it can't
           be used when getting a table.

           Combining the ``cli config`` option with the ``get`` method is giving
           an API way of obtaining the same result as the FortiManager CLI
           commands:
           
           .. code-block:: text

              execute fmpolicy print-adom-object <...>

           or 

           .. code-block:: text

              execute fmpolicy print-device-object <...>
         
Normalized Interfaces
---------------------

How to create a normalized interface?
+++++++++++++++++++++++++++++++++++++

**REQUEST:**

.. code-block:: json
   
   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "add",
     "params": [
       {
           "data": {
               "color": 2,
               "default-mapping": "enable",
               "defmap-intf": "ul_isp1",
               "description": "Underlay over ISP #1",
               "dynamic_mapping": [
                   {
                       "_scope": [
                           {
                               "name": "dut_fgt_2",
                               "vdom": "root"
                           }
                       ],
                       "local-intf": [
                           "port1"
                       ]
                   }
               ],
               "name": "ul_isp1",
               "platform_mapping": [
                   {
                       "intf-zone": "ul_isp1",
                       "name": "FortiGate-100F"
                   }
               ]
           },
           "url": "/pm/config/adom/{{adom}}/obj/dynamic/interface/ul_isp1"
       }
     ],
     "session": "{{session_id}}",
     "verbose": 1
   }  
   
**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "name": "ul_isp1"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/knock_06999/obj/dynamic/interface/ul_isp1"
       }
     ]
   }  

How to add a new per-platform mapping to an existing Normalized Interface?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**REQUEST:**

.. code-block:: json 

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": {
           "intf-zone": "ol_isp2",
           "name": "FortiGate-40F"
         },
         "url": "/pm/config/adom/root/obj/dynamic/interface/ol_isp2/platform_mapping"
       }
     ],
     "session": "6hngsu9e2X+JBkpzxVIdWYPqLeYactJjmyyXeGkpkB/BlzGI8R9ynUPSP2wKFH5rTcijjR4+XBXWfliD7ichEg=="
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": {
           "name": "FortiGate-40F"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/root/obj/dynamic/interface/ol_isp2/platform_mapping"
       }
     ]
   }

How to get the normalized interfaces with a per-device mapping set for a specific device?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to get the list of normalized interfaces with a
per-device mapping for the ``dut_fgt_03`` device and its ``root`` VDOM:

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json

        {
          "id": "1",
          "method": "get",
          "params":[
            {
              "url": "pm/config/adom/{{adom}}/obj/dynamic/interface",
              "fields": ["name"],
              "subfetch filter": 1,
              "sub fetch": {
                "dynamic_mapping": {
                  "fields": ["_scope", "local_intf"],
                  "subfetch count": ["==", 1],
                  "scope member": [
                    {
                      "name": "dut_fgt_03",
                      "vdom": "root"
                    }
                  ]
                },
                "platform_mapping": {
                  "subfetch hidden": 1
                }
              }
            }
          ],
          "session": "{{session}}"
        }

   .. tab:: RESPONSE

      .. code-block:: json

         {
           "id": "1",
           "result": [
             {
               "data": [
                 {
                   "dynamic_mapping": [
                     {
                       "_scope": [
                         {
                           "name": "dut_fgt_03",
                           "vdom": "root"
                         }
                       ],
                       "oid": 4890
                     }
                   ],
                   "oid": 4889,
                   "name": "foobar"
                 },
                 {
                   "dynamic_mapping": [
                     {
                       "_scope": [
                         {
                           "name": "dut_fgt_03",
                           "vdom": "root"
                         }
                       ],
                       "oid": 4856
                     }
                   ],
                   "oid": 112,
                   "name": "wan"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "pm/config/adom/production/obj/dynamic/interface"
             }
           ]
         }        

How to delete an existing per-platform mapping?
+++++++++++++++++++++++++++++++++++++++++++++++

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "delete",
     "params": [
       {
         "url": "/pm/config/adom/root/obj/dynamic/interface/ol_isp2/platform_mapping/FortiGate-40F"
       }
     ],
     "session": "vfIpN+LiUYGkHWcdTYcEe5RtIhDuIlw/42o9EsZ1KwNCHmSnytwa+cmTHGSJwEyYtencb3kLmFdq6AX5PK2FxQ=="
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
         "url": "/pm/config/adom/root/obj/dynamic/interface/ol_isp2/platform_mapping/FortiGate-40F"
       }
     ]
   }   

How to get the full ADOM database objects syntax?
-------------------------------------------------

Caught in #0607071.

**REQUEST:**

.. code-block:: json

		{
		  "id": 1,
		  "method": "get",
		  "params": [
		    {
		      "url": "pm/config/adom/root/obj",
		      "option": "syntax"
		    }
		  ]
		}

.. note::

   Option ``syntax`` is described in section [TODO].
   
Internet Service Objects
------------------------

How to get the regions that can be used in a Geographic Based Internet Service object?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

To get the regions that could be used to define a geographic based internet
service object: 

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/pm/config/adom/root/_fdsdb/internet-service/region"
       }
     ],
     "session": "cE/JiIBEdO4fWbjUPcrkyTCxuNnT6IGv3NKKHbgXRdSLwphqWRCYRu0M1ZZq4iwMhbQgft8evZlgokRV1bukNg==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json   

   {
     "id": 3,
     "result": [
       {
         "data": [
           {
             "id": 2,
             "name": "Aargau",
             "subarea": "34,1495,2468,3282,13226,13956,15459,17315,19920"
           },
           {
             "id": 3,
             "name": "Abidjan",
             "subarea": "73"
           },
           {
             "id": 4,
             "name": "Abitibi-OuestQuebec",
             "subarea": "12575"
           },
           {
             "...": "..."
           },
           {
             "id": 2141,
             "name": "Zonguldak",
             "subarea": "4207,27249"
           },
           {
             "id": 2142,
             "name": "Zulia",
             "subarea": "3575,4819,14422,21046"
           },
           {
             "id": 2143,
             "name": "Zurich",
             "subarea": "1836,6324,6902,7317,14740,17510,17737,18456,19790,20490,20503,21627,24895,25812,26600,27285"
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/root/_fdsdb/internet-service/region",
         "version": "7.2557"
       }
     ]
   }


How to get the countries that can be used in a Geographic Based Internet Service object?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

To get the countries that could be used to define a geographic based internet
service object:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/pm/config/adom/root/_fdsdb/internet-service/country"
       }
     ],
     "session": "B3w+I+2XazWeTp7nDKnycudpE7slpKntuw0BgsXlxu7cWi7qQyCd4lDUoWHdrRh/lSMLhVTh1cWdYTtJBY8BQQ==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": [
           {
             "id": 4,
             "name": "Afghanistan",
             "subarea": "826,65535"
           },
           {
             "id": 248,
             "name": "Aland Islands",
             "subarea": "65535"
           },
           {
             "id": 8,
             "name": "Albania",
             "subarea": "206,478,505,527,561,607,951,978,1048,1719,1892,2045"
           },
           {
             "...": "...",
           },
           {
             "id": 887,
             "name": "Yemen",
             "subarea": "309,65535"
           },
           {
             "id": 894,
             "name": "Zambia",
             "subarea": "431,1097,65535"
           },
           {
             "id": 716,
             "name": "Zimbabwe",
             "subarea": "264,671,1152,2193,65535"
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/root/_fdsdb/internet-service/country",
         "version": "7.2557"
       }
     ]
   }


How to get the cities that can be used in a Geographic Based Internet Service object?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

To get the cities that could be used to define a geographic based internet
service object:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/pm/config/adom/demo/_fdsdb/internet-service/city"
       }
     ],
     "session": "{{session}}",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": [
           {
             "id": 1,
             "name": "'s Hertogenbosch",
             "subarea": ""
           },
           {
             "id": 7,
             "name": "'s-Heer Hendrikskinderen",
             "subarea": ""
           },
           {
             "id": 13,
             "name": "3 de Mayo",
             "subarea": ""
           },
           {
             "...": "...",
           },        
           {
             "id": 27318,
             "name": "`Ayn al Fijah",
             "subarea": ""
           },
           {
             "id": 27319,
             "name": "`Ayn ash Sharqiyah",
             "subarea": ""
           },
           {
             "id": 29175,
             "name": "`Uqayribat",
             "subarea": ""
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/root/_fdsdb/internet-service/city",
         "version": "7.2557"
       }
     ]
   }        

How to get the list of the Internet Service objects?
++++++++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to get the list of Internet Service objects 
from the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
      		{
      		  "id": 3,
      		  "method": "get",
      		  "params": [
      		    {
      		      "url": "pm/config/adom/demo/_fdsdb/internet-service",
      		    }
      		  ],
            "session": "{{session}}",
            "verbose": 1
      		}
  
   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "database": 0,
                   "direction": 2,
                   "entry_count": 0,
                   "fosver": 15,
                   "icon-id": 0,
                   "id": 65536,
                   "name": "Google-Other",
                   "objver": "00007.00026",
                   "reputation": 0,
                   "sld-id": 0
                 },
                 {
                   "database": 0,
                   "direction": 1,
                   "entry_count": 0,
                   "fosver": 15,
                   "icon-id": 0,
                   "id": 65537,
                   "name": "Google-Web",
                   "objver": "00007.00026",
                   "reputation": 0,
                   "sld-id": 0
                 },
                 {
                   "database": 0,
                   "direction": 1,
                   "entry_count": 0,
                   "fosver": 15,
                   "icon-id": 0,
                   "id": 65538,
                   "name": "Google-ICMP",
                   "objver": "00007.00026",
                   "reputation": 0,
                   "sld-id": 0
                 },
                 {
                   "...": "..."
                 },
                 {
                   "database": 0,
                   "direction": 0,
                   "entry_count": 0,
                   "fosver": 15,
                   "icon-id": 0,
                   "id": 17760605,
                   "name": "Ahrefs-AhrefsBot",
                   "objver": "00007.03771",
                   "reputation": 0,
                   "sld-id": 0
                 },
                 {
                   "database": 0,
                   "direction": 0,
                   "entry_count": 0,
                   "fosver": 15,
                   "icon-id": 0,
                   "id": 17826142,
                   "name": "Semrush-SemrushBot",
                   "objver": "00007.03771",
                   "reputation": 0,
                   "sld-id": 0
                 },
                 {
                   "database": 0,
                   "direction": 1,
                   "entry_count": 0,
                   "fosver": 12,
                   "icon-id": 0,
                   "id": 17891679,
                   "name": "Zero.Networks-Zero.Networks",
                   "objver": "00007.03781",
                   "reputation": 0,
                   "sld-id": 0
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/_fdsdb/internet-service",
               "version": "7.3783"
             }
           ]
         }        

.. note::

   - Following method is only working with old FortiManager 6.4.X

     Caught in Mantis #0622870.

     .. tab-set::

        .. tab-item:: REQUEST

           .. code-block:: json
           
           		{
           		  "id": 3,
           		  "method": "get",
           		  "params": [
           		    {
           		      "url": "pm/config/adom/demo/obj/firewall/internet-service-name",
           		      "option": [
           		        "get used",
           			      "get flags",
           			      "get devobj mapping",
           			      "get meta",
           			      "extra info",
           			      "no loadsub"
           		      ]
           		    }
           		  ]
           		}

     But according to the #0622870, it is better to consider the ``datasrc``  method explained in section [TODO] (datasrc).

Operations on objects
---------------------

Cloning objects
+++++++++++++++

How to clone a firewall address?
________________________________

**REQUEST:**

.. code-block:: json

		{
		  "id": 1,
		  "jsonrpc": "1.0",
		  "method": "clone",
		  "params": [
		    {
		      "data": {
		        "name": "clone_host_001"
		      },
		      "url": "/pm/config/adom/DEMO_013/obj/firewall/address/host_001"
		    }
		  ],
		  "session": "/FPLhY0rgXbpuZYz3TpcGtHQirT0ZHF09ILBV0ZrsWs2Knebq+5+CZ0fXejmyNWVqUm9Aftknb1biLL2JwiyXw==",
		  "verbose": 1
		}

**RESPONSE:**

.. code-block:: json

		{
		  "id": 1,
		  "result": [
		    {
		      "data": {
		        "name": "clone_host_001"
		      },
		      "status": {
		        "code": 0,
			"message": "OK"
		      },
		      "url": "/pm/config/adom/DEMO_013/obj/firewall/address/host_001"
		    }
		  ]
		}

Filtering objects
+++++++++++++++++

Getting an object table could generate a lot of output data. 

Furthermore, most of the time, you're only interested by a sub-part of that
table if not by a single entry.

This is what you can achieve by filtering objects.

The ``contain`` operator
________________________

To get firewall address groups containing member ``host_001``:

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "fields": [
                 "name",
                 "member"
               ],
               "filter": [
                 "member",
                 "contain",
                 "host_001"
               ],
               "loadsub": 0,
               "url": "/pm/config/adom/dc_amer/obj/firewall/addrgrp"
             }
           ],
           "session": "{{ session }}"
         }            

   .. tab:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "member": [
                     "host_001",
                     "host_002"
                   ],
                   "name": "host_grp_001",
                   "oid": 5170
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/dc_amer/obj/firewall/addrgrp"
             }
           ]
         }


How to filter firewall address according to their IPs?
______________________________________________________

Caught in #0363496.

- Retrieve all firewall address objects matching a specific IP subnet

  The following example demonstrates how to use the ``<=`` (*in*) comparison
  operator to retrieve all firewall address objects that match the specified
  ``10.0.0.0/16`` subnet within the ``demo`` ADOM:

  .. tab-set::

     .. tab-item:: REQUEST

        .. code-block:: json

           {
             "id": 3,
             "method": "get",
             "params": [
               {
                 "fields": [
                   "name",
                   "type",
                   "subnet"
                 ],
                 "filter": [
                   [
                     "type",
                     "==",
                     "ipmask"
                   ],
                   "&&",
                   [
                     "subnet",
                     "<=",
                     [
                       "10.0.0.0",
                       "255.255.0.0"
                     ]
                   ]
                 ],
                 "loadsub": 0,
                 "url": "/pm/config/adom/demo/obj/firewall/address"
               }
             ],
             "session": "{{session}}",
             "verbose": 1
           }


     .. tab-item:: RESPONSE

        .. code-block:: json

           {
             "id": 3,
             "result": [
               {
                 "data": [
                   {
                     "name": "host_001",
                     "oid": 5672,
                     "subnet": [
                       "10.0.0.111",
                       "255.255.255.255"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "name": "host_002",
                     "oid": 5675,
                     "subnet": [
                       "10.0.0.112",
                       "255.255.255.255"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "name": "subnet_001",
                     "oid": 5674,
                     "subnet": [
                       "10.0.0.0",
                       "255.255.255.0"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "name": "subnet_002",
                     "oid": 5677,
                     "subnet": [
                       "10.0.0.0",
                       "255.255.0.0"
                     ],
                     "type": "ipmask"
                   }
                 ],
                 "status": {
                   "code": 0,
                   "message": "OK"
                 },
                 "url": "/pm/config/adom/demo/obj/firewall/address"
               }
             ]
           }

- Retrieve all firewall address objects that strictly match a specified IP 
  address or subnet

  The following example demonstrates how to use the ``==`` (*exact match*)
  comparison operator to retrieve all firewall address objects that exactly
  match the specified ``10.0.0.111/32`` IP address within the ``demo`` ADOM:

  .. tab-set::

     .. tab-item:: REQUEST

        .. code-block:: json

           {
             "id": 3,
             "method": "get",
             "params": [
               {
                 "fields": [
                   "name",
                   "type",
                   "subnet"
                 ],
                 "filter": [
                   [
                     "type",
                     "==",
                     "ipmask"
                   ],
                   "&&",
                   [
                     "subnet",
                     "==",
                     [
                       "10.0.0.111",
                       "255.255.255.255"
                     ]
                   ]
                 ],
                 "loadsub": 0,
                 "url": "/pm/config/adom/demo/obj/firewall/address"
               }
             ],
             "session": "{{session}}",
             "verbose": 1
           }

     .. tab-item:: RESPONSE

        .. code-block:: json

           {
             "id": 3,
             "result": [
               {
                 "data": [
                   {
                     "name": "host_001",
                     "oid": 5672,
                     "subnet": [
                       "10.0.0.111",
                       "255.255.255.255"
                     ],
                     "type": "ipmask"
                   }
                 ],
                 "status": {
                   "code": 0,
                   "message": "OK"
                 },
                 "url": "/pm/config/adom/demo/obj/firewall/address"
               }
             ]
           }

- Retrieve all firewall address subnets matching a specific IP address

  The following example demonstrates how to use the ``>=`` (*contain*)
  comparison operator to retrieve all firewall address objects that include the
  specified ``10.0.0.111/32`` IP address in the ``demo`` ADOM:

  .. tab-set::

     .. tab-item:: REQUEST

        .. code-block:: json

           {
             "id": 3,
             "method": "get",
             "params": [
               {
                 "fields": [
                   "name",
                   "type",
                   "subnet"
                 ],
                 "filter": [
                   [
                     "type",
                     "==",
                     "ipmask"
                   ],
                   "&&",
                   [
                     "subnet",
                     ">=",
                     [
                       "10.0.0.111",
                       "255.255.255.255"
                     ]
                   ]
                 ],
                 "loadsub": 0,
                 "url": "/pm/config/adom/demo/obj/firewall/address"
               }
             ],
             "session": "{{session}}",
             "verbose": 1
           }

     .. tab-item:: RESPONSE

        .. code-block:: json

           {
             "id": 3,
             "result": [
               {
                 "data": [
                   {
                     "name": "FABRIC_DEVICE",
                     "oid": 3428,
                     "subnet": [
                       "0.0.0.0",
                       "0.0.0.0"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "name": "FIREWALL_AUTH_PORTAL_ADDRESS",
                     "oid": 3427,
                     "subnet": [
                       "0.0.0.0",
                       "0.0.0.0"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "name": "RFC1918-10",
                     "oid": 3430,
                     "subnet": [
                       "10.0.0.0",
                       "255.0.0.0"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "name": "all",
                     "oid": 3426,
                     "subnet": [
                       "0.0.0.0",
                       "0.0.0.0"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "name": "host_001",
                     "oid": 5672,
                     "subnet": [
                       "10.0.0.111",
                       "255.255.255.255"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "name": "subnet_001",
                     "oid": 5674,
                     "subnet": [
                       "10.0.0.0",
                       "255.255.255.0"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "name": "subnet_002",
                     "oid": 5677,
                     "subnet": [
                       "10.0.0.0",
                       "255.255.0.0"
                     ],
                     "type": "ipmask"
                   }
                 ],
                 "status": {
                   "code": 0,
                   "message": "OK"
                 },
                 "url": "/pm/config/adom/demo/obj/firewall/address"
               }
             ]
           }

- Retrieve all firewall address ranges containing a specific IP address

  The following example demonstrates how to use the ``<=`` (*in*) and ``>=``
  (*contain*) operators together to identify firewall address ranges that
  include the ``10.0.0.111`` IP address within the ``demo`` ADOM:

  .. tab-set::

     .. tab-item:: REQUEST

        .. code-block:: json

           {
             "id": 3,
             "method": "get",
             "params": [
               {
                 "fields": [
                   "name",
                   "type",
                   "start-ip",
                   "end-ip"
                 ],
                 "filter": [
                   [
                     "type",
                     "==",
                     "iprange"
                   ],
                   "&&",
                   [
                     [
                       "start-ip",
                       "<=",
                       "10.0.0.111"
                     ],
                     "&&",
                     [
                       "end-ip",
                       ">=",
                       "10.0.0.111"
                     ]
                   ]
                 ],
                 "loadsub": 0,
                 "url": "/pm/config/adom/demo/obj/firewall/address"
               }
             ],
             "session": "{{session}}"
             "verbose": 1
           }

     .. tab-item:: RESPONSE

        .. code-block:: json           

           {
             "id": 3,
             "result": [
               {
                 "data": [
                   {
                     "end-ip": "10.0.0.120",
                     "name": "range_001",
                     "oid": 5673,
                     "start-ip": "10.0.0.100",
                     "type": "iprange"
                   }
                 ],
                 "status": {
                   "code": 0,
                   "message": "OK"
                 },
                 "url": "/pm/config/adom/demo/obj/firewall/address"
               }
             ]
           }

- Retrieve all firewall address subnets or ranges matching a specific IP address

  The following example demonstrates how to build a complex filter expression to
  search for objects based on various criteria. In this case, the objective is
  to retrieve all firewall address ranges or subnets that match the
  ``10.0.0.111/32`` IP address within the ``demo`` ADOM:

  .. tab-set:: 

     .. tab-item:: REQUEST

        .. code-block:: json

           {
             "id": 3,
             "method": "get",
             "params": [
               {
                 "fields": [
                   "name",
                   "type",
                   "subnet",
                   "start-ip",
                   "end-ip"
                 ],
                 "filter": [
                   [
                     [
                       "type",
                       "==",
                       "iprange"
                     ],
                     "&&",
                     [
                       [
                         "start-ip",
                         "<=",
                         "10.0.0.111"
                       ],
                       "&&",
                       [
                         "end-ip",
                         ">=",
                         "10.0.0.111"
                       ]
                     ]
                   ],
                   "||",
                   [
                     [
                       "type",
                       "==",
                       "ipmask"
                     ],
                     "&&",
                     [
                       "subnet",
                       ">=",
                       [
                         "10.0.0.111",
                         "255.255.255.255"
                       ]
                     ]
                   ]
                 ],
                 "loadsub": 0,
                 "url": "/pm/config/adom/demo/obj/firewall/address"
               }
             ],
             "session": "{{session}}",
             "verbose": 1
           }

     .. tab-item:: RESPONSE

        .. code-block:: json

           {
             "id": 3,
             "result": [
               {
                 "data": [
                   {
                     "end-ip": "0.0.0.0",
                     "name": "FABRIC_DEVICE",
                     "oid": 3428,
                     "start-ip": "0.0.0.0",
                     "subnet": [
                       "0.0.0.0",
                       "0.0.0.0"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "end-ip": "0.0.0.0",
                     "name": "FIREWALL_AUTH_PORTAL_ADDRESS",
                     "oid": 3427,
                     "start-ip": "0.0.0.0",
                     "subnet": [
                       "0.0.0.0",
                       "0.0.0.0"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "end-ip": "0.0.0.0",
                     "name": "RFC1918-10",
                     "oid": 3430,
                     "start-ip": "0.0.0.0",
                     "subnet": [
                       "10.0.0.0",
                       "255.0.0.0"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "end-ip": "0.0.0.0",
                     "name": "all",
                     "oid": 3426,
                     "start-ip": "0.0.0.0",
                     "subnet": [
                       "0.0.0.0",
                       "0.0.0.0"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "end-ip": "0.0.0.0",
                     "name": "host_001",
                     "oid": 5672,
                     "start-ip": "0.0.0.0",
                     "subnet": [
                       "10.0.0.111",
                       "255.255.255.255"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "end-ip": "10.0.0.120",
                     "name": "range_001",
                     "oid": 5673,
                     "start-ip": "10.0.0.100",
                     "type": "iprange"
                   },
                   {
                     "end-ip": "0.0.0.0",
                     "name": "subnet_001",
                     "oid": 5674,
                     "start-ip": "0.0.0.0",
                     "subnet": [
                       "10.0.0.0",
                       "255.255.255.0"
                     ],
                     "type": "ipmask"
                   },
                   {
                     "end-ip": "0.0.0.0",
                     "name": "subnet_002",
                     "oid": 5677,
                     "start-ip": "0.0.0.0",
                     "subnet": [
                       "10.0.0.0",
                       "255.255.0.0"
                     ],
                     "type": "ipmask"
                   }
                 ],
                 "status": {
                   "code": 0,
                   "message": "OK"
                 },
                 "url": "/pm/config/adom/demo/obj/firewall/address"
               }
             ]
           }           

How to get the Last Modified timestamp?
_______________________________________

The following example will get the Last Modified timestamp (i.e., ``_modified
timestamp``) for the firewall address groups declared in the ``dc_amer`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST:

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "fields": [
                 "name",
                 "_modified timestamp"
               ],
               "option": [
                 "extra info",
                 "no loadsub"
               ],
               "url": "/pm/config/adom/dc_amer/obj/firewall/addrgrp"
             }
           ],
           "session": "PT2or1RfAXowIdjpnhHiEx4W6p12Hx3AkWE5RK9noPTLN5gKy79kywOSYEL5P5vjAc2Ymvt7Zo9OoXV8TndYfQ=="
         }
         
   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "_created timestamp": 1681399819,
                   "_last-modified-by": "admin",
                   "_modified timestamp": 1681399819,
                   "name": "G Suite",
                   "obj ver": 1,
                   "oid": 3699
                 },
                 {
                   "_created timestamp": 1681399819,
                   "_last-modified-by": "admin",
                   "_modified timestamp": 1681399819,
                   "name": "Microsoft Office 365",
                   "obj ver": 1,
                   "oid": 3700
                 },
                 {
                   "_created timestamp": 1681408275,
                   "_last-modified-by": "admin",
                   "_modified timestamp": 1681813548,
                   "name": "host_grp_001",
                   "obj ver": 3,
                   "oid": 5170
                 },
                 {
                   "_created timestamp": 1681408290,
                   "_last-modified-by": "admin",
                   "_modified timestamp": 1681813548,
                   "name": "host_grp_002",
                   "obj ver": 4,
                   "oid": 5171
                 },
                 {
                   "_created timestamp": 1684190778,
                   "_last-modified-by": "admin",
                   "_modified timestamp": 1684190778,
                   "name": "grp_001",
                   "obj ver": 1,
                   "oid": 5235
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/dc_amer/obj/firewall/addrgrp"
             }
           ]
         }

How to filter on the Last Modified timestamp?
_____________________________________________

Idea is to retrieve the list of objects more recent that a specific
timestamp.

Caught in #0539624.

.. tab-set:: 
  
   .. tab-item:: REQUEST

      .. code-block:: json

         { 
           "id": 1,
           "method": "get",
           "params": [
             {
               "url": "pm/config/adom/FortiOS-54/obj/firewall/address",
               "option": [
                 "get used",
                 "get flags",
                 "get devobj mapping",
                 "get meta",
                 "extra info",
                 "no loadsub"
               ],
               "filter": [
                 "_modified timestamp",
                 ">=",
                 1549412522
               ]
             }
           ]
		     }

      .. note::

         The option of interest is ``extra info``.

The ``like`` operator
_____________________

What if goal is to retrieve all firewall addresses whose name start with
``host_``?

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "fields": [
                 "name",
                 "subnet"
               ],
               "filter": [
                 "name",
                 "like",
                 "host_%"
               ],
               "loadsub": 0,
               "url": "/pm/config/adom/demo/obj/firewall/address"
             }
           ],
           "session": "Wvq6WltRC50vmipqJhAacFrS0RAr/sxQGdrr3NaT2SbAdcz8XzyPbZTd98ewBhiFtMmWLDLkUrSQWCVGhqzvZA==",
           "verbose": 1
         }

   .. tab:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "name": "host_001",
                   "subnet": [
                     "10.0.0.111",
                     "255.255.255.255"
                   ]
                 },
                 {
                   "name": "host_002",
                   "subnet": [
                     "10.0.0.112",
                     "255.255.255.255"
                   ]
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/firewall/address"
             }
           ]
         }

How to delete multiple objects?
_______________________________

The ``filter`` operator can also be very useful to delete multiple objects with
a single |fmg_api| request.

For instance to delete all firewall addresses starting with ``host_``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "create task": {
       "adom": "dc_amer"
     },
     "method": "delete",
     "params": [
       {
         "filter": [
             "name",
             "like",
             "host_%"
         ],
         "url": "/pm/config/adom/dc_amer/obj/firewall/address"
       }
     ],
     "session": "{{session}}"
   }

.. note::

   - We're using the ``create task`` to get a sucessful response!
   - In this case, we will just receive a task ID and we will have to review the
     task output. 
   - The ``filter`` operator is for all ``name`` starting with ``host_``.

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "task": 7
         },
         "status": {
           "code": 0,
           "message": "OK"
         }
       }
     ]
   }

Task failed!

Message (captured from the FortiManager GUI) is:

.. code-block:: text

   The command is invalid for selected url

OK...

In fact, an yes message is really not meaningful, we need to confirm such
dangerous ``delete`` form.

We could place the wrong filter and delete a lot of objects!

Let's retry by confirming the operation:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "create task": {
       "adom": "dc_amer"
     },
     "method": "delete",
     "params": [
       {
         "confirm": 1,
         "filter": [
             "name",
             "like",
             "host_%"
         ],
         "url": "/pm/config/adom/dc_amer/obj/firewall/address"
       }
     ],
     "session": "{{session}}"
   }  

.. note::

   - To confirm, you just need to use the ``confirm`` attribute.

But...
Wait. The task failed again!

.. code-block:: text

   used

Of course, our objects are used in some firewall policies.

Let's force the delete operation!

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "create task": {
       "adom": "dc_amer"
     },
     "method": "delete",
     "params": [
       {
         "confirm": 1,
         "option": "force",
         "filter": [
             "name",
             "like",
             "host_%"
         ],
         "url": "/pm/config/adom/dc_amer/obj/firewall/address"
       }
     ],
     "session": "{{session}}"
   }  

.. note::

   - To force the requested operation, you have to use the ``option`` attribute
     set with the ``force`` keyword.

This time the task is succeeded.

.. warning::

   The operation is succeeded even if you have the following FortiManager CLI
   setting disabled:

   .. code-block:: text

      config system admin setting
          set objects-force-deletion disable 
      end

As a last word, on this particular exemple, to delete just the list of objects
(and not more matching the previous used ``filter`` value) you could have used
the following filter:

.. code-block::

   "filter": [
     "name",
     "in",
     "host_001",
     "host_002",
     "host_003",
   ]

   

Used/Unused objects
+++++++++++++++++++

.. note:: 

   This section will take the ``firewall address`` table as example, but you can
   apply it to all other tables.

How to know whether a specific object is used?
______________________________________________

We can use the option ``get used`` and observe the returned ``obj flags``.

Our firewall address ``foo_host_001`` is member of a firewall address group. It
is **only** used in this firewall address group.

If we get it with the option ``get used``, we can see a returned ``obj flags``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "get",
     "params": [
       {
         "fields": [
           "name",
           "obj flags"
         ],
         "loadsub": 0,
         "option": [
           "get used"
         ],
         "url": "/pm/config/adom/production_001/obj/firewall/address/foo_host_001"
       }
     ],
     "session": "oc+DBEboJovBLDkoYqyFkB3dnhoazTP1fbVTRIi1XbVHmVTvuL2A+lUxuYnhjk3L9Sdd74g/SqaOGFQO1saVB2aouTDXWgQg",
     "verbose": 1
   }

**RESPONSE:**

.. code-block::

   {
     "id": 1,
     "result": [
       {
         "data": {
           "name": "foo_host_001",
           "obj flags": 1
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/production_001/obj/firewall/address/foo_host_001"
       }
     ]
   }

When ``obj flags`` is equal to ``1`` it means the object is used.

If we remove firewall address ``foo_host_001`` from the group it was belonging
to, the same request now gives:

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "name": "foo_host_001"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/production_001/obj/firewall/address/foo_host_001"
       }
     ]
   }

The ``obj flags`` is no longer returned meaning the object isn't used.

How to get the list of used objects?
____________________________________

You can get the list of used objects by getting the table only using the ``get
used`` option as seen in section `How to know whether a specific object is
used?`_

For instance:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "fields": [
           "name"
         ],
         "option": [
           "no loadsub",
           "get used"
         ],
         "url": "/pm/config/adom/production_001/obj/firewall/address"
       }
     ],
     "session": "Shc2xxYYd6Q0apcJAYewlcFxv/pgyCg/ADzB0hC187N1i70lzP9v2808/D2F89JhRFKPbxVAv0XiiK8SUAjrPQ==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": [
           {
             "name": "FABRIC_DEVICE",
             "oid": 2644
           },
           {
             "name": "FIREWALL_AUTH_PORTAL_ADDRESS",
             "oid": 2643
           },
           {
             "name": "RFC1918-10",
             "obj flags": 1,
             "oid": 2646
           },
           {
             "name": "RFC1918-172",
             "obj flags": 1,
             "oid": 2647
           },
           "...": "...",
           {
             "name": "metadata-server",
             "oid": 2645
           },
           {
             "name": "none",
             "oid": 2634
           },
           {
             "name": "wildcard.dropbox.com",
             "oid": 2640
           },
           {
             "name": "wildcard.google.com",
             "obj flags": 1,
             "oid": 2639
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/knock_45329/obj/firewall/address"
       }
     ]
   }        
   
However, as you can see, FortiManager is still returning all firewall addresses!

You have to filter by yourself and isolate the returned objects which are using
the `obj flags`.

You can try to add a ``filter`` block:

.. code-block:: json

   "filter": [
     "obj flags",
     "==",
     1
   ]
   
but it won't work.

Fortunately, we can ask FortiManager to only return used objects using the
following request:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "fields": [
           "name"
         ],
         "filter": [
           [
             "object used",
             "==",
             1
           ],
           "&&",
           [
             "name",
             "like",
             "host_%"
           ]
         ],
         "option": [
           "no loadsub",
           "get used"
         ],
         "url": "/pm/config/adom/knock_45329/obj/firewall/address"
       }
     ],
     "session": "tdGYyiDdeDNhiaGmXCJShCAnWS+N5AIeWcb1bMtccP3xNmG6bGONVWUZkU5j+fpTAR48BlvGDfrebJdAcZGQBg==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": [
           {
             "name": "host_001",
             "obj flags": 1,
             "oid": 4156
           },
           {
             "name": "host_002",
             "obj flags": 1,
             "oid": 4157
           },
           {
             "name": "host_003",
             "obj flags": 1,
             "oid": 4158
           },
           "...": "...",
           {
             "name": "host_198",
             "obj flags": 1,
             "oid": 4353
           },
           {
             "name": "host_199",
             "obj flags": 1,
             "oid": 4354
           },
           {
             "name": "host_200",
             "obj flags": 1,
             "oid": 4355
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/knock_45329/obj/firewall/address"
       }
     ]
   }

.. note:: 

   - You can keep using the ``get used`` option just to confirm that all
     returned objects have the flag ``obj flags`` set to ``1``.
   
How to get unused objects?
__________________________

To get all unused firewall addresses from ADOM ``demo`` and matching a specific
``name``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "fields": [
           "name"
         ],
         "filter": [
           [
             "object used",
             "==",
             0
           ],
           "&&",
           [
             "name",
             "like",
             "host_%"
           ]
         ],
         "option": [
           "search all adoms",
           "no loadsub"
         ],
         "url": "/pm/config/adom/knock_45329/obj/firewall/address"
       }
     ],
     "session": "Iu1Msbu+H9FQO/IjfnpRMI96BfCoASYDwzizRfmx6Th6xcMWmCuERL4KYmej7vTRfR58KTYKNqRMbxa25l0vMg==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": [
           {
             "name": "host_201",
             "oid": 4489
           },
           {
             "name": "host_300",
             "oid": 4481
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/knock_45329/obj/firewall/address"
       }
     ]
   }
   
Where Used
++++++++++

How to where used from the global adom?
_______________________________________

1. First of all, you have to allow FortiManager to search in all
   ADOMs:

   .. code-block:: 

      config system global
      set search-all-adoms enable
      end

2. Then it's a three steps process:

   a) Start a *where used* request

      In this example, we have the global object ``g_host_001`` in the
      Global ADOM. We want to see where this object is used in all
      ADOMs.

      .. tab-set::

         .. tab-item:: REQUEST

            .. code-block:: json
		      
               {
                 "id": 1,
                 "method": "exec",
                 "params": [
                   {
                     "data": {
                       "mkey": "g_host_001",
                       "obj": "global/obj/firewall/address"
                     },
                     "url": "/cache/search/where/used/start"
                   }
                 ],
                 "session": "{{session}}"
               }

         .. tab-item:: RESPONSE

            .. code-block:: json

               {
                 "id": 1,
                 "result": [
                   {
                     "data": {
                       "token": "K11EnEPIkRUx23ws7sbm6A=="
                     },
                     "status": {
                       "code": 0,
                       "message": "OK"
                     },
                     "url": "/cache/search/where/used/start"
                   }
                 ]
               }

            .. note::
               
               - FortiManager returns the ``token`` attribute. 
               - Its value will allow you to follow the progress of the task,
                 then to get the final result

   b) Wait for the where used task to complete

      .. tab-set::

         .. tab-item:: REQUEST

            .. code-block:: json
      
               {
                 "id": 1,
                 "method": "exec",
                 "params": [
                   {
                     "token": "K11EnEPIkRUx23ws7sbm6A==",
                     "url": "cache/search/where/used/get/summary"
                   }
                 ],
                 "session": "{{session}}"
               }

         .. tab-item:: RESPONSE

            .. code-block:: json

               {
                 "id": 1,
                 "result": [
                   {
                     "data": {
                       "percent": 100
                     },
                     "status": {
                       "code": 0,
                       "message": "OK"
                     },
                     "url": "cache/search/where/used/get/summary"
                   }
                 ]
               }

            .. note::

               - The ``percent`` attribute is ``100`` meaning the task is 100%
                 complete. 
               - Should your value different than ``100``, just keep looping 
                 with same request till it returns ``100``

   c) We can now get the final result

      .. tab-set::

         .. tab-item:: REQUEST

            .. code-block:: json

               {
                 "id": 1,
                 "method": "exec",
                 "params": [
                   {
                     "token": "K11EnEPIkRUx23ws7sbm6A==",
                     "url": "/cache/search/where/used/get/detail"
                   }
                 ],
                 "session": "{{session}}"
               }

         .. tab-item:: RESPONSE      

            .. code-block:: json

               {
                 "id": 1,
                 "result": [
                   {
                     "data": {
                       "percent": 100,
                       "total_num": 1,
                       "where_used": [
                         {
                           "data": [
                             {
                               "attr": "dstaddr",
                               "category": 181,
                               "mapping_name": "firewall policy",
                               "mattr": "policyid",
                               "mkey": "4",
                               "pkg": {
                                 "name": "pp.device1",
                                 "oid": 4710
                               }
                             }
                           ],
                           "root": {
                             "name": "DEMO_014",
                             "oid": 22039
                           }
                         }
                       ]
                     },
                     "status": {
                       "code": 0,
                       "message": "OK"
                     },
                     "url": "/cache/search/where/used/get/detail"
                   }
                 ]
               }      

            .. note::

               This output shows that:

               - Object ``g_host_001`` is used as a destination in policy
                 package ``pp.device1``
               - The firewall policy referencing object ``g_host_001`` is
                 having the ``policyid`` ``4``
               - The policy package ``pp.device1`` is in ADOM ``DEMO_014``

How to where used from within a normal ADOM?
____________________________________________

Follow the same three steps process as the one describe in :ref:`How to where used from the global adom?`

You just need to replace the ``obj`` attribute's value with something like:

.. code-block:: text

   adom/<adom>/obj/firewall/address

For instance, if you want to where used the ``host_001`` firewall address from
within the ``dc_emea`` ADOM, your step 1 request will be:

.. code-block:: json

   {
     "id": 1,
     "method": "exec",
     "params": [
       {
         "data": {
           "mkey": "host_001",
           "obj": "adom/dc_emea/obj/firewall/address"
         },
         "url": "/cache/search/where/used/start"
       }
     ],
     "session": "{{session}}"
   }

Find duplicates objects
+++++++++++++++++++++++

To get duplicates firewall addresses:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "get",
     "params": [
       {
         "fields": [
           "name",
           "type",
           "subnet",
           "duplicate enntries"
         ],
         "load assigned": 0,
         "loadsub": 0,
         "option": [
           "find duplicates"
         ],
         "url": "/pm/config/adom/demo_002/obj/firewall/address"
       }
     ],
     "session": "V3pHwSOgmHZEQoqJ4pVHJFQSCIiaXm0cOjvXp40JN1ps2FQWNwqMNz0jATnrQxGr2K78L6+mY9Os8WRVBRCxKw==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": [
           {
             "duplicate entries": [
               "login.microsoft.com",
               "login.microsoftonline.com",
               "login.windows.net",
               "wildcard.dropbox.com",
               "wildcard.google.com"
             ],
             "name": "gmail.com",
             "subnet": [
               "0.0.0.0",
               "0.0.0.0"
             ],
             "type": "fqdn"
           },
           {
             "duplicate entries": [
               "FIREWALL_AUTH_PORTAL_ADDRESS",
               "all"
             ],
             "name": "FABRIC_DEVICE",
             "subnet": [
               "0.0.0.0",
               "0.0.0.0"
             ],
             "type": "ipmask"
           },
           {
             "duplicate entries": [
               "host_001_002"
             ],
             "name": "host_001_001",
             "subnet": [
               "10.0.0.1",
               "255.255.255.255"
             ],
             "type": "ipmask"
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/demo_002/obj/firewall/address"
       }
     ]
   }

FortiManager is using the ``fields`` attribute to format the response logic.
For instance, if we remove the ``type`` criteria we will obtain this output:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "get",
     "params": [
       {
         "fields": [
           "name",
           "subnet"
         ],
         "load assigned": 0,
         "loadsub": 0,
         "option": [
           "find duplicates"
         ],
         "url": "/pm/config/adom/demo_002/obj/firewall/address"
       }
     ],
     "session": "qpzdhu+2yDsbeuGJQB/OUGjnmIa+/35YCJrXTudpteCy2XnTgHPEeFZaYHs4sHq1yFQohl7NkpfVjkW7H1dUxF5/i1JnAyE+",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": [
           {
             "duplicate entries": [
               "FCTEMS_ALL_FORTICLOUD_SERVERS",
               "FIREWALL_AUTH_PORTAL_ADDRESS",
               "SSLVPN_TUNNEL_ADDR1",
               "all",
               "gmail.com",
               "login.microsoft.com",
               "login.microsoftonline.com",
               "login.windows.net",
               "wildcard.dropbox.com",
               "wildcard.google.com"
             ],
             "name": "FABRIC_DEVICE",
             "subnet": [
               "0.0.0.0",
               "0.0.0.0"
             ]
           },
           {
             "duplicate entries": [
               "host_001_002"
             ],
             "name": "host_001_001",
             "subnet": [
               "10.0.0.1",
               "255.255.255.255"
             ]
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/demo_002/obj/firewall/address"
       }
     ]
   }

Observe where are now listed the firewall addresses
``FIREWALL_AUTH_PORTAL_ADDRESS`` and ``all``.

The ``find duplicates`` option is working with other objects, like address
groups, IPv6 firewall addresses, VIP, etc. You just have to replace the ``url``
parameter with the proper path.

Merge objects
+++++++++++++

How to merge firewall addresses?
________________________________

We want to merge firewall address ``host_001_001`` and ``host_001_002``.
Destination firewall address name has to be one of them; we cannot merge for
instance to firewall address name ``host_001_merged``.

In below example, we will merge both firewall address in ``host_001_001``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "set",
     "params": [
       {
         "merge": [
           "host_001_001",
           "host_001_002"
         ],
         "url": "/pm/config/adom/demo_002/obj/firewall/address/host_001_001"
       }
     ],
     "session": "1PIOQRlz0dKA/xk8nUY1dsmOuiI7rHcjaAyiTjbaSzJVnpa8smZ8VSUAsWn7NWW/ZZWusUbbrNfte0RgNHdInGwTCiQICw3Y",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/demo_002/obj/firewall/address/host_001_001"
       }
     ]
   }

Note that the above merge operation is also:

- Replacing firewall address ``host_001_002`` with firewall address
  ``host_001_001`` everywhere it was used (in firewall policy, in firewall
  address group, etc.) 
- Deleting firewall address ``host_001_002``

The ``merge`` operation is working with other objects, like address groups,
IPv6 firewall addresses, VIP, etc. You just have to replace the ``url``
parameter with the proper path.

Find and Replace
++++++++++++++++

In the below example, we want to replace the antivirus profile
``av-profile-001`` used by some of our firewall policies, with antivirus profile
``av-profile-002``.

First you need to *where used* the antivirus profile ``av-profile-001`` object:

- As you know the *where used* is a three steps process:

  - Step #1: We Need To Start A New Where Used Task

    **REQUEST:**

    .. code-block:: json

                    {
                      "id": 1,
                      "method": "exec",
                      "params": [                
                        {
                          "data": {
                            "flags": [ 
                             "direct used"
                            ],
                            "mkey": "av-profile-001",
                            "obj": "adom/DEMO/obj/antivirus/profile"
                          },
                          "url": "cache/search/where/used/start"
                    	}
                      ], 
                      "session": 20456
                    }

    **RESPONSE:**

    .. code-block:: json

                    { 
                      "id": 1, 
                      "result": [
                        { 
                          "data": { 
                            "token": "ng9jCDhg9qZVmUt4oaYPZw=="
                          }, 
                          "status": { 
                            "code": 0, 
                            "message": "OK"
                          }, 
                          "url": "cache/search/where/used/start"
                        }
                      ]
                    }

  - Step #2: with the returned *token*, we need to wait for the task to be
    completed:

    **REQUEST:**

    .. code-block:: json

                    { 
                      "id": 1, 
                      "method": "exec", 
                      "params": [
                        { 
                          "token": "ng9jCDhg9qZVmUt4oaYPZw==", 
                          "url": "cache/search/where/used/get/summary"
                        }
                      ], 
                      "session": 20456
                    }

    **RESPONSE:**

    .. code-block:: json

                    { 
                      "id": 1, 
                      "result": [
                        { 
                          "data": { 
                            "percent": 100
                          }, 
                          "status": { 
                            "code": 0, 
                            "message": "OK"
                          }, 
                          "url": "cache/search/where/used/get/summary"
                        }
                      ]
                    }

    If the *percent* value isn't equal to 100, just retry till it is 100.

  - Step #3: we can collect the *where used* result:

    **REQUEST:**

	.. code-block:: json

                    { 
                      "id": 1,
                      "method": "exec", 
                      "params": [
                        { 
                          "token": "ng9jCDhg9qZVmUt4oaYPZw==", 
                          "url": "cache/search/where/used/get/detail"
                        }
                      ], 
                      "session": 20456
                    }


    **RESPONSE:**
	
	.. code-block:: json
	
                    { 
                      "id": 1, 
                      "result": [
                        { 
                          "data": { 
                            "percent": 100, 
                            "total_num": 2, 
                            "where_used": [
                              { 
                                "data": [
                                  { 
                                    "attr": "av-profile", 
                                    "category": 181, 
                                    "mapping_name": "firewall policy", 
                                    "mattr": "policyid", 
                                    "mkey": "1", 
                                    "pkg": { 
                                      "name": "default", 
                                      "oid": 4685
                                    }
                                  }, 
                                  { 
                                    "attr": "av-profile", 
                                    "category": 181, 
                                    "mapping_name": "firewall policy", 
                                    "mattr": "policyid", 
                                    "mkey": "2", 
                                    "pkg": { 
                                      "name": "default", 
                                      "oid": 4685
                                    }
                                  }
                                ], 
                                "root": { 
                                  "name": "DEMO", 
                                  "oid": 136
								}
                              }
                            ]
                          }, 
                          "status": { 
                            "code": 0, 
                            "message": "OK"
                          }, 
                          "url": "cache/search/where/used/get/detail"
                        }
                      ]
                    }

    From the above output, we can see that our antivirus profile
    ``av-profile-001`` is used by two firewall policies (id 1 and 2
    respectively) in policy package ``default`` from ADOM ``DEMO``.

- We can now proceed with the replace operation

  - To replace ``av-profile-001`` with ``av-profile-002`` for policy #1

    **REQUEST:**

	.. code-block:: json

                    { 
                      "id": 1, 
                      "method": "update", 
                      "params": [
                        { 
                          "url": "pm/config/adom/DEMO/pkg/default/firewall/policy/1", 
                          "used objs": { 
                            "from": "obj/antivirus/profile/av-profile-001", 
                            "to": [
                              "av-profile-002"
                            ]
                          }
                        }
                      ], 
                      "session": 20456
                    }

    **RESPONSE:**

	TBD

How to find and replace objects in firewall policy?
___________________________________________________

Caught in #0636807.

**REQUEST:**

.. code-block:: json

				{
				  "method": "update",
				  "params": [
			        {
				      "target start": 2,
				      "url": "pm/config/adom/BusySYSLabFG/pkg/BUSYSYSLABFG_Monitoring/firewall/policy/3",
				      "used objs": {
					  	"from": "obj/firewall/address/192.168.215.157-VCenter",
				        "to": [
					            "10.1.0.0/16-IT_BUSY"
					          ]
				      }
				    }
				  ],
				  "session": 4131
				}

Partial installation
++++++++++++++++++++

Caught in #0225600.

This is the template to install any objects:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json 
      
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "{{adom}}>",
                 "scope": [
                   {
                     "name": "{{device}}",
                     "vdom": "{{vdom}}"
                   },
                   {"...", "..."}
                 ],
                 "target": [
                   "{{target}}"
                 ]
               },
               "url": "/securityconsole/install/objects"
             }
           ],
           "session": "{{session}}",
         }

where:

- ``scope`` could be omitted, in that case FortiManager will manage to find the 
  devices/vdoms which are using the target object

- ``target`` is the target object to be install

  You declare a target using the usual format.
  
  For instance:

  .. code-block::

     # For any objects
     /pm/config/adom/<adom>/obj/<fortios cli>
	   
     # For a firewall policyid
     /pm/config/adom/<adom>/pkg/<pkg>/firewall/policy/<policyid>

     etc.

More information about the partial install mechanism are given in section
:ref:`Partial Install`

How to partial install an IPS profile?
______________________________________

Using the Legacy Partial Install API
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

See :ref:`Legacy Partial Install API` for more details about the *Legacy Partial Install API*.

The following example shows how to partial install the ``ips_sensor_001`` IPS 
profile from the ``demo`` ADOM against the ``dev_001`` and ``dev_002`` managed device and their respective ``root`` VDOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "demo",
                 "scope": [
                   {
                     "name": "dev_001",
                     "vdom": "root"
                   },
                   {
                     "name": "dev_002",
                     "vdom": "root"
                   }                   
                 ],
                 "target": [
                   "/pm/config/adom/demo/obj/ips/sensor/ips_sensor_001"
                 ]
               },
               "url": "/securityconsole/install/objects"
             }
           ],
           "session": "{{session}}"
         }
      
   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 1,
           "result": [
             {
               "data": {
                 "task": 441
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/securityconsole/install/objects"
             }
           ]
         }

Using the New Partial Install API
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

See :ref:`New Partial Install API` for more details about the *New Partial Install API*.

The following example shows how to partial install the ``ips_sensor_001`` IPS 
profile from the ``demo`` ADOM against the ``dev_001`` and ``dev_002`` managed device and their respective ``root`` VDOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "demo",
                 "flags": 0,
                 "objects": [
                   [
                     "update",
                     "obj/ips/sensor/ips_sensor_001",
                     "",
                     ""
                   ]
                 ],
                 "scope": [
                   {
                     "name": "dev_001",
                     "vdom": "root"
                   },
                   {
                     "name": "dev_002",
                     "vdom": "root"
                   }
                 ]
               },
               "url": "/securityconsole/install/objects/v2"
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
                 "task": 948
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/securityconsole/install/objects/v2"
             }
           ]
         }

      .. note::

         - It is important to wait for the end of the returned task ID before 
           closing the API session

         - If you close the API session before, the task will fail

        

How to check for a duplicate object name?
+++++++++++++++++++++++++++++++++++++++++

Caught in #893698

To check whether an object name is already used, you can use the option
``duplicate check``:

.. code-block:: json

   "option": [
       "duplicate check"
   ]

For instance, to check whether a firewall address with name ``host_001`` already
exists in ADOM ``dc_amiens``:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "method": "add",
           "id": 1,
           "session": "{{session}}",
           "params": [
             {
               "data": {
                 
               },
               "url": "/pm/config/adom/dc_amiens/obj/firewall/address/host_001",
               "option": ["duplicate check"]
             }
           ]
         }

      .. note::
        
         - The ``method`` attribute is ``add``

   .. tab-item:: RESPONSE

      .. tab-set::

         .. tab-item:: if name is already used

            .. code-block:: json

               {
                 "result": [
                   {
                     "data": "firewall address",
                     "status": {
                       "code": 0,
                       "message": "OK"
                     },
                     "url": "/pm/config/adom/dc_amiens/obj/firewall/address/host_001"
                   }
                 ],
                 "id": 1
               }

            The ``data`` attribute contains the object's category, here ``firewall address``.

         .. tab-item:: if name isn't used

            .. code-block:: json

               {
                 "result": [
                   {
                     "data": null,
                     "status": {
                       "code": 0,
                       "message": "OK"
                     },
                     "url": "/pm/config/adom/dc_amiens/obj/firewall/address/host_001"
                   }
                 ],
                 "id": 1
               }

            The ``data`` attribute is ``null``.         

Object Revision
---------------

How to add an object with an object revision note?
++++++++++++++++++++++++++++++++++++++++++++++++++

Following example applies to firewall address object type.

It is showing how to add a new firewall address with an object revision note:

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "color": 4,
                 "name": "host_005",
                 "subnet": "10.0.0.5/32"
               },
               "revision note": "Initial Revision",
               "url": "/pm/config/adom/dc_amer/obj/firewall/address"
             }
           ],
           "session": "{{ session }}"
         }        
         
   .. tab:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "name": "host_005"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/dc_amer/obj/firewall/address"
             }
           ]
         }

How to update an object with an object revision note?
+++++++++++++++++++++++++++++++++++++++++++++++++++++

Following example applies to firewall address object type.

It is showing how to update both an existing firewall address and its associated
object revision note:

.. tabs:: 

   .. tab:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "update",
           "params": [
             {
               "data": {
                 "color": 10
               },
               "revision note": "Color changed a second time",
               "url": "/pm/config/adom/dc_amer/obj/firewall/address/host_005"
             }
           ],
           "session": "{{ session }}"
         }

   .. tab:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "name": "host_005"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/dc_amer/obj/firewall/address/host_005"
             }
           ]
         }

How to get the revision notes for a specific object?
++++++++++++++++++++++++++++++++++++++++++++++++++++

Following example applies to firewall address object type.

It is showing how to get the revision notes for an existing firewall address:

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/dc_amer/_objrev/obj/firewall/address/host_005"
             }
           ],
           "session": "{{ session }}",
           "verbose": 1
         }

   .. tab:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "act": 1,
                   "category": 140,
                   "config": "{ \"allow-routing\": 0, \"associated-interface\": [ \"any\" ], \"clearpass-spt\": 0, \"color\": 4, \"dirty\": 1, \"dynamic_mapping\": null, \"fabric-object\": 0, \"list\": null, \"macaddr\": [ ], \"name\": \"host_005\", \"node-ip-only\": 0, \"obj-type\": 9, \"oid\": 4649, \"subnet\": [ \"10.0.0.5\", \"255.255.255.255\" ], \"tagging\": null, \"type\": 0, \"uuid\": \"2ea6e52a-d835-51ed-84f2-23efc39096ad\" }",
                   "flags": 0,
                   "key": "host_005",
                   "note": "Initial Revision",
                   "oid": 4649,
                   "pkg_oid": 0,
                   "timestamp": 1681195844,
                   "user": "devops"
                 },
                 {
                   "act": 3,
                   "category": 140,
                   "config": "{ \"_image-base64\": null, \"allow-routing\": 0, \"associated-interface\": [ \"aplink1\" ], \"cache-ttl\": 0, \"clearpass-spt\": 0, \"color\": 4, \"comment\": null, \"country\": [ ], \"dirty\": 1, \"dynamic_mapping\": null, \"end-ip\": \"0.0.0.0\", \"epg-name\": null, \"fabric-object\": 0, \"filter\": null, \"fqdn\": null, \"fsso-group\": [ ], \"interface\": [ ], \"list\": null, \"macaddr\": [ ], \"name\": \"host_005\", \"node-ip-only\": 0, \"obj-id\": null, \"obj-tag\": null, \"obj-type\": 9, \"oid\": 4649, \"organization\": null, \"policy-group\": null, \"sdn\": [ ], \"sdn-addr-type\": 0, \"sdn-tag\": null, \"start-ip\": \"0.0.0.0\", \"sub-type\": 0, \"subnet\": [ \"10.0.0.5\", \"255.255.255.255\" ], \"subnet-name\": null, \"tag-detection-level\": null, \"tag-type\": null, \"tagging\": null, \"tenant\": null, \"type\": 0, \"uuid\": \"2ea6e52a-d835-51ed-84f2-23efc39096ad\", \"wildcard\": [ \"0.0.0.0\", \"0.0.0.0\" ], \"wildcard-fqdn\": null }",
                   "flags": 0,
                   "key": "host_005",
                   "note": "Set interface to aplink1",
                   "oid": 4649,
                   "pkg_oid": 0,
                   "timestamp": 1681195844,
                   "user": "admin"
                 },
                 {
                   "act": 3,
                   "category": 140,
                   "config": "{ \"_image-base64\": null, \"allow-routing\": 0, \"associated-interface\": [ \"aplink1\" ], \"cache-ttl\": 0, \"clearpass-spt\": 0, \"color\": 22, \"comment\": null, \"country\": [ ], \"dirty\": 1, \"dynamic_mapping\": null, \"end-ip\": \"0.0.0.0\", \"epg-name\": null, \"fabric-object\": 0, \"filter\": null, \"fqdn\": null, \"fsso-group\": [ ], \"interface\": [ ], \"list\": null, \"macaddr\": [ ], \"name\": \"host_005\", \"node-ip-only\": 0, \"obj-id\": null, \"obj-tag\": null, \"obj-type\": 9, \"oid\": 4649, \"organization\": null, \"policy-group\": null, \"sdn\": [ ], \"sdn-addr-type\": 0, \"sdn-tag\": null, \"start-ip\": \"0.0.0.0\", \"sub-type\": 0, \"subnet\": [ \"10.0.0.5\", \"255.255.255.255\" ], \"subnet-name\": null, \"tag-detection-level\": null, \"tag-type\": null, \"tagging\": null, \"tenant\": null, \"type\": 0, \"uuid\": \"2ea6e52a-d835-51ed-84f2-23efc39096ad\", \"wildcard\": [ \"0.0.0.0\", \"0.0.0.0\" ], \"wildcard-fqdn\": null }",
                   "flags": 0,
                   "key": "host_005",
                   "note": "Color changed",
                   "oid": 4649,
                   "pkg_oid": 0,
                   "timestamp": 1681196213,
                   "user": "admin"
                 },
                 {
                   "act": 3,
                   "category": 140,
                   "config": "{ \"_image-base64\": null, \"allow-routing\": 0, \"associated-interface\": [ \"aplink1\" ], \"clearpass-spt\": 0, \"color\": 10, \"comment\": null, \"dirty\": 1, \"dynamic_mapping\": null, \"fabric-object\": 0, \"list\": null, \"macaddr\": [ ], \"name\": \"host_005\", \"node-ip-only\": 0, \"obj-tag\": null, \"obj-type\": 9, \"oid\": 4649, \"organization\": null, \"policy-group\": null, \"subnet\": [ \"10.0.0.5\", \"255.255.255.255\" ], \"subnet-name\": null, \"tag-detection-level\": null, \"tag-type\": null, \"tagging\": null, \"type\": 0, \"uuid\": \"2ea6e52a-d835-51ed-84f2-23efc39096ad\" }",
                   "flags": 0,
                   "key": "host_005",
                   "note": "Color changed a second time",
                   "oid": 4649,
                   "pkg_oid": 0,
                   "timestamp": 1681196478,
                   "user": "devops"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/dc_amer/_objrev/obj/firewall/address/host_005"
             }
           ]
         }        

How to revert to a specific object revision?
++++++++++++++++++++++++++++++++++++++++++++

Following example applies to firewall address object type.

It is showing how to revert an existing firewall address to a specific object
revision.

In fact, there's no specific *revert* operation. FortiManager is using the
``replace`` |fmg_api| method with datas obtained from the object revision to be
reverted with:

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "replace",
           "params": [
             {
               "data": {
                 "color": 4,
                 "name": "host_005",
                 "subnet": "10.0.0.5/32"
               },
               "revision note": "Reverted from revision 1",
               "url": "/pm/config/adom/dc_amer/obj/firewall/address/host_005"
             }
           ],
           "session": "{{ session }}"
         }        
         
   .. tab:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "name": "host_005"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/dc_amer/obj/firewall/address/host_005"
             }
           ]
         }

How to copy objects?
--------------------

Here the word *copy* refers to the action of copying an object from ADOM DB to
Device DB.

The target object isn't push down to the managed devices.

A proper install operation should be triggered.

The |fmg_api| endpoint used to trigger this copy operation isn't documented
hence we used the output of the following FortiManager debug command compile the
information shared in this section:

.. code-block:: text

   diagnose debug service main 255

When we issue the following FortiManager CLI command to trigger a copy
operation, we're getting the following output:

.. code-block:: text

   
   # execute fmpolicy copy-adom-object dc_helsinki "firewall address" foo_002 france
   Do you want to continue? (y/n)y

   Request [/bin/newcli:14057:3]:
   { "client": "\/bin\/newcli:14057", "id": 3, "method": "exec", "params": [{ "data": { "adom": 3273, "category": 140, "override_conflict": 1, "query_only": 0, "scope": [{ "oid": 3569}], "src_list": [{ "oid": 4827}]}, "url": "install\/global"}], "root": "securityconsole", "session": 12207}
   Waiting for task 1347...
   Task completed      

In the following example, we copy the ``foo_002``  firewall address from the
``dc_helsinki`` ADOM to the devices belonging to the ``france`` device group:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "dc_helsinki",
                 "category": 140,
                 "override_conflict": 1,
                 "query_only": 0,
                 "scope": [
                   {
                     "name": "france"
                   }
                 ],
                 "src_list": [
                   {
                     "oid": 4827
                   }
                 ]
               },
               "url": "/securityconsole/install/global"
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
                 "task": 1350
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/securityconsole/install/global"
             }
           ]
         }

FortiManager will return a task ID (``task`` attribute) but won't run it in the
background. We have to wait for the end of the request.

The request is having a lot of numerical information:

- The ``category`` attribute

  - ``140`` is the category ID for the ``firewall address`` table

  - Unfortunately, we cannot use the string ``"firewall address"`` as shown
    below:

    .. code-block:: json
       
       {
         "category": "firewall address"
       }

    We have to use an id

    How to get it?

    To get the category ID of the ``firewall address`` table:

    .. tab-set::

       .. tab-item:: REQUEST

          .. code-block:: json

             {
               "id": 3,
               "method": "get",
               "params": [
                 {
                   "option": [
                     "syntax"
                   ],
                   "url": "/pm/config/adom/dc_helsinki/obj/firewall/address"
                 }
               ],
               "session": "{{session}}"
             }
             
    In the response, you have to get:

    .. code-block:: text

       .result[0]["data"]["firewall address"]["category"]

- ``src_list`` attribute
 
  - This list contains the OID of the objects to copy
  - For the ``140`` category (``firewall address``) the ``src_list`` list
    contain OID of firewall address objects
  - How to get the OID of a firewall address?

    .. tab-set::

       .. tab-item:: REQUEST

          .. code-block:: json

             {
               "id": 3,
               "method": "get",
               "params": [
                 {
                   "fields": [
                     "name"
                   ],
                   "loadsub": 0,
                   "url": "/pm/config/adom/dc_helsinki/obj/firewall/address/foo_002"
                 }
               ],
               "session": "7bQB94D0zHu7I9EGtwIbQJEbrcH7qRBI/hwWbqrP/RVUWLd8h1PiFyTD+brojmELiV/rVHcSdYX2CqTAtEcmhg=="
             }

       .. tab-item:: RESPONSE

          .. code-block:: json

             {
               "id": 3,
               "result": [
                 {
                   "data": {
                     "name": "foo_002",
                     "oid": 4827
                   },
                   "status": {
                     "code": 0,
                     "message": "OK"
                   },
                   "url": "/pm/config/adom/dc_helsinki/obj/firewall/address/foo_002"
                 }
               ]
             }

You can use the usual ``scope``:

.. code-block:: json

   {
     "scope": [
        {
          "name": "device_group_001",
        },
        {
          "name": "device_group_002",
        },
        {
          "name": "device_001",
          "vdom": "vd_001"
        },        
        {
          "name": "device_001",
          "vdom": "vd_002"
        },
        {
           "...": "..."
        }
     ]
   }

Per-device mapping
------------------

This is a mechanism where FortiManager can push the same object to multiple
devices, but with different values.

For instance, you could have the `net_branch_lan` firewall address to represent the internal network of your remote sites and you would like it to be with the 
``10.0.1.0/24`` for site #1, ``10.0.2.0/24`` for site #2, etc.

The per-device mapping feature isn't available for all objects.

.. note::

   - CLI Template could be use to overcome the lack of per-device mapping 
     support.

Per-device mapping for firewall.address
+++++++++++++++++++++++++++++++++++++++

How to get per-device mapping info for a firewall address obejct?
_________________________________________________________________

The following example shows how to get the per-device mapping info for the
``net_branch_lan`` firewall address from the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
        
         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

      .. note::

         - To get the per-device mapping info, you just need to append the 
           ``dynamic_mapping`` subtable in the ``url``

   .. tab-item:: RESPONSE

      .. code-block:: json
                 
         {
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "_scope": [
                     {
                       "name": "dev_001",
                       "vdom": "root"
                     }
                   ],
                   "allow-routing": "disable",
                   "clearpass-spt": "unknown",
                   "color": 0,
                   "dirty": "dirty",
                   "fabric-object": "disable",
                   "macaddr": [],
                   "node-ip-only": "disable",
                   "obj-type": "ip",
                   "oid": 5584,
                   "route-tag": 0,
                   "subnet": [
                     "10.0.1.0",
                     "255.255.255.0"
                   ],
                   "type": "ipmask",
                   "unset attrs": [
                     "associated-interface"
                   ],
                   "uuid": "6c108da4-d257-51ee-25be-c01339bbfdb8"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping"
             }
           ]
         }

      .. note::

         - The ``net_branch_lan`` is having a single per-device mapping for the
           ``dev_001`` device and its ``root`` VDOM

         - When FortiManager will push the ``net_branch_lan`` against the
           ``dev_001.root`` device, it will use the IP address from the 
           ``subnet`` block

         - When FortiManager will push the ``net_branch_lan`` against the
           ``dev_002.root`` device, it will use the IP address from the 
           ``subnet`` block of the ``net_branch_lan`` object itself, because 
           there's no per-device mapping for this device.

How to add a per-device mapping to a firewall address object?
_____________________________________________________________

The following example shows how to add a new per-device mapping entry for the
``dev_002`` device and its ``root`` VDOM, for the ``net_branch_lan`` firewall
address from the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "_scope": [
                   {
                     "name": "dev_002",
                     "vdom": "root"
                   }
                 ],
                 "subnet": [
                   "10.0.2.0",
                   "255.255.255.0"
                 ]
               },
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping"
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
                 "_scope": [
                   {
                     "name": "dev_002",
                     "vdom": "root"
                   }
                 ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping"
             }
           ]
         }

      .. note::

         - FortiManager confirms the creation of the new per-device mapping
           entry returning its ``_scope`` attribute

You can add multiple per-device mapping entries in a single request.

The following example add per-device mapping entries for the ``dev_003`` and ``dev_004`` devices and their ``root`` VDOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": [
                 {
                   "_scope": [
                     {
                       "name": "dev_003",
                       "vdom": "root"
                     }
                   ],
                   "subnet": [
                     "10.0.3.0",
                     "255.255.255.0"
                   ]
                 },
                 {
                   "_scope": [
                     {
                       "name": "dev_004",
                       "vdom": "root"
                     }
                   ],
                   "subnet": [
                     "10.0.4.0",
                     "255.255.255.0"
                   ]
                 }
               ],
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping"
             }
           ],
           "session": "{{session}}",
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
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping"
             }
           ]
         }

      .. note::

         - For multiple per-device mapping entries, FortiManager confirms their 
           creation with a generic *OK* response

How to delete a per-device mapping from a firewall address object?
__________________________________________________________________

The following example shows how to delete the per-device mapping entry for the
``dev_004`` device and its ``root`` VDOM, for the ``net_branch_lan`` firewall
address from the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json         

         {
           "id": 3,
           "method": "delete",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping/dev_004/root"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping/dev_004/root"
             }
           ]
         }          

You can delete multiple per-device mapping entries in a single request.

The following example delete per-device mapping entries for the ``dev_003`` and 
``dev_002`` devices and their ``root`` VDOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "delete",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping/dev_003/root"
             },
             {
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping/dev_002/root"
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
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping/dev_03/root"
             },
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/firewall/address/net_branch_lan/dynamic_mapping/dev_002/root"
             }
           ]
         }

Replacement Message Group
-------------------------

How to get the default Replacement Message Groups?
++++++++++++++++++++++++++++++++++++++++++++++++++

Caught in #1040582.

The following example shows how to get the default Replacement Message Group for
the ``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 2,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/_system/replacemsg"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 2,
           "result": [
             {
               "data": [
                 {
                   "carrier": 0,
                   "groups": [
                     "default",
                     "utm"
                   ],
                   "msg-types": [
                     {
                       "_disp_desc": "admin_post_admin-disclaimer-text_desc",
                       "_disp_name": "admin_post_admin-disclaimer-text",
                       "...": "..."
                     },
                     "...",
                   ],
                   "...": "...",
                 },
                 "..."
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/dc_emea/obj/_system/replacemsg"
             }
           ]
         }      
