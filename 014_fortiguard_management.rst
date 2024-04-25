FortiGuard Management
=====================

Introduction to FortiGuard Management
-------------------------------------

In this section, a lot of API examples have been collected by enabling the
following debug command in FortiManager console:

.. code-block:: shell

   diagnose debug application fdssvrd 255
   diagnose debug enable

and playing with FortiGuard using either the FortiManager GUI or the 
following FortiManager CLI commands:

.. code-block:: shell

   execute fmupdate <option>
   diagnose fwmanager <option>
   
How to get the FMG FGD object versions?
---------------------------------------

The below example has been collected by using the following FortiManager CLI:

.. code-block:: text

   execute fmupdate fgd-dvber

with the debug enabled as described in the :ref:`Introduction to FortiGuard
Management` secion.

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "jsonrpc": "1.0",
           "method": "get",
           "params": [
             {
               "data": {
                 "flags": 0
               },
               "url": "/um/misc/fgd_db_ver"
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
               "data": {
                 "as1": {
                   "desc": "Antispam(IP)",
                   "size": 821269740,
                   "update_time": 1618820401,
                   "version": 6738278
                 },
                 "as2": {
                   "desc": "Antispam(URI)",
                   "size": 0,
                   "update_time": 0,
                   "version": 0
                 },
                 "as4": {
                   "desc": "Antispam(HASH)",
                   "size": 28683496,
                   "update_time": 1618821361,
                   "version": 5318876
                 },
                 "av": {
                   "desc": "AntiVirus Query",
                   "size": 0,
                   "update_time": 0,
                   "version": 0
                 },
                 "av2": {
                   "desc": "Outbreak Prevention",
                   "size": 0,
                   "update_time": 0,
                   "version": 0
                 },
                 "fq": {
                   "desc": "File Query",
                   "size": 0,
                   "update_time": 0,
                   "version": 0
                 },
                 "geoip": {
                   "desc": "GeoIP",
                   "size": 108984169,
                   "update_time": 1617692460,
                   "version": 131146
                 },
                 "wf": {
                   "desc": "Webfilter",
                   "size": 7054323572,
                   "update_time": 1589577005,
                   "version": 1522738
                 }
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/misc/fgd_db_ver"
             }
           ]
         }   
      
How to get the FMG upstream servers list?
-----------------------------------------
      
It's quite easy to expose the |fmg_api| endpoints by debugging the ``fdssvrd``
process while issuing the FortiManager CLI command:

.. code-block::

   diagnose fmupdate view-serverlist <fgd|fds>

To debug the ``fdssvrd`` process:

.. code-block:: shell

   diagnose debug application fdssvrd 255
   diagnose debug enable
   diagnose debug timestamp enable

Then we can ask for the upstream FDS servers using the following command:

.. code-block:: shell

   diagnose fmupdate view-serverlist fds

Following output should be displayed:

.. code-block::

   2022-03-22 23:06:12 Request:
   2022-03-22 23:06:12 { "client": "-newcli:22493", "id": 4, "method": "get", "params": [{ "data": { "flags": 0}, "target start": 1, "url": "misc\/server_list"}], "root": "um"}
   2022-03-22 23:06:12 Response:
   2022-03-22 23:06:12 { "id": 4, "result": [{ "data": { "loose_mode": 1, "public_network": 1, "server_list": [{ "0": { "addr": "208.184.237.67", "distance": 1, "port": 443, "src": 4, "timezone": 0}, "1": { "addr": "12.34.97.16", "distance": 6, "port": 443, "src": 4, "timezone": -5}, "2": { "addr": "208.184.237.68", "distance": 8, "port": 443, "src": 4, "timezone": 9}, "3": { "addr": "208.184.237.66", "distance": 9, "port": 443, "src": 4, "timezone": -8}, "4": { "addr": "usfds1.fortinet.com", "distance": 0, "port": 443, "src": 2, "timezone": 1}, "count": 5, "curr_svr_index": 3, "service_type": "fds"}, { "0": { "addr": "208.184.237.75", "distance": 9, "port": 443, "src": 4, "timezone": -8}, "1": { "addr": "usforticlient.fortinet.net", "distance": 0, "port": 443, "src": 2, "timezone": 1}, "count": 2, "curr_svr_index": 0, "service_type": "fct"}, { "0": { "addr": "65.210.95.253", "distance": 6, "port": 443, "src": 4, "timezone": -5}, "1": { "addr": "usfqsvr.fortinet.net", "distance": 0, "port": 443, "src": 2, "timezone": 1}, "count": 2, "curr_svr_index": 1, "service_type": "geoip"}]}, "status": { "code": 0, "message": "OK"}, "url": "misc\/server_list"}]}
   2022-03-22 23:06:12
   Fortiguard Server Comm : Enabled
   Server Override Mode   : Loose
   FDS   server list      :
   Index   Address                    Port            TimeZone        Distance        Source
   ------------------------------------------------------------------------------------------------------
    0      208.184.237.67             443             0               1               FDNI
    1      12.34.97.16                443             -5              6               FDNI
    2      208.184.237.68             443             9               8               FDNI
   *3      208.184.237.66             443             -8              9               FDNI
    4      usfds1.fortinet.com        443             1               0               DEFAULT

   FCT   server list      :
   Index   Address                    Port            TimeZone        Distance        Source
   ------------------------------------------------------------------------------------------------------
   *0      208.184.237.75             443             -8              9               FDNI
    1      usforticlient.fortinet.net 443             1               0               DEFAULT

   GEOIP server list      :
   Index   Address                    Port            TimeZone        Distance        Source
   ------------------------------------------------------------------------------------------------------
    0      65.210.95.253              443             -5              6               FDNI
   *1      usfqsvr.fortinet.net       443             1               0               DEFAULT
   
