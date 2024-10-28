FMG JSON API Introduction
=========================

The |fmg_api| is based on the JSON RPC standard.

The same HTTP body structure will be used for all kind of requests (login,
provisioning, monitoring, operating, logout):

- HTTP method and URL will be of the form:

  .. code-block:: text

     POST https://<fmg_ip>/jsonrpc

- HTTP body will be using the JSON RPC standard format:

  .. code-block:: text

     {
       "id": <id>,
       "method": "<method, could be exec, add, set, delete, etc.>",
       "params": [<this is where all the stuff is done], 
       "session": <session_id>
     }

In the rest of this document, a request will be always represented with its
payload (i.e., the HTTP method and URL, since always the same, won't be
represented). 

For instance:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json
    
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": [
                 {
                   "passwd": "fortinet", 
                   "user": "admin"
                 }
               ], 
               "url": "sys/login/user"
             }
           ], 
           "session": null, 
         }
    
Login to FortiManager
---------------------

Session based authentication
++++++++++++++++++++++++++++

A login operation is required in order to get a session ID.

This session ID will then have to be used in all subsequent |fmg_api| requests.

To login, you can use any kind of FortiManager users: locally defined or defined
on some external LDAP, RADIUS, TACACS servers. 2FA is also supported (but won’t
be seen in this document).

The definition of a FortiManager user has to be slightly modified with the
``rpc-permit`` attribute in in order to be used as an |fmg_api| user:

.. code-block:: text

   config system admin user
       edit <user>
           set rpc-permit read-write
       next
   end


To API login a FortiManager, the |json_rpc_u| ``sys/login/user`` with
|json_rpc_m| ``exec`` can be used.

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1, 
           "method": "exec", 
           "params": [
             {
               "data": [
                 {
                   "passwd": "fortinet", 
                   "user": "admin"
                 }
               ], 
               "url": "sys/login/user"
             }
           ], 
           "session": null, 
           "verbose": 1
         }

      .. note::

         - You can omit the ``session`` attribute when login in to FortiManager
         - If you prefer to keep it, just set it with the ``null`` value

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
               "url": "sys/login/user"
             }
           ], 
           "session": "y5I9dOaJyotAoco6nY3VfUcgTwp7Alk7jib3tX5ECEv4WabzSllv9umEzfAFVJxI4azqZE9xEh3lEWLi1AOYbw=="
         }
      
From now on, the returned ``session`` value should be used in all subsequent
|fmg_api| requests.

Token-based authentication
++++++++++++++++++++++++++

