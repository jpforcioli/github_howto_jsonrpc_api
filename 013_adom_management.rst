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

How to perform an ADOM upgrade dry-run?
+++++++++++++++++++++++++++++++++++++++

Starting with FortiManager 7.4.7/7.6.3 (#1084231), it is now possible to start
an ADOM upgrade dry-run.

Following example shows how to perform the dry-run for the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/_upgrade",
               "data": {
                 "scope member": [
                   {
                     "oid":2629
                   }
                ],
                "flags": [
                  "same-version",
                  "dryrun",
                ]
             }
           ],
           "Session": "{{session}}"
         }

      .. note::

         - ``same-version``
         - ``from-cli``
         - ``dryrun``
         - ``downgrade``

ADOM Workspace Mode
-------------------

Locking
+++++++

ADOM Lock
_________

Following example is showing how to lock the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lock"
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
               "status": {
                 "code": 0, 
                 "message": "OK" 
               },
               "url": "/dvmdb/adom/demo/workspace/lock"
             }
           ]
         }

Policy Package Lock
___________________

The following example shows how to lock the ``ppkg_001`` Policy Package from the ``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lock/pkg/ppkg_001"
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
               "url": "/dvmdb/adom/demo/workspace/lock/pkg/ppkg_001"
             }
           ]
         }

Firewall Policy Lock
____________________

Following example is showing how to lock firewall policy with ``policyid`` ``1`` in the ``ppkg_001`` Policy Package from the ``demo`` ADOM:

.. tab-set:: 
  
   .. tab-item:: REQUEST

      .. code-block:: json
  
         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lock/pkg/ppkg_001/firewall/policy/1"
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
               "url": "/dvmdb/adom/demo/workspace/lock/pkg/ppkg_001/firewall/policy/1"
             }
           ]
         }
      
Object Lock
___________

To lock an object, you need first to lock a Policy Package (see :ref:`Policy Package Lock`) or a firewall policy (see :ref:`Firewall Policy Lock`).

The endpoint to lock an object is:

.. code-block:: text

   /dvmdb/adom/{adom}/workspace/obj/{path_to_the_object}

where ``path_to_the_object`` is the usual path used to refer to objects.

For instance:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - To lock...
     - ``path_to_the_object`` is

   * - the ``host_001`` firewall address
     - ``/firewall/address/host_001``

   * - the ``grp_001`` firewall address
     - ``/firewall/addrgrp/grp_001``

   * - the ``tcp_8080`` TCP service
     - ``/firewall/service/custom/tcp_8080``

The following exemple shows how to lock the ``host_001`` firewall address from the ``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 4,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lock/obj/firewall/address/host_001"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 4,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/lock/obj/firewall/address/host_001"
             }
           ]
         }

Device Lock
___________

Device lock has been introduced in #0544637 (FMG 6.0.5/6.2.0).

The following example show how to tock the ``dev_001`` device from the ``demo`` ADOM:

.. tab-set:: 
   
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lock/dev/dev_001"
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
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/lock/dev/dev_001"
             }
           ]
         }

Comitting changes
+++++++++++++++++

ADOM Commit
___________

Before unlocking an ADOM, a Policy Package or a firewall policy, a *save* operation is required in order have all pending changes applied to the running 
ADOM database.

If you unlock without saving, all changes will be lost.

To save changes made in the ``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block::

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/commit"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: 

         {
           "id": 1,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "taskid": 3332,
               "url": "/dvmdb/adom/demo/workspace/commit"
             }
           ]
         }

Device commit
_____________

The following example shows how to commit changes made to the locked ``dev_001`` device from the ``demo`` ADOM:

.. tab-set:: 
   
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/commit/dev/dev_001"
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
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/commit/dev/dev_001"
             }
           ]
         }

Policy Package Commit
_____________________

The following example shows how to commit changes made to the locked ``ppkg_001`` Policy Package from the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 9,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/commit/pkg/ppkg_001"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json         

         {
           "id": 9,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/commit/pkg/ppkg_001"
             }
           ]
         }

How to detect unsaved changes?
______________________________

How do you know when a save operation is required?

It is important to answer that question otherwise you may lose all of your unsaved changes when unlocking your resource.

FortiManager is maintaining a ``dirty`` flag.

When it is ``0``, it means there's no unsaved changes.

When it is ``1``, it means it is required to trigger a save operation before 
unlocking the ADOM.

To understand the process, review the following complete sequence of operations
performed in the ``demo`` ADOM:

#. Lock the ADOM

   .. tab-set::
    
      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 3,
              "method": "exec",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/lock"
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
                  "url": "/dvmdb/adom/demo/workspace/lock"
                }
              ]
            }
      