When formatted and cleaned a bit, we can see the following |fmg_api| exchange:

**REQUEST:**

.. code-block:: json

   {
     "id": 4,
     "method": "get",
     "params": [
       {
         "data": {
           "flags": 0
         },
         "url": "/um/misc/server_list"
       }
     ],
   }  

**RESPONSE:**

.. code-block:: json

   {
     "id": 4,
     "result": [
       {
         "data": {
           "loose_mode": 1,
           "public_network": 1,
           "server_list": [
             {
               "0": {
                 "addr": "208.184.237.67",
                 "distance": 1,
                 "port": 443,
                 "src": 4,
                 "timezone": 0
               },
               "1": {
                 "addr": "12.34.97.16",
                 "distance": 6,
                 "port": 443,
                 "src": 4,
                 "timezone": -5
               },
               "2": {
                 "addr": "208.184.237.68",
                 "distance": 8,
                 "port": 443,
                 "src": 4,
                 "timezone": 9
               },
               "3": {
                 "addr": "208.184.237.66",
                 "distance": 9,
                 "port": 443,
                 "src": 4,
                 "timezone": -8
               },
               "4": {
                 "addr": "usfds1.fortinet.com",
                 "distance": 0,
                 "port": 443,
                 "src": 2,
                 "timezone": 1
               },
               "count": 5,
               "curr_svr_index": 3,
               "service_type": "fds"
             },
             {
               "0": {
                 "addr": "208.184.237.75",
                 "distance": 9,
                 "port": 443,
                 "src": 4,
                 "timezone": -8
               },
               "1": {
                 "addr": "usforticlient.fortinet.net",
                 "distance": 0,
                 "port": 443,
                 "src": 2,
                 "timezone": 1
               },
               "count": 2,
               "curr_svr_index": 0,
               "service_type": "fct"
             },
             {
               "0": {
                 "addr": "65.210.95.253",
                 "distance": 6,
                 "port": 443,
                 "src": 4,
                 "timezone": -5
               },
               "1": {
                 "addr": "usfqsvr.fortinet.net",
                 "distance": 0,
                 "port": 443,
                 "src": 2,
                 "timezone": 1
               },
               "count": 2,
               "curr_svr_index": 1,
               "service_type": "geoip"
             }
           ]
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "misc/server_list"
       }
     ]
   }

Using same process, we can easily get the FGD upstream servers:

**REQUEST**:

.. code-block:: json



**RESPONSE**:

.. code-block:: json


Firmware Management
-------------------

How to get the list of firmware images for FortiGate device?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

It is to get the same list as the one you get when visiting the *FortiGuard* > *Firmware Images*:

.. thumbnail:: images/image_009.png

Following example shows how to get the list of fimware images for the 
FortiGate-60F platform:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "flags": 1,
                 "platform": "FortiGate-60F",
                 "product": "FGT"
               },
               "url": "/um/image/version/list"
             }
           ],
           "session": "{{session}}",
         }

   .. tab-item:: RESPONSE

      .. code-block:: text

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "status": "success",
                 "version_list": [
                   {
                     "fdsid": "FGT60F",
                     "platform": "FortiGate-60F",
                     "product": "FGT",
                     "versions": [
                       {
                         "bdate": "2001251225",
                         "image_type": "NA",
                         "objid": "06000000FIMG00242-00000.00009-2001251225",
                         "type": "GA",
                         "version": "6.0.9-b6665"
                       },
                       {
                         "bdate": "2209090404",
                         "image_type": "NA",
                         "objid": "06000000FIMG00242-00000.00015-2209090404",
                         "type": "GA",
                         "version": "6.0.15-b6930"
                       },
                       {
                         "SNIP": "SNIP",
                       }         
                       {
                         "bdate": "2306101549",
                         "image_type": "F",
                         "objid": "07002000FIMG00242-00002.00005-2306101549",
                         "type": "GA",
                         "version": "7.2.5-b1517"
                       },
                       {
                         "bdate": "2210052037",
                         "image_type": "F",
                         "objid": "07002000FIMG00242-00002.00002-2210052037",
                         "type": "GA",
                         "version": "7.2.2-b1255"
                       }
                     ]
                   }
                 ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/image/version/list"
             }
           ]
         }