Starting with FortiManager 7.2.2 (#0809732), it is now possible to use a pre-defined API key or token.

The API key (or token) is obtained by:

#. Defining an API user in FortiManager GUI or CLI

   As you can see below, an API user is a normal FortiManager user with the
   ``user_type`` attribute set to ``api``:

   .. code-block:: text

      config system admin user
          edit api_001
              set user_type api
              set rpc-permit read-write
          next
      end
   
   .. note::

      You still have to set the ``rpc-permit`` attribute if you want this user
      to be able to operate the FortiManager using the |fmg_api|.   

#. Generating the API key using the FortiManager GUI or CLI:

   Use the following FortiManager CLI command:

   .. code-block:: text

      execute api-user generate-key api_001

   It will return the API key:

   .. code-block:: text

      New API key: 33fzwipq4amujunzgzn46mg1to9p8wbi

The generated API key is **permanent** (i.e., never expires).

However, you can renew it whenever you want using the FortiManager GUI or CLI as
shown above.

You can now interact with the |fmg_api| without issuing an explicit login (or
logout) operation.

You just need to insert the API key:

- Using the ``Authorization`` HTTP header with the *bearer* form:

  .. code-block:: text

     POST https://{{fmg_ip}}/jsonrpc HTTP/1.1
     [...]
     Authorization: Bearer 33fzwipq4amujunzgzn46mg1to9p8wbi
     [...]

- Using the ``access_token`` URL query string:

  .. code-block::

     POST https://fmg_ip}}/jsonrpc?access_token=33fzwipq4amujunzgzn46mg1to9p8wbi
     [...]

FortiManager Cloud API authentication
+++++++++++++++++++++++++++++++++++++

Before starting reading this section, there are some pre-requisites:

- Make sure you have an *IAM API User* declared in the FortiCloud account *hosting* your FortiManager Cloud instance

  - See :bdg-link-primary-line:`here <https://docs.fortinet.com/document/forticloud/24.1.0/identity-access-management-iam/282341/adding-an-api-user>`

- Make sure you know the URL of your FortiManager Cloud instance

  - You can easily obtain it when you're connected to it via your browser.
  
  - Just take the URL visible in your browser, it should be something like:

    .. code-block:: text
  
       https://{account_id}.{region}.fortimanager.forticloud.com

    For instance:

    .. code-block:: text

       https://123456.eu-central-1.fortimanager.forticloud.com

To API authenticate your FortiManager Cloud instance, you need to follow this 
multi steps process:

.. _Get a FortiCloud Token:

#. Get a FortiCloud Token

   - This step is documented :bdg-link-primary-line:`here <https://docs.fortinet.com/document/fortiauthenticator/6.1.2/rest-api-solution-guide/498666/oauth-server-token-oauth-token>`

   - You will need to build the following JSON payload:

     .. code-block:: json

        {
          "username": "{IAM API user's apiId}",
          "password": "{IAM API user's password}",
          "client_id": "FortiManager",
          "grant_type": "password"
        }

   - Based on the above example, create a ``forticloud_token.json`` file using 
     the information from your IAM API user:

     .. code-block:: json

        {
          "username": "E8766032-7309-409F-902A-REDACTEDD045",
          "password": "a6455940eefREDACTED4a458dddcb2c2!1Aa",
          "client_id": "FortiManager",
          "grant_type": "password"
        }

   - To get the FortiCloud Token using the ``curl`` command:

     .. code-block:: shell

        curl -s -k -X POST -H "Content-Type: application/json" \
          https://customerapiauth.fortinet.com/api/v1/oauth/token/ \
          -d @forticloud_token.json | jq

     .. note::

        - The ``jq`` command will produce a pretty JSON output

     You should obtain the following output:

     .. code-block:: json

        {
            "access_token": "srgkxUG9SqqREDACTEDK5qG27tqktk",
            "expires_in": 3600,
            "message": "successfully authenticated",
            "refresh_token": "jie6v6qV62REDACTEDwmL6GEcmZgst",
            "scope": "read write",
            "status": "success",
            "token_type": "Bearer"
        }

   - Your FortiCloud Token is the value in the ``access_token`` attribute

.. _Obtain a FortiManager API session ID:

#. Obtain a FortiManager API session ID

   - Like with an on-prem FortiManager instance, you need to obtain a 
     FortiManager API session ID. 
     
   - You will follow a slightly modifed Session-based authentication (see 
     :ref:`Session based authentication`) process described in next step

     .. note::

        FortiManager Cloud doesn't support Token-based authentication (see 
        :ref:`Token-based authentication`)
    
   - The FortiManager Cloud API base URL to be used is also slightly different 
     than with a normal FortiManager instance. It has the following form:

     .. code-block:: text
      
        https://{account_id}.{region}.fortimanager.forticloud.com/p/forticloud_jsonrpc_login/

     For instance:

     .. code-block:: text
      
        https://123456.eu-central-1.fortimanager.forticloud.com/p/forticloud_jsonrpc_login/

   - The JSON payload to be used is also different than the usual JSON RPC one 
     used when login in a normal FortiManager instance:

     - It has the following format:

       .. code-block:: json

          {
            "access_token": "{access_token}"
          }

       where ``access_token`` is the FortiCloud Token obtained in previous step 
       `Get a FortiCloud Token`_

   - Create the `fmg_cloud_login.json` JSON file with following content:

     .. code-block:: json

        {
          "access_token": "srgkxUG9SqqREDACTEDK5qG27tqktk"
        }

   - You can now obtain your FortiManager API session ID using the following 
     ``curl`` command

     .. code-block:: shell
      
        curl -s -k -X POST -H "Content-Type: application/json" \
          https://123456.eu-central-1.fortimanager.forticloud.com/p/forticloud_jsonrpc_login/ \
          -d @fmg_cloud_login.json --https1.1 | jq

     .. note::

        - Why using ``--https1.1``? Because of #0893680.
        - The ``jq`` command will produce a pretty JSON output

     You should obtain the following output:

     .. code-block:: json

        {
          "session": "/cl0oZgKn3trxIIkRJEqV09+0pqk8TwfOVz2x9wB0Vjk5Bgs+ADpIo1aREDACTEDF23qAjP+LaZg6iM19ia85w=="
        }

#. API the FortiManager Cloud!
 
   - You can now API the FortiManager Cloud using the normal base URL and JSON 
     payload

   - The base URL form is like:

     .. code-block:: text

        https://{account_id}.{region}.fortimanager.forticloud.com/jsonrpc

     For instance:

     .. code-block:: text

        https://123456.eu-central-1.fortimanager.forticloud.com/jsonrpc      


   - The JSON payload is the normal JSON RPC payload

     .. code-block:: json

        {
            "id": 3,
            "method": "get",
            "params": [
              {
                "url": "/cli/global/system/status"
              }
            ],
            "session": "{{session}}"
        }

     where ``session`` is the FortiManager API session ID obtained in        
     `Obtain a FortiManager API session ID`_

     For instance:

     .. code-block:: json

        {
            "id": 3,
            "method": "get",
            "params": [
              {
                "url": "/cli/global/system/status"
              }
            ],
            "session": "/cl0oZgKn3trxIIkRJEqV09+0pqk8TwfOVz2x9wB0Vjk5Bgs+ADpIo1aREDACTEDF23qAjP+LaZg6iM19ia85w=="
        }

Logout from FortiManager
------------------------

.. warning:: 
  
   This is only applicable if a login operation using the session-based 
   authentication was used (see :ref:`Session based authentication`).

To API logout from a FortiManager, |json_rpc_u| ``sys/logout`` with |json_rpc_m|
``exec`` can be used.

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1, 
           "jsonrpc": "1.0", 
           "method": "exec", 
           "params": [
             {
               "url": "sys/logout"
             }
           ], 
           "session": "y5I9dOaJyotAoco6nY3VfUcgTwp7Alk7jib3tX5ECEv4WabzSllv9umEzfAFVJxI4azqZE9xEh3lEWLi1AOYbw==", 
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
               "url": "sys/logout"
             }
           ]
         }
      
