Proxying any APIs within FMG JSON API
=====================================

Security
--------

- TODO

   - Find the Internal Reference...
   
     The resource need to be in file
     ``/usr/local/webclient/config/fos_json_api.json`` or
     ``/usr/local/webclient/config_json_api_named.json``? 

Replacing ``sys/proxy/json``
----------------------------

Caught in #0579366.

To proxy FAZ API in FMG JSON API:

**REQUEST:**

.. code-block:: json
		
		{
		  "id": "2333c69e-bf19-11e5-924a-000c2986047b",
		  "jsonrpc": "2.0",
		  "method": "add",
		  "root":"deployment/proxy/adom/root/FAZVM64",
		  "params": [
		    {
		      "apiver": 3,
		      "case-sensitive": false,
		      "device": [
                        {
                          "devid": "All_FortiGate"
                        }
                      ],
                      "filter": "",
                      "limit": 10,
                      "sort-by": [
                        {
                          "field": "sessions",
                          "order": "desc"
                        }
                      ],
                      "time-range": {
                        "end": "2019-07-17 10:00",
                        "start": "2019-07-17 09:00"
                      },
                      "url": "fortiview/adom/root/top-sources/run"
		    }
		  ]
		}

How to encapsulate FOS REST API call within FMG JSON RPC API?
-------------------------------------------------------------

The FMG JSON RPC API url is:

.. code-block:: text

   /sys/proxy/json

But let's have a look first at a FMG debug output when from the FMG GUI, we try
to get the kernel routes from a managed devices. The following FMG CLI
commands:

.. code-block:: shell

   diagnose debug service sys 255
   diagnose debug timestamp enable
   diagnose debug enable

will expose this debug output:

.. code-block:: json
 
   {
     "client": "gui json:17054",
     "id": "0b346cc9-4576-4fc1-8f1e-1ae8e22c6e21",
     "keep_session_idle": 1,
     "method": "exec",
     "params": [
       {
         "data": {
           "action": "get",
           "resource": "/api/v2/monitor/router/ipv4/select?&global=1&count=-1",
           "target": [
             "adom/adom_dut/device/fgt_dut1"
           ]
         },
         "target start": 1,
         "url": "sys/proxy/json"
       }
     ],
     "session": 27540
   }

We can observe that:

* The ``action`` attribute is to indicate the FOS REST API HTTP method
* The ``resource`` attribute is to indicate the main URI (along with the query
  string) 
* The ``target`` attribute is to indicate the managed devices.

  The ``target`` attribute could have multiple forms:

  - For one device:

    .. code-block:: json
             
       "target": [
           "adom/adom_dut/device/fgt_dut1"
       ]

  - For multiple devices:

    .. code-block:: json
             
       "target": [
           "adom/adom_dut/device/fgt_dut1",
           "adom/adom_dut/device/fgt_dut2"           
       ]       

  - For one device group:

    .. code-block:: json
             
       "target": [
           "adom/adom_dut/group/emea_devices"
       ]       

    .. note::

       It means the FOS REST API call will be automatically sent to all managed
       devices belonging to device group ``emea_devices``.

       To be used with caution since It could be a large number of devices.

       But It shows how simple it is when you need to collect something from
       multiple devices, it is not required to poll each devices individually. 

    .. note::

       We can use the special default device group ``All_FortiGate`` to target
       all managed devices for the specified ADOM. See the examples below.

  - For multiple device groups:

    .. code-block:: json
             
       "target": [
           "adom/adom_dut/group/emea_devices",
           "adom/adom_dut/group/apac_devices"           
       ]                     

  - For multiple devices and device groups:

    .. code-block:: json
             
       "target": [
           "adom/adom_dut/group/emea_devices",
           "adom/adom_dut/group/apac_devices",
           "adom/adom_dut/device/fgt_dut1",
           "adom/adom_dut/device/fgt_dut2"            
       ]                            

    .. note::

       FMG will optimize the list of target: if ``fgt_dut1`` belongs to device
       group ``emea_devices``, only one request will be generated; not two.

  - For all devices in ADOM ``foobar``:

    .. code-block:: json

       "target": [
           "/adom/foobar/group/All_FortiGate"
       ]

  - Cross ADOM request: for all devices in ADOM ``foobar`` and ``barfoo``:

    .. hint::

       - Yes! a single API call will be somehow targeting managed devices in
         different ADOMs

    .. code-block:: json

       "target": [
           "/adom/foobar/group/All_FortiGate",
           "/adom/barfoo/group/All_FortiGate"
       ]       

  - We can also target devices without mentioning the ADOM information:
  
    .. code-block:: json

       "target": [
         "/device/device_001",
         "/device/device_002"
       ]

  - It works for device groups too! For instance, this one will target all
    devices managed by FortiManager, whatever the ADOMs:

    .. code-block:: json

       "target": [
           "/group/All_FortiGate"
       ]
       
FNDN page for FMG JSON RPC API URL ``/sys/proxy/json`` is also exposing another
attribute:

* The ``payload`` attribute wich is to set the data the we would pass in the
  HTTP body of our FOS REST API call (for POST or PUT HTTP method for
  instance).

With this in mind, we can now easily convert any FOS REST API calls to a FOS
REST API call encapsulated in FMG JSON RPC API.