#. Observe the ``dirty`` flag

   .. tab-set::
    
      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 4,
              "method": "get",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/dirty"
                }
              ],
              "session": "{{session}}",
              "verbose": 1
            }

      .. tab-item:: RESPONSE

         .. code-block:: json            

            {
              "id": 4,
              "result": [
                {
                  "data": {
                    "dirty": 0
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/dirty"
                }
              ]

            }

   This is expected: ``dirty`` flag is ``0`` since no change were done yet.

#. Do a change

   Modify the ``comment`` of an existing ``host_001`` firewall address in the  
   ``demo`` ADOM:
   
   .. tab-set::
    
      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 5,
              "method": "set",
              "params": [
                {
                  "data": {
                    "comment": "New comment #001"
                  },
                  "url": "/pm/config/adom/demo/obj/firewall/address/host_001"
                }
              ],
              "session": "{{session}}"
            }

      .. tab-item:: RESPONSE

         .. code-block:: json

            {
              "id": 5,
              "result": [
                {
                  "data": {
                    "name": "host_001"
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/pm/config/adom/demo/obj/firewall/address/host_001"
                }
              ]
            }
      
#. Observe the ``dirty`` flag

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 6,
              "method": "get",
              "params": [
                {
                  "url": "/dvmdb/adom/dc_us/workspace/dirty"
                }
              ],
              "session": "{{session}}",
              "verbose": 1
            }

      .. tab-item:: RESPONSE

         .. code-block:: json      

            {
              "id": 6,
              "result": [
                {
                  "data": {
                    "dirty": 1
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/dirty"
                }
              ]
            }

         Now the ``dirty`` flag is ``1``.

         It indicates there are unsaved changes!

   You could have use the ``lockinfo`` to observe the *dirty* status (see 
   :ref:`How to figure out there is a lock?`).

   For instance:

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json

            {
              "id": 6,
              "method": "get",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/lockinfo"
                }
              ],
              "session": "{{session}}",
              "verbose": 1
            }

      .. tab-item:: RESPONSE

         .. code-block:: json
            :emphasize-lines: 7,10

            {
              "id": 6,
              "result": [
                {
                  "data": [
                    {
                      "adom_dirty": 1,
                      "db_mode": 1,
                      "dev_oid": 399,
                      "dirty": 1,
                      "flags": 1,
                      "lock_sid": 31952,
                      "lock_time": 1721801037,
                      "lock_user": "devops",
                      "obj_cat": 0,
                      "obj_oid": 0,
                      "obj_url": "",
                      "type": 1,
                      "wfsid": 0
                    }
                  ],
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/lockinfo"
                }
              ]
            }
   
         You can see that the ``adom_dirty`` attribute is ``1``.

         There's also another ``dirty`` flag with value ``1``.

#. Save the change

   .. tab-set::
    
      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 7,
              "method": "exec",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/commit"
                }
              ],
              "session": "{{session}}"
            }

      .. tab-item:: RESPONSE

         .. code-block:: json

            {
              "id": 7,
              "result": [
                {
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/commit"
                }
              ]
            }
      
#. Observe the ``dirty`` flag

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 8,
              "method": "get",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/dirty"
                }
              ],
              "session": "{{session}}",
              "verbose": 1
            }

      .. tab-item:: RESPONSE

         .. code-block:: json

            {
              "id": 8,
              "result": [
                {
                  "data": {
                    "dirty": 0
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/dirty"
                }
              ]
            }

   Changes were saved in previous operation step.

   The ``dirty`` flag is back to ``0`` to indicate there's no unsaved change
   anymore.

#. Unlock the ADOM

   See :ref:`ADOM Unlock`

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 9,
              "method": "exec",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/unlock"
                }
              ],
              "session": "{{session}}"
            }
    
      .. tab-item:: RESPONSE

         .. code-block:: json

            {
              "id": 9,
              "result": [
                {
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/unlock"
                }
              ]
            }

   .. note:: 
   
      - You can only get the ``dirty`` flag of your own workspace session

Unlocking
+++++++++

ADOM Unlock
___________

.. warning::

   - If you unlock without a ``commit`` operation then unsaved changes will be 
     lost

   - See :ref:`ADOM Commit`

The following example shows how to unlock the locked ``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block::

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/unlock"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block::

         {
           "id": 1,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/unlock"
             }
           ]
         }  

Device Unlock
_____________

The following example shows how to unlock the locked ``dev_001`` device from 
the ``demo`` ADOM:

.. tab-set:: 
   
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/unlock/dev/dev_001"
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
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/unlock/dev/dev_001"
             }
           ]
         }

Policy Package Unlock
_____________________

The following example shows how to unlock the locked ``ppkg_001`` Policy 
Package from the ``demo`` ADOM:

.. tab-set:: 
   
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 12,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/unlock/pkg/ppkg_001"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 12,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/unlock/pkg/ppkg_001"
             }
           ]
         }

How to figure out there is a lock?
++++++++++++++++++++++++++++++++++

``lockinfo`` can be used to obtain information about an existing lock.

ADOM lockinfo
_____________

When ADOM isn't locked
@@@@@@@@@@@@@@@@@@@@@@

