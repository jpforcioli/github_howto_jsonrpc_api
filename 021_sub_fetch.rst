Sub fetch operations
====================

When getting a table, the ``sub fetch`` attribute allows to apply usual
FortiManager API operations like ``fields`` or ``filter`` on sub-tables.

.. note::

   Since your interest is about sub-tables, you cannot use the:

   .. code-block:: json

      "loadsub": 0

   mechanism which is preventing loading the sub-tables.

How to reduce the amount of information returned in sub-table?
--------------------------------------------------------------

The ``fields`` operator can be used to reduce the volume of information to
return.

It can be used at different table level as illustrated by the following example
which demonstrates how to obtain specific attributes at both the main table
level (the ``system sdwan health-check``) and its `sla` sub-table for the
``dev_001`` managed device:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "fields": [
                 "addr-mode",
                 "detect-mode",
                 "protocol",
                 "latency-threshold",
                 "jitter-threshold",
                 "packetloss-threshold"
               ],
               "sub fetch": {
                 "sla": {
                   "fields": [
                     "latency-threshold",
                     "jitter-threshold",
                     "packetloss-threshold"
                   ]
                 }
               },
               "url": "/pm/config/device/dev_001/vdom/root/system/sdwan/health-check"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

   .. tab-item:: REQUEST

      .. code-block:: json         

         {
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "addr-mode": "ipv4",
                   "detect-mode": "active",
                   "oid": 2671,
                   "protocol": "http",
                   "sla": [
                     {
                       "jitter-threshold": 50,
                       "latency-threshold": 250,
                       "oid": 2672,
                       "packetloss-threshold": 5
                     }
                   ]
                 },
                 {
                   "addr-mode": "ipv4",
                   "detect-mode": "active",
                   "oid": 2665,
                   "protocol": "dns",
                   "sla": [
                     {
                       "jitter-threshold": 50,
                       "latency-threshold": 250,
                       "oid": 2666,
                       "packetloss-threshold": 5
                     }
                   ]
                 },
                 {
                   "addr-mode": "ipv4",
                   "detect-mode": "active",
                   "oid": 2675,
                   "protocol": "http",
                   "sla": [
                     {
                       "jitter-threshold": 50,
                       "latency-threshold": 250,
                       "oid": 2676,
                       "packetloss-threshold": 5
                     }
                   ]
                 },
                 {
                   "addr-mode": "ipv4",
                   "detect-mode": "active",
                   "oid": 2669,
                   "protocol": "ping",
                   "sla": [
                     {
                       "jitter-threshold": 50,
                       "latency-threshold": 250,
                       "oid": 2670,
                       "packetloss-threshold": 2
                     }
                   ]
                 },
                 {
                   "addr-mode": "ipv4",
                   "detect-mode": "active",
                   "oid": 2673,
                   "protocol": "http",
                   "sla": [
                     {
                       "jitter-threshold": 50,
                       "latency-threshold": 250,
                       "oid": 2674,
                       "packetloss-threshold": 5
                     }
                   ]
                 },
                 {
                   "addr-mode": "ipv4",
                   "detect-mode": "active",
                   "oid": 2667,
                   "protocol": "http",
                   "sla": [
                     {
                       "jitter-threshold": 50,
                       "latency-threshold": 250,
                       "oid": 2668,
                       "packetloss-threshold": 5
                     }
                   ]
                 },
                 {
                   "addr-mode": "ipv4",
                   "detect-mode": "active",
                   "oid": 3535,
                   "protocol": "ping",
                   "sla": [
                     {
                       "jitter-threshold": 5,
                       "latency-threshold": 300,
                       "oid": 3536,
                       "packetloss-threshold": 10
                     },
                     {
                       "jitter-threshold": 5,
                       "latency-threshold": 400,
                       "oid": 3537,
                       "packetloss-threshold": 10
                     }
                   ]
                 },
                 {
                   "addr-mode": "ipv4",
                   "detect-mode": "active",
                   "oid": 3538,
                   "protocol": "ping",
                   "sla": [
                     {
                       "jitter-threshold": 5,
                       "latency-threshold": 100,
                       "oid": 3539,
                       "packetloss-threshold": 10
                     }
                   ]
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/device/dev_001/vdom/root/system/sdwan/health-check"
             }
           ]
         }
   
How to hide a specific sub-table?
---------------------------------

Caught in #0378630.

Since you can't use:

.. code-block:: json

   "loadsub": 0