Recentely (#0689396) FMG exposed a new attribute:

* The ``timeout`` option to avoid waiting the complete timeout:

  .. code-block:: 
  
     "action": "get",
     "resource": "/api/v2/monitor/virtual-wan/members?global=1",
     "target": ["adom/FPC-ADOM-D/group/All_FortiGate"],
     "timeout": 10

  When omitted, default timeout is 60 seconds.
  
  Maximum value is 28800 seconds.

Add a new firewall address
++++++++++++++++++++++++++

To add a new firewall address ``host_001`` in device ``dut_fgt3`` and VDOM
``vd_001``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "data": {
           "action": "post",
           "payload": {
             "name": "host_001",
             "subnet": "10.0.0.1/32"
           },
           "resource": "/api/v2/cmdb/firewall/address?vdom=vd_001",
           "target": [
             "adom/adom_dut/device/fgt_dut3"
           ]
         },
         "url": "/sys/proxy/json"
       }
     ],
     "session": "CudTWpfYXUDaEXLcri+EhokgysjqLFtTK2InWxr/AEREIql5buIuTpgDmbNZUvZaSCeLi1DO85t8nF6pUNKr8Q==",
     "verbose": 1
   }

.. note::

   We shouldn't create objects directly in the managed FortiGate devices. This
   is something FortiManager is doing very well already :-).

   But this example shows that you can also perform some provisioning
   operations.

**RESPONSE:**

.. code-block::

   {
     "id": 1,
     "result": [
       {
         "data": [
           {
             "response": {
               "build": 1803,
               "http_method": "POST",
               "http_status": 200,
               "mkey": "host_001",
               "name": "address",
               "old_revision": "7d4cf25c6f5d3d6e1db497b4fcaed47c",
               "path": "firewall",
               "revision": "926d4f9c1148cf281b99bd9d87adafb6",
               "revision_changed": true,
               "serial": "FGVMULREDACTED68",
               "status": "success",
               "vdom": "vd_001",
               "version": "v6.4.4"
            },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "fgt_dut3"
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/sys/proxy/json"
       }
     ]
   }
 
Same example this time using the special default device group
``All_FortiGate``. It means we're able to create the same object on multiple
managed FortiGate by sending a single request to the FortiManager!

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "data": {
           "action": "post",
           "payload": {
             "name": "host_111",
             "subnet": "10.0.0.111/32"
           },
           "resource": "/api/v2/cmdb/firewall/address?vdom=root",
           "target": [
             "adom/adom_dut/group/All_FortiGate"
           ]
         },
         "url": "/sys/proxy/json"
       }
     ],
     "session": "5fLb+Zd15gc3vczurXt+WEWtulTcMoWf/1KV0IZshFXDwJrZ+P52M3JuVOitxhpwPOmLH/Luer9K/BdUTg/xkA==",
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
             "response": {
               "build": 1803,
               "http_method": "POST",
               "http_status": 200,
               "mkey": "host_111",
               "name": "address",
               "old_revision": "d9f6a63630566b0614d9c07dbb2d827d",
               "path": "firewall",
               "revision": "cae094c858c3209389351cc5cb5b1250",
               "revision_changed": true,
               "serial": "FGVMULREDACTED09",
               "status": "success",
               "vdom": "root",
               "version": "v6.4.4"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "fgt_dut1"
           },
           {
             "response": {
               "build": 1803,
               "http_method": "POST",
               "http_status": 200,
               "mkey": "host_111",
               "name": "address",
               "old_revision": "96ff190e287105f12b5de346674794c5",
               "path": "firewall",
               "revision": "934d3884dec21ef732e2eea3ba5dbedd",
               "revision_changed": true,
               "serial": "FGVMULREDACTED81",
               "status": "success",
               "vdom": "root",
               "version": "v6.4.4"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "fgt_dut2"
           },
           {
             "response": {
               "build": 1803,
               "http_method": "POST",
               "http_status": 200,
               "mkey": "host_111",
               "name": "address",
               "old_revision": "147220be553b6c71f8b3201d2188521a",
               "path": "firewall",
               "revision": "ee124f04143debb78ab5f0b8c0d42728",
               "revision_changed": true,
               "serial": "FGVMULREDACTED68",
               "status": "success",
               "vdom": "root",
               "version": "v6.4.4"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },  
             "target": "fgt_dut3"
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/sys/proxy/json"
       }
     ]
   }

To get list of banned users
+++++++++++++++++++++++++++

To get list of banned users from ``root`` VDOMs of all managed FortiGates in
ADOM ``adom_dut``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "data": {
           "action": "get",
           "resource": "/api/v2/monitor/user/banned?vdom=root",
           "target": [
             "adom/adom_dut/group/All_FortiGate"
           ]
         },
         "url": "/sys/proxy/json"
       }
     ],
     "session": "yWaJOx+dMwqIikWJEVvGza3ErXLfhoOejBgh6bC9nIZI9eHBuT0wHLYjPM5a26lwKbFIjbe+cvBOpE1m2cJbpQ==",
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
             "response": {
               "build": 1803,
               "http_method": "GET",
               "name": "banned",
               "path": "user",
               "results": [],
               "serial": "FGVMULREDACTED68",
               "status": "success",
               "vdom": "root",
               "version": "v6.4.4"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "fgt_dut3"
           },
           {
             "response": {
               "build": 1803,
               "http_method": "GET",
               "name": "banned",
               "path": "user",
               "results": [],
               "serial": "FGVMULREDACTED81",
               "status": "success",
               "vdom": "root",
               "version": "v6.4.4"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "fgt_dut2"
           },
           {
             "response": {
               "build": 1803,
               "http_method": "GET",
               "name": "banned",
               "path": "user",
               "results": [],
               "serial": "FGVMULREDACTED09",
               "status": "success",
               "vdom": "root",
               "version": "v6.4.4"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "fgt_dut1"
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/sys/proxy/json"
       }
     ]
   }

.. note::

   We don't have any banned users. This is why the ``results`` array is empty. 