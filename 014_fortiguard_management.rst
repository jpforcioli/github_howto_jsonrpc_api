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
   
How to get the FMG FortiGuard object versions?
----------------------------------------------

The below example has been collected by using the following FortiManager CLI:

.. code-block:: text

   diagnose fmupdate fgd-dvber

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
           "id": 3,
           "result": [
             {
               "data": {
                 "as1": {
                   "delta": 1,
                   "desc": "Antispam(IP)",
                   "size": 0,
                   "update_time": 0,
                   "version": 0
                 },
                 "as2": {
                   "delta": 1,
                   "desc": "Antispam(URI)",
                   "size": 0,
                   "update_time": 0,
                   "version": 0
                 },
                 "as4": {
                   "delta": 1,
                   "desc": "Antispam(HASH)",
                   "size": 0,
                   "update_time": 0,
                   "version": 0
                 },
                 "av": {
                   "delta": 1,
                   "desc": "AntiVirus Query",
                   "size": 0,
                   "update_time": 0,
                   "version": 0
                 },
                 "av2": {
                   "delta": 1,
                   "desc": "Outbreak Prevention",
                   "size": 2234602358,
                   "update_time": 1740748501,
                   "version": 1030686
                 },
                 "catl": {
                   "delta": 0,
                   "desc": "Query Category",
                   "size": 17368,
                   "update_time": 1710961260,
                   "version": 655360
                 },
                 "fq": {
                   "delta": 1,
                   "desc": "File Query",
                   "size": 4281787620,
                   "update_time": 1713868799,
                   "version": 10617241
                 },
                 "geoip": {
                   "delta": 0,
                   "desc": "GeoIP",
                   "size": 245852542,
                   "update_time": 1744736400,
                   "version": 131349
                 },
                 "iotm": {
                   "delta": 0,
                   "desc": "IoT(mapping)",
                   "size": 0,
                   "update_time": 0,
                   "version": 0
                 },
                 "iotr": {
                   "delta": 0,
                   "desc": "IoT(range)",
                   "size": 0,
                   "update_time": 0,
                   "version": 0
                 },
                 "iots": {
                   "delta": 1,
                   "desc": "IoT(single)",
                   "size": 0,
                   "update_time": 0,
                   "version": 0
                 },
                 "wf": {
                   "delta": 1,
                   "desc": "Webfilter",
                   "size": 13765660808,
                   "update_time": 1739874023,
                   "version": 15355124
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

      .. note::

         If you look at the ``wf`` (webfilter) block, the ``version`` returned
         is ``15355124``. However, running the FortiManager CLI command 
         ``execute fmupdate fgd-dvber wf`` will show the version in a symbolic
         major.minor format (``00234.19700``) as illustrated below:

         .. code-block:: text

            Category   Description         Version        Date/Time                  Size
            --------   -----------         -------        ---------                  ----
            wf         Webfilter           00234.19700    2025-02-18 11:20:23(CET)   12.82G


         In this output, the version is represented in major.minor format where:
         
         - major = ``234``
         - minor = ``19700``
       
         To convert the numeric ``version`` from the API to the symbolic format,
         use the following formula:

         .. code-block:: text

            major = version / 65535
            minor = version % 65535

         For example, using the returned version ``15355124`` from the
         API:

         .. code-block:: text
  
            major = 15355124 / 65535 = 234
            minor = 15355124 % 65535 = 19700

         Thus, the symbolic version is ``00234.19700`` matching what is shown in
         the FortiManager CLI.

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

.. dropdown:: Click here to interpret a different but similar output
   :icon: book
   :color: warning

   If you look carefuly at the end of the response you're getting this:
   
   .. code-block:: json
   
      "support_level_desc": "05:Advanced HW*06:Web/Online*10:8x5*20:Premium*55:Premium service*99:Trial",
   
   If you decompose the string value for the ``support_level_desc``, it reads 
   as follows:
   
   - ``05: Advanced HW``
   - ``06: Web Online``
   - ``10: 8x5``
   - ``20: Premium``
   - ``55: Premium service``
   - ``99: Trial``
  
   So ``99`` seems to be for *Trial*, for instance.
   
   Now, if you look at the output for the ``FTSV04REDACTED5719`` device:
   
   .. code-block:: json
   
      {
        "account": "foo@bar.com",
        "address": "10.150.10.160",
        "company": "Fortinet UK Limited",
        "contract_item": [
          "ATTC-1-06-20241102:0:1:1:0",
          "AVDB-1-99-20231027:0:1:1:0",
          "AVEN-1-99-20231027:0:1:1:0",
          "COMP-1-20-20241102:0:1:1:0",
          "ENHN-1-20-20241102:0:1:1:0",
          "FMWR-1-06-20241102:0:1:1:0",
          "FRVS-1-06-20241102:0:1:1:0",
          "FTMS-1-06-20241102:0:1:1:0",
          "FTSS-1-55-20241102:0:1:1:0",
          "NIDS-1-99-20231027:0:1:1:0",
          "SPRT-1-20-20241102:0:1:1:0"
        ],
        "industry": "Technology",
        "rawdata": "Contract=ATTC-1-06-20241102:0:1:1:0*AVDB-1-99-20231027:0:1:1:0*AVEN-1-99-20231027:0:1:1:0*COMP-1-20-20241102:0:1:1:0*ENHN-1-20-20241102:0:1:1:0*FMWR-1-06-20241102:0:1:1:0*FRVS-1-06-20241102:0:1:1:0*FTMS-1-06-20241102:0:1:1:0*FTSS-1-55-20241102:0:1:1:0*NIDS-1-99-20231027:0:1:1:0*SPRT-1-20-20241102:0:1:1:0|AccountID=foo@bar.com|Industry=Technology|Company=Fortinet UK Limited|UserID=123456",
        "serial": "FTSV04REDACTED19"
      }

   You could replace it like this:
   
   .. code-block:: json
   
      {
        "account": "foo@com.com",
        "address": "10.150.10.160",
        "company": "Fortinet UK Limited",
        "contract_item": [
          "ATTC-1-[Web Online]-20241102:0:1:1:0",
          "AVDB-1-[Trial]-20231027:0:1:1:0",
          "AVEN-1-[Trial]-20231027:0:1:1:0",
          "COMP-1-[Premium]-20241102:0:1:1:0",
          "ENHN-1-[Premium]-20241102:0:1:1:0",
          "FMWR-1-[Web Online]-20241102:0:1:1:0",
          "FRVS-1-[Web Online]-20241102:0:1:1:0",
          "FTMS-1-[Web Online]-20241102:0:1:1:0",
          "FTSS-1-[Premium service]-20241102:0:1:1:0",
          "NIDS-1-[Trial]-20231027:0:1:1:0",
          "SPRT-1-[Premium]-20241102:0:1:1:0"
        ],
        "industry": "Technology",
        "rawdata": "Contract=ATTC-1-06-20241102:0:1:1:0*AVDB-1-99-20231027:0:1:1:0*AVEN-1-99-20231027:0:1:1:0*COMP-1-20-20241102:0:1:1:0*ENHN-1-20-20241102:0:1:1:0*FMWR-1-06-20241102:0:1:1:0*FRVS-1-06-20241102:0:1:1:0*FTMS-1-06-20241102:0:1:1:0*FTSS-1-55-20241102:0:1:1:0*NIDS-1-99-20231027:0:1:1:0*SPRT-1-20-20241102:0:1:1:0|AccountID=foo@bar.com|Industry=Technology|Company=Fortinet UK Limited|UserID=123456",
        "serial": "FTSV04REDACTED19"
      }
   
   As you can observe from this output, you should have three expired trial for 
   this device:
   
   - ``"AVDB-1-[Trial]-20231027:0:1:1:0"``
   - ``"AVEN-1-[Trial]-20231027:0:1:1:0"``
   - ``"NIDS-1-[Trial]-20231027:0:1:1:0"``
   
   It's easy to decode the expiry date: *October, 27th 2023*.
   
   And by the way, you can decode the 4-letter codes (for instance ``ATTC`` or 
   ``AVDB``) using the string values returned by the ``support_type_desc``
   attribute.
   
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
         
How to get the license status for managed devices?
--------------------------------------------------

This is more or less what you're trying to achieve in :ref:`How to get 
contracts for managed devices?` or in :ref:`How to get the package versions for 
your managed devices?` by using data collected by the FortiManager.

However, it doesn't seem to giver you the full list of contracts, packages name 
and versions.

The following example is getting the license status from the managed devices 
themselves:

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
                 "resource": "/api/v2/monitor/license/status",
                 "target": [
                   "adom/demo/group/All_FortiGate"
                 ]
               },
               "url": "sys/proxy/json"
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
                     "build": 2571,
                     "http_method": "GET",
                     "name": "status",
                     "path": "license",
                     "results": {
                       "ai_malware_detection": {
                         "entitlement": "AVDB",
                         "expires": 1731283200,
                         "last_update": 978303600,
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "0.00000"
                       },
                       "antispam": {
                         "entitlement": "SPAM",
                         "expires": 1731283200,
                         "status": "licensed",
                         "type": "live_fortiguard_service"
                       },
                       "antivirus": {
                         "db_status": "db_type_extended",
                         "engine": {
                           "last_update": 1698359340,
                           "version": "7.00021"
                         },
                         "entitlement": "AVDB",
                         "expires": 1731283200,
                         "last_update": 1523293620,
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "1.00000"
                       },
                       "appctrl": {
                         "entitlement": "FMWR",
                         "expires": 1731283200,
                         "last_update": 1448933400,
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "6.00741"
                       },
                       "blacklisted_certificates": {
                         "entitlement": "FURL",
                         "expires": 1731283200,
                         "last_update": 1713819991,
                         "last_update_attempt": 1714168271,
                         "last_update_method_status": "update_method_sched",
                         "last_update_result_status": "update_result_no_updates",
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "1.00477"
                       },
                       "botnet_domain": {
                         "entitlement": "AVDB",
                         "expires": 1731283200,
                         "last_update": 1714157471,
                         "last_update_attempt": 1714168271,
                         "last_update_method_status": "update_method_sched",
                         "last_update_result_status": "update_result_no_updates",
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "3.00752"
                       },
                       "botnet_ip": {
                         "last_update": 1714164158,
                         "last_update_attempt": 1714168271,
                         "last_update_method_status": "update_method_sched",
                         "last_update_result_status": "update_result_no_updates",
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "7.03667"
                       },
                       "data_leak_prevention": {
                         "entitlement": "DLDB",
                         "last_update": 978303600,
                         "last_update_attempt": 1714168271,
                         "last_update_method_status": "update_method_manual",
                         "last_update_result_status": "update_result_not_authorized",
                         "status": "no_license",
                         "type": "downloaded_fds_object",
                         "version": "0.00000"
                       },
                       "device_os_id": {
                         "entitlement": "FMWR",
                         "expires": 1731283200,
                         "last_update": 1714063871,
                         "last_update_attempt": 1714168271,
                         "last_update_method_status": "update_method_sched",
                         "last_update_result_status": "update_result_no_updates",
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "1.00167"
                       },
                       "firmware_updates": {
                         "entitlement": "FMWR",
                         "expires": 1731283200,
                         "status": "licensed",
                         "type": "live_fortiguard_service"
                       },
                       "fortianalyzer_cloud": {
                         "entitlement": "FAZC",
                         "expires": 1731283200,
                         "status": "licensed",
                         "type": "live_cloud_service"
                       },
                       "fortianalyzer_cloud_premium": {
                         "entitlement": "AFAC",
                         "status": "no_license",
                         "type": "live_cloud_service"
                       },
                       "forticare": {
                         "account": "foo@bar.com",
                         "company": "Fortinet",
                         "industry": "Technology",
                         "registration_status": "registered",
                         "registration_supported": true,
                         "status": "registered",
                         "support": {
                           "enhanced": {
                             "expires": 1731283200,
                             "status": "licensed",
                             "support_level": "Premium"
                           }
                         },
                         "type": "cloud_service_status"
                       },
                       "forticloud": {
                         "status": "cloud_logged_out",
                         "type": "cloud_service_status"
                       },
                       "forticloud_logging": {
                         "log_retention_days": 7,
                         "max_bytes": 0,
                         "status": "free_license",
                         "type": "live_cloud_service",
                         "used_bytes": 0
                       },
                       "forticloud_sandbox": {
                         "entitlement": "AVDB",
                         "expires": 1731283200,
                         "files_uploaded_daily": 0,
                         "max_files_daily": 100,
                         "status": "licensed",
                         "type": "live_cloud_service"
                       },
                       "forticonverter": {
                         "entitlement": "FCSS",
                         "expires": 1731283200,
                         "status": "licensed",
                         "type": "live_cloud_service"
                       },
                       "fortiems_cloud": {
                         "entitlement": "FCEM",
                         "expires": 1736899200,
                         "status": "licensed",
                         "type": "account_level_live_cloud_service"
                       },
                       "fortiguard": {
                         "connected": true,
                         "connection_issue": false,
                         "fortigate_wan_ip": "34.140.239.116",
                         "has_connected": true,
                         "last_connection_success": 1714168271,
                         "next_scheduled_update": 1714169160,
                         "scheduled_updates_enabled": true,
                         "server_address": "173.243.141.6:443",
                         "supported": true,
                         "type": "cloud_service_status",
                         "update_server_usa": true
                       },
                       "fortiguard_ai_based_sandbox": {
                         "entitlement": "FAIS",
                         "status": "no_license",
                         "type": "live_cloud_service"
                       },
                       "fortimanager_cloud": {
                         "entitlement": "FMGC",
                         "expires": 1731283200,
                         "status": "licensed",
                         "type": "live_cloud_service"
                       },
                       "fortimanager_cloud_alci": {
                         "entitlement": "FMGC",
                         "expires": 1700697600,
                         "status": "expired",
                         "type": "account_level_live_cloud_service"
                       },
                       "fortisandbox_cloud": {
                         "entitlement": "FSAC",
                         "status": "no_license",
                         "type": "live_cloud_service"
                       },
                       "fortisandbox_cloud_alci": {
                         "entitlement": "FSAP",
                         "status": "no_license",
                         "type": "account_level_live_cloud_service"
                       },
                       "fortisase_lan_extension": {
                         "entitlement": "FSFG",
                         "status": "no_license",
                         "type": "live_cloud_service"
                       },
                       "fortisase_private_access": {
                         "entitlement": "FSPA",
                         "status": "no_license",
                         "type": "live_cloud_service"
                       },
                       "icdb": {
                         "entitlement": "FMWR",
                         "expires": 1731283200,
                         "last_update": 1713806476,
                         "last_update_attempt": 1714168271,
                         "last_update_method_status": "update_method_sched",
                         "last_update_result_status": "update_result_no_updates",
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "1.00043"
                       },
                       "industrial_db": {
                         "entitlement": "ISSS",
                         "expires": 1731283200,
                         "last_update": 1448933400,
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "6.00741"
                       },
                       "inline_casb": {
                         "entitlement": "FMWR",
                         "expires": 1731283200,
                         "last_update": 1712184731,
                         "last_update_attempt": 1714168271,
                         "last_update_method_status": "update_method_sched",
                         "last_update_result_status": "update_result_no_updates",
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "1.00005"
                       },
                       "internet_service_db": {
                         "last_update": 1714164158,
                         "last_update_attempt": 1714168271,
                         "last_update_method_status": "update_method_sched",
                         "last_update_result_status": "update_result_no_updates",
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "7.03667"
                       },
                       "iot_detection": {
                         "definitions": {
                           "entitlement": "IOTH",
                           "expires": 1731283200,
                           "last_update": 1660753860,
                           "status": "licensed",
                           "type": "downloaded_fds_object",
                           "version": "0.00000"
                         },
                         "entitlement": "IOTH",
                         "expires": 1731283200,
                         "status": "licensed",
                         "type": "live_fortiguard_service"
                       },
                       "ips": {
                         "db_status": "db_type_extended",
                         "engine": {
                           "last_update": 1701106200,
                           "version": "7.00524"
                         },
                         "entitlement": "NIDS",
                         "expires": 1731283200,
                         "last_update": 1448933400,
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "6.00741"
                       },
                       "local_in_virtual_patching": {
                         "entitlement": "FMWR",
                         "expires": 1731283200,
                         "last_update": 1713889272,
                         "last_update_attempt": 1714168271,
                         "last_update_method_status": "update_method_sched",
                         "last_update_result_status": "update_result_no_updates",
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "24.00040"
                       },
                       "malicious_urls": {
                         "entitlement": "NIDS",
                         "expires": 1731283200,
                         "last_update": 1420070460,
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "1.00001"
                       },
                       "mobile_malware": {
                         "entitlement": "AVDB",
                         "expires": 1731283200,
                         "last_update": 978303600,
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "0.00000"
                       },
                       "ot_detection": {
                         "detect_definitions": {
                           "entitlement": "ISSS",
                           "expires": 1731283200,
                           "last_update": 978303600,
                           "status": "licensed",
                           "type": "downloaded_fds_object",
                           "version": "0.00000"
                         },
                         "entitlement": "IOTH",
                         "expires": 1731283200,
                         "patch_definitions": {
                           "entitlement": "ISSS",
                           "expires": 1731283200,
                           "last_update": 978303600,
                           "status": "licensed",
                           "type": "downloaded_fds_object",
                           "version": "0.00000"
                         },
                         "status": "licensed",
                         "type": "live_fortiguard_service"
                       },
                       "outbreak_prevention": {
                         "entitlement": "ZHVO",
                         "expires": 1731283200,
                         "status": "licensed",
                         "type": "live_fortiguard_service"
                       },
                       "outbreak_security_rating": {
                         "entitlement": "FMWR",
                         "expires": 1731283200,
                         "last_update": 1710249207,
                         "last_update_attempt": 1714168271,
                         "last_update_method_status": "update_method_sched",
                         "last_update_result_status": "update_result_no_updates",
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "5.00032"
                       },
                       "psirt_security_rating": {
                         "entitlement": "FMWR",
                         "expires": 1731283200,
                         "last_update": 1710249207,
                         "last_update_attempt": 1714168271,
                         "last_update_method_status": "update_method_sched",
                         "last_update_result_status": "update_result_no_updates",
                         "status": "licensed",
                         "type": "downloaded_fds_object",
                         "version": "5.00032"
                       },
                       "sdwan_network_monitor": {
                         "entitlement": "SWNM",
                         "expires": 1731283200,
                         "status": "licensed",
                         "type": "live_fortiguard_service"
                       },
                       "sdwan_overlay_aas": {
                         "entitlement": "SWOS",
                         "status": "no_license",
                         "type": "live_cloud_service"
                       },
                       "security_rating": {
                         "entitlement": "FGSA",
                         "expires": 1731283200,
                         "status": "licensed",
                         "type": "functionality_enabling"
                       },
                       "sms": {
                         "max": 0,
                         "status": "no_license",
                         "type": "other",
                         "used": 0
                       },
                       "vdom": {
                         "can_upgrade": true,
                         "max": 10,
                         "type": "platform",
                         "used": 1
                       },
                       "vm": {
                         "closed_network": false,
                         "cpu_max": 1,
                         "cpu_used": 1,
                         "expires": 1731106800,
                         "is_payg": false,
                         "license_from_forticare": true,
                         "license_model": 6,
                         "license_platform_name": "FGVM01",
                         "mem_used": 2089811968,
                         "status": "vm_valid",
                         "type": "platform",
                         "valid": true
                       },
                       "web_filtering": {
                         "category_list_version": 10,
                         "entitlement": "FURL",
                         "expires": 1731283200,
                         "running": false,
                         "status": "licensed",
                         "type": "live_fortiguard_service"
                       }
                     },
                     "serial": "FG421F0000000001",
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
               "url": "sys/proxy/json"
             }
           ]
         }

      .. note::

         - The special ``All_FortiGate`` device group is for all managed devices
           from the specified ADOM

         - Above output is for one managed device; it means the ``demo`` ADOM 
           was having only one managed device at the time this request was made

How to get the update history for a specific FortiGuard objects?
----------------------------------------------------------------

The update history gives you how many time and which database versions a
FortiGuard object has been downloaded by FortiManager.

Using FortiManager GUI, this is when you're in the ***FortiGuard*** >
***Packages*** page and you click the ***Update History*** cell:

.. thumbnail:: images/fortiguard_management/image_001.png

In this case, you get this:

.. thumbnail:: images/fortiguard_management/image_002.png

The following shows the corresponding API request:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "data": {
                 "category": {
                   "fds": {
                     "objid": [
                       "05000000FAPV00000"
                     ]
                   }
                 }
               },
               "url": "/um/misc/update_history"
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
               "data": {
                 "fds": {
                   "05000000FAPV00000": {
                     "history": [
                       {
                         "event": "PollUpdate",
                         "size": 19432,
                         "status": "Success",
                         "update_time": 1742982143,
                         "version": 131177
                       }
                     ]
                   }
                 }
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/misc/update_history"
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

Local External Resources
------------------------

Starting with FortiManager 7.4.1 and 7.2.5 (#0934664), it is possible to manage
external resource files hosted by FortiManager.

.. note::

   The following ``url`` is used in this section:
   
   .. code-block::
   
      /pm/config/global/_external/resource
   
   
   This refers to the *Global ADOM* for convenience. Alternatively, you can use:
   
   .. code-block::
   
      /pm/config/adom/<adom>/_external/resource
   
   Both forms yield the same result. External resource files are accessible to 
   all ADOMs.

How to add a local external resource file?
++++++++++++++++++++++++++++++++++++++++++

Using |fmg_api| for adding a local external resource file
_________________________________________________________

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

Using REST API for adding a local external resource file
________________________________________________________

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

How to get the list of local external resource files?
+++++++++++++++++++++++++++++++++++++++++++++++++++++

Caught in #0953203 (7.2.5/7.4.2).

The following example shows how to get the list of external resource files:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "pm/config/global/_external/resource"
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
                   "modified": 1739378022,
                   "name": "file_001.txt",
                   "size": 601428
                 },
                 {
                   "modified": 1738768252,
                   "name": "file_002.txt",
                   "size": 55
                 },
                 {
                   "modified": 1739950759,
                   "name": "file_003.txt",
                   "size": 64
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "pm/config/global/_external/resource"
             }
           ]
         }

      .. note:

         For performance reason, the file content isn't returned. Some of the
         files could be large.

How to get a local external resource file content?
++++++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to retrieve the content of the ``file_001.txt``
external resource file:

.. tab-set::
   
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "pm/config/global/_external/resource/file_001.txt"
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
               "data": {
                 "content": "38.180.91.21\n45.8.146.229\n45.83.140.121\n45.89.53.41\n86.104.72.41",
                 "modified": 1739950759,
                 "name": "file_001.txt",
                 "size": 64
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "pm/config/global/_external/resource/file_001.txt"
             }
           ]
         }         

How to delete a local external resource file?
+++++++++++++++++++++++++++++++++++++++++++++

Using |fmg_api| for deleting a local external resource file
___________________________________________________________

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

Using REST API for deleting a local external resource file
__________________________________________________________

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

Remote External Resources
-------------------------

Starting in version 7.6.3 (#1039834), FortiManager supports downloading external
resources from a web server.

Once downloaded by FortiManager, the file becomes a :ref:`local external resource <Local External Resources>`.

How to add a remote external resource?
++++++++++++++++++++++++++++++++++++++

The following example shows how to add a remote external resource file named
`remote_external_resource_001`:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "http_auth": 0,
                 "name": "remote_external_resource_001",
                 "refresh_rate": 5,
                 "status": 1,
                 "url": "http://www.url-001.com/filename_001.txt",
                 "use_web_proxy": 0
               },
               "url": "/um/external_resource"
             }
           ],
           "session": "{{session}}",
         }

      .. note::

         - ``http_auth: 0``: No authentication is required to access the URL.
         - ``refresh_rate: 5``: FortiManager will check the URL and refresh the
           file every 5 minutes.
         - ``use_web_proxy: 0``: FortiManager will access the URL directly,
           without using a proxy.

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
               "url": "/um/external_resource"
             }
           ]
         }

How to get the existing remote external resources?
++++++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to get the list of existing remote external
resources:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/um/external_resource"
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
               "data": {
                 "object_list": [
                   {
                     "comment": "",
                     "filename": "filename_001.txt",
                     "http_auth": 0,
                     "http_auth_password": "ENC [TRUNCATED]",
                     "http_auth_username": "",
                     "name": "remote_external_resource_001",
                     "refresh_rate": 5,
                     "status": 1,
                     "type": 0,
                     "url": "http://www.url-001.com/filename_001.txt",
                     "use_web_proxy": 0
                   },
                   {
                     "comment": "",
                     "filename": "filename_002.txt",
                     "http_auth": 0,
                     "http_auth_password": "ENC [TRUNCATED]",
                     "http_auth_username": "",
                     "name": "remote_external_resource_002",
                     "refresh_rate": 5,
                     "status": 1,
                     "type": 0,
                     "url": "https://www.url-002.com/filename_002.txt",
                     "use_web_proxy": 0
                   }
                 ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/external_resource"
             }
           ]
         }

How to delete a remote external resource?
+++++++++++++++++++++++++++++++++++++++++

The following example shows how to delete the
``remote_external_resource_001``:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "delete",
           "params": [
             {
               "data": {
                 "name": "foobar"
               },
               "url": "/um/external_resource"
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
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/external_resource"
             }
           ]
         }

How to check for an external resource?
++++++++++++++++++++++++++++++++++++++

Caught in #1140702.

The capability of FortiManager to fetch a remote external resource can be validated using the FortiManager API to check the corresponding URL.

The example below describes how to check for an URL prior to set it in a remote
external resource:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "opt": "check_url",
                 "url": "http:/www.url-003.com"
               },
               "url": "/um/external_resource"
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
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/external_resource"
             }
           ]
         }

      This output indicates that the ``http://www.url-003.com`` is valid.
      An invalid URL would produce the following output:

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "status": {
                 "code": -6,
                 "message": "Invalid url"
               },
               "url": "/um/external_resource"
             }
           ]
         }        