Managing Device Settings
------------------------

To manage Network & System settings for managed devices - all the operations
performed under the Device Manager module of FortiManager - the |fmg_api| is
using one of the following JSON RPC url: 

For global scope settings (i.e. ``config global``)

.. code-block:: text
  
   /pm/config/device/<device>/global/<cli>

For VDOM scope settings (i.e. ``config vdom``):

.. code-block:: text

   /pm/config/device/<device>/vdom/<vdom>/<cli>

Global scope settings
+++++++++++++++++++++

The first form (global sco[e settings) applies when you need to configure global
settings like DNS, SNMP, etc.

In that case ``<device>`` refers to the device name as displayed in Device
Manager under column Device Name. 

``<cli>`` refers to the FortiGate CLI without the ``config`` keyword and where
spaces are replaced by ``/``.

For instance, to configure the DNS settings (i.e. ``config system dns``) of
managed device ``FGT1`` the FMG JSON RPC url will be:  

.. code-block:: text
  
   /pm/config/device/FGT1/global/system/dns

We have to use that form even if the managed device isn't having the VDOM status
turned on.

.. warning::

   Even though interfaces (i.e. ``config system interface``) are assigned to
   VDOMa, it is required to use the global scope settings form to operate them. 
   
   For instance, to configure interface ``port1`` (i.e. ``config system
   interface`` + ``edit port1``) for managed device ``FGT1``, the FMG JSON RPC
   url will be:

   .. code-block:: text

      /pm/config/device/FGT1/global/system/interface/port1

VDOM scope settings
+++++++++++++++++++

The second form (VDOM scope settings) has to be used when you need to configure
per-VDOM settings like VPN Phase1/Phase2, Static or Dynamic Routing, etc. 

In that case ``<device>`` refers to the device name as displayed in Device
Manager under column Device Name. 

``<vdom>`` refers to the VDOM name. 

``<cli>`` refers to the FortiGate CLI without the ``config`` keyword and where
spaces are replaced by ``/``.

For instance, to manage static routes (i.e. ``config router static``) for device
``FGT1`` and its VDOM ``vd1``, the FMG JSON RPC url will be:

.. code-block:: text

   /pm/config/device/FGT1/vdom/vd1/router/static

Installing Device Settings
--------------------------

FortiManager allows to install pending network and system settings changes only!

It means that no pending security settings changes (like new/edited objects or
policies) will be pushed down to managed devices during the Install Device
Settings operation.

The main JSON RPC url will be:

.. code-block:: text
  
   /securityconsole/install/device

The JSON RPC method will be ``exec`` (i.e. execute)

Here is an example to install pending network & system settings changes for
device ``FG600C-194-77``, with no VDOM (i.e. default ``root`` VDOM), from ADOM
``FOOBAR``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1, 
     "method": "exec", 
     "params": [
       {
         "data": {
           "adom": "FOOBAR", 
           "dev_rev_comments": "A comment", 
           "flags": [
             "none"
           ], 
           "scope": [
             {
               "name": "FG600C-194-77", 
               "vdom": "root"
             }
           ]
         }, 
         "url": "/securityconsole/install/device"
       }
     ], 
     "session": "cEeh7eax9AbTauJpEAtapIogYlWT5IQazR1vGvw7QAKsmUy3E7ZJ4FQINA1GMSatBQTOpFZ1fceuH7UqLRYfzMJwUYo9T5/F", 
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json
  
   {
     "id": 1, 
     "result": [
       {
         "data": {
           "task": 2066
         }, 
         "status": {
           "code": 0, 
           "message": "OK"
         }, 
         "url": "/securityconsole/install/device"
       }
     ]
   }

The response contains a task ID (here it is ``2066``).

It is required to monitor the install progress and final status.

See section `Monitoring a task`_.

Managing Security Settings
--------------------------

To manage Security objects for managed devices - all the operations performed
under the Policy & Objects module of FortiManager - the |fmg_api| is using the
following JSON RPC url: 

For objects:

.. code-block:: text
  
  /pm/config/adom/<adom>/obj/<cli>

where ``<adom>`` refers to the ADOM name. 

``<cli>`` refers to the FortiGate CLI without the ``config`` keyword and where
spaces are replaced by ``/``.

For instance, to manage Firewall Address (i.e. ``config firewall address``)
objects in ADOM ``ADOM1`` the JSON RPC url will be:

.. code-block:: text
  
   /pm/config/adom/ADOM1/obj/firewall/address

For policy packages:

.. code-block:: text

   /pm/config/adom/<adom>/pkg/<pkg>/firewall/policy

where ``<adom>`` refers to the ADOM name.

``<pkg>`` refers to the policy package name. 

For instance, to manage policy ID ``11`` (i.e. ``config firewall policy`` +
``edit 11``) from policy package ``PP_001`` in ADOM ``ADOM1``, the JSON RPC url
will be:

.. code-block:: text

   /pm/config/adom/ADOM1/pkg/PP_001/firewall/policy/11

Installing Security Settings
----------------------------

When triggering a policy package installation, FortiManager is installing both:

- Pending device settings (network and system settings changes) (see `Managing
  Device Settings`_ above)

- Pending security settings (objects and policy packages changes) (see `Managing
  Security Settings`_ above)
  
The JSON RPC url will be:

.. code-block:: text

   /securityconsole/install/package

with JSON RPC method being ``exec`` (i.e. execute).

For instance, to install policy package ``PP_FG600C-194-77`` from ADOM
``FOOBAR``, on managed device ``FG600C-194-77`` with no VDOM (i.e. default
``root`` VDOM):

**REQUEST:**

.. code-block:: json

   {
     "id": 1, 
     "method": "exec", 
     "params": [
       {
         "data": {
           "adom": "CARWASH", 
           "flags": [
             "none"
           ], 
           "pkg": "PP_FG600C-194-77", 
           "scope": [
             {
               "name": "FG600C-194-77", 
               "vdom": "root"
             }
           ]
         }, 
         "url": "/securityconsole/install/package"
       }
     ], 
     "session": "hJdopAeMzkgdJ6uQbfIgz48Eq+aXy8B/IvkNnrUuBbT1ni6eQ8GbrZPlUv6enG1pAXVqwS4tWmkaC13jAa0RnJBxW4xcC6xi", 
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1, 
     "result": [
       {
         "data": {
           "task": 2071
         }, 
         "status": {
           "code": 0, 
           "message": "OK"
         }, 
         "url": "/securityconsole/install/package"
       }
     ]
   }

The response contains a task ID (here it is ``2071``).

It is required to monitor the install progress and final status.

See section `Monitoring a task`_.

Monitoring a task
-----------------

For API calls wich could require time, FortiManager prefers to immediately
return with a task ID.

This task ID can then be used to monitor the progress of the operation and also
to get its final status.

The JSON RPC url will be: 

.. code-block:: text

   /task/task/<id>

To monitor a task, the JSON RPC method ``get`` can be used.

For instance to monitor task ID ``2066``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1, 
     "method": "get", 
     "params": [
       {
         "url": "/task/task/2066"
       }
     ], 
     "session": "lfNHxnG2uuGLwjaGiLFPvNSpeKD/0rc4bH0yiGnWK3VGpOPpAmmBY7hib9q3Wig7HGwL/hUMWdRTRYEBY4soYMHpz8ENRiMG", 
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1, 
     "result": [
       {
         "data": {
           "adom": 364, 
           "end_tm": 1515752051, 
           "flags": 0, 
           "history": [
             {
               "detail": "2018-01-12 02:13:44:start to install dev(FG600C-194-77)", 
               "name": "FG600C-194-77", 
               "percent": 0, 
               "vdom": null
             }, 
             {
               "detail": "2018-01-12 02:13:46:init state: start to get pre-checksum", 
               "name": "FG600C-194-77", 
               "percent": 15, 
               "vdom": null
             }, 
             {
               "detail": "2018-01-12 02:13:53:get pre-checksum state: start get diff(chkout=1)", 
               "name": "FG600C-194-77", 
               "percent": 25, 
               "vdom": null
             }, 
             {
               "detail": "2018-01-12 02:13:53:script done state: start to FGFM install", 
               "name": "FG600C-194-77", 
               "percent": 35, 
               "vdom": null
             }, 
             {
               "detail": "2018-01-12 02:13:55:fgfm install state: prepare to post-checksum", 
               "name": "FG600C-194-77", 
               "percent": 80, 
               "vdom": null
             }, 
             {
               "detail": "2018-01-12 02:14:01:post-checksum state: start verification", 
               "name": "FG600C-194-77", 
               "percent": 90, 
               "vdom": null
             }, 
             {
               "detail": "2018-01-12 02:14:06:install and save finished status=OK", 
               "name": "FG600C-194-77", 
               "percent": 100, 
               "vdom": null
             }, 
             {
               "detail": "2018-01-12 02:13:46:Start copying shared objs to devdb, device(FG600C-194-77), vdomid(root)", 
               "name": "FG600C-194-77(root)[copy]", 
               "percent": 1, 
               "vdom": "root"
             }, 
             {
               "detail": "2018-01-12 02:13:46:Initiate request to install to real device", 
               "name": "FG600C-194-77(root)[copy]", 
               "percent": 80, 
               "vdom": "root"
             }, 
             {
               "detail": "2018-01-12 02:13:46:Copy to device done", 
               "name": "FG600C-194-77(root)[copy]", 
               "percent": 90, 
               "vdom": "root"
             }, 
             {
               "detail": "2018-01-12 02:14:11:Installation to real device done", 
               "name": "FG600C-194-77(root)[copy]", 
               "percent": 100, 
               "vdom": "root"
             }
           ], 
           "id": 2066, 
           "line": [
             {
               "detail": "install and save finished status=OK", 
               "err": 0, 
               "ip": null, 
               "name": "FG600C-194-77", 
               "oid": 366, 
               "percent": 100, 
               "state": "done", 
               "vdom": null
             }, 
             {
               "detail": "Installation to real device done", 
               "err": 0, 
               "ip": "192.168.194.77", 
               "name": "FG600C-194-77(root)[copy]", 
               "oid": 366, 
               "percent": 100, 
               "state": "done", 
               "vdom": "root"
             }
           ], 
           "num_done": 2, 
           "num_err": 0, 
           "num_lines": 2, 
           "num_warn": 0, 
           "percent": 100, 
           "pid": 26153, 
           "src": "install device", 
           "start_tm": 1515752024, 
           "state": "done", 
           "title": "Install Device", 
           "tot_percent": 200, 
           "user": "admin"
         }, 
         "status": {
           "code": 0, 
           "message": "OK"
         }, 
         "url": "/task/task/2066"
       }
     ]
   }

