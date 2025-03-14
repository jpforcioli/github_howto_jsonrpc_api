Alternative FortiManager APIs
=============================

FortiManager GUI API
--------------------

Introduction to FortiManager GUI API
++++++++++++++++++++++++++++++++++++

When should you use this API?

Typically, you'll need to use it when the FortiManager JSON API does not provide
an *endpoint* for an operation that is available in the FortiManager GUI.

.. warning::

   - This API is not official and may be modified without prior notice

   - Use it only when the FortiManager JSON API cannot fulfill your needs

   - In any case, please consult your Fortinet technical contact to verify if
     there are any supported alternative methods
   
How to Login?
+++++++++++++

Use the following request to retrieve and save the session cookies:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: text

         POST https://10.210.34.143/cgi-bin/module/flatui_auth
         content-type: application/json
         Content-Length: 118
         
         {
           "url": "/gui/userauth",
           "method": "login",
           "params": {
             "secretkey": "fortinet",
             "logintype": 0,
             "username": "devops"
           }
         }

      .. note::
       
         - ``username`` and ``secretkey`` refer to a declared FortiManager 
           administrator and the corresponding password.
         - The ``content-type`` header is mandatory.

   .. tab-item:: RESPONSE:

      .. code-block:: text

         200 
         Date: Fri, 30 Aug 2024 06:31:33 GMT
         Cache-Control: no-store,no-cache,must-revalidate
         Expires: -1
         Pragma: no-cache
         Set-Cookie: CURRENT_SESSION=d1RnYgP7204uiYezuDfoSQ2KHdsJdrMawvo1h8D28thDHUPXl8SNinWC3cEj7w2VVcM0CSYlTz0Y9u62d1D4Kw==; Path=/; HttpOnly; SameSite=Strict; Secure; Version=1, auth_state=; Path=/; Secure; Version=1, remoteauth=; Path=/; Secure; Version=1, HTTP_CSRF_TOKEN=5XZchgLl1faoaKobfowPdMfTLsqTRVo; Path=/; Secure; Version=1
         X-Frame-Options: SAMEORIGIN
         Upgrade: h2
         Connection: Upgrade
         Vary: Accept-Encoding
         Strict-Transport-Security: max-age=63072000
         X-UA-Compatible: IE=Edge
         X-XSS-Protection: 1; mode=block
         X-Content-Type-Options: nosniff
         Content-Security-Policy: frame-ancestors 'none'; object-src 'none'; script-src 'self';
         Transfer-Encoding: chunked
         Content-Type: application/json
         
          {
           "result": [
             {
               "data": null,
               "id": null,
               "status": {
                 "code": 0,
                 "message": ""
               },
               "url": "/gui/userauth"
             }
           ]
         }

A corresponding ``curl`` command could be:

.. tab-set::
   
   .. tab-item:: REQUEST

      .. code-block:: shell

         curl -k -s -c cookie.jar -H "Content-Type: application/json" \
           https://10.210.34.143/cgi-bin/module/flatui_auth -d @login.json

      .. note::

         - It is important to save the returned cookies in the ``cookies.jar``
           file. They will have to be re-used in subsequent calls.

         - ``login.json`` file is with the following content:

           .. code-block:: json
           
             {
               "url": "/gui/userauth",
               "method": "login",
               "params": {
                 "secretkey": "fortinet",
                 "logintype": 0,
                 "username": "devops"
               }
             }


Again, remember to reuse the cookies returned in the login operations in your
subsequent calls.

This is also the time to set the `Xsrf-Token` header with the value of the
captured ``HTTP_CSRF_TOKEN``. 

The ``Xsrf-Token`` is required for all subsequent ``POST`` requests.
For instance for the *Logout* operation.

However, you can also include it in your ``GET`` requests; it won’t cause any 
issues.

Considering the response above, you should set the following ``Xsrf-Token`` 
header:

.. code-block:: text

   Xsrf-Token: 5XZchgLl1faoaKobfowPdMfTLsqTRVo

how to Logout?
++++++++++++++

