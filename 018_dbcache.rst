Using ``dbcache``
=================

You can expose the API activity related to the DB cache mechanism by running the
following FortiManager CLI commands:

.. code-block:: text

   diagnose debug service dbcache 255
   diagnose debug enable

Then, using the GUI, create a normalized interface and a corresponding
per-device mapping. 

You will see the DB cache API calls logged in the debug output.

How to get the list of interfaces for a specific device?
--------------------------------------------------------

Caught in #455627 and #1199950.

The following example shows how to get the list of interfaces from the DB cache
system for the ``dev_001`` managed device in the ``demo`` ADOM:

.. tab-set::
	
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "current_adom": "demo",
               "fields": [
                 "name",
                 "ip",
                 "mode",
                 "type",
                 "vdom",
                 "status"
               ],
               "loadsub": 0,
               "option": [
                 "scope member"
               ],
               "scope member": [
                 {
                   "name": "dev_001",
                   "vdom": "global"
                 }
               ],
               "url": "/dbcache/system/interface"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "cid": 27,
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "ip": [
                     "10.255.1.1",
                     "255.255.255.0"
                   ],
                   "mode": "static",
                   "name": "fortilink",
                   "oid": 5436,
                   "scope member": [
                     {
                       "name": "fgt-002",
                       "vdom": "global"
                     }
                   ],
                   "status": "up",
                   "type": "aggregate",
                   "vdom": [
                     "root"
                   ]
                 },
				 {"...": "..."},
                 {
                   "ip": [
                     "0.0.0.0",
                     "0.0.0.0"
                   ],
                   "mode": "static",
                   "name": "tun_002",
                   "oid": 5442,
                   "scope member": [
                     {
                       "name": "fgt-002",
                       "vdom": "global"
                     }
                   ],
                   "status": "up",
                   "type": "tunnel",
                   "vdom": [
                     "root"
                   ]
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dbcache/system/interface"
             }
           ]
         }		

.. _dbcache_sdwan_configuration_for_all_devices:

How to get the SD-WAN configuration for all devices?
----------------------------------------------------

Caught in #0467643 and #0574392.

**REQUEST:**

.. code-block:: json

		{
		  "id": 1,
		  "jsonrpc": "1.0",
		  "method": "get",
		  "params": [
		    {
		      "current_adom": "DEMO",
		      "option": [
		        "scope member"
		      ],
		      "scope member": [
		        {
			  "name": "All_FortiGate"
			}
		      ],
		      "url": "/dbcache/system/virtual-wan-link"
		    }
		  ],
		  "session": "320Oe9yHZoTzqmMTrPrZygfxV//0ljUlbyq0ufSHsa3hH3oAlFI1NtqGOgS1vnVMD2LwfyD1TOE5wA4awcKmzw==",
		  "verbose": 1
		}

**RESPONSE:**

.. code-block::

   {
     "id": 1,
  "result": [
    {
      "data": [
        {
          "fail-alert-interfaces": [],
          "fail-detect": "disable",
          "health-check": null,
          "load-balance-mode": "source-ip-based",
          "members": [
            {
              "_dynamic-member": [],
              "comment": null,
              "cost": 0,
              "detect-failtime": 0,
              "detect-http-get": null,
              "detect-http-match": null,
              "detect-http-port": 0,
              "detect-interval": 0,
              "detect-protocol": null,
              "detect-recoverytime": 0,
              "detect-server": null,
              "detect-timeout": 0,
              "gateway": "0.0.0.0",
              "gateway6": "::",
              "ingress-spillover-threshold": 0,
              "interface": [
                "ol_inet_0"
              ],
    [...]
    }