Should you want to get the firmware images for all FortiGate device?
Just omit the ``platform`` attribute and keep the ``product`` one set with ``FGT``:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "flags": 1,
                 "product": "FGT"
               },
               "url": "/um/image/version/list"
             }
           ],
           "session": "{{session}}",
         }

You can also get the firmware images for the following procuct:

.. list-table:: 
   :header-rows: 1
   :widths: auto

   * - Name
     - ``product``

   * - FortiGate
     - ``FGT``

   * - FortiAnalyzer
     - ``FAZ``

   * - FortiManager
     - ``FMG``

   * - FortiAP
     - ``FAP``

   * - FortiExtender
     - ``FXT``

   * - FortiSwitch
     - ``FSW``

   * - FortiProxy
     - ``FPX``

If you omit both the ``platform`` and the ``product`` attributes, then you 
will get the firmware images list for all platforms/products!

.. note::

   - FortiManager indicates in the output when the firmware image has been 
     already downloaded:

     .. tab-set::

        .. tab-item:: RESPONSE

           .. code-block:: json

              {
                "bdate": "2304132147",
                "image_type": "NA",
                "objid": "06002000FIMG00259-00002.00014-2304132147",
                "type": "GA",
                "version": "6.2.14-b1364"
              },
              {
                "bdate": "2312230056",
                "image_path": "/var/fwm/image/FGT40F_7.4.2_b2571_FORTINET.out",
                "image_size": 81475306,
                "image_type": "F",
                "objid": "07004000FIMG00259-00004.00002-2312230056",
                "type": "GA",
                "version": "7.4.2-b2571"
              },

           .. note::

              In the above response snipet, you can see that build ``6.2.14``  
              is still in the public FortiGuard servers while the build 
              ``7.4.2`` has already been download in FortiManager.

How to download a firmware image?
+++++++++++++++++++++++++++++++++

The following example shows hot to download the firmware image for the FortiOS version 7.0.1 build 0489 and the FortiGate-100F platform:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         { 
           "id": 1,
           "method": "exec", 
           "params": [
             { 
               "data": { 
                 "create_task": "enable", 
                 "platform": "FortiGate-100F", 
                 "version": "7.0.11-b0489-GA"
               }, 
               "url": "/um/image/download"
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
               "data": { 
                 "status": "success", 
                 "taskid": 1403
               }, 
               "status": { 
                 "code": 0, 
                 "message": "OK"
               }, 
               "url": "/um/image/download"
             }
           ]
         }

How to get contracts for managed devices?
-----------------------------------------

There are multiple ways to obtain more or less the same thing: the list of contracts or entitlements associated with the managed devices.

Using ``/um/device/list``
+++++++++++++++++++++++++

The following example shows how to get the contracts for all managed devices:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "url": "/um/device/list"
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
                 "count": 19,
                 "dev_object": [ "... LIST IS TOO LONG ..." ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/device/list"
             }
           ]
         }               

      .. note::

         - As indicated by the ``count`` attribute, 19 entries are returned
         - It could be a longer list
         - This is why we can use some filtering options like ``serial`` or 
           ``os_type``