Use the following request to logout from your FortiManager:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: text

         POST https://10.210.34.143/p/logout-api/
         content-type: application/json
         Xsrf-Token: tvWjDHOjchGBkOxr2mGHTaNm/28Tp1g
         X-Csrf-Token: ezhD6yzSJYqaHGd48GA956ly9eV88v7sGT3kXjiI8lzDbj57RgvrHzjOgGxozxEm6kXmraRXrTTUMT5ox+CeyA==
         Referer: https://10.210.34.143
         Cookie: CURRENT_SESSION=qYMtxynwUfFGsJ9DxjZ/EksNA32EQ8ZuLfINleCv2aSnhzefG2MrUjs2KJ5eqDbfA30n2dWV5jTtKrOGw9tO/A==; auth_state=; remoteauth=; HTTP_CSRF_TOKEN=tvWjDHOjchGBkOxr2mGHTaNm/28Tp1g; universalconnector_csrftoken=uFZ9kGrZzpWi0ucUmK8swUM3E0jYpVPYzQzaNv9obJQ=; universalconnector_csrftoken_masked=ezhD6yzSJYqaHGd48GA956ly9eV88v7sGT3kXjiI8lzDbj57RgvrHzjOgGxozxEm6kXmraRXrTTUMT5ox%2BCeyA%3D%3D
         Content-Length: 0

      .. note::

         - Don't forget the trailing slash in the URL!

         - You have include the ``Xsrf-Token`` header as set during the login 
           operation (see :ref:`How to Login?`). Don't rely on the value from
           this header; it won't match the one captured in the section
           :ref:`How to Login?`.

         - You need to use the ``Referer`` header; in this case, setting it with
           the HTTPS URL of the FortiManager IP address is sufficient

   .. tab-item:: RESPONSE

      .. code-block:: text         

         200 OK
         Date: Fri, 30 Aug 2024 07:11:54 GMT
         X-Frame-Options: SAMEORIGIN
         Content-Language: en
         Vary: Cookie,Accept-Encoding
         X-Content-Type-Options: nosniff
         Referrer-Policy: strict-origin-when-cross-origin
         Cross-Origin-Opener-Policy: same-origin-allow-popups
         Strict-Transport-Security: max-age=63072000
         X-UA-Compatible: IE=Edge
         X-XSS-Protection: 1; mode=block
         Content-Security-Policy: frame-ancestors 'none'; object-src 'none'; script-src 'self';
         Transfer-Encoding: chunked
         Content-Type: application/json; charset=UTF-8
         
         {
           "result": [
             {
               "status": {
                 "code": 0
               },
               "data": {}
             }
           ]
         }        

How to get the License Information
++++++++++++++++++++++++++++++++++

This is to get most of the information exposed in the *License Information* widget of the *Dashboard* page:

.. thumbnail:: images/019_flatui_proxy/image_001.png

#. Obtain the URL used by the FortiManager GUI

   - Open the browser's developer tool
   - Click the refresh icon as shown below:

     .. thumbnail:: images/019_flatui_proxy/image_002.png

   - You can see that used URL is:

     .. code-block:: text

        GET https://10.210.35.112/cgi-bin/module/flatui/SysDashboard?action=read&type=license


