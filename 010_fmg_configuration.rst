Operating the FortiManager's own configuration
==============================================

It is possible to operate the FortiManager CMDB configuration using |fmg_api|.

*CMDB* means all of the ``config something`` a FortiManager administrator could
perform via the FortiManager CLI.

The |fmg_api| url for this is:

.. code-block::
  
    /cli/global/{something}

where ``{something``} is:

- FortiManager CLI without the ``config`` keyword
- Spaces are replaced with slashes

For instance, when the FortiManager administrator wants to manage the list of
existing FortiManager administrators using the CLI, he will do something like:

.. code-block::
  
   config system admin user

Hence the corresponding |fmg_api| url will be:

.. code-block::
  
   /cli/global/system/admin/user

How to get the tablesize (maximum values) information?
------------------------------------------------------

Caught in #0380729.

This is to get the tablesize (or maximum values) for multiple components of FortiManager.

Following request will dump the tablesize for all components ADOM database:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/root/_data/tablesize"
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
                   "items": ["<truncated>"],
                   "name": "FortiGate",
                   "tag": "FOS"
                 },
                 {
                   "items": ["<truncated>"],
                   "name": "Sql-report",
                   "tag": "LOG"
                 },
                 {
                   "items": ["<truncated>"],
                   "name": "FortiManager",
                   "tag": "FMG"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/root/_data/tablesize"
             }
           ]
         }            

It seems possible to get more specific tablesize using URL similar to the following:

.. code-block:: text

   /pm/config/adom/root/_data/tablesize/fos
   /pm/config/adom/root/_data/tablesize/fos/firewall/policy
   /pm/config/adom/root/_data/tablesize/log/sql-report/output
   /pm/config/adom/root/_data/tablesize/fmg/system/aggregation-client
   /pm/config/adom/root/_data/tablesize/faz

For instance to get the tablesize for the firewall address in ADOM database:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/root/_data/tablesize/fos/firewall/address"
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
                   "items": [
                     {
                       "name": "firewall address",
                       "sz": {
                         "adom": 400000
                       }
                     }
                   ],
                   "name": "FortiGate",
                   "tag": "FOS"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/root/_data/tablesize/fos/firewall/address"
             }
           ]
         }

The maximum value for the firewall address table in ADOM database is 400K entries!         

How to get list of FortiManager Administrators?
-----------------------------------------------

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/cli/global/system/admin/user"
       }
     ],
     "session": "NH5ns7lDKQlJGvshlHWDv3QaKaraR+43+qwdaPlLq4E/iVlsCNevILyr1kpA78b3/WTj8zHk+lsO31OyXlrVNg==",
     "verbose": 1
   }
   
**RESPONSE:**