For instance, the following example shows how to get the contracts for the managed device with the ``FG421F0000000001`` Serial Number:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "serial": "FG421F0000000001"
               },
               "url": "/um/device/list"
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
                 "count": 1,
                 "dev_object": [
                   {
                     "account": "foo@bar.com",
                     "address": "10.82.10.133",
                     "announce_ip": "",
                     "announce_port": 0,
                     "build": 1639,
                     "company": "Bar Inc.",
                     "contract": "Contract=AVDB-1-06-20250316:0:1:1:0*AVEN-1-06-20250316:0:1:1:0*COMP-1-20-20250316:0:1:1:0*ENHN-1-20-20250316:0:1:1:0*FMWR-1-06-20250316:0:1:1:0*FRVS-1-06-20250316:0:1:1:0*FURL-1-06-20250316:0:1:1:0*HDWR-1-05-20250316:0:1:1:0*NIDS-1-06-20250316:0:1:1:0*SPAM-1-06-20250316:0:1:1:0*SPRT-1-20-20250316:0:1:1:0*ZHVO-1-06-20250316:0:1:1:0|AccountID=foo@bar.com|Company=Bar Inc.|UserID=123456",
                     "firmware": "FG421F-FW-7.02-1639",
                     "flags": 0,
                     "industry": "",
                     "lic_map": {
                       "AVDB": "AVDB-1-06-20250316:0:1:1:0",
                       "AVEN": "AVEN-1-06-20250316:0:1:1:0",
                       "COMP": "COMP-1-20-20250316:0:1:1:0",
                       "ENHN": "ENHN-1-20-20250316:0:1:1:0",
                       "FMWR": "FMWR-1-06-20250316:0:1:1:0",
                       "FRVS": "FRVS-1-06-20250316:0:1:1:0",
                       "FURL": "FURL-1-06-20250316:0:1:1:0",
                       "HDWR": "HDWR-1-05-20250316:0:1:1:0",
                       "NIDS": "NIDS-1-06-20250316:0:1:1:0",
                       "SPAM": "SPAM-1-06-20250316:0:1:1:0",
                       "SPRT": "SPRT-1-20-20250316:0:1:1:0",
                       "ZHVO": "ZHVO-1-06-20250316:0:1:1:0"
                     },
                     "obj_map": {
                       "07002000AFDB00100": 65548,
                       "07002000APDB00105": 1770243,
                       "07002000AVDB00201": 6032945,
                       "07002000AVDB00701": 6032945,
                       "07002000AVDB01901": 146887,
                       "07002000AVEN03300": 393513,
                       "07002000CIDB00000": 65702,
                       "07002000CRDB00000": 65586,
                       "07002000DBDB00100": 197353,
                       "07002000FFDB02008": 462412,
                       "07002000FLDB00201": 6032945,
                       "07002000FLEN08000": 459088,
                       "07002000FMWP00105": 1572884,
                       "07002000ICDB00101": 65579,
                       "07002000MADB00200": 65749,
                       "07002000MCDB00100": 66013,
                       "07002000MMDB00101": 6032945,
                       "07002000SFAS00000": 262199,
                       "07002000UWDB00100": 262347
                     },
                     "os_mr": 2,
                     "os_type": 0,
                     "os_ver": 7,
                     "platform": "FortiGate-4201F",
                     "serial": "FG421F0000000001",
                     "setup_info": "",
                     "sync_time": 1713886270,
                     "uid_active_time": 0,
                     "umdb_exist": 1,
                     "userid": "814571",
                     "vmlic_check_time": 0,
                     "vmlic_reg_time": 0,
                     "vmlic_status": "",
                     "vmlic_uid": ""
                   }
                 ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/device/list"
             }
           ]
         }        

      .. note::

         As indicated by the ``count`` attribute, only 1 entry is returned 
         since you asked for a single device's serial number

Or the following example shows how to get the contracts for all managed 
FortiGate units (i.e., the ones with the FortiOS operating system type ``os_type`` is ``0``):

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "os_type": 0,
               },
               "url": "/um/device/list"
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
                 "count": 17,
                 "dev_object": [ "... LIST IS TOO LONG ..." ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/device/list"
             }
           ]
         }   

.. tip:: 

   - Where is the ``0`` value from for the ``os_type``?
   - It's in the file ``/var/dm/syntax/dvmcmd_syntax.json``
   - Existing values are:

     .. code-block:: json

        "OS_TYPE_OPTIONS": {
          "unknown": -1,
          "fos": 0,
          "fsw": 1,
          "foc": 2,
          "fml": 3,
          "faz": 4,
          "fwb": 5,
          "fch": 6,
          "fct": 7,
          "log": 8,
          "fmg": 9,
          "fsa": 10,
          "fdd": 11,
          "fac": 12,
          "fpx": 13,
          "fna": 14
        }
   - You cannot use the symbolic form: for instance you can't use ``fos`` 
     instead of ``0``

Using ``/um/misc/dump_contract``
++++++++++++++++++++++++++++++++

