ADOM management
===============

ADOM creation
-------------

How to create an ADOM?
++++++++++++++++++++++

The following request creates ADOM ``NEW_ADOM_001`` to manage FortiGate with
version 6.2:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "add",
     "params": [
       {
         "data": {
           "desc": "This is a new ADOM",
           "mr": 2,
           "name": "NEW_ADOM_001",
           "os_ver": "6.0"
         },
         "url": "/dvmdb/adom"
       }
     ],
     "session": "tVdUjweRYU4vl6xLy7OMHcC7YzorWKDIJVIEElX6g0xrUqjJyJUfg2mqTsPfYm/+kTNN1RuGMRS/n/krgOZ7EA==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "name": "NEW_ADOM_001"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom"
       }
     ]
   }

How to create an ADOM with options not available in symbolic format?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

At the time of this writing, the ADOM option *Default Device Selection for
Install* exposed in the FortiManager GUI when creating an ADOM isn't having a
corresponding symbolic value to be used with the FortiManager API in the
corresponding ``flags`` attribute.

.. admonition:: Internal Reference

   .. code:: text
      
      0600155

The alternative is to work with a numerical ``flags`` attribute as shown below:

#. Using FortiManager GUI, create a new ADOM, uncheck the *Default Device
   Selection for Install* ADOM option 

#. Using FortiManager API, ``get`` the ADOM and look at the returned ``flags``
   attribute; don’t enable the ``verbose`` attribute when doing the ``get``:

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json

            {
              "id": 3,
              "method": "get",
              "params": [
                {
                  "fields": [
                    "flags"
                  ],
                  "url": "/dvmdb/adom/dc_copenhagen"
                }
              ],
              "session": "{{ session }}"
            }

      .. tab-item:: RESPONSE

         .. code-block:: json

            {
              "id": 3,
              "result": [
                {
                  "data": {
                    "flags": 2120,
                    "name": "dc_copenhagen",
                    "oid": 3326
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/dc_copenhagen"
                }
              ]
            }

#. This returned ``flags`` attribute encodes all the ADOM options along with the
   *Default Device Selection for Install* one

#. You can use it to create a new ADOM:

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-blocK:: json

            {
              "id": 3,
              "method": "add",
              "params": [
                {
                  "data": {
                    "flags": 2120,
                    "mr": 4,
                    "name": "dc_roubaix",
                    "os_ver": "7.0",
                    "restricted_prds": "fos"
                  },
                  "url": "/dvmdb/adom"
                }
              ],
              "session": "{{ adom }}"
            }
            
      .. tab-item:: RESPONSE

         .. code-block:: json

            {
              "id": 3,
              "result": [
                {
                  "data": {
                    "name": "dc_roubaix"
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom"
                }
              ]
            }

How to create an ADOM with existing managed devices?
++++++++++++++++++++++++++++++++++++++++++++++++++++

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "add",
     "params": [
       {
         "data": {
           "desc": "This is a test",
           "mr": 4,
           "name": "demo_020",
           "object member": [
             {
               "name": "foo_001",
               "vdom": "root"
             },
             {
               "name": "foo_002",
               "vdom": "root"
             }
           ],
           "os_ver": "6.0"
         },
         "url": "/dvmdb/adom"
       }
     ],
     "session": "shoqp0HeZBTYl6jGIscHlnHMfeANXlgIipiZ50qAu7qbztu6oXLU2yRjOAK2e01shwwsZAUsxEo/Oif6ywSgWQ==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "name": "demo_020"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom"
       }
     ]
   }

How to clone an ADOM?
+++++++++++++++++++++