#. Use ``curl``/``jq``

   - Login to FortiManager (see section :ref:`How to Login?`)
   - The ``curl``/``jq`` command:

     .. code-block:: text

        curl -s -k -b cookie-jar.txt -H "XSRF-TOKEN: nDbJ1AXyyeVwW6rOgZVTzHcszM8Fb2u" 'https://10.210.35.112/cgi-bin/module/flatui/SysDashboard?action=read&type=license' | jq

     .. note::

        - A HTTP header named ``XSRF-TOKEN`` has been added using the value from the cookie ``HTTP_CSRF_TOKEN``

   - The ``curl``/``jq`` output:

     .. code-block:: json

        {
            "adom_enabled": 1,
            "faz_status": 1,
            "is_vm": 1,
            "is_vm_trial_lic": 0,
            "valid": 1,
            "duplicate_license": 0,
            "has_vmmeter": 1,
            "fortimeter_lic": "None",
            "type": 9,
            "max_num_dev": 100,
            "current_num_dev": 50,
            "dev_num_count": {
              "fap_cnt": {
                "label": "FortiAPs",
                "val": 3
              },
              "fex_cnt": {
                "label": "FortiExtenders",
                "val": 1
              },
              "fgt_cnt": {
                "label": "FortiGates/Logging Devices",
                "val": 50
              },
              "fsw_cnt": {
                "label": "FortiSwitches",
                "val": 1
              }
            },
            "enc_type": 3,
            "max_num_adom": 25,
            "max_gb_day": "5",
            "used_gb_day": "0#0.0",
            "used_gb_day_history": [
              {
                "date": "Today",
                "used": "0.00 GB",
                "is_exceed": 0
              },
              {
                "date": "Aug 08, 2023",
                "used": "0.00 GB",
                "is_exceed": 0
              },
              {
                "date": "Aug 07, 2023",
                "used": "0.00 GB",
                "is_exceed": 0
              },
              {
                "date": "Aug 06, 2023",
                "used": "0.00 GB",
                "is_exceed": 0
              },
              {
                "date": "Aug 05, 2023",
                "used": "0.00 GB",
                "is_exceed": 0
              },
              {
                "date": "Aug 04, 2023",
                "used": "0.00 GB",
                "is_exceed": 0
              },
              {
                "date": "Aug 03, 2023",
                "used": "0.00 GB",
                "is_exceed": 0
              }
            ],
            "max_disk": "1.00 TB",
            "used_disk": "0#59.24 GB",
            "max_disk_gb": "1024",
            "used_disk_gb": "59.240234",
            "en_com_fgd_svr": 1,
            "usg": 1,
            "usg_has_lic": 0,
            "account_id": "foo@bar.com",
            "company": "Fortinet",
            "licenses": {
              "ENHN": {
                "css": "ok",
                "txt": "24x7 Support (Expires 2026-05-25)",
                "status": "ok"
              },
              "AVEN": {
                "css": "warning-red",
                "txt": "Expired (Expires 2023-04-29)",
                "status": "warning-red"
              },
              "ADOM": {
                "css": "ok",
                "txt": "Web/Online Support (Expires 2026-05-25)",
                "status": "ok"
              },
              "SPRT": {
                "css": "ok",
                "txt": "24x7 Support (Expires 2026-05-25)",
                "status": "ok"
              },
              "VMLS": {
                "css": "ok",
                "txt": "Web/Online Support (Expires 2026-05-25)",
                "status": "ok"
              },
              "NIDS": {
                "css": "warning-red",
                "txt": "Expired (Expires 2023-04-29)",
                "status": "warning-red"
              },
              "FRVS": {
                "css": "ok",
                "txt": "Web/Online Support (Expires 2026-05-25)",
              "status": "ok"
            },
            "COMP": {
              "css": "ok",
              "txt": "24x7 Support (Expires 2026-05-25)",
              "status": "ok"
            },
            "AVDB": {
              "css": "warning-red",
              "txt": "Expired (Expires 2023-04-29)",
              "status": "warning-red"
            },
            "FMWR": {
              "css": "ok",
              "txt": "Web/Online Support (Expires 2026-05-25)",
              "status": "ok"
            }
          }
        }        

How to get session information?
+++++++++++++++++++++++++++++++

Caught in #0643655.

**REQUEST:**

.. code-block::

   POST https://10.210.35.200:443/cgi-bin/module/flatui_proxy

   {
       "method": "get",
       "url": "/gui/sys/session"
   }

**RESPONSE:**

.. code-block::

   {
       "result": [
           {
               "data": {
                   "admin_adom": "root",
                   "admin_prof": "Super_User",
                   "admin_user": "admin",
                   "adom_list": [],
                   "adom_override": 0,
                   "login_user": "admin"
               },
               "id": null,
               "status": {
                   "code": 0,
                   "message": ""
               },
               "url": "/gui/sys/session"
           }
       ]
   }

