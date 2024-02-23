Alternative FortiManager APIs
=============================

REST API
--------

Yes you can use REST API!

Caught in #0872278.

Most |fmg_api| requests have a REST counterpart.

For instance:

+----------------------------------------------+--------------------------------------------------------------------+
|FortiManager JSON RPC url                     |HTTP url                                                            |
+==============================================+====================================================================+
|``/dvmdb/adom``                               |``https://<fmg_ip>/jsonrpc/dvmdb/adom``                             |
+----------------------------------------------+--------------------------------------------------------------------+
|``/pm/config/adom/root/obj/firewall/address/``|``https://<fmg_ip>/jsonrpc/pm/config/adom/roo/obj/firewall/address``|
+----------------------------------------------+--------------------------------------------------------------------+

JSON RPC methods are mapped to HTTP methods:

+---------------+-----------+
|JSON RPC method|HTTP method|
+===============+===========+  
|``get``        |``GET``    |
+---------------+-----------+
|``put``        |``PUT``    |
+---------------+-----------+
|``exec``       |``POST``   |
+---------------+-----------+
|``update``     |``UPDATE`` |
+---------------+-----------+
|``delete``     |``DELETE`` |
+---------------+-----------+

The ``data`` block used by some |fmg_api| requests should be part of the HTTP
query string!

If the |fmg_api|  cannot be converted with the above instructions, then it's
simply not supported for REST API.

REST API is using HTTP basic authentication; you can use same credentias as
with the |fmg_api|.

Getting system status
+++++++++++++++++++++

**REQUEST:**

.. code-block:: shell

   curl -s -k -u devops:fortinet https://10.210.35.112/jsonrpc/sys/status | jq

**RESPONSE:**