The following example shows how to get the lock details for the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
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
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
             }
           ]
         }

      .. note::

         - When the ADOM isn't locked, nothing special is returned

When ADOM is locked
@@@@@@@@@@@@@@@@@@@

The following example shows how to get the lock details for the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
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
                   "adom_dirty": 0,
                   "db_mode": 1,
                   "dev_oid": 399,
                   "dirty": 0,
                   "flags": 0,
                   "lock_sid": 37154,
                   "lock_time": 1714077048,
                   "lock_user": "devops",
                   "obj_cat": 0,
                   "obj_oid": 0,
                   "obj_url": "",
                   "type": 1,
                   "wfsid": 0
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
             }
           ]
         }
      .. note::

         - When the ADOM is locked, FortiManager returns multiple information 
           like the owner of the lock (``lock_user``) and the lock time 
           (``lock_time``)

Policy Package lockinfo
_______________________

When Policy Package isn't locked
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The following example shows how to get the lock details for the ``ppkg_001`` Policy Package in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
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
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
             }
           ]
         }

      .. note::

         - When the ADOM isn't locked, nothing special is returned

When Policy Package is locked
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The following example shows how to get the lock details for the ``ppkg_001`` Policy Package in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 5,
           "method": "get",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lockinfo/pkg/ppkg_001"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

   .. tab-item:: RESPONSE

      .. code-block:: json
         
         {
           "id": 5,
           "result": [
             {
               "data": [
                 {
                   "db_mode": 1,
                   "dev_oid": 399,
                   "dirty": 0,
                   "flags": 0,
                   "lock_sid": 39089,
                   "lock_time": 1721802745,
                   "lock_user": "devops",
                   "obj_cat": 0,
                   "obj_oid": 6079,
                   "obj_url": "ppkg_001",
                   "type": 2,
                   "wfsid": 0
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/dc_emea/workspace/lockinfo/pkg/ppkg_001"
             }
           ]
         }

      .. note::

         - When the Policy Package is locked, FortiManager returns multiple 
           information like the owner of the lock (``lock_user``), the lock 
           time (``lock_time``) and the locked resource (``obj_url``).

         - The ``adom_dirty`` flag (see :ref:`ADOM lockinfo`) isn't visible, 
           since you're getting the ``lockinfo`` for a Policy Package
        
         - However, the ``dirty`` attribute is visible - ``1`` means there are
           pending changes in this Policy Package; ``0`` means there's no such 
           pending changes.

         - ``dev_oid`` is the ID of the ``demo`` ADOM
         - ``obj_oid`` is the ID of the ``ppkg_001`` Policy Package

Per-ADOM workspace mode
+++++++++++++++++++++++

How to figure out whether an ADOM is with or without workspace mode?
____________________________________________________________________

The following example shows how to figure out whether the ``demo`` ADOM is with
workspace mode enable or disable:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "fields": [
                 "workspace_mode"
               ],
               "loadsub": 0,
               "url": "/dvmdb/adom/demo"
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
                 "name": "demo",
                 "oid": 311,
                 "workspace_mode": 0
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo"
             }
           ]
         }  

      .. note::

         - ``0`` means workspace mode is not enabled
         - ``1`` means workspace mode is enabled      

ADOM Workflow Mode
------------------

The operations required to perform a change when FortiManager operates in workflow mode are described here.

For additional API details, use the FortiManager GUI and observe the output
produced by the following FortiManager CLI debug commands:

.. code-block:: text

   diagnose debug service dvmdb 255
   diagnose debug enable
   diagnose debug timestamp enable

How to lock an adom in workflow mode?
+++++++++++++++++++++++++++++++++++++

The following example shows how to lock the ``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lock"
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
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/lock"
             }
           ]
         }

How to create a workflow session?
+++++++++++++++++++++++++++++++++

We want to start a new session.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/start"
       }
     ],
     "session": "M1CzeItUayZBbsftqkyBXetQJTKB1nm7X7+/QknqiLR9vbCuIkLW/qSDK/TwtCDuarPbEXc1taOnLzOzg0rD4dX5qqYOrmOB",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "new_session": 1,
           "sessionid": 1
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/start"
       }
     ]
   }

.. note::

   - ``new_session``: ``1`` indicates it's a new session, ``0`` indicates it's
     an existing session (we can re-enter an existing session provided it hasn't
     been submitted yet).

     To start an existing session, we just have to use same method as above but
     with this url:

     .. code-block::

        /dvmdb/adom/ZTP_SINGLE/workflow/start/<session_id>

   - ``session_id`` will have to be used to reference that specific session for
     other workflow operations (for instance to save or approve it).

How to get existing sessions?
+++++++++++++++++++++++++++++

It could be required to get the list of existing sessions to perform additional
workspace workflow operations on them.