anymore, you need a way to instruct FortiManager to not return some specific sub
tables. You can use the:

.. code-block:: json

   "subfetch hidden": 1

instruction with a specific sub-table to prevent returning it.

This is an example where the ``subfetch hidden`` instruction isn't used. The
goal is to get the list of managed devices:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "get",
           "params": [
             {
               "fields": [
                 "name"
               ],
               "url": "/dvmdb/device"
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
                   "ha_slave": null,
                   "name": "dev_001",
                   "oid": 170,
                   "vdom": [
                     {
                       "comments": "",
                       "devid": "dev_001",
                       "ext_flags": 1,
                       "flags": null,
                       "name": "root",
                       "node_flags": 4,
                       "oid": 3,
                       "opmode": "nat",
                       "rtm_prof_id": 0,
                       "status": null,
                       "tab_status": null,
                       "vpn_id": 0
                     }
                   ]
                 },
                 {"...": "..."},
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/device"
             }
           ]
         }

FortiManager returned your list of managed devices. However, for each devices
returned, you can see the ``ha_slave`` and ``vdom`` sub-tables. 

The following example, which now uses the ``subfetch hidden`` instruction,
demontrates how to instruct FortiManager not to return those two sub-tables:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "get",
           "params": [
             {
               "fields": [
                 "name"
               ],
               "sub fetch": {
                 "ha_slave": {
                   "subfetch hidden": 1
                 },
                 "vdom": {
                   "subfetch hidden": 1
                 }
               },
               "url": "/dvmdb/device"
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
                   "name": "dev_001",
                   "oid": 170
                 },
                 {"...", "..."},
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/device"
             }
           ]
         }

Sub fetch TODO
--------------

Sub fetch dictionnary + subfetch hidden:

.. code-block:: text

   {
     "id": 1,
     "method": "get",
     "params": [
       ...
       {
         "url": "pm/config/adom/root/obj/firewall/profile-group",
         "option": "datasrc",
         "attr": "application-list",
         "sub fetch": {
           "application list": {
             "subfetch hidden": 1
           }
         }
       },
    ...
     ]
   }

Sub fetch option:

.. code-block:: text

   {
     "id": "ce0a766f-0167-4f50-ad93-25cc32845003",
     "method": "get",
     "params": [
       {
         "url": "pm/config/adom/600/pkg/default/firewall/policy/5",
         "expand datasrc": [
           ... ...
           {
             "name": "internet-service-id",
             "datasrc": [
               {
                 "obj type": "firewall internet-service",
                 "option": [
                   "get flags"
                 ]
               }
             ]
           },
           {
             "name": "internet-service-custom",
             "datasrc": [
               {
                 "obj type": "firewall internet-service-custom",
                 "option": [
                   "get flags"
                 ]
               }
             ]
           },
           ... ...
           ... ...
         ],
         "sub fetch": 1,
         "loadsub": 1,
         "object template": 0,
         "option": [
           "scope member",
           "get flags",
           "get meta",
           "extra info"
         ]
       }
     ]
   }

subfecth filter

.. code-block:: text

   { "client": "\/usr\/local\/apache2\/bin\/httpd:15030", "method": "get", "params": [{ "sub fetch": { "dynamic_mapping": { "scope member": [{ "name": "FortiGate-VM64", "vdom": "vdom1"}]}}, "subfetch filter": 1, "target start": 2, "url": "pm\/config\/adom\/ad62\/obj\/dynamic\/interface"}], "session": 32518, "src": "127.0.0.1"}


"subfetch count":["!=", 0] // "match count" filter, op could be "!=", "==", ">=", "<=", ">", "<"