How to get an installation log for a given task?
++++++++++++++++++++++++++++++++++++++++++++++++

You need the task ID and the device OID :-)

The following example shows how to retrieve the installation log for an
installation made against device with the ``39590`` OID. The corresponding task
ID is ``2243``:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: text

         POST https://10.210.34.120/cgi-bin/module/flatui_proxy
         Content-Type: application/json
         Xsrf-Token: 7PdpjDYkaR18jfMoc6N9ccA+cXBx69T
         
         {
           "url": "/gui/deployment/adom/devices/39590/tasks/2243/log/preview",
           "method": "get"
         }
         
   .. tab-item:: RESPONSE

      .. code-block:: text
   
         200
         date: Wed, 04 Dec 2024 14:25:30 GMT
         cache-control: no-store,no-cache,must-revalidate
         expires: -1
         pragma: no-cache
         x-time-request: 1733322330
         x-frame-options: SAMEORIGIN
         upgrade: h2
         connection: Upgrade, Keep-Alive
         vary: Accept-Encoding
         strict-transport-security: max-age=63072000
         x-ua-compatible: IE=Edge
         x-xss-protection: 1; mode=block
         x-content-type-options: nosniff
         content-security-policy: frame-ancestors 'none'; object-src 'none'; script-src 'self';
         content-length: 561
         keep-alive: timeout=5, max=500
         content-type: html
   
         Starting log (Run on device)
   
   
         Start installing
         fgt-001  config endpoint-control fctems
         fgt-001 (fctems)  edit 1
         fgt-001 (1)  set cloud-authentication-access-key ************
         Provided string is not an EMS Cloud access key. Please provide a EMS Cloud access key.
         (Length should be 20, provided string length is 10)
         node_check_object fail! for cloud-authentication-access-key 0123456789
         
         value parse error before '0123456789'
         Command fail. Return code -61
         fgt-001 (1)  next
         fgt-001 (fctems)  edit 2
         fgt-001 (2)  set name "ems_002"
         fgt-001 (2)  set fortinetone-cloud-authentication enable
         fgt-001 (2)  set status enable
         fgt-001 (2)  set cloud-authentication-access-key ************
         Provided string is not an EMS Cloud access key. Please provide a EMS Cloud access key.
         (Length should be 20, provided string length is 10)
         node_check_object fail! for cloud-authentication-access-key 0123456789
         
         value parse error before '0123456789'
         Command fail. Return code -61
         fgt-001 (2)  next
         Cannot configure two duplicate FortiCloud EMS. Global EMS entry '1' has the same access key (empty key).
         object set operator error, -15 discard the setting
         Command fail. Return code 1
         fgt-001 (fctems)  edit 3
         fgt-001 (3)  set name "ems_NNN"
         fgt-001 (3)  set fortinetone-cloud-authentication enable
         fgt-001 (3)  set status enable
         fgt-001 (3)  next
         Cannot configure two duplicate FortiCloud EMS. Global EMS entry '1' has the same access key (empty key).
         object set operator error, -15 discard the setting
         Command fail. Return code 1
         fgt-001 (fctems)  end
         fgt-001  config system zone
         fgt-001 (zone)  edit "z_001"
         fgt-001 (z_001)  set interface "port8" "port9" "port10"
         fgt-001 (z_001)  next
         fgt-001 (zone)  end
         
         
         ---> generating verification report
         <--- done generating verification report
         
         
         install finished      

Some URLs caught in #0659916
++++++++++++++++++++++++++++