To get the list of sessions:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "get",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow"
       }
     ],
     "session": "3AyIKOdJl27+OoZj8TJsHMqBovc4x031AuPFIl1r7pl616x/ewMTaqEmmEMwWow9O4Q45tRP+Dfv85e+WIyAXGL01M0xfw/c",
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
             "audit_time": "",
             "audit_user": "",
             "create_time": "2020-07-22 18:37:38",
             "create_user": "devops",
             "desc": "Workflow session",
             "flags": 1,
             "name": "Workflow session",
             "oid": 616,
             "revid": 0,
             "sessionid": 1,
             "state": 1,
             "submit_time": "",
             "submit_user": "",
             "wflog": null
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow"
       }
     ]
   }

We can use the returned ``sessionid`` to perform other workspace workflow mode
operation on that particular session.

How to save changes made in a session?
++++++++++++++++++++++++++++++++++++++

We assume that some changes have been made.
We now want to save them.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/save/1"
       }
     ],
     "session": "MOhyT02bbKOCrqqwt0X2OH3G27LifDHr/5AZ3cwg2ySRYvAi2jHZZl9veO61BgM1Inbu/mHsBuBDEIK1fK4zH/ZovswIBCCO",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/save/1"
       }
     ]
   }

How to discard saved changes?
+++++++++++++++++++++++++++++

We're in a situation where we have an existing session with some saved changes
and our session is still not submitted.

We want to discard the changes.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/discard/1"
       }
     ],
     "session": "nkv/vQ8R9/zwnrP/Vp+f+LzjzsspQUe0a2u9LS74BgCScsQOekgPhJEJ3So/D5zCCGHvwSdfdINiR36P4fi0QV2BR9QVnkD8",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/discard/1"
       }
     ]
   }

.. note::

   Session ``1`` still exists in the system. Hence it is possible to re-open it
   and perform new changes.

How to submit a session?
++++++++++++++++++++++++

We submit a session when we want the saved changes to be approved.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/submit/1",
         "workflow": {
           "desc": "We have finished our changes.",
           "fmgip": "10.210.35.200",
           "no_diff": 0
         }
       }
     ],
     "session": "eaXr97ungqgR31ecapTPnt5hiDhqmegidS1668ZxEsgEJjgnR/yAdGzoBOVg7ndaAnWcsozbd9rCczPvf42cYJ8U8jckwCMJ",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/submit/1"
       }
     ]
   }

.. note::

   It is no longer possible to add extra changes to a submitted session. If we
   try to start a submitted session, a brand new session will be created.

How to delete a session?
++++++++++++++++++++++++

This operation can only be performed by an approver.
If we receive this error:

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "status": {
           "code": -20020,
           "message": "No permission"
         },
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/drop/1"
       }
     ]
   }

it is probably because our API session has been created with the credentials of a
non approver user.

We want to delete session 1.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/drop/1"
       }
     ],
     "session": "avGakSAPiuvAfqvIIaYMFjEIOz2GymtIzFYMGJNuR05mxgYUgGyS1ILDuJOg/QTOP5An32HahKIEnh2hySXw7Lbf+JLxdIK4",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/drop/1"
       }
     ]
   }

Deleting a non approved session will also delete all other sessions made on top
of this one (which are by essence also not approved).

How to reject a session?
++++++++++++++++++++++++

This operation can only be performed by an approver.
A rejected session could be repaired.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/reject/1",
         "workflow": {
           "desc": "Wrong changes. Please repair",
           "user": "admin"
         }
       }
     ],
     "session": "NMTPFix6qkkKFJ7bDLFpjhVMSMcPfJKv61aH928174/xMOro+aZYBAg6zdJxxTmMnDglPxp81mKqwQd4nCv6DQ==",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/reject/1"
       }
     ]
   }

How to repair a rejected session?
+++++++++++++++++++++++++++++++++

Repairing a rejected session consists just in creating a new session.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/repair/1"
       }
     ],
     "session": "sai90w4hlWdSWOzn5sqVHmhxWPRFTtZ2R08pyW352avvqGxc1C167nkGNtjvHXEJ6XAT4sCnfCkHWeZRC/cLtw==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "sessionid": 2
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/repair/1"
       }
     ]
   }

How to approve a submitted session?
+++++++++++++++++++++++++++++++++++

This operation can only be performed by an approver.
Once approved, a submitted session can't be deleted anymore.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/approve/2",
         "workflow": {
           "desc": "Good!. I approve.",
           "user": "admin"
         }
       }
     ],
     "session": "FfBwDLjz5g23TIiAXg6OI6d3Re7qrERN+EaojGzRg5eN0ArKUflPs6YZabrKaGT++y87fDPGuXuFRI3stlfQKcj4/HTmIwyP",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/approve/2"
       }
     ]
   }

How to unlock an adom in workflow mode?
+++++++++++++++++++++++++++++++++++++++

When we no longer need to perform any workflow mode operations we have to
release the ADOM since it could be needed by another administrator.