The following example shows how to get the contracts for all managed devices:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         { 
           "id": 1, 
           "method": "exec", 
           "params": [
             { 
               "data": { 
                 "flags": 0, 
               }, 
               "url": "/um/misc/dump_contract"
             }
           ], 
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "...": "... LIST IS TOO LONG ..."
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/device/list"
             }
           ]
         }           

The following example shows how to get the contracts for the managed device with the ``FG421F0000000001`` Serial Number:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

      
         { 
           "id": 1, 
           "method": "exec", 
           "params": [
             { 
               "data": { 
                 "flags": 0, 
                 "serial": "FG421F0000000001"
               }, 
               "url": "/um/misc/dump_contract"
             }
           ], 
         }


   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "acli": [
                   "UserID=123456|SerialNumber=FCLDPS0000000001|Contract=FCEP-6-20250411-1-1\r",
                   "UserID=123456|SerialNumber=FCTEMS8824000001|Contract=FCEM-6-20240507-50-50\r",
                   "UserID=123456|SerialNumber=FSACLPTM24000001|Contract=FSAP-6-20250411-1-1\r",
                   "\r",
                   ""
                 ],
                 "contract": [
                   {
                     "account": "foo@bar.com",
                     "address": "10.83.10.133",
                     "company": "FORTINET",
                     "contract_item": [
                       "AVDB-1-06-20250316:0:1:1:0",
                       "AVEN-1-06-20250316:0:1:1:0",
                       "COMP-1-20-20250316:0:1:1:0",
                       "ENHN-1-20-20250316:0:1:1:0",
                       "FMWR-1-06-20250316:0:1:1:0",
                       "FRVS-1-06-20250316:0:1:1:0",
                       "FURL-1-06-20250316:0:1:1:0",
                       "HDWR-1-05-20250316:0:1:1:0",
                       "NIDS-1-06-20250316:0:1:1:0",
                       "SPAM-1-06-20250316:0:1:1:0",
                       "SPRT-1-20-20250316:0:1:1:0",
                       "ZHVO-1-06-20250316:0:1:1:0"
                     ],
                     "industry": "",
                     "rawdata": "Contract=AVDB-1-06-20250316:0:1:1:0*AVEN-1-06-20250316:0:1:1:0*COMP-1-20-20250316:0:1:1:0*ENHN-1-20-20250316:0:1:1:0*FMWR-1-06-20250316:0:1:1:0*FRVS-1-06-20250316:0:1:1:0*FURL-1-06-20250316:0:1:1:0*HDWR-1-05-20250316:0:1:1:0*NIDS-1-06-20250316:0:1:1:0*SPAM-1-06-20250316:0:1:1:0*SPRT-1-20-20250316:0:1:1:0*ZHVO-1-06-20250316:0:1:1:0|AccountID=foo@bar.com|Company=Bar Inc.|UserID=123456",
                     "serial": "FG421F0000000001"
                   }
                 ],
                 "count": 1,
                 "support_level_desc": "05:Advanced HW*06:Web/Online*10:8x5*20:Premium*99:Trial",
                 "support_type_desc": "AVDB:Advanced Malware Protection*COMP:*DLDB:DLP*ENHN:*FAIS:FortiGuard AI-based Sandbox Service*FAZC:FortiAnalyzer Cloud Basic*FCSS:FortiConverter Service*FGSA:FortiGuard Attack Surface Security Service*FMGC:FortiManager Cloud*FMWR:Firmware & General Updates*FRVS:Vulnerability Management*FSPA:SPA License*FURL:FortiGuard URL, DNS & Video Filtering Service*HDWR:Hardware*IOTH:IoT Detection*IPMC:IPAM Cloud*ISSS:FortiGuard OT Security Service*NIDS:FortiGuard IPS Service*SBCL:FortiSandbox Cloud*SPAM:AntiSpam*SPRT:*SWNC:SD-WAN Orchestrator*SWNM:FortiGuard SD-WAN Underlay Service*SWNO:SD-WAN Overlay Controller*SWOS:SD-WAN Overlay as a Service*VDOM:VDOM*VMLS:VM license*ZHVO:FortiGuard Virus Outbreak Protection Service"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/misc/dump_contract"
             }
           ]
         }            

How to get the package versions for your managed devices?
---------------------------------------------------------

Here *package* means IPS, AV, Applications, etc. databases that are used by your
managed devices.