.. code-block::

   Fri 2020-10-23 10:11:38.788 ======== PARAMETERS THAT ARE BEING USED ========
   Fri 2020-10-23 10:11:38.788 test type = json
   Fri 2020-10-23 10:11:38.788 user = qa12
   Fri 2020-10-23 10:11:38.788 password = **********
   Fri 2020-10-23 10:11:38.788 json_url = https://10.2.88.20/jsonrpc
   Fri 2020-10-23 10:11:38.788 json_web_proxy = 2
   Fri 2020-10-23 10:11:38.789 json_web_login_urls = ['https://10.2.88.20/cgi-bin/module/flatui_auth', 'https://10.2.88.20/p/app/']
   Fri 2020-10-23 10:11:38.789 json_web_logout_url = https://10.2.88.20/cgi-bin/module/frame/logout
   Fri 2020-10-23 10:11:38.789 json_web_url = https://10.2.88.20/cgi-bin/module/flatui/json
   Fri 2020-10-23 10:11:38.789 json_web_fast_url = https://10.2.88.20/cgi-bin/module/forward
   Fri 2020-10-23 10:11:38.789 rest_file_content = False

How to perform a device revision diff?
++++++++++++++++++++++++++++++++++++++

The GUI-based device revision diff is entirely managed by the GUI side.
The FortiManager GUI API is just used to return two revisions as shown below.
We ask for a revision diff for device revisions 3 and 4 from device with ID
434.

**REQUEST:**

.. code-block::

   POST https://10.210.35.208:443/cgi-bin/module/flatui_proxy
   
   {
       "url": "/gui/adom/dvm/device/revision/diff",
       "method": "get",
       "params": {
           "deviceId": "434",
           "from": 3,
           "to": 4,
           "options": 1
       },
       "id": 1
   }

**RESPONSE:**

.. code-block::

   {
       "result": [
           {
               "data": {
                   "version1": "#config-version=FG100F-6.0[...]",
                   "version2": "#config-version=FG100F-6.0[...]",                 
               },
               "id": 1,
               "status": {
                   "code": 0,
                   "message": ""
               },
               "url": "/gui/adom/dvm/device/revision/diff"
           }
       ]
   }   

How to get the factory default config of a managed device?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**REQUEST**:

.. code-block::

   {
     "url": "/gui/adom/dvm/device/revision/content", 
     "method": "get_download", 
     "params": {
       "deviceId": "201", 
       "deviceName": "dut_fgt1", 
       "rev": 0, 
       "sn": "FGVMULREDACTED77", 
       "options": 3, 
       "user": "admin", 
       "password": ""
     }
   }

**RESPONSE**:

.. code-block::

   #config-version=FGVMK6-6.00-FW-build1803-000000:opmode=0:vdom=0:user=admin
   #version=600
   #build=1803
   #branch_pt=1803
   #platform=FORTIGATE-VM64-KVM
   #serialno=FGVMULREDACTED77
   #logdisk=1
   #mgmt.data=00000000000000000000,00000000000000000000,00000000000000000000,00000000000000000000
   #mgmt.dat2=00000000000000000000,00000000000000000000,00000000000000000000,00000000000000000000

   config system global
   set alias "FortiGate-VM64-KVM"
   set hostname "FortiGate-VM64-KVM"
   set timezone 04
   end
   config system accprofile
   edit "prof_admin"
   set secfabgrp read-write
   set ftviewgrp read-write
   set authgrp read-write
   set sysgrp read-write
   set netgrp read-write

How to operate the policy package check operation?
++++++++++++++++++++++++++++++++++++++++++++++++++

1. Trigger the policy package check operation

**REQUEST:**

.. code-block:: json

   {
       "method": "create", 
       "url": "/gui/adoms/157/pkgs/7494/consistency-checker"
   }

where ``157`` and ``7494`` are the ADOM and Policy Package OIDs respectively.

**RESPONSE:**

.. code-block:: json

   {
       "result": [
           {
               "data": {
                   "taskId": 365
               },
               "id": null,
               "status": {
                   "code": 0,
                   "message": ""
               },
               "url": "/gui/adoms/157/pkgs/7494/consistency-checker"
           }
       ]
   }

It is required to wait for task completion.

2. Get the Policy Package check result

**REQUEST:**

.. code-block:: json

   {
       "method": "get", 
       "url": "/gui/adoms/157/pkgs/7494/consistency-checker"
   }