FortiManager is returning the whole history (or part of it if in the middle of
the operation) and most importantly some global attributes that allow to figure
out whether the task did succeed or not: 
   
- ``num_lines``: The number of sub tasks; a task could be composed of multiple
  sub tasks. Here it is 2 meaning the Install Device Settings operation is
  generating two sub tasks 
- ``tot_percent``: The progress of all the sub tasks. Here it is 200 because we
  have two sub tasks (2 x 100) 
- ``num_err``: The number of failed sub tasks. Here it is 0 meaning that the
  Install Device Settings task did succeed
- ``num_warn``: The number of sub tasks completed with warning 
- ``percent``: The global task progress

To monitor a task, it is required to get the task ID multiple times; preferably
using a loop.

The loop could stop when ``percent`` is equal to 100.

The task is successful when ``num_err`` is equal to 0. 

Multiplexing requests
---------------------

This is the art of regoupring multiple API operations in a single request.

The ``params`` attribute of the JSON RPC payload is a list.

It is possible to pass multiple elements in this list as shown in the next
sessions.

Same JSON RPC URL
+++++++++++++++++

Seen in #0767076.

You can use the following request to get the webfilter profiles of multiple
ADOMs:

.. tab-set:: 
  
   .. tab-item:: REQUEST

     .. code-block:: json
     
        {
          "id": 1,
          "method": "get",
          "params": [
            {
              "url": "pm/config/adom/adom_001/obj/webfilter/profile",
              "fields": [
                "name"
              ],
              "loadsub": 0
            },
            {
              "url": "pm/config/adom/adom_002/obj/webfilter/profile",
              "fields": [
                "name"
              ],
              "loadsub": 0
            },
            {
              "url": "pm/config/adom/adom_003/obj/webfilter/profile",
              "fields": [
                "name"
              ],
              "loadsub": 0
            }
          ],
          "session": "{{session_id}}"
        }
     