The following example shows how to get the package versions for all your 
managed devices:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "flags": 0
               },
               "url": "/um/device/object"
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
                 "count": 19,
                 "dev_object": [ "... TO LARGE OUTPUT ..." ],
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/device/object"
             }
           ]
         }        

The following example shows how to get the package versions for the managed device with the ``FG421F0000000001`` Serial Number:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "flags": 0,
                 "serial": "FG421F0000000001"
               },
               "url": "/um/device/object"
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
                 "count": 1,
                 "dev_object": [
                   {
                     "exclude_reason": "",
                     "flags": 0,
                     "object_version": [
                       {
                         "current_version": "00001.00166",
                         "latest_version": "00001.00166",
                         "license": "valid",
                         "license_type": "FMWR",
                         "obj_desc": "Client ID DB",
                         "obj_fmgi": {
                           "ext_desc": "Client ID DB",
                           "objid": "07002000CIDB00000",
                           "product": "FortiManager",
                           "service": "Firmware",
                           "subtype": "",
                           "version": "7.2.1+"
                         },
                         "objid": "07002000CIDB00000",
                         "prefer_version": "00000.00000",
                         "status": "up-to-date"
                       },
                       {
                         "current_version": "00001.00043",
                         "latest_version": "00001.00043",
                         "license": "valid",
                         "license_type": "FMWR",
                         "obj_desc": "ICDB",
                         "obj_fmgi": {
                           "ext_desc": "Object for a list of SaaS Applications.",
                           "objid": "07002000ICDB00101",
                           "product": "Inline Casb DataBase",
                           "service": "FMWR",
                           "subtype": "",
                           "version": "7.2"
                         },
                         "objid": "07002000ICDB00101",
                         "prefer_version": "00000.00000",
                         "status": "up-to-date"
                       },
                       {
                         "current_version": "00004.00055",
                         "latest_version": "00004.00055",
                         "license": "valid",
                         "license_type": "FGSA:FMWR",
                         "obj_desc": "Security",
                         "obj_fmgi": {
                           "ext_desc": "Security",
                           "objid": "07002000SFAS00000",
                           "product": "FortiManager",
                           "service": "Security",
                           "subtype": "",
                           "version": "7.2.1+"
                         },
                         "objid": "07002000SFAS00000",
                         "prefer_version": "00000.00000",
                         "status": "up-to-date"
                       }
                     ],
                     "serial": "FG421F0000000001",
                     "status": "up-to-date",
                     "update_time": 1713888672
                   }
                 ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/device/object"
             }
           ]
         }
         
How to get the list of FortiGuard objects downloaded by FortiManager?
---------------------------------------------------------------------

Goal is to produce the same listing as the one available in
FortiManager GUI  when visiting the *FortiGuard > Package Management >
Receive Status* page.

We need to use the following method and url:

+------------+-------------------------------+
| **Method** | ``get``                       |
+------------+-------------------------------+
| **URL**    | ``/um/object/list``           |
+------------+-------------------------------+

We need to specify the Fortinet product of interest by using the
``system`` attribute with one of the following values:

+-------------+-------------------+
| *Attribute* | *Product*         |
+=============+===================+
| ``FGT``     | ``FortiGate``     |
+-------------+-------------------+
| ``FML``     | ``FortiMail``     |
+-------------+-------------------+
| ``FAZ``     | ``FortiAnalyzer`` |
+-------------+-------------------+
| ``FWB``     | ``FortiWeb``      |
+-------------+-------------------+
| ``FCT``     | ``FortiClient``   |
+-------------+-------------------+

We also need to specify whether we want to get all objects related to
a product or only the used objects by setting the attribute
``used_only`` to ``0`` or ``1`` respectively.

The FortiManager JSON API request/response:

**REQUEST:**

.. code-block:: json

		{
		  "id": 1,
		  "jsonrpc": "1.0",
		  "method": "get",
		  "params": [
		    {
		      "data": {
		        "system": "FGT",
			"used_only": 0
		      },
		      "url": "/um/object/list"
		    }
		  ],
		  "session": "hdRJAukKyAHEw+I6bZcn0wxxeWWBYDSOU6kq2aYvMgWOQJMBvo+YwdRonWgie93RF/80VgAUcTMNp7nLPIO/FVOCg3J7QFF8",
		  "verbose": 1
		}

**RESPONSE:**