In fact this request will alway return the latest Policy Package check report.

**RESPONSE:**

.. code-block::

   {
       "result": [
           {
               "status": "ok",
               "timestamp": "Mon Apr 19 10:14:35 2021",
               "type": 1,
               "name": "demo",
               "pkgname": "ppkg_buggy",
               "rec": [
                   {
                       "type": 3,
                       "name": "4",
                       "full_shadow_count": "3",
                       "partial_shadow_count": "8",
                       "none policy count": "0",
                       "none_rec": [],
                       "rec": [
                           [REPORT HERE]
                       ]
                   }
               ]
           }
       ]
   }

How to operate a policy package diff operation?
+++++++++++++++++++++++++++++++++++++++++++++++

1. Trigger the policy package diff operation

   ..tab-set::

     .. tab-item:: REQUEST

        .. code-block:: json
        
           {
               "url": "/gui/adom/installation/pkg/install",
               "method": "processPreview",
               "params": {
                   "pkgOid": 3292,
                   "installDevIds": "170-0"
               }
           }

        where ``pkgOid`` and ``installDevIds`` are the policy package and 
        managed device OIDs. For the managed device, "170-0" refers to device 
        OID and VDOM OID.

     .. tab-item:: RESPONSE

        .. code-block:: json
        
           {
               "result": [
                   {
                       "data": {
                           "isSchd": 0,
                           "msg": "",
                           "result": "ok",
                           "tid": 369
                       },
                       "id": null,
                       "status": {
                           "code": 0,
                           "message": ""
                       },
                       "url": "/gui/adom/installation/pkg/install"
                   }
               ]
           }

        When we look in task monitor in FortiManager GUI, this action trigger a 
        *copy* operation. 
        
        When the task is complete we have to trigger an install preview 
        operation.

2. Trigger an install preview operation

   Here we could use the normal FortiManager JSON RPC API, but we have to 
   remain in the same session. This is why we're using the flatui_proxy to
   trigger the install preview operation.

How to CSV export components from policy package?
+++++++++++++++++++++++++++++++++++++++++++++++++

By components we mean:

- Firewall policies
- Global header/footer policies
- Shaping policies
- etc.

It's a two steps process:

1. First we need to trigger the export task, mentioning what do we want to CSV
   export
2. Then we need to download the resulting file.

Trigger the CSV export task
___________________________

That's an example:

**REQUEST**:

.. code-block:: json

   {
       "url": "/gui/adoms/157/pkgs/3292/file-csv",
       "method": "create",
       "params": {
           "content": [
               {
                   "cateId": 181,
                   "fields": [
                       "policyid",
                       "action",
                       "name"
                   ]
               }
           ]
       }
   }
   
Let's have a look at the ``content`` attribute.

- ``cateId`` is the type of the policy we want to export. In this example
  ``181`` is for the ``firewall policy``. 
  
  * Should you want to export ``global header policy`` or ``global footer
    policy`` you will have to use ``1474`` or ``1476`` respectively.
  
  * For ``firewall shaping-policy`` or ``firewall proxy-policy`` you will have
    to use ``1640`` or ``1844`` respectively. 

  * All of those ID could be obtain by using the commands:

    .. code-block::

       execute fmpolicy print-adom-object <adom> ?
       execute fmpolicy print-adom-package <adom> 1 <package> ?

- It is possible to ask for multiple policy types in a single request:

**REQUEST**:

.. code-block:: json

   {
       "url": "/gui/adoms/157/pkgs/3292/file-csv",
       "method": "create",
       "params": {
           "content": [
               {
                   "cateId": 181,
                   "fields": [
                       "policyid",
                       "action",
                       "name"
                   ]
               }
               {
                   "cateId": 1474,
                   "fields": [
                       "policyid",
                       "action",
                       "name",
                       "comments",
                       "srcaddr"
                   ]
               },
                   "cateId": 1476,
                   "fields": [
                       "policyid",
                       "action",
                       "name",
                       "dstaddr"
                   ]
               }                              
           ]
       }
   }
   