I'm in the ``dc_amer`` ADOM, but I want to clone the ``root`` ADOM to a new
``root_002`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": "1",
           "create task": {
             "adom": "dc_amer",
             "name": "clone ADOM root to root_002"
           },
           "method": "clone",
           "params": [
             {
               "url": "/dvmdb/adom/root",
               "data": {
                 "name": "root_002"
               }
             }
           ],
           "session": "{{session}}"
         }
    
      .. note::

         - You can omit the ``create task`` code.
         - In this case, the request will return only when the ``clone`` operation will complete.
         - Otherwise, you will have, as usual, to monitor the progress and the final status of the returned task 

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "task": 8
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               }
             }
           ]
         }  

ADOM deletion
-------------

How to where used an ADOM?
++++++++++++++++++++++++++

You can delete an ADOM if it is having managed devices, device groups or is assigned with FortiManager administrators or Global objects and policy packages.

The *where used* operation allows to identify all the objects referencing the 
ADOM you want to delete.

The following example shows how to where used the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/dvmdb/adom/demo/where used"
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
                 "cmdb": [
                   {
                     "attr": "adom",
                     "category": 18,
                     "last use": 1,
                     "mapping_name": "system admin user",
                     "mattr": "userid",
                     "mkey": "admin_001"
                   }
                 ],
                 "dvmdb": [
                   {
                     "attr": "object member",
                     "category": 2,
                     "last use": 0,
                     "mapping_name": "device_group",
                     "mattr": "name",
                     "mkey": "dev_grp_001"
                   },
                   {
                     "attr": "object member",
                     "category": 2,
                     "last use": 0,
                     "mapping_name": "device_group",
                     "mattr": "name",
                     "mkey": "dev_grp_002"
                   },
                   {
                     "attr": "object member",
                     "category": 2,
                     "last use": 0,
                     "mapping_name": "device_group",
                     "mattr": "name",
                     "mkey": "dev_grp_003"
                   },
                   {
                     "attr": "object member",
                     "category": 0,
                     "last use": 0,
                     "mapping_name": "device",
                     "mattr": "name",
                     "mkey": "dev_001"
                   },
                   {
                     "attr": "object member",
                     "category": 0,
                     "last use": 0,
                     "mapping_name": "device",
                     "mattr": "name",
                     "mkey": "dev_002"
                   },
                   {
                     "attr": "object member",
                     "category": 0,
                     "last use": 0,
                     "mapping_name": "device",
                     "mattr": "name",
                     "mkey": "dev_003"
                   }
                 ],
                 "provider": [
                   {
                     "attr": "assignment",
                     "category": 0,
                     "last use": 0,
                     "mapping_name": "policy",
                     "mattr": "name",
                     "mkey": "g_ppkg_001"
                   }
                 ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/where used"
             }
           ]
         }

      .. note::

         - The ``demo`` ADOM is referenced by:

           - The ``admin_001`` FortiManager administrator

           - The ``dev_grp_001``, ``dev_grp_002`` and ``dev_grp_002`` device 
             groups

           - The ``dev_001``, ``dev_002`` and ``dev_003`` managed devices

           - The ``g_ppkg_001`` Global Policy Package

      .. warning::

         - To delete this ADOM, you will need to, at least,  delete the 
           ``dev_001``, ``dev_002`` and ``dev_003`` managed devices

How to delete an ADOM?
++++++++++++++++++++++

Forced ADOM deletion
____________________

This applies when your ADOM is still referenced by objects, and you don't have time or inclination to remove those references. 

Refer to the section :ref:`How to where used an ADOM?` to identify which objects are referencing your ADOM.

To delete an ADOM, even using the forced method, you must first  delete its managed devices!

Otherwise you'll receive a response like:

.. tab-set::

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "status": {
                 "code": -20063,
                 "message": "Unable to delete because one or more devices in Device Manager"
               },
               "url": "/dvmdb/adom/demo"
             }
           ]
         }

The following example shows how to delete an ADOM using the forced method:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "delete",
           "params": [
             {
               "confirm": 1,
               "option": "force",
               "url": "/dvmdb/adom/demo"
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
               "url": "/dvmdb/adom/demo"
             }
           ]
         }    

.. note::

   - The forced deletion will:

     - Delete FortiManager administrators referencing the deleted ADOM
     - Will delete all device groups which were still within the deleted ADOM
     - Will remove the ADOM from the Global Policy Packages's list of assigned 
       ADOMs

How to move a device/VDOM in a new ADOM?
----------------------------------------

To move device ``foo_003`` and its VDOM ``root`` in the ADOM ``demo_020``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "method": "add",
     "create task": {
       "adom": "demo_020",
     },
     "params": [
       {
         "data": [
           {
             "name": "foo_003",
             "vdom": "root"
           }
         ],
         "url": "/dvmdb/adom/demo_020/object member"
       }
     ],
     "session": "LcJsZ5G6ItjdbEUqiLMEr/X1uRzFynmvckQgL5QwBWSf2WNs3SlUpdju9bvZq+JlKj3Pgg7jY8Xpfm9y/NpWEg==",
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "task": 612
         },
         "status": {
           "code": 0,
           "message": "OK"
         }
       }
     ]
   }

How to get an ADOM checksum?
----------------------------

See section :ref:`*devinfo*`.

How to manage the ADOM and Device Display Options?
--------------------------------------------------

Starting with FMG 7.0.1 (#0716016), FMG JSON RPC API introduces new endpoints.

The only important item of interest is that the prefix URL also changed from:

.. code-block:: 

   https://{fmg_ip}/jsonrpc

to:

.. code-block::

   https://{fmg_ip}/jsonrpc-ui

The new endpoints:

To get the display options for a specific ADOM
++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: json

   {
      "id": 10,
      "session": "xxxxxxxxxxx",
      "method": "get",
      "params": [
        {
          "url": "/ui/config/adom/root/customize"
        }
      ]
   }

To set the display options for a specific ADOM
++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: json

   {
     "id": 10,
     "session": "xxxxxxxxxxx",
     "method": "set",
     "params": [
       {
         "url": "/ui/config/adom/root/customize",
         "data": [
           {
             "pnoCustomize": ["fws", "wafprof"],
             "dvmCustomize": ["dashboard", "interface"]
           }
         ]
       }
     ]
   }

.. note::

   Not that it's also possible to set the ADOM display options for all devices
   here (see ``dvmCustomize`` attribute).

To get the display options for the global ADOM
++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: json

   {
     "id": 10,
     "session": "xxxxxxxxxxx",
     "method": "get",
     "params": [
       {
         "url": "/ui/config/global/customize"
       }
     ]
   }

To set the display options for the global ADOM
++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: json

   {
     "id": 10,
     "session": "xxxxxxxxxxx",
     "method": "set",
     "params": [
       {
         "url": "/ui/config/global/customize",
         "data": [
           {
             "pnoCustomize": ["fws", "wafprof"],
           }
         ]
       }
     ]
   }

To get the display options for a specific device
++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: json

   {
     "id": 10,
     "session": "xxxxxxxxxxx",
     "method": "get",
     "params": [
       {
         "url": "/ui/config/adom/root/device/FGT100000/customize"
       }
     ]
   }

To set the display options for a specific device
++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: json

   {
     "id": 10,
     "session": "xxxxxxxxxxx",
     "method": "set",
     "params": [
       {
         "url": "/ui/config/adom/root/device/FGT100000/customize",
         "data": [
           {
             "customize": ["KW_local", "dashboard", "interface", "dhcpsvr_all", "modem", "snmp", "replacemsg", "staticroute_all"]
           }
         ]
       }
     ]
   }

To get the display options for a specific VDOM
++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: json

   {
     "id": 10,
     "session": "xxxxxxxxxxx",
     "method": "get",
     "params": [
       {
         "url": "/ui/config/adom/root/device/FGT100001/vdom/root/customize"
       }
     ]
   }

.. code-block:: json

   {
     "id": 10,
     "session": "xxxxxxxxxxx",
     "method": "set",
     "params": [
       {
         "url": "/ui/config/adom/root/device/FGT100000/vdom/root/customize",
         "data": [
           {
             "customize": ["KW_local", "dashboard", "interface", "dhcpsvr_all", "modem", "snmp", "replacemsg", "staticroute_all"]
           }
         ]
       }
     ]
   }

How to figure out whether an ADOM is used by some Global Policy Packages from Global ADOM?
------------------------------------------------------------------------------------------

We can use the |fmg_api| url:

.. code-block::

   /pm/config/adom/{adom}/_adom/options

In this first example, our ADOM ``demo`` is simply not referenced by any Global
Policy Packages:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/pm/config/adom/demo/_adom/options"
       }
     ],
     "session": "XmlYqsuf6Z2meBVDBZJGTlBaFPQUxOH0Utc//OWid+NwfB6wr60cNqlrU/6zFO9STLC/bw9t+T9u7rxOrg/fRw==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": [],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/demo/_adom/options"
       }
     ]
   }
   
In this second example, our ADOM ``demo`` is assigned to Global Policy Package
``default``: 

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/pm/config/adom/demo/_adom/options"
       }
     ],
     "session": "o0r5MVWBIzynzu+vdkyYXRUzeK4VlFE86mal8JMK2E/TBFSaY+CEoAaglXHwYL9082ukcNgq4UIFXwGkbUrqQw==",
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
             "name": "__gpkg__3784",
             "oid": 3763,
             "pkg list": []
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/demo/_adom/options"
       }
     ]
   }

In the above output, we can see that ADOM ``demo`` is assigned with a global
policy package with OID ``3784``.

.. note::
  
   We can obtain the corresponding global policy package name using the following FMG CLI command:

   .. code-block::

      execute fmpolicy print-adom-package Global 1 ?

   In our case, we're getting the following output:

   .. code-block::

        ID	      <package name>
      3784	      name=default, pathname=default

   This output confirms our ADOM ``demo`` is assigned with Global Policy
   Package ``default``.

.. note::

   We can also obtain that same information using the |fmg_api| url:      

   .. code-block:: text

      /pm/pkg/global

   For instance:

   **REQUEST:**

   .. code-block:: json
     
     {
       "id": 3,
       "method": "get",
       "params": [
         {
           "url": "/pm/pkg/global"
         }
       ],
       "session": "v8G4nDQU8DE/y3MIOjoizD8tpS3hF1deP7LvaFx3VtEDeLWrnKkR+ccxlYlajW5/UgmGZ+NPwDQ3q6lRbDju4Q==",
       "verbose": 1
     }

   But we will have to parse the returned list of policy package in order to
   select the one with the OID of interest (``filter`` doesn't work on url
   ``/pm/pkg/global``). 

In this third example, we have:

- Global Policy Package ``g_ppkg_001`` is assigned with policy package
  ``ppkg_001`` from ADOM ``demo``

- Global Policy Package ``g_ppkg_002`` is assigned with policy package
  ``ppkg_002`` from ADOM ``demo``  

.. note:: 

   This is possible since FortiManager 7.0.1.

**REQUEST:**

.. code-block:: json
     
   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/pm/config/adom/demo/_adom/options"
       }
     ],
     "session": "3ibSO2PJgH4HZiTJbefN4Y85hs2o1w7RXi3Qas/LewtkQGrj6yLWiak5wrwn3lewnUpurFp0ku+zYti9V3zxew==",
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
             "name": "__gpkg__3832",
             "oid": 3773,
             "pkg list": [
               {
                 "name": "ppkg_002",
                 "oid": 3767
               }
             ],
             "specify_assign_pkg_list": "enable"
           },
           {
             "name": "__gpkg__3830",
             "oid": 3775,
             "pkg list": [
               {
                 "name": "ppkg_001",
                 "oid": 3765
               }
             ],
             "specify_assign_pkg_list": "enable"
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/demo/_adom/options"
       }
     ]
   }   

In this fourth example, we have:

- Global Policy Package ``g_ppkg_001`` is assigned to ADOM ``demo`` with policy
  package exclusion set for policy packages ``default`` and ``ppkg_002``

- Global Policy Package ``g_ppkg_002`` is assigned to ADOM ``demo`` with policy
  package exclusion set for policy packages ``default`` and ``ppkg_001``  

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/pm/config/adom/demo/_adom/options"
       }
     ],
     "session": "9qjuMZBW+8nQEwxgh6FAfBfkB7xGNPtAmRc7joj406vIo2yha/YcaJzG85olGPoAAdfL7mUGCRokr6ULrk4WTQ==",
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
             "assign_excluded": "enable",
             "name": "__gpkg__3832",
             "oid": 3773,
             "pkg list": [
               {
                 "name": "default",
                 "oid": 3746
               },
               {
                 "name": "ppkg_001",
                 "oid": 3765
               }
             ],
             "specify_assign_pkg_list": "enable"
           },
           {
             "assign_excluded": "enable",
             "name": "__gpkg__3830",
             "oid": 3775,
             "pkg list": [
               {
                 "name": "default",
                 "oid": 3746
               },
               {
                 "name": "ppkg_002",
                 "oid": 3767
               }
             ],
             "specify_assign_pkg_list": "enable"
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/demo/_adom/options"
       }
     ]
   }
   
How to get the ADOM limit details?
----------------------------------

This call was captured during a GUI debug of recent FMG, but we're not able to
get anything else, in term of output, than the one presented below:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "get",
     "params": [
       {
         "url": "/dvmdb/query/adomlimit"
       }
     ],
     "session": "USTJ6sCgfrmrv8JvbZAaYFRapMy6zKNMu5F7yOs7LATLMz9mgcTOoVIy1x5D9iWi8n/A2+LkhPAwvpI4OXV1LA==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "max": 0,
           "warning": 0
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/query/adomlimit"
       }
     ]
   }

ADOM Revision
-------------

How to get list of ADOM revisions?
++++++++++++++++++++++++++++++++++

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "get",
     "params": [
       {
         "url": "/dvmdb/adom/demo/revision"
       }
     ],
     "session": "v/iHml/z33LbEmRgQ9MUbOpk7IQ+ncRag86In+8CscssR+5ppAH5DmSlT1tMTB//UEPzhDjbrYt1bIHFzXBXaQ==",
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
             "created_by": "devops",
             "created_time": 1626787333,
             "desc": "Copy to devices SUCCESS on Tue Jul 20 15:22:13 2021\n",
             "locked": 0,
             "name": "pre_tc_001",
             "oid": 193,
             "version": 1
           },
           {
             "created_by": "devops",
             "created_time": 1626787398,
             "desc": "Copy to devices SUCCESS on Tue Jul 20 15:23:18 2021\n",
             "locked": 0,
             "name": "pre_tc_001",
             "oid": 194,
             "version": 2
           },
           {
             "created_by": "devops",
             "created_time": 1626787566,
             "desc": "Copy to devices SUCCESS on Tue Jul 20 15:26:06 2021\n",
             "locked": 0,
             "name": "main_tc_001",
             "oid": 195,
             "version": 3
           },
           {
             "created_by": "devops",
             "created_time": 1626793953,
             "desc": "Copy to devices SUCCESS on Tue Jul 20 17:12:33 2021\n",
             "locked": 0,
             "name": "pre_tc_001",
             "oid": 196,
             "version": 4
           },
           {
             "created_by": "devops",
             "created_time": 1626794001,
             "desc": "Copy to devices SUCCESS on Tue Jul 20 17:13:21 2021\n",
             "locked": 0,
             "name": "main_tc_001",
             "oid": 197,
             "version": 5
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom/demo/revision"
       }
     ]
   }

How to diff an ADOM revision with current configuration?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

First, we have to start the diff process by obtaining a token.

We want to diff the current configuration for ADOM `demo` with revision number
3:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "data": {
           "dst": "adom/demo",
           "src": "adom/demo/revision/3"
         },
         "url": "/cache/diff/start"
       }
     ],
     "session": "u7BuIVsGJhGLOvVhsnRFoM1jIpPdq/0kArzP1+RUuMKWeNXr8Gn/IJ5qCZiMfZwf66DAabsO+HhOkNT2nICZoQ==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "token": "tyPyMomT3WqkYN8/WtD6zg=="
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/cache/diff/start"
       }
     ]
   }

With the returned ``token``, we can now ask for the summary report.
We have to keep asking for it as long as the ``percent`` attribute isn't
returned with value ``100``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "token": "tyPyMomT3WqkYN8/WtD6zg==",
         "url": "/cache/diff/get/summary"
       }
     ],
     "session": "u7BuIVsGJhGLOvVhsnRFoM1jIpPdq/0kArzP1+RUuMKWeNXr8Gn/IJ5qCZiMfZwf66DAabsO+HhOkNT2nICZoQ==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "obj": {
             "changed": 1,
             "summary": [
               {
                 "category": 142,
                 "changed": [
                   {
                     "name": "src_grp_001",
                     "timestamp": 1626794085,
                     "user": "devops"
                   }
                 ]
               }
             ]
           },
           "percent": 37,
           "pkg": {
             "changed": 1,
             "summary": [
               {
                 "category": 0,
                 "changed": [
                   {
                     "name": "ppkg_001",
                     "percent": 100,
                     "scope member": [
                       {
                         "name": "device_01",
                         "vdom": "vd_01"
                       }
                     ],
                     "timestamp": 1626795461,
                     "user": "admin"
                   }
                 ]
               }
             ]
           }
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/cache/diff/get/summary"
       }
     ]
   }

The returned ``percent`` attribute isn't ``100``. So we have to keep asking...

Finally, when ``percent`` attribute reaches ``100``, we can ask for the
detailed object diff report:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "token": "tyPyMomT3WqkYN8/WtD6zg==",
         "url": "cache/diff/get/detail/obj/all objs"
       }
     ],
     "session": "u7BuIVsGJhGLOvVhsnRFoM1jIpPdq/0kArzP1+RUuMKWeNXr8Gn/IJ5qCZiMfZwf66DAabsO+HhOkNT2nICZoQ==",
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
             "category": 142,
             "data": [
               {
                 "_image-base64": null,
                 "allow-routing": 0,
                 "color": 1,
                 "comment": "Created with FortiManager Ansible",
                 "diff_flag": 2,
                 "exclude": 0,
                 "exclude-member": [],
                 "member": {
                   "n": [
                     "\"host_10.0.0.1\"",
                     "\"host_10.0.2.1\"",
                     "\"host_10.0.4.1\""
                   ],
                   "o": [
                     "\"host_10.0.0.1\"",
                     "\"host_10.0.2.1\""
                   ]
                 },
                 "name": "src_grp_001",
                 "timestamp": 1626787596,
                 "user": "devops",
                 "uuid": "f2faf34a-e94d-51eb-1263-26d6de6ec083",
                 "visibility": 1
               }
             ]
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "cache/diff/get/detail/obj/all objs"
       }
     ]
   }

We can also ask for the detailed firewall policy diff report:

**REQUEST:**

.. code-block:: json

   
    "id": 1,
    "jsonrpc": "1.0",
    "method": "exec",
    "params": [
      {
        "token": "waIVmBKE/i1jGN8NJUV6Zw==",
        "url": "/cache/diff/get/summary/pkg/ppkg_001"
      }
    ],
    "session": "giMkvu5P0wHNQ2qlN+YvuqYZTR+xvrmSWKUZNlAF01QxDVeB2OJa9U+9BlwIAwYwc1GGxYYBLykGkxsRED5f2w==",
    "verbose": 1
   
**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "obj": {
             "changed": 1,
             "summary": [
               {
                 "category": 181,
                 "changed": [
                   {
                     "name": 6,
                     "obj seq": 2,
                     "timestamp": 1626795461,
                     "user": "admin"
                   }
                 ],
                 "size": 4
               },
               {
                 "category": 1103,
                 "size": 1
               }
             ]
           },
           "percent": 100
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/cache/diff/get/summary/pkg/ppkg_001"
       }
     ]
   }

Here as well, it will be required to wait for the main ``percent`` attribute to
get returned with value ``100``.

The category ``181`` is for the ``firewall policy``. This is why we're asking
for the firewall policy report detail:

**REQUEST:**

.. code-block:: json

  {
    "id": 1,
    "jsonrpc": "1.0",
    "method": "exec",
    "params": [
      {
        "fields": [
          "action",
          "app-category",
          "app-group",
          "application",
          "application-list",
          "auto-asic-offload",
          "av-profile",
          "capture-packet",
          "comments",
          "diffserv-forward",
          "diffserv-reverse",
          "diffservcode-forward",
          "disclaimer",
          "dlp-sensor",
          "dnsfilter-profile",
          "dstaddr",
          "dstaddr-negate",
          "dstintf",
          "emailfilter-profile",
          "fixedport",
          "fsso-groups",
          "global-label",
          "groups",
          "icap-profile",
          "inspection-mode",
          "internet-service",
          "internet-service-custom",
          "internet-service-custom-group",
          "internet-service-group",
          "internet-service-id",
          "internet-service-negate",
          "internet-service-src",
          "internet-service-src-custom",
          "internet-service-src-custom-group",
          "internet-service-src-group",
          "internet-service-src-id",
          "internet-service-src-negate",
          "ippool",
          "ips-sensor",
          "label",
          "logtraffic",
          "logtraffic-start",
          "name",
          "nat",
          "per-ip-shaper",
          "policyid",
          "poolname",
          "profile-group",
          "profile-protocol-options",
          "profile-type",
          "replacemsg-override-group",
          "schedule",
          "service",
          "service-negate",
          "srcaddr",
          "srcaddr-negate",
          "srcintf",
          "ssl-ssh-profile",
          "status",
          "tos",
          "tos-mask",
          "traffic-shaper",
          "traffic-shaper-reverse",
          "url-category",
          "users",
          "utm-status",
          "uuid",
          "voip-profile",
          "vpntunnel",
          "waf-profile",
          "webfilter-profile",
          "webproxy-forward-server",
          "_created timestamp",
          "_last-modified-by",
          "_modified timestamp",
          "extra info",
          "scope member",
          "visibility"
        ],
        "token": "waIVmBKE/i1jGN8NJUV6Zw==",
        "url": "/cache/diff/get/detail/pkg/ppkg_001/firewall/policy"
      }
    ],
    "session": "giMkvu5P0wHNQ2qlN+YvuqYZTR+xvrmSWKUZNlAF01QxDVeB2OJa9U+9BlwIAwYwc1GGxYYBLykGkxsRED5f2w==",
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
             "action": 1,
             "app-category": [],
             "app-group": [],
             "application": [],
             "application-list": [],
             "auto-asic-offload": {
               "n": 1,
               "o": 1
             },
             "av-profile": [],
             "capture-packet": 0,
             "comments": {
               "n": "Created with FortiManager Ansible\nTest #001",
               "o": "Created with FortiManager Ansible"
             },
             "diff_flag": 2,
             "diffserv-forward": 0,
             "diffserv-reverse": 0,
             "diffservcode-forward": "000000",
             "disclaimer": 0,
             "dlp-sensor": [],
             "dnsfilter-profile": [],
             "dstaddr": [
               "\"dst_grp_001\""
             ],
             "dstaddr-negate": 0,
             "dstintf": [
               "\"any\""
             ],
             "emailfilter-profile": [],
             "fixedport": 0,
             "fsso-groups": [],
             "global-label": "section_title_002",
             "groups": [],
             "icap-profile": [],
             "inspection-mode": 1,
             "internet-service": 0,
             "internet-service-custom": [],
             "internet-service-custom-group": [],
             "internet-service-group": [],
             "internet-service-id": [],
             "internet-service-negate": 0,
             "internet-service-src": 0,
             "internet-service-src-custom": [],
             "internet-service-src-custom-group": [],
             "internet-service-src-group": [],
             "internet-service-src-id": [],
             "internet-service-src-negate": 0,
             "ippool": 0,
             "ips-sensor": [],
             "label": null,
             "logtraffic": 3,
             "logtraffic-start": 0,
             "name": "Test rule #001",
             "nat": 0,
             "obj seq": 2,
             "per-ip-shaper": [],
             "policyid": 6,
             "poolname": [],
             "profile-group": [],
             "profile-protocol-options": {
               "n": [],
               "o": [
                 "default"
               ]
             },
             "profile-type": 0,
             "replacemsg-override-group": [],
             "schedule": [
               "\"always\""
             ],
             "service": [
               "\"svc_grp_001\""
             ],
             "service-negate": 0,
             "srcaddr": [
               "\"src_grp_001\""
             ],
             "srcaddr-negate": 0,
             "srcintf": [
               "\"any\""
             ],
             "ssl-ssh-profile": [
               "\"no-inspection\""
             ],
             "status": 1,
             "timestamp": 1626795461,
             "tos": "0x00",
             "tos-mask": "0x00",
             "traffic-shaper": [],
             "traffic-shaper-reverse": [],
             "url-category": [],
             "user": "admin",
             "users": [],
             "utm-status": 0,
             "uuid": "03cb89e0-e96d-51eb-e0ea-e0db81318e00",
             "voip-profile": [],
             "vpntunnel": [],
             "waf-profile": [],
             "webfilter-profile": [],
             "webproxy-forward-server": []
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/cache/diff/get/detail/pkg/ppkg_001/firewall/policy"
       }
     ]
   }

Always good to end the diff task:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "token": "tyPyMomT3WpgsFsoTYvmQg==",
         "url": "cache/diff/end"
       }
     ],
     "session": "fLoOiuwn9alZYE/UhPil1anzDZ4xwtlJthKeieG9cXdnwswu0JcWIHw+Cb97+oRv1uIhjj9yfyYi/srsSVMOCw==",
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
         "url": "cache/diff/end"
       }
     ]
   }

How to revert an ADOM Revision?
+++++++++++++++++++++++++++++++

Reverting to a specific ADOM Revision version is as simple as cloning it.

First, you need to get the ``version`` of the ADOM Revision you want to revert.
See section :ref:`How to get list of ADOM revisions?`.

Then to revert ADOM Revision version ``1`` from the ``dc_emea`` ADOM, you can
use the following ``clone`` operation: 

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "clone",
           "params": [
             {
               "data": {
                 "created_by": "admin",
                 "created_time": 1697462692,
                 "desc": "Revert of ADOM Revision #1",
                 "locked": 0,
                 "name": "Restored-rev_001_002"
               },
               "url": "/dvmdb/adom/dc_emea/revision/1"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - ``created_time`` is current time in epoch format
         - ``locked`` is when you want to protect the cloned ADOM Revision from
           deletion. 

           If set to ``1``, the created ADOM Revision will be cloned and
           couldn't be deleted.

   .. tab-item:: RESPONSE

      .. code-block:: json    

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "version": 4
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/dc_emea/revision/1"
             }
           ]
         }
      
      .. note::

         - The returned ``version`` is the version of the created ADOM Revision

ADOM Upgrade
------------

How to upgrade an ADOM?
+++++++++++++++++++++++

Caught in #0764328.

The following example shows how to upgrade the `demo` ADOM.

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {  
           "id": 3,
           "method": "exec",
           "params": [
             {
               "url": "/pm/config/adom/demo/_upgrade"
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
                 "task": 97
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/_upgrade"
             }
           ]
         }

      .. note::
         
         - The ADOM will be upgraded to its next supported Maintenance Release
         - If ADOM version is 7.0, then it will be upgraded to 7.2
         - If ADOM version is 7.2, then it will be upgraded to 7.4, etc.

How to check whether an ADOM upgrade is ongoing?
++++++++++++++++++++++++++++++++++++++++++++++++

Caught in #1050287.

The following example shows how to check whether the `root` and `demo` ADOMs are
being ADOM upgraded:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "data": {
                 "scope member": [
                   {
                     "name": "root"
                   },
                   {
                     "name": "demo"
                   }
                 ]
               },
               "url": "/dvmdb/_upgrade"
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
                   "message": "no upgrade is being processed",
                   "oid": 3,
                   "status": 0
                 },
                 {
                   "message": "no upgrade is being processed",
                   "oid": 204,
                   "status": 0
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/_upgrade"
             }
           ]
         }            