Different JSON RPC URL
++++++++++++++++++++++

To get the list of managed devices and FortiGate ADOMs:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "fields": [
           "name"
         ],
         "loadsub": 0,
         "url": "/dvmdb/device"
       },
       {
         "fields": [
           "name"
         ],
         "filter": [
           "restricted_prds",
           "==",
           "fos"
         ],
         "loadsub": 0,
         "url": "/dvmdb/adom"
       }
     ],
     "session": "tCnuMMWQhq0rT4oEROMN5I5v5U+k3Ody1wBvcSHOZ9iyOJRbTlwIlRzTngW7CfLnmZ6Gtd2KpUw6YRqtFeuFwQ=="
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": [
           {
             "name": "fgt_dc1",
             "oid": 164
           },
           {
             "name": "fgt_dc2",
             "oid": 227
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/device"
       },
       {
         "data": [
           {
             "name": "adom_dc1",
             "oid": 160
           },
           {
             "name": "adom_dc2",
             "oid": 162
           },
           {
             "name": "root",
             "oid": 3
           },
           {
             "name": "rootp",
             "oid": 10
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom"
       }
     ]
   }

Monitoring different elements in different ADOMs
++++++++++++++++++++++++++++++++++++++++++++++++

To get the firewall policy statistics for all managed devices belonging to ADOM
``dc_emea`` along with all available interfaces for all managed managed devices
belonging to ADOM ``dc_amer``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "method": "exec",
     "params": [
       {
         "data": {
           "action": "get",
           "resource": "/api/v2/monitor/firewall/policy",
           "target": [
             "/adom/dc_emea/group/All_FortiGate"
           ]
         },
         "url": "/sys/proxy/json"
       },
       {
         "data": {
           "action": "get",
           "resource": "/api/v2/monitor/system/available-interfaces?format=name|ipv4_addresses",
           "target": [
             "/adom/dc_amer/group/All_FortiGate"
           ]
         },
         "url": "/sys/proxy/json"
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
         "data": [
           {
             "response": {
               "action": "",
               "build": 1255,
               "http_method": "GET",
               "name": "policy",
               "path": "firewall",
               "results": [
                 {
                   "active_sessions": 0,
                   "asic_bytes": 0,
                   "asic_packets": 0,
                   "bytes": 0,
                   "packets": 0,
                   "policyid": 0,
                   "software_bytes": 0,
                   "software_packets": 0
                 }
               ],
               "serial": "FGVMMLTM23000162",
               "status": "success",
               "vdom": "root",
               "version": "v7.2.2"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "dut_fgt_03"
           },
           {
             "response": {
               "action": "",
               "build": 234,
               "http_method": "GET",
               "name": "policy",
               "path": "firewall",
               "results": [
                 {
                   "1_week_ipv4": {
                     "bytes": [
                       9073,
                       246710,
                       117978,
                       0,
                       0,
                       0,
                       0,
                       0
                     ],
                     "hit_count": [
                       82,
                       2281,
                       1092,
                       0,
                       0,
                       0,
                       0,
                       0
                     ],
                     "packets": [
                       83,
                       2281,
                       1092,
                       0,
                       0,
                       0,
                       0,
                       0
                     ]
                   },
                   "active_sessions": 0,
                   "bytes": 374481,
                   "first_used": 1673472304,
                   "hit_count": 3465,
                   "last_used": 1674124082,
                   "packets": 3466,
                   "policyid": 0
                 },
                 {
                   "active_sessions": 0,
                   "bytes": 0,
                   "packets": 0,
                   "policyid": 1,
                   "uuid": "d5da7da8-81ef-51ed-613b-60e3503a06a1"
                 },
                 {
                   "active_sessions": 0,
                   "bytes": 0,
                   "packets": 0,
                   "policyid": 2,
                   "uuid": "b2cfeacc-90f5-51ed-12ba-ca7a5af8e4a7"
                 }
               ],
               "serial": "FGVMMLTM22006608",
               "status": "success",
               "vdom": "root",
               "version": "v7.0.2"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "dut_fgt_01"
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/sys/proxy/json"
       },
       {
         "data": [
           {
             "response": {
               "action": "",
               "build": 1255,
               "http_method": "GET",
               "name": "available-interfaces",
               "path": "system",
               "results": [
                 {
                   "name": "any"
                 },
                 {
                   "ipv4_addresses": [
                     {
                       "cidr_netmask": 23,
                       "ip": "10.210.35.104",
                       "netmask": "255.255.254.0"
                     }
                   ],
                   "name": "port1"
                 },
                 {
                   "ipv4_addresses": [
                     {
                       "cidr_netmask": 24,
                       "ip": "10.2.0.1",
                       "netmask": "255.255.255.0"
                     }
                   ],
                   "name": "port2"
                 },
                 {
                   "name": "port3"
                 },
                 {
                   "name": "port4"
                 },
                 {
                   "name": "naf.root"
                 },
                 {
                   "name": "l2t.root"
                 },
                 {
                   "name": "ssl.root"
                 },
                 {
                   "ipv4_addresses": [
                     {
                       "cidr_netmask": 24,
                       "ip": "10.255.1.1",
                       "netmask": "255.255.255.0"
                     }
                   ],
                   "name": "fortilink"
                 },
                 {
                   "name": "virtual-wan-link"
                 }
               ],
               "revision": "1674589859.651219",
               "serial": "FGVMMLTM23000178",
               "status": "success",
               "vdom": "root",
               "version": "v7.2.2"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "dut_fgt_04"
           },
           {
             "response": {
               "action": "",
               "build": 1390,
               "http_method": "GET",
               "name": "available-interfaces",
               "path": "system",
               "results": [
                 {
                   "name": "any"
                 },
                 {
                   "ipv4_addresses": [
                     {
                       "cidr_netmask": 23,
                       "ip": "10.210.35.105",
                       "netmask": "255.255.254.0"
                     }
                   ],
                   "name": "port1"
                 },
                 {
                   "ipv4_addresses": [
                     {
                       "cidr_netmask": 27,
                       "ip": "172.18.0.30",
                       "netmask": "255.255.255.224"
                     }
                   ],
                   "name": "port2"
                 },
                 {
                   "ipv4_addresses": [
                     {
                       "cidr_netmask": 24,
                       "ip": "10.3.0.1",
                       "netmask": "255.255.255.0"
                     }
                   ],
                   "name": "port3"
                 },
                 {
                   "name": "port4"
                 },
                 {
                   "name": "naf.root"
                 },
                 {
                   "name": "l2t.root"
                 },
                 {
                   "name": "ssl.root"
                 },
                 {
                   "ipv4_addresses": [
                     {
                       "cidr_netmask": 24,
                       "ip": "10.255.1.1",
                       "netmask": "255.255.255.0"
                     }
                   ],
                   "name": "fortilink"
                 },
                 {
                   "ipv4_addresses": [
                     {
                       "cidr_netmask": 32,
                       "ip": "172.16.255.253",
                       "netmask": "255.255.255.255"
                     }
                   ],
                   "name": "HUB1-Lo"
                 },
                 {
                   "name": "virtual-wan-link"
                 }
               ],
               "revision": "1674589859.655205",
               "serial": "FGVMMLTM22002644",
               "status": "success",
               "vdom": "root",
               "version": "v7.2.4"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "dut_fgt_05"
           },
           {
             "response": {
               "action": "",
               "build": 1390,
               "http_method": "GET",
               "name": "available-interfaces",
               "path": "system",
               "results": [
                 {
                   "name": "any"
                 },
                 {
                   "ipv4_addresses": [
                     {
                       "cidr_netmask": 23,
                       "ip": "10.210.35.102",
                       "netmask": "255.255.254.0"
                     }
                   ],
                   "name": "port1"
                 },
                 {
                   "name": "naf.root"
                 },
                 {
                   "name": "l2t.root"
                 },
                 {
                   "name": "ssl.root"
                 },
                 {
                   "ipv4_addresses": [
                     {
                       "cidr_netmask": 24,
                       "ip": "10.255.1.1",
                       "netmask": "255.255.255.0"
                     }
                   ],
                   "name": "fortilink"
                 },
                 {
                   "name": "virtual-wan-link"
                 }
               ],
               "revision": "1674589859.656882",
               "serial": "FGVMMLTM22006609",
               "status": "success",
               "vdom": "root",
               "version": "v7.2.4"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "dut_fgt_02"
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
   
Working with symbolic (human readable) values
---------------------------------------------
   
FortiManager JSON API can work with both numerical and symbolic or (human
readable) values. 
   
For instance, to create a host firewall address we can specify the type in two
ways: 
   
- Numerical:
   
  .. code-block::
   
     "type": 0

- Symbolic:

  .. code-block:: 
          
     "type": "ipmask"

The symbolic form is obviously more intuitive and when used, it produces more
readable and easier to understand code. 

It works for any provisioning operations made with the FortiManager JSON API
(``method``: ``add``, ``update``, ``set``, etc.). 

However, when retrieving (i.e., ``method`` is ``get``) objects, FortiManager
returns by default a JSON output with numerical values. 

With the ``verbose`` attribute set, you can instruct FortiManager to return
objects using the symbolic way. 

The ``verbose`` attribute can be placed in the JSON RPC request as shown below: 

.. code-block::

   {
     "id": 1,
     "verbose": 1,
     "method": "get",
     "params": [ ... ],
     "session": "..."
   }

Operations on tables, objects and attributes
--------------------------------------------

This section is to explain some important mechanism related to tables, their objects, and their attributes.

How to unset a specific attribute?
++++++++++++++++++++++++++++++++++

The capability to unset a specific attribute was added in FMG 5.4.1 (#0365372).

To unset the IP address the ``dmz`` interface from managed device ``TEST-FGT``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1, 
     "method": "set", 
     "params": [
       {
         "data": {
           "name": "dmz", 
           "unset attrs": [
             "ip"
           ]
         }, 
         "url": "pm/config/device/TEST-FGT/global/system/interface"
       }
     ], 
     "session": "w4KqkMrExJNUibihOZakWE/0j8VCeKGP1MbeG3Pne6ac5m5FBSJuBd20uuocfPHUZJGzYA/N10ZPTjWmPbJ9AA==", 
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
         "url": "pm/config/device/TEST-FGT/global/system/interface"
       }
     ]
   }

Sometimes, it seems just enough to *unset* an attribute by ommiting it when
doing the ``set`` (captured in #891341).

In following example, to unset the ``secondary`` attribute of a System Template,
you just need to set the System Template without mentioning the attribute:

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json

         {
           "session": "{{sess_id}}",
           "method": "set",
           "params": [
             {
               "data": {
                 "seq": 1,
                 "value": {
                   "alt-primary": "0.0.0.0",
                   "alt-secondary": "0.0.0.0",
                   "cache-notfound-responses": 0,
                   "dns-cache-limit": 5000,
                   "dns-cache-ttl": 1800,
                   "domain": null,
                   "interface": null,
                   "interface-select-method": 0,
                   "ip6-primary": "::",
                   "ip6-secondary": "::",
                   "log": 0,
                   "primary": "192.168.199.230",
                   "protocol": 1,
                   "retry": 2,
                   "server-hostname": null,
                   "server-select-method": 1,
                   "source-ip": "0.0.0.0",
                   "ssl-certificate": "Fortinet_Factory",
                   "timeout": 5
                 },
               },
               "url": "pm/config/adom/SF70/devprof/system_branch_default_78/device/template/widget/dns/action-list"
             }
           ]
         }

Permissions
-----------

Using a normal FortiManager administrator
+++++++++++++++++++++++++++++++++++++++++

A ``normal`` administrator is a user with attribute
``system.admin.user.user_type`` different than ``api``, ``sso`` or ``group``.

On the FortiManager side, you have to define an API user and assign it at least
two things:

- A permission profile,
- A ``system.admin.user.rpc-permit`` value.

When ``rpc-permit`` is ``none``, the API user can simply not log in to
FortiManager:

**REQUEST:**

.. code-block:: json

   {
       "id": 1,
       "method": "exec",
       "params": [
           {
               "data": {
                   "user": "devops",
                   "passwd": "fortinet"
                },
               "url": "/sys/login/user"
           }
       ],
       "session": null
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "status": {
           "code": -11,
           "message": "No permission for the resource"
         },
         "url": "/sys/login/user"
       }
     ]
   }

When ``rpc-permit`` is ``read``, the API user cannot read-write anything, even
if associated permission profile allows read-write permission:

For instance, the API user associated with permission profile ``Super_User`` but
with ``rpc-permit`` set to ``read`` can't create a new firewall address:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": {
           "name": "host_1001",
           "subnet": "10.0.0.2/32"
         },
         "url": "/pm/config/adom/dc_amer/obj/firewall/address"
       }
     ],
     "session": "nMMf3m/6Pp28Azuhx/3PT/JinJT74r8zHNZ/a7BV9vKoklrpB4ca66y7uR20KDi31acSTKOSFf4bH1COB6mKDA=="
   }

**RESPONSE:**

.. code-block:: json
  
   {
     "id": 3,
     "result": [
       {
         "status": {
           "code": -11,
           "message": "No permission for the resource"
         },
         "url": "/pm/config/adom/dc_amer/obj/firewall/address"
       }
     ],
     "session": 13807
   }

It is also applicable if the API user attempts to add a firewall object directly
in the managed device using the ``sys/proxy/json``:

**REQUEST:**

.. code-block:: json
  
   {
     "id": 3,
     "method": "exec",
     "params": [
       {
         "data": {
           "action": "post",
           "payload": {
             "color": 13,
             "name": "host_1006",
             "subnet": "10.0.0.6/32"
           },
           "resource": "/api/v2/cmdb/firewall/address",
           "target": [
             "/adom/dc_amer/device/dut_fgt_03"
           ]
         },
         "url": "/sys/proxy/json"
       }
     ],
     "session": "TJSY8zbQOyMSVsZxIU4xL5Tj3es06do42OVDi2MVmattWPhxpDhpVIy4C0VbvNwt02Z+SOErU1Nb/2geB18jHg=="
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "status": {
           "code": -11,
           "message": "No permission for the resource"
         },
         "url": "/sys/proxy/json"
       }
     ]
   }

(Benefit of #0601553)   

Of course, such user can get (read) object:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "fields": [
           "name",
           "subnet"
         ],
         "loadsub": 0,
         "url": "/pm/config/adom/dc_amer/obj/firewall/address/host_001"
       }
     ],
     "session": "E3tjmsND1L4zCe5qNw3V6xJAynVK1PYeZ3f1fNPI0Q/rLez1t9qMpSkUNkkScbjrJOPvDKHPUaNf3c7YQNvZig=="
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": {
           "name": "host_001",
           "oid": 4805,
           "subnet": [
             "21.103.33.206",
             "255.255.255.255"
           ]
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/dc_amer/obj/firewall/address/host_001"
       }
     ]
   }