As you can see, we can also be very specific when it comes to declare the fields
we want to be exported in the CSV output. And the other important information,
is that the order of the exported fields will be respected. 

For instance, in
the above request, the FortiManager will export the fields ``policyid``, ``action``,
``name`` and ``dstaddr``, in that order, for ``global footer policy`` (i.e.,
``1476``).

Obviously, values ``157`` and ``3293`` are the ADOM and Policy Package OID
respectively.

In all cases, this is the kind of response you will get:

**RESPONSE:**

.. code-block:: json

   {
      "result": [
        {
            "data": {
                "taskid": "a287fb14-0b18-11ec-ae55-02090f000116"
            },
            "id": null,
            "status": {
                "code": 0,
                "message": ""
            },
            "url": "/gui/adoms/157/pkgs/3292/file-csv"
        }
      ]
   }

Download the CSV file
_____________________

**REQUEST:**

.. code-block::

   GET https://secops-demo-001.gcp.fortipoc.net:10421/flatui/api/gui/download?filepath=policypackage-3292.csv&downloadname=ppkg_branches-20210901-120531.csv

**RESPONSE:**

.. code-block::

   policyid,action,name,scope
   "1","accept","ul_egress_traffic","[All Devices/Groups]"
   "2","accept","ol_ingress_traffic","[All Devices/Groups]"
   "3","accept","ol_egress_traffic","[All Devices/Groups]"
   "10001","accept","policy_0001","[All Devices/Groups]"
   "10002","accept","policy_0002","[All Devices/Groups]"
   "10003","accept","policy_0003","[All Devices/Groups]"
   "11001","deny","","[All Devices/Groups]"
   "10004","accept","policy_0004","[All Devices/Groups]"
   "10005","accept","policy_0005","[All Devices/Groups]"
   "10006","accept","policy_0006","[All Devices/Groups]"
   "10007","accept","policy_0007","[All Devices/Groups]"
   "10008","accept","policy_0008","[All Devices/Groups]"
   [...]    

The attribute ``downloadname`` is optional; if ommited, the CSV file name will
be from the value of the ``filepath`` attribute.

How to download a FortiManager packet capture?
++++++++++++++++++++++++++++++++++++++++++++++

See section :ref:`FortiManager Packet capture` for more details about operating
FortiManager packet captures using the FortiManager API.

The following example shows how to download an existing FortiManager packet
capture file:

.. code-block:: shell

   curl -o sniffer_port1.1.pcap  -v -s -k -b cookie.jar \
     -H "Xsrf-Token: uvTrN9S6HJrxXWPanUkVwA5IRXDdql7" \
     -H "Content-Type: application/json" \
     'https://{{fmg_ip}}/flatui/api/gui/sniff/export?filename=sniffer_port1.1.pcap&downloadname=sniffer_port1.1.pcap'


How to get the list of vulnerabilities for your managed devices?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This is to get the list of vulnerabilities as shown in the following screenshot
from FortiManager 7.4.5:

.. thumbnail:: images/alternative_fortimanager_api/image_001.png

The following example shows how to get the list of vulnerabilities for the
managed devices in the ADOM ``root``:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: text

         POST https://10.210.34.139/cgi-bin/module/flatui_proxy
         Content-Type: application/json
         Xsrf-Token: P6DtO5DLqp8ox5ZI9sjgdw6lEzbAXuA

         {
             "url": "/gui/adoms/3/dvm/psirt",
             "method": "get"
         }

      .. note::

         ``3`` is the OID of the ADOM ``root``.

   .. tab-item:: RESPONSE

      .. literalinclude:: datas/alternative_fortimanager_api/output_001.json
         :language: json
      
You can consider reading section :ref:`How to get Fortinet vulnerabilities for
your managed devices?` to get the list of vulnerabilities for your managed
devices using a more regular way.

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

REST API only supports HTTP basic authentication; you can use same credentias as
with the |fmg_api|. It doesn't support token-based authentication; you can't use
a ``Authorization`` header to pass a bearer token.

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
