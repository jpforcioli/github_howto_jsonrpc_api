VPN Management
==============

SSL VPN
-------

How to get the default SSLVPN os-check-list?
++++++++++++++++++++++++++++++++++++++++++++

Caught in #0678319.

Before #0678319, the default ``os-check-list`` was differing between different ``os_ver``, ``mr`` and *branch point*. They were keeping on changing according to the *Windows* and *macOS* version that were used in the world.

However, inside FortiManager code (GUI and backend) this ``os-check-list`` was 
hard-coded and it could have caused inconsistencies between FortiManager and its managed FortiGate.

Now FortiManager can extract this ``os-check-list`` from FortiOS syntax.

Using ADOM DB
_____________

The following example shows how to get the ``os-check-list`` from the ``demo`` 
ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/_data/default_sslvpn_os_check_list"
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
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "windows-7",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "windows-8.1",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "windows-10",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "22000",
                   "name": "windows-11",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-mojave-10.14",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-catalina-10.15",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.0",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-bigsur-11.1",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.2",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.3",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-bigsur-11.4",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.5",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.6",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.7",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-monterey-12.0",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-monterey-12.1",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-monterey-12.2",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-monterey-12.3",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-monterey-12.4",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-monterey-12.5",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-monterey-12.6",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-ventura-13",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-sonoma-14",
                   "tolerance": 0
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/_data/default_sslvpn_os_check_list"
             }
           ]
         }

Using Device DB
_______________

The following example shows how to get the ``os-check-list`` from the ``dev_001`` managed device:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
        
         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/device/dev_001/_data/default_sslvpn_os_check_list"
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
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "windows-7",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "windows-8.1",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "windows-10",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "22000",
                   "name": "windows-11",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-mojave-10.14",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-catalina-10.15",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.0",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-bigsur-11.1",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.2",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.3",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-bigsur-11.4",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.5",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.6",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-bigsur-11.7",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-monterey-12.0",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-monterey-12.1",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-monterey-12.2",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-monterey-12.3",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-monterey-12.4",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-monterey-12.5",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "1",
                   "name": "macos-monterey-12.6",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-ventura-13",
                   "tolerance": 0
                 },
                 {
                   "action": "allow",
                   "latest_patch_level": "0",
                   "name": "macos-sonoma-14",
                   "tolerance": 0
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/device/dev_001/_data/default_sslvpn_os_check_list"
             }
           ]
         }
         
IPseC VPN
---------

How to add a member to a vpn topology?
++++++++++++++++++++++++++++++++++++++

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