.. code-block:: json

		{
		  "id": 1,
		  "result": [
		    {
		      "data": {
		        "object_list": {
			  "05000000IPGE00000": {
			    "latest_verdate": "2002080500",
			    "latest_version": 131120,
			    "latest_versize": 1080752,
			    "obj_desc": "IP Geo DB",
			    "obj_used": 0,
			    "objid": "05000000IPGE00000",
			    "prefer_version": 0,
			    "version_list": {
			      "00002.00048": {
			        "date": "2002080500",
			        "size": 1080752,
			        "version": 131120
			      }
			    }
			  },
			  "05004000NIDS02200": {
			    "latest_verdate": "2003102346",
			    "latest_version": 983833,
			    "latest_versize": 369848,
			    "obj_desc": "IPS Meta-Data",
			    "obj_used": 0,
			    "objid": "05004000NIDS02200",
			    "prefer_version": 0,
			    "version_list": {
			      "00015.00793": {
			        "date": "2003102346",
			        "size": 369848,
			        "version": 983833
			      }
			    }
		          },
			  "05004000NIDS02300": {
		            "latest_verdate": "2003102346",
		            "latest_version": 983833,
		            "latest_versize": 78128,
		            "obj_desc": "AppCat Meta-Data",
		            "obj_used": 0,
			    "objid": "05004000NIDS02300",
			    "prefer_version": 0,
			    "version_list": {
			      "00015.00793": {
			        "date": "2003102346",
				"size": 78128,
				"version": 983833
			      }
			    }
			  }
			},
			"system": "FGT",
			"used_only": 0
		      },
		      "status": {
		        "code": 0, 
		        "message": "OK"
		      },
		      "url": "/um/object/list"
		    }
		  ]
    }

How to export/import FortiGuard objects?
----------------------------------------

Caught in #077802 (FortiManager 7.2.2).


Those export/import operations have been implemented to allow an air-gapped FortiManager to receive FortiGuard Updates in an automated manner.

For instance, it could be used in this quite common :bdg-link-primary-line:`data-diode <https://en.wikipedia.org/?title=Data_diode&redirect=no>` (OT environment) use case:

.. code-block:: text

   INTERNET + FMG1 + DEVOPS ---- [data-diode >>>] ---- FMG2 + managed devices

where:

- ``INTERNET`` is the Internet where are located the public FortiGuard servers
- ``FMG1`` is the FortiManager able to get FortiGuard objects from the Internet
- ``DEVOPS`` is an external system from where you can trigger some |fmg_api| 
  operations
- ``data-diode`` is a data-diode
 
  - In this exemple, traffic can only flow from left to right
- ``FMG2`` is the air-gapped FortiManager

  - It can't get get updates from the public FortiGuard servers
  - It is managing the FortiGate devices

In this use case, the ``DEVOPS`` system can:

- Use the |fmg_api| to export FortiGuard objects from ``FMG1``
- Use the |fmg_api| to import FortiGuard object to ``FMG2``

Traffic from ``DEVOPS`` to ``FMG2`` will be accepted by the ``data-diode`` since
going into the right direction; from left to right.

How to export a FortiGuard Object?
++++++++++++++++++++++++++++++++++

To export a FortiGuard object, you need to know its ``objid``.

This is what is showing up in the FortiManager GUI when you navigate to 
*FortiGuard* > *Package* > *Receive Status*: 

.. thumbnail:: images/image_005.png

.. note:: 
  
   - You can also obtain a list of available FortGuard objects via the |fmg_api|
     (see section :ref:`How to get the list of FortiGuard objects downloaded by FortiManager?`).

To export ``06002000NIDS02400`` (*Signature Meta Data (IPS Regular)*)
FortiGuard Object:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "category": {
                   "fds": {
                     "objid": [
                       "06002000NIDS02400"
                     ]
                   }
                 },
                 "flags": "base64"
               },
               "url": "/um/object/export"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - The ``objid`` attribute is a list; you could pass muliple FortiGuard 
           objects
         - The ``base64`` value for the ``flags`` attribute is required if you
           want to get the requested FortiGuard objects returned in base64 format in the API response.
         - If the ``flags`` attribute is omitted, FortiGuard objects will be 
           placed in the FortiManager filesystem (in folder 
           ``/var/tmp/um/export``)

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "category": {
                   "fds": {
                     "base64": "UFVURjA0MDAwMDAwAwAAAHiZEABAAAAAMj[...]",
                   }
                 },
                 "taskid": 58
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/object/export"
             }
           ]
         }  

      .. note::

         - The ``base64`` attribute contains all the requested FortiGuard 
           objects in base64 format

How to import a FortiGuard Object?
++++++++++++++++++++++++++++++++++