.. code-block::

   {
     "id": 3,
     "result": [
       {
         "data": [
           {
             "adom": [
               {
                 "adom-name": "knock_29735"
               },
               {
                 "adom-name": "knock_06999"
               }
             ],
             "adom-access": "specify",
             "app-filter": null,
             "avatar": "",
             "ca": "",
             "change-password": "enable",
             "dashboard": [
               {
                 "column": 1,
                 "diskio-content-type": "util",
                 "diskio-period": "1hour",
                 "log-rate-period": "2min",
                 "log-rate-topn": "5",
                 "log-rate-type": "device",
                 "moduleid": 1,
                 "name": "System Information",
                 "num-entries": 10,
                 "refresh-interval": 0,
                 "res-cpu-display": "average",
                 "res-period": "10min",
                 "res-view-type": "history",
                 "status": "open",
                 "tabid": 1,
                 "time-period": "1hour",
                 "widget-type": "sysinfo"
               },
               {
                 "column": 1,
                 "diskio-content-type": "util",
                 "diskio-period": "1hour",
                 "log-rate-period": "2min",
                 "log-rate-topn": "5",
                 "log-rate-type": "device",
                 "moduleid": 2,
                 "name": "System Resources",
                 "num-entries": 10,
                 "refresh-interval": 0,
                 "res-cpu-display": "average",
                 "res-period": "10min",
                 "res-view-type": "real-time",
                 "status": "open",
                 "tabid": 1,
                 "time-period": "1hour",
                 "widget-type": "sysres"
               },
               {
                 "column": 2,
                 "diskio-content-type": "util",
                 "diskio-period": "1hour",
                 "log-rate-period": "2min",
                 "log-rate-topn": "5",
                 "log-rate-type": "device",
                 "moduleid": 4,
                 "name": "Unit Operation",
                 "num-entries": 10,
                 "refresh-interval": 0,
                 "res-cpu-display": "average",
                 "res-period": "10min",
                 "res-view-type": "history",
                 "status": "open",
                 "tabid": 1,
                 "time-period": "1hour",
                 "widget-type": "sysop"
               },
               {
                 "column": 2,
                 "diskio-content-type": "util",
                 "diskio-period": "1hour",
                 "log-rate-period": "2min",
                 "log-rate-topn": "5",
                 "log-rate-type": "device",
                 "moduleid": 5,
                 "name": "Alert Message Console",
                 "num-entries": 0,
                 "refresh-interval": 0,
                 "res-cpu-display": "average",
                 "res-period": "10min",
                 "res-view-type": "history",
                 "status": "open",
                 "tabid": 1,
                 "time-period": "1hour",
                 "widget-type": "alert"
               },
               {
                 "column": 2,
                 "diskio-content-type": "util",
                 "diskio-period": "1hour",
                 "log-rate-period": "2min",
                 "log-rate-topn": "5",
                 "log-rate-type": "device",
                 "moduleid": 6,
                 "name": "License Information",
                 "num-entries": 10,
                 "refresh-interval": 0,
                 "res-cpu-display": "average",
                 "res-period": "10min",
                 "res-view-type": "history",
                 "status": "open",
                 "tabid": 1,
                 "time-period": "1hour",
                 "widget-type": "licinfo"
               },
               {
                 "column": 1,
                 "diskio-content-type": "util",
                 "diskio-period": "1hour",
                 "log-rate-period": "2min",
                 "log-rate-topn": "5",
                 "log-rate-type": "device",
                 "moduleid": 9,
                 "name": "CLI Console",
                 "num-entries": 10,
                 "refresh-interval": 0,
                 "res-cpu-display": "average",
                 "res-period": "10min",
                 "res-view-type": "history",
                 "status": "open",
                 "tabid": 1,
                 "time-period": "1hour",
                 "widget-type": "jsconsole"
               }
             ],
             "dashboard-tabs": null,
             "description": "",
             "dev-group": "",
             "email-address": "",
             "ext-auth-accprofile-override": "disable",
             "ext-auth-adom-override": "disable",
             "ext-auth-group-match": "",
             "first-name": "",
             "force-password-change": "disable",
             "group": "",
             "hidden": 0,
             "ips-filter": null,
             "ipv6_trusthost1": "::/0",
             "ipv6_trusthost10": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128",
             "ipv6_trusthost2": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128",
             "ipv6_trusthost3": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128",
             "ipv6_trusthost4": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128",
             "ipv6_trusthost5": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128",
             "ipv6_trusthost6": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128",
             "ipv6_trusthost7": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128",
             "ipv6_trusthost8": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128",
             "ipv6_trusthost9": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128",
             "last-name": "",
             "ldap-server": "",
             "login-max": 32,
             "meta-data": [
               {
                 "fieldlength": 50,
                 "fieldname": "Contact Email",
                 "fieldvalue": "",
                 "importance": "optional",
                 "status": "enabled"
               },
               {
                 "fieldlength": 50,
                 "fieldname": "Contact Phone",
                 "fieldvalue": "",
                 "importance": "optional",
                 "status": "enabled"
               }
             ],
             "mobile-number": "",
             "pager-number": "",
             "password": "ENC ",
             "password-expire": [
               "0000/00/00",
               "00:00:00"
             ],
             "phone-number": "",
             "policy-package": [
               {
                 "policy-package-name": "all_policy_packages"
               }
             ],
             "profileid": "Restricted_User",
             "radius_server": "",
             "rpc-permit": "none",
             "ssh-public-key1": [
               ""
             ],
             "ssh-public-key2": [
               ""
             ],
             "ssh-public-key3": [
               ""
             ],
             "subject": "",
             "tacacs-plus-server": "",
             "trusthost1": [
               "0.0.0.0",
               "0.0.0.0"
             ],
             "trusthost10": [
               "255.255.255.255",
               "255.255.255.255"
             ],
             "trusthost2": [
               "255.255.255.255",
               "255.255.255.255"
             ],
             "trusthost3": [
               "255.255.255.255",
               "255.255.255.255"
             ],
             "trusthost4": [
               "255.255.255.255",
               "255.255.255.255"
             ],
             "trusthost5": [
               "255.255.255.255",
               "255.255.255.255"
             ],
             "trusthost6": [
               "255.255.255.255",
               "255.255.255.255"
             ],
             "trusthost7": [
               "255.255.255.255",
               "255.255.255.255"
             ],
             "trusthost8": [
               "255.255.255.255",
               "255.255.255.255"
             ],
             "trusthost9": [
               "255.255.255.255",
               "255.255.255.255"
             ],
             "two-factor-auth": "disable",
             "use-global-theme": "enable",
             "user-theme": "blue",
             "user_type": "local",
             "userid": "admin1",
             "web-filter": null,
             "wildcard": "disable"
           },
   [...]
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/cli/global/system/admin/user"
       }
     ]
   }

How to import local certificates?
---------------------------------

To import a certificate with a password protected private key:

**REQUEST**: 

.. code-block:: json

   {
     "id": 1,
     "method": "add",
     "params": [
       {
         "data": {
           "certificate": "-----BEGIN CERTIFICATE-----\nMIID[...]KNs=\n-----END CERTIFICATE-----\n",
           "comment": "Created via FMG JSON RPC API",
           "name": "cert_001",
           "password": "fortinet",
           "private-key": "-----BEGIN ENCRYPTED PRIVATE KEY-----\nMII[...]Amo+g==\n-----END ENCRYPTED PRIVATE KEY-----\n"
         },
         "url": "/cli/global/system/certificate/local"
       }
     ],
     "session": "{{session}}"
   }

**RESPONSE**:

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "name": "cert_001"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/cli/global/system/certificate/local"
       }
     ]
   }

To import a certificate with a non-protected private key:   

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "method": "add",
     "params": [
       {
         "data": {
           "certificate": "-----BEGIN CERTIFICATE-----\nMIID[...]70A==\n-----END CERTIFICATE-----\n",
           "comment": "Created via FMG JSON RPC API",
           "name": "cert_002",
           "private-key": "-----BEGIN RSA PRIVATE KEY-----\nMII[...]Adg==\n-----END RSA PRIVATE KEY-----\n"
         },
         "url": "/cli/global/system/certificate/local"
       }
     ],
     "session": "{{session}}"
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "name": "cert_002"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/cli/global/system/certificate/local"
       }
     ]
   }