We unlock adom ``ZTP_SINGLE``.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workspace/unlock"
       }
     ],
     "session": "X8ccl04rmuhRIdZo/VgArjUwWQylAmUYcbRG5h1xz49yBW0j/fCH6M6PbkPJAt726osTNIFg++gEivQi1isIqx5l6tlZd57r",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workspace/unlock"
       }
     ]
   }

How to trigger a workflow session diff?
+++++++++++++++++++++++++++++++++++++++

Sometimes, it's necessary to capture the session diff either before or after
approving it.

For example, some enterprise customers require all changes to be captured in
their corporate CMS, rather than being stored solely in FortiManager.

This section explains how to trigger a workflow session diff.

As you will see, it involves a multi-step process:

1. List your sessions

   This steps allows you to retrieve the session ID needed for the diff 
   operation.

2. Trigger the session diff operation

3. Monitor the session diff operation

   Using the returned token, monitor the operation and obtain an overall 
   summary.

4. Collect the session diff output

   Retrieve the session diff output in either JSON or CLI format for all
   detected changes, such as changes to firewall policies, firewall addresses,
   etc.
   

The following section demonstrates capturing the session diff for the pending  ``SR #003`` session:

.. thumbnail:: images/adom_management/image_001.png

Workflow Mode - List your sessions
__________________________________

The following example shows how to get the list of workflow sessions for the
``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "loadsub": 0,
               "sortings": [
                 {
                   "revid": -1
                 }
               ],
               "url": "/dvmdb/adom/demo/workflow"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

      .. note::

         - The ``sortings`` attribute is used to obtain a session list ordered
           by descendent ``revid``

         - The first item in the list represents the most recent session created
           by the FortiManager administrator

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "audit_time": "",
                   "audit_user": "",
                   "create_time": "1724672125",
                   "create_user": "admin",
                   "desc": "Workflow session",
                   "flags": 0,
                   "name": "SR #003",
                   "oid": 189,
                   "revid": 4,
                   "sessionid": 3,
                   "state": 2,
                   "submit_time": "1724672166",
                   "submit_user": "admin"
                 },
                 {
                   "audit_time": "1724672318",
                   "audit_user": "admin",
                   "create_time": "1724671974",
                   "create_user": "admin",
                   "desc": "Workflow session",
                   "flags": 0,
                   "name": "SR #002",
                   "oid": 183,
                   "revid": 3,
                   "sessionid": 2,
                   "state": 3,
                   "submit_time": "1724671988",
                   "submit_user": "admin"
                 },
                 {
                   "audit_time": "1724672299",
                   "audit_user": "admin",
                   "create_time": "1724671895",
                   "create_user": "admin",
                   "desc": "Workflow session",
                   "flags": 0,
                   "name": "SR #001",
                   "oid": 176,
                   "revid": 2,
                   "sessionid": 1,
                   "state": 3,
                   "submit_time": "1724671916",
                   "submit_user": "admin"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo_001/workflow"
             }
           ]
         }

Workspace Mode - Trigger the session diff operation
___________________________________________________

In the previous section (:ref:`Workflow Mode - List your sessions`) you obtained
the list of workflow sessions ordered by descendent `revid`.

In this section, you will request the changes made in the most recent workflow
session with ``revid`` ``4``.

