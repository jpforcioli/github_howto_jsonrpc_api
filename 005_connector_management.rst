Connector Management
====================

JSON API Connector
------------------

How to create a new JSON API Connector?
+++++++++++++++++++++++++++++++++++++++

It's a two steps process:

#. Create the JSON API connector without tags
#. Create the tags

Create the JSON API connector without tags
__________________________________________


.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "name": "json_api_connector_001",
                 "status": "enable"
               },
               "url": "/pm/config/adom/adom_70_001/obj/user/json"
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
                 "name": "json_api_connector_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/adom_70_001/obj/user/json"
             }
           ]
         }

Create the tags
_______________

Adding tags is very straightforward.

It is just about adding new entries in table ``user adgrp`` with a name matching
the following format: 

.. code-block:: text

   js_<json_api_connector_name>_<tag_name>


For instance, considering the above created JSON API connector
``json_api_connector_001`` (i.e., ``json_api_connector_name``), if you want to
add ``tag_001`` (i.e., ``tag_name``), then the name of the ``user adgrp`` entry
will be:

.. code-block:: text

   js_json_api_connector_001_tag_001

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
                   "name": "js_json_api_connector_001_tag_001",
                   "connector-source": "FMG JSON",
                   "server-name": "FortiManager"
                 },
                 {
                   "name": "js_json_api_connector_001_tag_002",
                   "connector-source": "FMG JSON",
                   "server-name": "FortiManager"
                 },
                 {
                   "name": "js_json_api_connector_001_tag_003",
                   "connector-source": "FMG JSON",
                   "server-name": "FortiManager"
                 }
               ],
               "url": "/pm/config/adom/adom_70_001/obj/user/adgrp"
             }
           ],
           "session": "{{session}}"
         }
      
      .. note::
      
         - You have to use specific a value for ``server-name```; it has to be
           ``FortiManager``.
         - However, you can use any string value for ``connector-source`` but better
           to keep the one used by FortiManager GUI which is ``FMG JSON``.

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
               "url": "/pm/config/adom/adom_70_001/obj/user/adgrp"
             }
           ]
         }
      
Create both using a single API request
______________________________________

If you like multiplexing API calls:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
         	
         {
           "id": 1,
           "method": "add",
           "params": [
             {
               "data": {
                 "name": "json_api_connector_001",
                 "status": "enable"
               },
               "url": "/pm/config/adom/adom_70_001/obj/user/json"
             },
             {
               "url": "/pm/config/adom/adom_70_001/obj/user/adgrp",
               "data": [
                 {
                   "name": "js_json_api_connector_001_tag_001",
                   "server-name": "FortiManager",
                   "connector-source": "FMG JSON"
                 },
                 {
                   "name": "js_json_api_connector_001_tag_002",
                   "server-name": "FortiManager",
                   "connector-source": "FMG JSON"
                 },
                 {
                   "name": "js_json_api_connector_001_tag_003",
                   "server-name": "FortiManager",
                   "connector-source": "FMG JSON"
                 }
               ]
             }
           ],
           "session": "{{session}}"
         }

      .. note::
      
         - You have to use specific a value for ``server-name``; it has to be
           ``FortiManager``. 
      
         - However, you can use any string value for ``connector-source`` but
           better to keep the one used by FortiManager GUI which is ``FMG
           JSON``.

   .. tab-item:: RESPONSE

      .. code-block:: json
      
         {
           "id": 1,
           "result": [
             {
               "data": {
                 "name": "json_api_connector_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/adom_70_001/obj/user/json"
             },
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/adom_70_001/obj/user/adgrp"
             }
           ]
         }
      
How to delete a JSON API Connector?
+++++++++++++++++++++++++++++++++++

To delete JSON API Connector ``json_api_connector_001`` from ADOM ``dc_amer``:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "delete",
           "params": [
             {
               "url": "/pm/config/adom/dc_amer/obj/user/json/json_api_connector_001"
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
               "url": "/pm/config/adom/dc_amer/obj/user/json/json_api_connector_001"
             }
           ]
         }

Managing JSON API Connector tags?
+++++++++++++++++++++++++++++++++

Add IP addresses
________________

This request adds IPv4 addresses ``10.1.0.{1,2,3}`` and IPv6 addresses
``2001:DB8::{1,2,3}`` to the ``tag_001`` tag which has been declared within the
``json_api_connector_001`` JSON API Connector:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "command": "add",
                 "group": "tag_001",
                 "ip-addr": [
                   "10.1.0.1",
                   "10.1.0.2",
                   "10.1.0.3",
                   "10.2.0.1",
                   "2001:DB8::1",
                   "2001:DB8::2",
                   "2001:DB8::3"
                 ],
                 "path": "{{adom}}/json_api_connector_001"
               },
               "url": "/connector/user/manage"
             }
           ]
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/connector/user/manage"
             }
           ],
           "id": 3
         }

Get IP addresses
________________

This request retrieves IP addresses corresponding to the ``tag_001`` tag which
has been declared within the ``json_api_connector_001`` JSON API Connector:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "{{adom}}",
                 "connector": "json_api_connector_001",
                 "server_type": "json",
                 "type": "connector",
                 "group":"tag_001"
               },
               "url": "/connector/get/user"
             }
           ]
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "result": [
             {
               "data": [
                 {
                   "grpname": "js_json_api_connector_001_tag_001",
                   "ip_addr": "10.1.0.1",
                   "ip_addr6": "::-::",
                   "name": "",
                   "state": 1
                 },
                 {
                   "grpname": "js_json_api_connector_001_tag_001",
                   "ip_addr": "10.1.0.2",
                   "ip_addr6": "::-::",
                   "name": "",
                   "state": 1
                 },
                 {
                   "grpname": "js_json_api_connector_001_tag_001",
                   "ip_addr": "10.1.0.3",
                   "ip_addr6": "::-::",
                   "name": "",
                   "state": 1
                 },
                 {
                   "grpname": "js_json_api_connector_001_tag_001",
                   "ip_addr6": "2001:db8::1-2001:db8::1",
                   "name": "",
                   "state": 1
                 },
                 {
                   "grpname": "js_json_api_connector_001_tag_001",
                   "ip_addr6": "2001:db8::2-2001:db8::2",
                   "name": "",
                   "state": 1
                 },
                 {
                   "grpname": "js_json_api_connector_001_tag_001",
                   "ip_addr6": "2001:db8::3-2001:db8::3",
                   "name": "",
                   "state": 1
                 }				 
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/connector/get/user"
             }
           ]
         }		

Delete IP addresses
___________________

To delete ``10.1.0.1``, ``10.1.0.3`` and ``10.1.0.5`` IP addresses from tag
``tag_001`` declared within the ``json_api_connector_001`` JSON API Connector:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "command": "delete",
                 "group": "tag_001",
                 "ip-addr": [
                   "10.1.0.1",
                   "10.1.0.3",
                   "10.1.0.5"
                 ],
                 "path": "{{adom}}/json_api_connector_001"
               },
               "url": "/connector/user/manage"
             }
           ],
           "session": "{{session}"
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
               "url": "/connector/user/manage"
             }
           ]
         }

ClearPass
---------

TODO: How to simulate
+++++++++++++++++++++

.. code-block:: text

   diagnose system print connector DEMO clearpass cp-10.210.34.247
   2020-04-20 17:57:30 Request:
   2020-04-20 17:57:30 { "client": "-newcli:24885", "id": 2, "method": "exec", "params": [{ "data": { "adom": "DEMO", "connector": "cp-10.210.34.247", "server_type": "clearpass"}, "target start": 1, "url": "debug"}], "root": "connector"}
   2020-04-20 17:57:30 __get_user_list : no user info obtained from server cp-10.210.34.247
   2020-04-20 17:57:30 __get_cuser_list : no user info obtained from server cp-10.210.34.247
   2020-04-20 17:57:30 __get_adgrp_list : no adgrp info obtained from server cp-10.210.34.247
   2020-04-20 17:57:30 Response:
   2020-04-20 17:57:30 { "id": 2, "result": [{ "status": { "code": 0, "message": "OK"}, "url": "debug"}]}2020-04-20 17:57:30

How to get a defined ClearPass connector?
+++++++++++++++++++++++++++++++++++++++++

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "get",
           "params": [
             {
               "object template": 0,
               "option": ["get used", "get flags", "get devobj mapping", "get meta", "loadsub", "extra info"],
               "url": "/pm/config/adom/ClearPass/obj/user/clearpass/cp-001"
             }
           ],
           "session": 41581
         }

How to get users?
+++++++++++++++++

This request is retrieving the user which are considered as authenticated at the
ClearPass level.

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "ClearPass",
                 "connector": "cp-001",
                 "domid": "user-v-tree",
                 "if_all_user": 0,
                 "server_type": "clearpass",
                 "type": "clearpass"
               },
               "url": "/connector/get/user"
             }
           ],
           "session": 35742
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 1,
           "result": [
             {
               "data": [
                 {
                   "grpname": "cp_cp-001_Support",
                   "ip_addr": "10.210.34.185",
                   "name": "user1",
                   "state": 1
                 },
                 {
                   "grpname": "cp_cp-001_Marketing",
                   "ip_addr": "10.210.34.186",
                   "name": "user2",
                   "state": 1
                 },
                 {
                   "grpname": "cp_cp-001_Sales",
                   "ip_addr": "10.210.34.187",
                   "name": "user3",
                   "state": 1
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/connector/get/user"
             }
           ]
         }

H ow to get address groups?
+++++++++++++++++++++++++++

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "ClearPass",
                 "connector": "cp-001",
                 "server_type":
                 "clearpass"
               },
               "url": "/connector/get/adgrp"
             }
           ],
           "session": 35742
         }

Update connector (ie. retrieve logged in users)
+++++++++++++++++++++++++++++++++++++++++++++++

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "ClearPass",
                 "connector": "cp-001",
                 "server_type": "clearpass",
                 "service_type": 0
               },
               "url": "/connector/update"
            }
           ],
           "session": 35742
         }

Response is having a ``taskid``

How to simulate a user login via FMG JSON API?
++++++++++++++++++++++++++++++++++++++++++++++

The end result will be that FMG will see an authenticated clearpass
user, and will send it to the managed devices.

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "ClearPass",
                 "connector": "cp-001",
                 "ip-addr": "10.0.0.100",
                 "role": "Marketing, [User Authenticated]",
                 "user": "user100"
               },
               "url": "/connector/user/login"
             }
           ],
           "session": "Nsr3neywQlAxPXm+IHNhsjGr0bzzD4SRXSP8Q7zuBiwMpT+1yFrISKBvIdJBokSxL15X9OLr6HZPH4BpU3FmTQ==",
           "verbose": 1
         }

      .. note::
        
         ``Marketing`` has to be mapped to an existing ``user.group`` used in a 
         firewall policy. Or ``user.adgrp`` object named 
         ``cp_<connector>_Marketing`` has to be used by a firewal policy

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
               "url": "/connector/user/login"
             }
           ]
         }

How to simulate a user logout via FMG JSON API?
+++++++++++++++++++++++++++++++++++++++++++++++

The end result will be that FMG will see an authenticated clearpass
user, and will send it to the managed devices.

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "ClearPass",
                 "connector": "cp-001",
                 "ip-addr": "10.0.0.100",
                 "role": "Marketing, [User Authenticated]",
                 "user": "user100"
               },
               "url": "/connector/user/logout"
             }
           ],
           "session": "y1S9rwduTi71hMjLsur1P4vQ5ZbnX6aMpjBsSVfYLtVyeXGM0Srg1hbyIx6jLqcxWJ4h1gxp02BLBITWE5DGMg==",
           "verbose": 1
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
               "url": "/connector/user/logout"
             }
           ]
         }

Cisco ACI
---------

.. _how_to_get_all_tenants:

How to get all tenants?
+++++++++++++++++++++++

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "root",
                 "command": "epgs",
                 "connector_name": "APIC-MOW"
               },
               "url": "/sys/api/sdnconnector"
             }
           ],
           "session": 11221
         }

   .. tab-item:: RESPONSE

      .. code-block:: json
	  
         {
           "id": 1,
           "result": [
             {
               "data": "[{\"epgs\": [{\"name\": \"classic|VLAN_3102\", \"tags\": []}, {\"name\": \"classic|uAPP\", \"tags\": []}, {\"name\": \"classic|uWeb.test\", \"tags\": []}, {\"name\": \"classic|VLAN_3100\", \"tags\": []}, {\"name\": \"classic|uWEB\", \"tags\": []}, {\"name\": \"classic|uApp.test\", \"tags\": []}], \"tenant\": \"customer\"}, {\"epgs\": [{\"name\": \"K8sDemo_bd_kubernetes-service|ToOut-L3OUT\", \"tags\": [\"K8sDemo-8bb120060f0848e0280b450eeea23d95\"]}, {\"name\": \"K8sDemo_bd_kubernet[...]",
             }
           "[...]": "[...]"
         }

Note that the *data* attribute is a string!
	  
How to import a tenant?
+++++++++++++++++++++++

First you need to get the available tenants by using the info
how_to_get_all_tenants_.

Then you just have to pick one tenant from the outout, and create a Firewall
Address.

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "add",
           "params": [
             {
               "data": {
                 "epg-name": "classic|VLAN_3100",
                 "name": "customer-classic|VLAN_3100",
                 "sdn": "AP IC-MOW",
                 "tenant": "customer",
                 "type": 15
               },
               "url": "pm/config/adom/root/obj/firewall/address"
             }
           ],
           "session": 11221
         }

SSO Agent
----------

How to retrieve new ``user.agrp``?
++++++++++++++++++++++++++++++++++

The goal is to trigger the same operation as the *Apply&Refresh* button present
when editing a *Fortinet Single Sign-On Agent*.

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": "1",
           "method": "exec",
           "params": [
             {
               "url": "sys/api/fsso",
               "data": {
                 "adom": "{{adom}}",
                 "user_fsso": "fsso_agent_001"
               }
             }
           ],
           "session": "{{session}}"
         }

Thread Feeds Connectors
-----------------------

How to define External Resources hosted in FortiManager?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

See section :ref:`External Resources`.

How to get resolved IP addresses for an IP Address Threat Feed?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to get the resolved IP addresses for the 
``malicicous_ip`` IP Address Thread Feed defined in the ``demo`` ADOM and from 
the perspective of the ``dev_001`` managed device:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "action": "get",
                 "resource": "/api/v2/monitor/system/external-resource/entry-list?count=0&mkey=malicious_ip&vdom=root",
                 "target": [
                   "adom/demo/device/dev_001"
                 ]
               },
               "url": "/sys/proxy/json"
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
                   "response": {
                     "action": "entry-list",
                     "build": 2571,
                     "http_method": "GET",
                     "name": "external-resource",
                     "path": "system",
                     "results": {
                       "conn_attempt_time": 1715356114,
                       "entries": [
                         {
                           "entry": "192.168.2.100",
                           "valid": true
                         },
                         {
                           "entry": "172.200.1.4/16",
                           "valid": true
                         },
                         {
                           "entry": "172.16.1.2/24",
                           "valid": true
                         },
                         {
                           "entry": "172.16.8.1-172.16.8.100",
                           "valid": true
                         },
                         {
                           "entry": "2001:0db8::eade:27ff:fe04:9a01/120",
                           "valid": true
                         },
                         {
                           "entry": "2001:0db8::eade:27ff:fe04:aa01-2001:0db8::eade:27ff:fe04:ab01",
                           "valid": true
                         }
                       ],
                       "http_status_code": 304,
                       "invalid_count": 0,
                       "last_content_update_time": 1715355563,
                       "overflow": false,
                       "resource_file_status": "downloaded",
                       "status": "success",
                       "valid_count": 6
                     },
                     "serial": "FGVMMLREDACTED40",
                     "status": "success",
                     "vdom": "root",
                     "version": "v7.4.2"
                   },
                   "status": {
                     "code": 0,
                     "message": "OK"
                   },
                   "target": "dev_001"
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

SASE Connector
--------------

TODO:

.. code-block:: text

   # Get SASE Controller status
   Request [gui forward:23891:9aed47df-a7fd-4c2f-acdf-65c35e4756c4]:
   { "client": "gui forward:23891", "id": "9aed47df-a7fd-4c2f-acdf-65c35e4756c4", "keep_session_idle": 1, "method": "get", "params": [{ "scope member": { "name": "FFSASEREDACTED67", "vdom": "root"}, "target start": 2, "url": "pm\/config\/adom\/root\/obj\/fmg\/sase-manager\/status"}], "session": 3761}
   Response [gui forward:23891:9aed47df-a7fd-4c2f-acdf-65c35e4756c4]:
   { "id": "9aed47df-a7fd-4c2f-acdf-65c35e4756c4", "result": [{ "data": { "forticlient-ver": "7.0.11", "forticloud-id": 1705791, "license-type": 0, "oid": 8283, "spa-hubs": 0}, "status": { "code": 0, "message": "OK"}, "url": "pm\/config\/adom\/root\/obj\/fmg\/sase-manager\/status"}]}

   # Get SASE Controller settings
   Request [gui forward:23894:0b253ff9-cfee-44e2-a066-fef040565032]:
   { "client": "gui forward:23894", "id": "0b253ff9-cfee-44e2-a066-fef040565032", "keep_session_idle": 1, "method": "get", "params": [{ "object template": 0, "option": ["get used", "get flags", "get devobj mapping", "get meta", "loadsub"], "scope member": { "name": "FFSASEREDACTED67", "vdom": "root"}, "target start": 2, "url": "pm\/config\/adom\/root\/obj\/fmg\/sase-manager\/settings"}], "session": 3761}
   Response [gui forward:23894:0b253ff9-cfee-44e2-a066-fef040565032]:
   { "id": "0b253ff9-cfee-44e2-a066-fef040565032", "result": [{ "data": {   "address": ["BaaS_Backup_Clients_FAL", "ACE_Tacacs_Clients", "Bad_IPs_Group", "sase-BSA_Host_List", "AKLHYDRA1"], "oid": 8282, "profile-group": ["CMI Mandated", "DOE Mandated", "sase-security-group"], "sync-address": 5, "sync-profile-group": 5, "sync-user": 5, "user": ["sase-servers-group", "sase-groups", "sase-user2", "sase-user1", "sase-ldap-server", "sase-radius-server"]}, "status": { "code": 0, "message": "OK"}, "url": "pm\/config\/adom\/root\/obj\/fmg\/sase-manager\/settings"}]}

