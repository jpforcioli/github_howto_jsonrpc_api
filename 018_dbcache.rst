Using ``dbcache``
=================

How to get the list of interfaces for a specific device?
--------------------------------------------------------

Caught in #455627.

**REQUEST:**

.. code-block:: json
		
		{
		  "id": 1,
		  "method": "get",
		  "params": [
		    {
		      "url": "/dbcache/system/interface",
		      "option": [
		        "scope member"
		      ],
		      "scope member": [
		        {
			  "name": "FGT60Da",
			  "vdom": "global"
			}
		      ],
		      "fields": [
		        "name",
			"alias",
			"ip",
			"ipv6",
			"mode",
			"type",
			"vdom",
			"status"
		      ],
		      "current_adom": "455627_mapping"
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