The following examples shows how to trigger the session diff operation for the
session with ``revid`` ``4`` in the ``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 4,
           "method": "exec",
           "params": [
             {
               "data": {
                 "dst": "/adom/demo/revision/3",
                 "flags": 16,
                 "src": "/adom/demo/revision/4"
               },
               "url": "/cache/diff/start"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - The ``flags`` attribute with its ``16`` value is required if you 
           want to obtain the session diff output in CLI format (caught in
           #0893188)

   .. tab-item:: RESPONSE

      .. code-block:: json
         :emphasize-lines: 5    
         
           "id": 4,
           "result": [
             {
               "data": {
                 "token": "TDXIV3JsxW3sBy9BCgRXe4DGRPPH9zi3thtl5QMesqs="
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/cache/diff/start"
             }
           ]
         }

      .. note::

         - You now have to consider the value of the returned ``token`` 
           attribute

Workflow Mode - Monitor the session diff operation
__________________________________________________

Using the value of the returned ``token`` attribute (see :ref:`Workspace Mode -
Trigger the session diff operation`) monitor the session diff operation and obtain an overall summary.

The following example shows how to monitor the session diff operation and how to
obtain an overall summary for a specific token value:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 5,
           "method": "exec",
           "params": [
             {
               "token": "TDXIV3JsxW3sBy9BCgRXe4DGRPPH9zi3thtl5QMesqs=",
               "url": "/cache/diff/get/summary"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json
         :emphasize-lines: 21

         {
           "id": 8,
           "result": [
             {
               "data": {
                 "obj": {
                   "added": 1,
                   "summary": [
                     {
                       "added": [
                         {
                           "name": "host_001",
                           "timestamp": 1724672145,
                           "user": "admin"
                         }
                       ],
                       "category": 140
                     }
                   ]
                 },
                 "percent": 100,
                 "pkg": {
                   "changed": 1,
                   "summary": [
                     {
                       "category": 0,
                       "changed": [
                         {
                           "name": "ppkg_001",
                           "percent": 100,
                           "timestamp": 1724672160,
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
         
      .. note::

         - If the value of the returned ``percent`` attribute isn't equal to
           `100`, you must continue making same request using the same
           token value

         - In this output, you know that the ``host_001`` firewall address
           object (``obj``) was added (``added``) and that the ``ppkg_001``
           Policy Package (``pkg``) was updated (``changed``) but no further
           details are available

         - The value ``140`` for the ``category`` attribute, in the ``obj``
           section is the number of the table ``firewall address``

           - You can get this number by issuing following command:

             .. code-block:: text

                execute fmpolicy print-adom-object demo ?

             In the output, you will see this line:

             .. code-block:: text

                [...]
                140	"firewall address"
                [...]           

For the ``ppkg_001`` Policy Package case, you can optionnally ask for further
details using the following API request:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 9,
           "method": "exec",
           "params": [
             {
               "token": "TDXIV3JsxW3sBy9BCgRXe4DGRPPH9zi3thtl5QMesqs=",
               "url": "/cache/diff/get/summary/pkg/ppkg_001"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 9,
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
                           "name": 1,
                           "obj seq": 0,
                           "timestamp": 1724672160,
                           "user": "admin"
                         }
                       ],
                       "size": 1
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
      
      .. note::

         - If the value of the returned ``percent`` attribute isn't equal to
           `100`, you must continue making same request using the same
           token value

         - In this output, you know that the policy with policy ID ``1``
           (``name``) was updated (``changed``)

         - The value ``181`` for the ``category`` attribute, in the ``obj``
           section is the number of the table ``firewall policy``

           - You can get this number by issuing following command:

             .. code-block:: text

                execute fmpolicy print-adom-package demo 1 <ppkg_id> ?

             In the output, you will see this line:

             .. code-block:: text

                [...]
                181	"firewall policy"
                [...]           

         
Workflow Mode - Collect the session diff output
_______________________________________________

Retrieve the session diff output in either JSON or CLI format for all detected
changes, such as changes to firewall policies, firewall addresses, etc.

In the previous section, you obtained a summary of the session diff operation,
which indicated that the ``host_001`` firewall address object was
added and that the ``ppkg_001`` Policy Package was updated but no further
details were available.

In this section, you will retrieve the details of those specific changes, either
in JSON or CLI format.

Get details about the updated firewall address:

.. tab-set::

   .. tab-item:: JSON format

      .. tab-set::

         .. tab-item:: REQUEST

            .. code-block:: json

               {
                 "id": 10,
                 "method": "exec",
                 "params": [
                   {
                     "token": "TDXIV3JsxW3sBy9BCgRXe4DGRPPH9zi3thtl5QMesqs=",
                     "url": "/cache/diff/get/detail/obj/all objs"
                   }
                 ],
                 "session": "{{session}}"
               }            

         .. tab-item:: RESPONSE

            .. code-block:: json

               {
                 "id": 10,
                 "result": [
                   {
                     "data": [
                       {
                         "category": 140,
                         "data": [
                           {
                             "_image-base64": null,
                             "allow-routing": 0,
                             "associated-interface": [
                               "\"any\""
                             ],
                             "clearpass-spt": 0,
                             "color": 20,
                             "comment": null,
                             "diff_flag": 1,
                             "dirty": 1,
                             "dynamic_mapping": null,
                             "fabric-object": 0,
                             "hw-model": null,
                             "hw-vendor": null,
                             "list": null,
                             "name": "host_001",
                             "node-ip-only": 0,
                             "obj-tag": null,
                             "obj-type": 9,
                             "organization": null,
                             "os": null,
                             "policy-group": null,
                             "route-tag": 0,
                             "subnet": [
                               "10.0.0.1",
                               "255.255.255.255"
                             ],
                             "subnet-name": null,
                             "sw-version": null,
                             "tag-detection-level": null,
                             "tag-type": null,
                             "tagging": null,
                             "timestamp": 1724672145,
                             "type": 0,
                             "user": "admin",
                             "uuid": "553bd7e4-639f-51ef-9fc2-a05f1ed8b6fe"
                           }
                         ]
                       }
                     ],
                     "status": {
                       "code": 0,
                       "message": "OK"
                     },
                     "url": "/cache/diff/get/detail/obj/all objs"
                   }
                 ]
               }              

   .. tab-item:: CLI format

      .. tab-set::

         .. tab-item:: REQUEST

            .. code-block:: json

               {
                 "id": 11,
                 "method": "exec",
                 "params": [
                   {
                     "token": "TDXIV3JsxW3sBy9BCgRXe4DGRPPH9zi3thtl5QMesqs=",
                     "url": "/cache/diff/get/cli/obj"
                   }
                 ],
                 "session": "{{session}}"
               }              

         .. tab-item:: RESPONSE

            .. code-block:: json

               {
                 "id": 11,
                 "result": [
                   {
                     "data": {
                       "percent": 100,
                       "script": "config firewall address\nedit \"host_001\"\nset uuid 553bd7e4-639f-51ef-9fc2-a05f1ed8b6fe\nset color 20\nset subnet 10.0.0.1 255.255.255.255\nnext\nend\n"
                     },
                     "status": {
                       "code": 0,
                       "message": "OK"
                     },
                     "url": "/cache/diff/get/cli/obj"
                   }
                 ]
               }                        

Get details about the updated firewall policy:

.. tab-set::

   .. tab-item:: JSON format

      .. tab-set::

         .. tab-item:: REQUEST

            .. code-block:: json

               {
                 "id": 12,
                 "method": "exec",
                 "params": [
                   {
                     "token": "TDXIV3JsxW3sBy9BCgRXe4DGRPPH9zi3thtl5QMesqs=",
                     "url": "/cache/diff/get/detail/pkg/ppkg_001/firewall/policy"
                   }
                 ],
                 "session": "{{session}}"
               }

         .. tab-item:: RESPONSE

            .. code-block:: json                                  

               {
                 "id": 12,
                 "result": [
                   {
                     "data": [
                       {
                         "_global-dst-intf": null,
                         "_global-label-color": 0,
                         "_global-src-intf": null,
                         "...",
                         "srcaddr": {
                           "n": [
                             "\"host_001\""
                           ],
                           "o": [
                             "\"all\""
                           ]
                         },
                         "...",
                         "ztna-policy-redirect": 0,
                         "ztna-status": 0,
                         "ztna-tags-match-logic": 0
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

            .. note::

               - Look at the ``srcaddr`` attribute; it shows old value (``o``,
                 it was ``all``) and the new value (``n``, it is ``host_001``)

   .. tab-item:: CLI format

      .. tab-set::

         .. tab-item:: REQUEST

            .. code-block:: json

               {
                 "id": 13,
                 "method": "exec",
                 "params": [
                   {
                     "token": "TDXIV3JsxW3sBy9BCgRXe4DGRPPH9zi3thtl5QMesqs=",
                     "url": "/cache/diff/get/cli/pkg/ppkg_001"
                   }
                 ],
                 "session": "{{session}}"
               }

         .. tab-item:: RESPONSE

            .. code-block:: json                                  

               {
                 "id": 13,
                 "result": [
                   {
                     "data": {
                       "percent": 100,
                       "script": "config firewall policy\nedit 1\nset srcaddr \"host_001\"\nnext\nend\n"
                     },
                     "status": {
                       "code": 0,
                       "message": "OK"
                     },
                     "url": "/cache/diff/get/cli/pkg/ppkg_001"
                   }
                 ]
               }

How to keep the session idle?
-----------------------------

Caught in #0643153.

Sometimes, we need to perform some actions but we don't want to reset the
idle_timeout timer. This is making sense from the GUI where some background
requests shouldn't reset the connected user idle_timeout (otherwise he will stay
connected forever).

FMG API comes with the attribute *keep_session_idle*. When set, the idle_timeout
timer won't be reset by the API call.

For instance:

**REQUEST:**

.. code-block:: json

                {
                  "id": 1,
                  "method": "get",
                  "params": [
                    {
                      "fields": [
                        "name",
                        "flags"
                      ],
                      "filter": [
                        "name",
                        "in",
                        "dut_fgt1"
                      ],
                      "keep_session_idle": 1,
                      "sub fetch": {
                        "vdom": {
                          "fields": [
                            "name",
                            "flags",
                            "status"
                          ]
                        }
                      },
                      "url": "/dvmdb/device"
                    }
                  ],
                  "session": 19874,
                  "verbose": 1
                }

ADOM Backup Mode
----------------

It is possible to centrally manage certain objects used in your managed devices’
firewall policies, even when they are within an ADOM in backup mode.

Similar to a normal ADOM, you define objects in FortiManager, making them
available to all your managed devices. The key difference is that in a backup
mode ADOM, there is no install capability. The synchronization process must be
triggered from the FortiGate GUI. This process is documented here: :bdg-link-primary-line:`Importing objects to backup ADOMs
<https://docs.fortinet.com/document/fortimanager/7.6.0/administration-guide/729689/importing-objects-to-backup-adoms>`

If you need to automate this process, first, obtain an ADOM checksum for your
managed device. If the checksum differs from the previous one, it indicates that
new objects need to be reviewed. Once identified, you can retrieve their CLI or
JSON syntax to update the managed device.

How to get the ADOM checksum for a managed device?
++++++++++++++++++++++++++++++++++++++++++++++++++

The checksum is used to track ADOM objects that can be synchronized with managed
devices. When you add or update objects in an ADOM, a new checksum will be
generated. 

Here’s an example of how to get the ADOM checksum for the VDOM ``root`` of a
managed device with the serial number ``FGVMUL0000000001``:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/devrpc/sharedobj/checksum/FGVMUL0000000001/root"
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
                 "checksum": "a3df1f4c75a8311cde9e7834e7927182"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/devrpc/sharedobj/checksum/FGVMUL0000000001/root"
             }
           ]
         }

How to review the ADOM objects?
+++++++++++++++++++++++++++++++

You need to review the ADOM objects whenever a new ADOM checksum is generate
(see :ref:`How to get the ADOM checksum for a managed device?`).

The following example shows how to review the ADOM objects for the VDOM ``root``
of a managed device with the serial number ``FGVMUL0000000001``:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/devrpc/sharedobj/summary/FGVMUL0000000001/root"
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
                 "checksum": "a3df1f4c75a8311cde9e7834e7927182",
                 "conflict object": 75,
                 "local object": 2,
                 "missing object": 2,
                 "percent": 100,
                 "pid": 24480,
                 "summary": [
                   {
                     "category": "firewall address",
                     "local object": [
                       {
                         "mkey": "tun_01_remote_subnet_1"
                       },
                       {
                         "mkey": "tun_01_remote_gateway"
                       }
                     ],
                     "missing object": [
                       {
                         "mkey": "RFC1918-192"
                       },
                       {
                         "mkey": "metadata-server"
                       }
                     ]
                   },
                   {
                     "category": "firewall service custom",
                     "conflict object": [
                       {
                         "mkey": "ALL_TCP"
                       },
                       {
                         "mkey": "ALL_UDP"
                       },
                       {
                         "mkey": "GTP"
                       },
                       {"TRUNCARED": "TRUNCATED"},
                       {
                         "mkey": "LDAP_UDP"
                       },
                       {
                         "mkey": "SMB"
                       },
                       {
                         "mkey": "NONE"
                       }
                     ]
                   }
                 ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/devrpc/sharedobj/summary/FGVMMLTM22002640/root"
             }
           ]
         }

      .. note::

         - Usually, you review the objects returned in the ``missing object``
           block as these are the ones you're trying to make available in
           your managed device's object list.

         - Objects listed in the ``missing object`` block exist in the ADOM in
           backup mode, but are not present in the managed device specified in
           the request.

How to get the details of ADOM objects?
+++++++++++++++++++++++++++++++++++++++

Typically, you review the details of ADOM objects listed in the ``missing
object`` block when you checking your ADOM objects (see
:ref:`How to review the ADOM objects?`). You need these details because you're
likely need to create similar objects on your manage FortiGate.

The following example shows how to get the detail of the firewall address
``RFC1918-192`` for the ``root`` VDOM of the managed device with serial number
``FGVMUL0000000001``:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/devrpc/sharedobj/detail/FGVMUL0000000001/root/firewall/address/RFC1918-192"
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
                 "json": {
                   "allow-routing": "disable",
                   "associated-interface": [
                     "any"
                   ],
                   "clearpass-spt": "unknown",
                   "color": 0,
                   "dirty": "dirty",
                   "fabric-object": "disable",
                   "name": "RFC1918-192",
                   "node-ip-only": "disable",
                   "obj-type": "ip",
                   "route-tag": 0,
                   "subnet": [
                     "192.168.0.0",
                     "255.255.0.0"
                   ],
                   "type": "ipmask",
                   "uuid": "f5258644-8d23-51ef-e3ca-3902e80d9667"
                 },
                 "mkey": "RFC1918-192",
                 "object status": "missing object",
                 "script": "config firewall address\nedit \"RFC1918-192\"\nset uuid f5258644-8d23-51ef-e3ca-3902e80d9667\nset subnet 192.168.0.0 255.255.0.0\nnext\nend\n"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/devrpc/sharedobj/detail/FGVMUL0000000001/root/firewall/address/RFC1918-192"
             }
           ]
         }


      .. note::

         - Two blocks are returned: the ``json`` and ``script`` blocks
         - You can ask FortiManager to return either one of them using the
           option ``json`` or ``script``:

           .. tab-set::
            
              .. tab-item:: ``json`` option

                 .. code-block:: json
           
                    {
                      "id": 3,
                      "method": "get",
                      "params": [
                        {
                          "url": "/devrpc/sharedobj/detail/FGVMUL0000000001/root/firewall/address/RFC1918-192",
                          "option": "json"
                        }
                      ],
                      "session": "{{session}}",
                      "verbose": 1
                    }

              .. tab-item:: ``script`` option

                 .. code-block:: json
           
                    {
                      "id": 3,
                      "method": "get",
                      "params": [
                        {
                          "url": "/devrpc/sharedobj/detail/FGVMUL0000000001/root/firewall/address/RFC1918-192",
                          "option": "script"
                        }
                      ],
                      "session": "{{session}}",
                      "verbose": 1
                    }                    