.. code-block:: json

   {
     "result": [
       {
         "data": {
           "Admin Domain Configuration": "Enabled",
           "BIOS version": "04000002",
           "Branch Point": "1317",
           "Build": "1317",
           "Current Time": "Mon Jan 09 22:51:15 CET 2023",
           "Daylight Time Saving": "Yes",
           "FIPS Mode": "Disabled",
           "HA Mode": "Stand Alone",
           "Hostname": "prod-fmg-722-interim-001",
           "License Status": "Valid",
           "Major": 7,
           "Max Number of Admin Domains": 105,
           "Max Number of Device Groups": 100,
           "Minor": 2,
           "Offline Mode": "Disabled",
           "Patch": 2,
           "Platform Full Name": "FortiManager-VM64-KVM",
           "Platform Type": "FMG-VM64-KVM",
           "Release Version Information": " (Interim)",
           "Serial Number": "FMVMELTM22000017",
           "TZ": "Europe/Brussels",
           "Time Zone": "(GMT+1:00) Brussels, Copenhagen, Madrid, Paris.",
           "Version": "v7.2.2-build1317 230107 (Interim)",
           "x86-64 Applications": "Yes"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/sys/status"
       }
     ]
   }

Get list of ADOMs
+++++++++++++++++

**REQUEST:**

.. code-block:: shell

   curl -s -k -u devops:fortinet https://10.210.35.112/jsonrpc/dvmdb/adom/root | jq
   

**RESPONSE:**

.. code-block:: json

   {
     "result": [
       {
         "data": {
           "create_time": 0,
           "desc": "",
           "flags": 136,
           "log_db_retention_hours": 1440,
           "log_disk_quota": 51200,
           "log_disk_quota_alert_thres": 90,
           "log_disk_quota_split_ratio": 70,
           "log_file_retention_hours": 8760,
           "logview_customize": "",
           "mig_mr": 0,
           "mig_os_ver": 0,
           "mode": 1,
           "mr": 2,
           "name": "root",
           "obj_customize": "",
           "oid": 3,
           "os_ver": 7,
           "restricted_prds": 1,
           "state": 1,
           "tab_status": "",
           "uuid": "14d92a26-8dd6-51ed-b0ed-8258bafad045",
           "workspace_mode": 1
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom/root"
       }
     ]
   }

Using FortiManager GUI
----------------------

Caught in #273964.

It seems to be available only with the new FortiManager flat UI (FortiManager 5.0.0).

We have to use this special HTTP URL:

.. code-block::

   https://FMG_IP/cgi-bin/module/flatui/json?req={<your JSON request>}

For instance, to get firewall policy ID 2 from Policy Package ``default`` located in ADOM ``ADOM_54_001``:

**REQUEST:**

.. code-block::

   https://192.168.194.62/cgi-bin/module/flatui/json?req={'id':2,'method':'get', 'params':[{'url':'pm/config/adom/ADOM_54_001/pkg/default/firewall/policy/2', 'data':{}}]}

**RESPONSE:**

.. code-block:: json

		{ "code": 0, "message": "", "data": { "id": 2, "result": [ { "data": { "_byte": 789, "_first_hit": 1443701598, "_global-dst-intf": "", "_global-src-intf": "", "_global-vpn-tgt": 0, "_hitcount": 377, "_last_hit": 1444003543, "_pkts": 55, "action": 1, "auth-path": 0, "auth-redirect-addr": "", "auto-asic-offload": 1, "block-notification": 0, "captive-portal-exempt": 0, "capture-packet": 0, "comments": "", "diffserv-forward": 0, "diffserv-reverse": 0, "diffservcode-forward": "000000", "diffservcode-rev": "000000", "disclaimer": 0, "dsri": 0, "dstaddr": [ "HOST_102" ], "dstaddr-negate": 0, "dstintf": [ "OUT" ], "firewall-session-dirty": 0, "fixedport": 0, "fsso": 0, "global-label": "Project #1", "inbound": 0, "ippool": 0, "label": "Project #1", "logtraffic": 2, "logtraffic-start": 0, "match-vip": 0, "name": "Policy_002", "nat": 0, "natinbound": 0, "natip": [ "0.0.0.0", "0.0.0.0" ], "natoutbound": 0, "ntlm": 0, "ntlm-guest": 0, "obj seq": 2, "outbound": 0, "permit-any-host": 0, "permit-stun-host": 0, "policyid": 2, "profile-type": 0, "redirect-url": "", "rsso": 0, "rtp-nat": 0, "scan-botnet-connections": 0, "schedule": [ "always" ], "schedule-timeout": 0, "send-deny-packet": 0, "service": [ "ALL" ], "service-negate": 0, "session-ttl": 0, "srcaddr": [ "HOST_002" ], "srcaddr-negate": 0, "srcintf": [ "IN" ], "ssl-mirror": 0, "status": 1, "tcp-mss-receiver": 0, "tcp-mss-sender": 0, "timeout-send-rst": 0, "utm-status": 0, "uuid": "d9a9999e-ad46-51e5-9f9a-e454832135f0", "vlan-cos-fwd": 255, "vlan-cos-rev": 255, "wanopt": 0, "wanopt-detection": 1, "wanopt-passive-opt": 0, "wccp": 0, "webcache": 0, "webcache-https": 0, "wsso": 1 }, "status": { "code": 0, "message": "OK" }, "url": "pm\/config\/adom\/ADOM_54_001\/pkg\/default\/firewall\/policy\/2" } ] } }
		

Using *requests* python module
------------------------------

Caught in #600130.

The advantage is that we don't have to:

- Authenticate
- Provide a session ID

1. Enter the FortiManager shell and launch python
   
.. code-block:: shell

		fmg # execute shell
		# python

2. Enter the following python excerpt

.. code-block:: python

		>>> python
		>>> import requests
		>>> url = "http://localhost/jsonrpc"
		>>> data = {
		... "id": 1,
		... "method": "get",
		... "params": [
		... {
		... "url": "/pm/config/device/FGTv2/vdom/root/system/dhcp/server"
		... }
		... ]
		... }
		{'id': 1, 'method': 'get', 'params': [{'url':
		'/pm/config/device/FGTv2/vdom/root/system/dhcp/server'}]}
		>>> r = requests.post(url, json=data)
		>>> r.json()

Using *ServiceProxy* python module
----------------------------------

Caught in #602275.

1. Enter the FortiManager shell and launch python
   
.. code-block:: shell

		fmg # execute shell
		# python

2. Enter the following python excerpt

.. code-block:: python

		>>> from jsonrpc.proxy import ServiceProxy
		>>> s=ServiceProxy("http://localhost/jsonrpc")
		>>> p={"url": "dvmdb/adom/INTERNET_FW", "data":{"flags":17821}}
		>>> ret=s.set(p)


.. note::

   It doesn't work anymore since FortiManager is using python 3.7.x