When ``rpc-permit`` is ``read-write``, the API user can read-write what the
permission profile is allowing him to read-write.

For instance, the API user associated with permission profile ``rw_all`` but
only for ADOM ``dc_amer`` can't create a firewall address in ADOM ``dc_us``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": {
           "name": "host_1001",
           "subnet": "10.0.0.2/32"
         },
         "url": "/pm/config/adom/dc_us/obj/firewall/address"
       }
     ],
     "session": "+sdy+ca8+NbZhTXxhjZOgByoZJiqCMhzEwo+9ufQ40z2zTjK/sLhFhxt1+atozzGwJ8wPHGBx50smv5hkekYgg=="
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "status": {
           "code": -11,
           "message": "No permission for the resource"
         },
         "url": "/pm/config/adom/dc_us/obj/firewall/address"
       }
     ],
     "session": 21
   }

When ``rpc-permit`` is ``read-write``, and the user is also assigned with a
device group, then the API user can't read-write a device which doesn't belong
to the device group: BUG!!!! (tested with FMG 7.2.3-INTERIM build 1360)

In below example, device ``dut_fgt_03`` doesn't belong to the device group
assigned to the API user...

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": {
           "name": "host_1001",
           "subnet": "10.0.0.2/32"
         },
         "url": "/pm/config/device/dut_fgt_03/vdom/root/firewall/address"
       }
     ],
     "session": "RiMtKVLNZH/zc5nVkZ/Y4XNFXAWCvCBnOXEySrUCNUrsdNJQpDqUrFa+5yYF7e2K1uRFq146GAQ8BKxIoLMvNQ=="
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": {
           "name": "host_1001"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/device/dut_fgt_03/vdom/root/firewall/address"
       }
     ]
   }