.. code-block:: text

   {"id":"32caabcc-e58d-40a8-8096-c4795af59ece","method":"get","params":[{"url":"pm/config/device/FGVM08HZ20319061/vdom/root/vpn/ipsec/phase1-interface","sub
   fetch":1,"loadsub":1,"object template":1}]}

Another example captured when showing the managed FAP:

.. code-block:: json

   {
     "id": "6d31c923-e2b9-460c-a91f-49483d9950bc",
     "method": "get",
     "params": [
       {
         "url": "pm/config/adom/DEMO/obj/wireless-controller/wtp",
         "scope member": [
           {
             "name": "demo_branch-1-fgt",
             "vdom": "root"
           }
         ],
         "expand datasrc": [
           {
             "name": "wtp-profile",
             "datasrc": [
               {
                 "obj type": "wireless-controller wtp-profile",
                 "sub fetch": {
                   "platform": {
                     "subfetch hidden": 1
                   },
                   "lan": {
                     "subfetch hidden": 1
                   },
                   "lbs": {
                     "subfetch hidden": 1
                   },
                   "radio-1": {},
                   "radio-2": {},
                   "radio-3": {}
                 },
                 "subfetch filter": 1
               }
             ]
           }
         ],
         "data": null
       }
     ]
   }

How to get entries when a subtable isn't empty?
-----------------------------------------------

Caught in #378630.

Following |fmg_api| call will return all firewall address from the ``dc_emea`` ADOM which are with some per-device mapping:

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
                 "dynamic_mapping": {},
                 "fields": [
                   "subnet"
                 ]
               },
               "subfetch filter": 1,
               "url": "/pm/config/adom/dc_emea/obj/firewall/address"
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
                   "dynamic_mapping": [
                     {
                       "_scope": [
                         {
                           "name": "dc_emea_dev_001",
                           "vdom": "root"
                         }
                       ],
                       "allow-routing": "disable",
                       "cache-ttl": 0,
                       "clearpass-spt": "unknown",
                       "color": 0,
                       "comment": null,
                       "country": [],
                       "dirty": "dirty",
                       "end-ip": "0.0.0.0",
                       "epg-name": null,
                       "fabric-object": "disable",
                       "filter": null,
                       "fqdn": null,
                       "fsso-group": [],
                       "hw-model": null,
                       "hw-vendor": null,
                       "interface": null,
                       "macaddr": [],
                       "node-ip-only": "disable",
                       "obj-id": null,
                       "obj-tag": null,
                       "obj-type": "ip",
                       "oid": 5092,
                       "organization": null,
                       "os": null,
                       "policy-group": null,
                       "route-tag": 0,
                       "sdn": [],
                       "sdn-addr-type": "private",
                       "sdn-tag": null,
                       "start-ip": "0.0.0.0",
                       "sub-type": "sdn",
                       "subnet": [
                         "10.1.0.1",
                         "255.255.255.255"
                       ],
                       "subnet-name": null,
                       "sw-version": null,
                       "tag-detection-level": null,
                       "tag-type": null,
                       "tenant": null,
                       "type": "ipmask",
                       "unset attrs": [
                         "associated-interface"
                       ],
                       "uuid": "69da87b4-88b1-51ee-6922-a01ab7807499",
                       "wildcard": [
                         "0.0.0.0",
                         "0.0.0.0"
                       ],
                       "wildcard-fqdn": null
                     }
                   ],
                   "list": null,
                   "name": "host_001",
                   "oid": 5091,
                   "tagging": null
                 },
                 {
                   "dynamic_mapping": [
                     {
                       "_scope": [
                         {
                           "name": "fgt_001",
                           "vdom": "root"
                         }
                       ],
                       "allow-routing": "disable",
                       "cache-ttl": 0,
                       "clearpass-spt": "unknown",
                       "color": 0,
                       "comment": null,
                       "country": [],
                       "dirty": "dirty",
                       "end-ip": "0.0.0.0",
                       "epg-name": null,
                       "fabric-object": "disable",
                       "filter": null,
                       "fqdn": null,
                       "fsso-group": [],
                       "hw-model": null,
                       "hw-vendor": null,
                       "interface": null,
                       "macaddr": [],
                       "node-ip-only": "disable",
                       "obj-id": null,
                       "obj-tag": null,
                       "obj-type": "ip",
                       "oid": 5094,
                       "organization": null,
                       "os": null,
                       "policy-group": null,
                       "route-tag": 0,
                       "sdn": [],
                       "sdn-addr-type": "private",
                       "sdn-tag": null,
                       "start-ip": "0.0.0.0",
                       "sub-type": "sdn",
                       "subnet": [
                         "10.2.0.1",
                         "255.255.255.255"
                       ],
                       "subnet-name": null,
                       "sw-version": null,
                       "tag-detection-level": null,
                       "tag-type": null,
                       "tenant": null,
                       "type": "ipmask",
                       "unset attrs": [
                         "associated-interface"
                       ],
                       "uuid": "7aebfef2-88b1-51ee-b723-479f05b588a5",
                       "wildcard": [
                         "0.0.0.0",
                         "0.0.0.0"
                       ],
                       "wildcard-fqdn": null
                     }
                   ],
                   "list": null,
                   "name": "host_002",
                   "oid": 5093,
                   "tagging": null
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/dc_emea/obj/firewall/address"
             }
           ]
         }