To import a FortiGuard object, you need to pass the base64 output you obtain at
the time your exported it (see section :ref:`How to export a FortiGuard
Object?`):

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "base64": "UFVURjA0MDAwMDAwAwAAAHiZEABAAAAAMj[...]",
               }
               },
               "url": "/um/object/import"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - The ``base64`` attribute is set with the base64 output of one or
           multiple FortiGuard objects

   .. tab-item:: RESPONSE

      .. code-block:: json         

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "taskid": 59
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/object/import"
             }
           ]
         }

.. hint::

   If you want to control the effectiveness of the import operation for the 
   FortiGuard Object with ``objid`` ``06002000NIDS02400``, you can perform
   the following operation:

   #. Check this FortiGuard object exists using FortiManager CLI
     
      Enter:
     
      .. code-block:: text
     
         diagnose fmupdate list-object fds 06002000/NIDS02400
     
      You should get this output:
     
      .. code-block:: text      
     
         06002000/NIDS02400
         06002000/NIDS02400/00026.00713-2401110136
     
   #. Export the FortiGuard object to save it in an external system
     
      See :ref:`how to export a fortiguard object?`
     
   #. Delete the FortiGuard object using FortiManager CLI
     
      Enter:
     
      .. code-block:: text

         fmupdate del-object fds 06002000/NIDS02400          
     
      You should get this output:
     
      .. code-block:: text
     
         06002000/NIDS02400
         06002000/NIDS02400/00026.00713-2401110136
           
         This operation will delete all fds 06002000/NIDS02400 objects.
         Do you want to continue? (y/n)

      Enter ``y`` then :bdg-primary-line:`ENTER` to confirm the delete 
      operation

   #. Check this FortiGuard object does no longer exist using FortiManager CLI
     
      Enter:
     
      .. code-block:: text
     
         diagnose fmupdate list-object fds 06002000/NIDS02400
     
      You should get this output:
     
      .. code-block:: text

         no object was found for service "fds" by type "06002000/NIDS02400".
         Command fail. Return code -9999

    #. Import the FortiGuard Object as described in this section

   #. Check this FortiGuard object is back using FortiManager CLI
     
      Enter:
     
      .. code-block:: text
     
         diagnose fmupdate list-object fds 06002000/NIDS02400
     
      You should get this output:
     
      .. code-block:: text

         06002000/NIDS02400
         06002000/NIDS02400/00026.00713-2401110136

How to export/import Entitlement?
---------------------------------

Caught in #0778029.

TBD.

External Resources
------------------

Starting with FortiManager 7.4.1 (#0934664), it is possible to manage
external resource files hosted by FortiManager.

How to add a new external resource file?
++++++++++++++++++++++++++++++++++++++++

Using |fmg_api| for adding a new external resource file
_______________________________________________________

To add a new external resource file named ``addresses_003.txt``:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "method": "set",
           "params": [
             {
               "url": "/pm/config/global/_external/resource/addresses_003.txt",
               "data": {
                 "content": "11.11.11.11\n11.11.11.22\n11.11.11.44\n"
               },
               "session": "{{session}}"
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
               "url": "/pm/config/global/_external/resource/addresses_003.txt"
             }
           ]
         }

Using REST API for adding a new external resource file
______________________________________________________

To add a new external resource file named ``addresses_004.txt``:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: shell

         curl -sk -u devops:fortinet -X PUT \
         https://10.210.35.112/jsonrpc/pm/config/global/_external/resource/addresses_004.txt \ 
         --data-binary @addresses_004.txt | jq

      .. note::
        
         File ``addresses_004.txt`` is with following content:
         
         .. code-block:: text
          
            10.0.0.1
            10.0.0.2
            10.0.0.3
            10.0.0.4
            10.0.0.5

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/global/_external/resource/addresses_004.txt"
             }
           ]
         }                    

How to delete an external resource file?
++++++++++++++++++++++++++++++++++++++++

Using |fmg_api| for deleting a new external resource file
_________________________________________________________

To delete the external resource file named ``addresses_003.txt``:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "method": "delete",
           "params": [
             {
               "url": "/pm/config/global/_external/resource/addresses_003.txt",
               "session": "{{session}}"
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
               "url": "/pm/config/global/_external/resource/addresses_003.txt"
             }
           ]
         }

Using REST API for deleting a new external resource file
________________________________________________________

To add a new external resource file named ``addresses_004.txt``:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: shell

         curl -sk -u devops:fortinet -X DELETE \
         https://10.210.35.112/jsonrpc/pm/config/global/_external/resource/addresses_004.txt \
         | jq

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/global/_external/resource/addresses_004.txt"
             }
           ]
         }        