Neither if he attempts to read-write directly a managed device which doesn't
belong to the assigned device group, using ``sys/proxy/json``: BUG!!!! (tested
with FMG 7.2.3-INTERIM build 1360)

In below example, device ``dut_fgt_03`` doesn't belong to the device group
assigned to the API user...

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "exec",
     "params": [
       {
         "data": {
           "action": "post",
           "payload": {
             "color": 13,
             "name": "host_1007",
             "subnet": "10.0.0.7/32"
           },
           "resource": "/api/v2/cmdb/firewall/address",
           "target": [
             "/adom/dc_amer/device/dut_fgt_03"
           ]
         },
         "url": "/sys/proxy/json"
       }
     ],
     "session": "kOB0O/NuH7JPaTGVKsXCn5jWf8qkfAreEMFx2tElofuDioiKOfL42GJNMVBieEs1eTNe+0ehQY4sEkT4/gZJSQ=="
   }

**RESPONSE:**

.. code-block:: json

   {  
     "id": 3,
     "result": [
       {
         "data": [
           {
             "response": {
               "build": 1396,
               "http_method": "POST",
               "http_status": 200,
               "mkey": "host_1007",
               "name": "address",
               "old_revision": "0105b076d0779621cfe555d34b1f6986",
               "path": "firewall",
               "revision": "3f2780027733bd7a9ba00b76d7197892",
               "revision_changed": true,
               "serial": "FGVMMLTM23000162",
               "status": "success",
               "vdom": "root",
               "version": "v7.2.4"
             },
             "status": {
               "code": 0,
               "message": "OK"
             },
             "target": "dut_fgt_03"
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
