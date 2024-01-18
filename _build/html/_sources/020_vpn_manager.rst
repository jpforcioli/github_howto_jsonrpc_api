VPN Manager
===========

How to add a member to a vpn topology?
--------------------------------------

We add device ``hub2`` and its vdom ``root`` to the vpn topology ``ol_isp1``
from adom ``DEMO-008``:

**REQUEST:**

.. code-block:: 

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "add",
     "params": [
       {
         "data": {
           "add-route": "disable",
           "assign-ip": "enable",
           "dhcp-server": "enable",
           "iface": "ul_isp1",
           "ipv4-end-ip": "10.1.0.254",
           "ipv4-netmask": "255.255.255.0",
           "ipv4-start-ip": "10.1.0.2",
           "mode-cfg": "enable",
           "net-device": "disable",
           "peertype": "any",
           "protected_subnet": [
             {
               "addr": "all"
             }
           ],
           "scope member": [
             {
               "name": "hub2",
               "vdom": "root"
             }
           ],
           "vpntable": [
             "ol_isp1"
           ]
         },
         "url": "/pm/config/adom/DEMO_008/obj/vpnmgr/node"
       }
     ],
     "session": "zg9cud8ztatc7X4zW4heK2bDnYgcg1cofjKTPGq/BHy75yHBA95uPLAHYD4Zi8oxX6q9idyaWw5eanfjhso6OA==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block::

   {
     "id": 1,
     "result": [
       {
         "data": {
           "id": 1
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/DEMO_008/obj/vpnmgr/node"
       }
     ]
  }