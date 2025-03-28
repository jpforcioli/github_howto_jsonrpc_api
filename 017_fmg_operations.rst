FortiManager operations
=======================

FortiManager Certificates
-------------------------

How to get FortiManager certificates?
+++++++++++++++++++++++++++++++++++++

You can get any of the following FMG API endpoints:

.. code-block:: text

   /cli/global/system/certificate/ca
   /cli/global/system/certificate/local
   /cli/global/system/certificate/crl
   /cli/global/system/certificate/remote

The following example shows how to get the ``Fortinet_CA`` CA certificate:

.. tab-set::
   
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/cli/global/system/certificate/ca/Fortinet_CA"
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
                 "ca": [
                   "\"-----BEGIN CERTIFICATE-----\nMIIKLDCCBhSgAwIBAgIBADANBgkqhkiG9w0BAQsFADCBpTELMAkGA1UEBhMCVVMx\nEzARBgNVBAgTCkNhbGlmb3JuaWExEjAQBgNVBAcTCVN1bm55dmFsZTERMA8GA1UE\nChMIRm9ydGluZXQxHjAcBgNVBAsTFUNlcnRpZmljYXRlIEF1dGhvcml0eTEVMBMG\nA1UEAxMMZm9ydGluZXQtY2EyMSMwIQYJKoZIhvcNAQkBFhRzdXBwb3J0QGZvcnRp\nbmV0LmNvbTAgFw0xNjA2MDYyMDI3MzlaGA8yMDU2MDUyNzIwMjczOVowgaUxCzAJ\nBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRIwEAYDVQQHEwlTdW5ueXZh\nbGUxETAPBgNVBAoTCEZvcnRpbmV0MR4wHAYDVQQLExVDZXJ0aWZpY2F0ZSBBdXRo\nb3JpdHkxFTATBgNVBAMTDGZvcnRpbmV0LWNhMjEjMCEGCSqGSIb3DQEJARYUc3Vw\ncG9ydEBmb3J0aW5ldC5jb20wggQiMA0GCSqGSIb3DQEBAQUAA4IEDwAwggQKAoIE\nAQC9YkiEs7iwMQVeJuZyV5hYi8RGwE5N8X8I8jLo1BI/r/HD/RbbtmPBkyWVgPpa\nRQnAgnupxy06qJcWNrinZBxZyqKJrqke2RIBstV3lfoevSP7pmjF2raDZqL7EaDG\nkvRzaLyei5pifzcBzpoY8TpBk6upDD2pjkU60MqgWY/0Eo7SsiTKAukWvEqK3mL0\nK05+UNcEYzboWi0tIMBgXIYgIDDmYvOqUbDnPFYRTZQ6eltSFWrU+TvR4wEhBcwg\nDxlFQHY02Ee9UxEav4Ej02KzdjDKq3ZKMHaczGLiam4N/5TwtLG5+7il2TZ309Uf\n4Tjr5aWvEKMvHNTI4/hLDd+DsUs43qf0yD8HQ4kzpkyEEzdfXxPjbt6UNX7Dlz2T\nDQXvcqESs27kRxcEQ3gmVeL3cyDC4R4G3DhyBQQxNi22rROOX5DRMNC0TIrLslld\nRBMZfDbSUOrLZobfuOE4bMDHGz7pzJWxqkfBI/GoO9G4ZMFxC5JYr2/3lzod5K4P\nlGRyWUJ9vax2JIeF5DM/UgfBdqhZetTXLKnKCOxT85cseAeYT335vlHNo/YVnYg5\nLFfCpqAJMJYjFz9EG6oOBXeT34GHwtXOxpaib1uYqM6REzhiqSRLvwYdlQtXM7Tn\n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\nx+nkkKoLQHPUczTwYRxQUQ==\n-----END CERTIFICATE-----\""
                 ],
                 "comment": "Default CA certificate",
                 "name": "Fortinet_CA"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/cli/global/system/certificate/ca/Fortinet_CA"
             }
           ]
         }

How to get FortiManager certificates in a human-readable form?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Caught in #1031557.

You can use the ``get certinfo`` option.

The following example shows how to get the ``Fortinet_CA`` CA certificate in a human-readable form:

.. tab-set::
   
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "option": [
                 "get certinfo"
               ],
               "url": "/cli/global/system/certificate/ca/Fortinet_CA"
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
                 "ca": {
                   "Extension": [
                     {
                       "Content": "A3:31:AF:A3:48:EE:A1:E2:5F:B1:F2:FD:D6:FB:41:48:50:1B:3A:75",
                       "Critical": "no",
                       "Name": "X509v3 Subject Key Identifier"
                     },
                     {
                       "Content": "A3:31:AF:A3:48:EE:A1:E2:5F:B1:F2:FD:D6:FB:41:48:50:1B:3A:75",
                       "Critical": "no",
                       "Name": "X509v3 Authority Key Identifier"
                     },
                     {
                       "Content": "CA:TRUE",
                       "Critical": "yes",
                       "Name": "X509v3 Basic Constraints"
                     },
                     {
                       "Content": "Digital Signature, Certificate Sign, CRL Sign",
                       "Critical": "yes",
                       "Name": "X509v3 Key Usage"
                     }
                   ],
                   "Fingerprint": "86:40:5C:F4:C2:A6:0B:96:82:9E:5F:E7:4F:D9:51:22",
                   "Issuer": "C = US, ST = California, L = Sunnyvale, O = Fortinet, OU = Certificate Authority, CN = fortinet-ca2, emailAddress = support@fortinet.com",
                   "Root CA": "Yes",
                   "SN": "00 ",
                   "Status": 0,
                   "Subject": "C = US, ST = California, L = Sunnyvale, O = Fortinet, OU = Certificate Authority, CN = fortinet-ca2, emailAddress = support@fortinet.com",
                   "Valid from": "2016-06-06 20:27:39  GMT",
                   "Valid to": "2056-05-27 20:27:39  GMT",
                   "Version": 3
                 },
                 "comment": "Default CA certificate",
                 "name": "Fortinet_CA"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/cli/global/system/certificate/ca/Fortinet_CA"
             }
           ]
         }

How to get the FortiManager System HA Status?
---------------------------------------------

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/sys/ha/status"
       }
     ],
     "session": "xe7wJZJrY2y5/KT4jZk+GNh2bUbF/VUbK3GV2gjxbuM+O55HbJCY9Z35HakLnQywuzvGGeWVfO7nUD5lGmJEpXjFcvH5+XV7",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json
  
   {
     "id": 3,
     "result": [
       {
         "data": {
           "Average Idle CPU": "95.31",
           "Average Memory Usage": "57.15",
           "Average Nice CPU": "0.00",
           "Average System CPU": "1.84",
           "Average User CPU": "2.80",
           "Cluster-ID": 1,
           "Debug": "off",
           "FMG-HA Status": "Synchronized State",
           "File-Quota": 4096,
           "HA Health Status": "OK",
           "HA Primary Uptime": "Mon Jul  4 13:34:01 2022",
           "HA Primary state change timestamp": "Mon Jul  4 13:34:18 2022",
           "HA Role": "Primary",
           "HB-Interval": 10,
           "HB-Lost-Threshold": 30,
           "Model": "FortiManager-VM64",
           "Primary": "fmg-connectors-primary, FMG-VMTM22005246, 10.210.34.230",
           "members": [
             {
               "Average Idle CPU": "99.39",
               "Average Memory Usage": "37.76",
               "Average Nice CPU": "0.00",
               "Average System CPU": "0.36",
               "Average User CPU": "0.15",
               "Estimated Sync Time Left (seconds)": 0,
               "HA Sync status": "up,in-sync",
               "Hostname": "FMG-VM64",
               "IP": "10.210.34.236",
               "Last Error": "",
               "Last Heartbeat (seconds)": 8,
               "Last Sync (seconds)": 30007,
               "Pending Synced Data (bytes)": "0",
               "Serial Number": "FMG-VMTM22005248",
               "Total Synced Data (bytes)": "6670248"
             }
           ]
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/sys/ha/status"
       }
     ]
   }

How to get the FortiManager *get system status*?
------------------------------------------------

Output will give you important info like the FMG firmware version FMG.

**REQUEST:**

.. code-block:: json

		{
		  "id": 1,
		  "jsonrpc": "1.0",
		  "method": "get",
		  "params": [
		    {
		      "url": "/cli/global/system/status"
		    }
		  ],
		  "session": "Iq63nDbtYQB3CrRUbSQDKAW20nervesJG2idL0Buyn0DFHYy9aISECEONR/lYfkYAq6SD+ZonSP0BZ1yRypOVA==",
		  "verbose": 1
		}

**RESPONSE:**

.. code-block:: json

		{
		  "id": 1,
		  "result": [
		    {
		      "data": {
		        "Admin Domain Configuration": "Enabled",
		        "BIOS version": "04000002",
		        "Branch Point": "1954",
		        "Build": "1954",
		        "Current Time": "Tue Feb 11 07:22:50 CET 2020",
		        "Daylight Time Saving": "Yes",
		        "FIPS Mode": "Disabled",
		        "HA Mode": "Stand Alone",
		        "Hostname": "FMG-6.4.X-INTERIM",
		        "License Status": "Valid",
		        "Major": 6,
		        "Max Number of Admin Domains": 10000,
		        "Max Number of Device Groups": 10000,
		        "Minor": 4,
		        "Offline Mode": "Disabled",
		        "Patch": 0,
		        "Platform Full Name": "FortiManager-VM64-KVM",
		        "Platform Type": "FMG-VM64-KVM",
		        "Release Version Information": " (Interim)",
		        "Serial Number": "FMG-VMTM20000078",
		        "Time Zone": "(GMT+1:00) Brussels, Copenhagen, Madrid, Paris.",
		        "Version": "v6.4.0-build1954 200206 (Interim)",
		        "x86-64 Applications": "Yes"
  		    },
		      "status": {
  		      "code": 0,
		        "message": "OK"
		      },
		      "url": "/cli/global/system/status"
		    }
		  ]
    }

How to get the FortiManager license?
------------------------------------

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
               "url": "/um/license/self"
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
                 "contract": [
                   {
                     "account": "foo@bar.com",
                     "company": "Fortinet",
                     "contract_item": [
                       "ADOM-1-06-20260525:0:5000:5000:0",
                       "AVDB-1-99-20221001:0:1:1:0",
                       "AVEN-1-99-20221001:0:1:1:0",
                       "COMP-1-20-20260525:0:1:1:0",
                       "ENHN-1-20-20260525:0:1:1:0",
                       "FMWR-1-06-20260525:0:1:1:0",
                       "FRVS-1-06-20260525:0:1:1:0",
                       "NIDS-1-99-20221001:0:1:1:0",
                       "SPRT-1-20-20260525:0:1:1:0",
                       "VMLS-1-06-20260525:0:5000:5000:0"
                     ],
                     "industry": "Technology",
                     "rawdata": "Contract=ADOM-1-06-20260525:0:5000:5000:0*AVDB-1-99-20221001:0:1:1:0*AVEN-1-99-20221001:0:1:1:0*COMP-1-20-20260525:0:1:1:0*ENHN-1-20-20260525:0:1:1:0*FMWR-1-06-20260525:0:1:1:0*FRVS-1-06-20260525:0:1:1:0*NIDS-1-99-20221001:0:1:1:0*SPRT-1-20-20260525:0:1:1:0*VMLS-1-06-20260525:0:5000:5000:0|AccountID=foo@bar.com|Industry=Technology|Company=Fortinet|UserID=106728",
                     "serial": "FMVMMLREDACTED79"
                   }
                 ],
                 "count": 1
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/um/license/self"
             }
           ]
         }    

RBAC
----

External Authentication Servers
+++++++++++++++++++++++++++++++

How to create a TACACS+ server?
________________________________

To create the ``tacacs_001`` TACACS+ server:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 2,
           "method": "set",
           "params": [
             {
               "data": {
                 "authen-type": "auto",
                 "authorization": "enable",
                 "key": "nsefortinet",
                 "name": "tacacs+_001",
                 "port": 49,
                 "server": "172.16.31.6"
               },
               "url": "/cli/global/system/admin/tacacs"
             }
           ],
           "session": "{{session}}"
         }        

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 2,
           "result": [
             {
               "data": {
                 "name": "tacacs+_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/cli/global/system/admin/tacacs"
             }
           ]
         }           

How to delete a TACACS+ server?
________________________________

To delete the ``tacacs_001`` TACACS+ server:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 2,
           "method": "delete",
           "params": [
             {
               "url": "/cli/global/system/admin/tacacs/tacacs+_001"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 2,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/cli/global/system/admin/tacacs/tacacs+_001"
             }
           ]
         }

Session Management
++++++++++++++++++

How to get user session information?
____________________________________

Has been added in FMG 6.4.1 with #0632548.

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "get",
           "params": [
             {
               "url": "/sys/session"
             }
           ],
           "session": "{{session_id}}"
         }
      
   .. tab-item:: RESPONSE

      .. code-block:: json
      
         {
           "id": 1,
           "result": [
             {
               "data": {
                 "admin_adom": "root",
                 "admin_prof": "Super_User",
                 "admin_user": "devops",
                 "adom_list": [],
                 "adom_override": 0,
                 "current_adom_name": "root",
                 "email": "",
                 "first_name": "",
                 "last_name": "",
                 "login_user": "devops",
                 "time_left": 28800,
                 "timestamp": 1641926409,
                 "valid": 1
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/sys/session"
             }
           ]
         }
      
How to create Device Meta fields?
---------------------------------

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "method": "set",
     "params": [
       {
         "data": {
           "importance": "required",
           "length": 20,
           "name": "foobar",
           "status": "enable"
         },
         "url": "/dvmdb/_meta_fields/device"
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
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/_meta_fields/device"
       }
     ]
   }

How to create an ADOM in a managed FAZ 
--------------------------------------

This is for the situation where fortimanager is managing a fortianalyzer and we
don't want to create the fortianalyzer ADOM by using the fortianalyzer.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "method": "add",
     "params": [
       {
         "data": [
           {
             "create_time": 1594363171,
             "desc": "This is a test",
             "flags": 2056,
             "mig_mr": 0,
             "mig_os_ver": 0,
             "mr": 4,
             "name": "FOOBAR_007",
             "os_ver": 6,
             "restricted_prds": 1,
             "state": 1
           }
         ],
         "url": "/dvmdb/adom"
       }
     ],
     "remote": "deployment/proxy/703",
     "session": "AxLiomO/CpbyM6ObMs0Z2aTEg2UVeTkPjKZpVZb7Q1FqTY5A2/cClfQ7/A77NYV1xzGm5/VyPcw0pCs/czD0xA==",
     "verbose": 1
   }

We can also use this one:

**REQUEST:**

.. code-block::

   {
     "id": 72,
     "method": "exec",
     "params": [
       {
         "url": "faz/cmd/sync/dvmdb",
         "data": {
           "device": "fazfoo",
           "adom": "FOOBAR"
         }
       }
     ]
   }

How to get details about the connected API user?
------------------------------------------------

Caught in #0632548.

**REQUEST**: 

.. code-block:: json

                {
                  "id": 1,
                  "jsonrpc": "1.0",
                  "method": "get",
                  "params": [
                    {
                      "url": "/sys/session"
                    }
                  ],
                  "session": "AfbffH1jvS34Wa/ZJElS7lQPlhWWYvAsikl/eO7k3ikaqH4Q0AgfIJYAJVcaNTydybdd/fN5HPj8rLy7QVIL7w==",
                  "verbose": 1
                }

**RESPONSE:**

.. code-block:: json

                {
                  "id": 1,
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
                      "status": {
                        "code": 0,
                        "message": "OK"
                      },
                      "url": "/sys/session"
                    }
                  ]
                }

Operating the FortiManager system
---------------------------------

How to reboot FortiManager?
+++++++++++++++++++++++++++

Caught in #621300.

The followinge example shows how to reboot your FortiManager unit:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
      		{
      		  "id": 1,
      		  "method": "exec",
      		  "params": [
      		    {
                "url": "/sys/reboot",
                "message": "We're rebooting!"
      		    }
      		  ],
      		  "session": "{{session}}"
      		}

   .. tab-item:: RESPONSE

      .. code-block:: json
      
      		{
      		  "id": 1,
      		  "result": {
      		    "status": {
      		      "code": 0,
      		      "message": "OK"
      		    }
      		  }
      		}

How to backup the FortiManager?
+++++++++++++++++++++++++++++++

Caught in #621300.

Using REST API
______________

FortiManager backup could be trigger with this simple API:

.. code-block:: shell

   curl --silent --user devops:fortinet --insecure -o fmg_backup_001.dat https://10.210.35.112/jsonrpc/sys/backup

This is generating a non encrypted protected archive named
``fmg_backup_001.dat``.

.. warning::

   - Starting with FortiManager 7.0.11, 7.2.5 and 7.4.2 (#0959025), it is no 
     longer possible to generate a non encrypted backup file.

   - Starting with FortiManager 7.2.6, 7.4.4 and 7.6.1 (#1049364), if you debug 
     FortiManager using following command:

     .. code-block:: text

        diagnose debug service sys 255
        diagnose debug enable

     You should see the following error output:

     .. code-block:: text
        :emphasize-lines: 3

        Request [/usr/local/apache2/bin/httpd:27987:30]: { "__from_rest": 1, "client": "\/usr\/local\/apache2\/bin\/httpd:27987", "id": 30, "method": "get", "params": [{ "target start": 1, "url": "\/sys\/backup"}], "session": "nJEOlg5gbzoTtHmxpeKGxww9bab06XRLGXWJd7UjRNmREC4zl2OJ326racvBw0Qo3dZFjRddWNBj0nRksTX6fQ==", "src": "172.26.128.5"}
        Chkperm Response [/usr/local/apache2/bin/httpd:27987:30]: { "id": 30, "result": [{ "status": { "code": 0, "message": "OK"}, "url": "\/sys\/backup"}], "session": 2534}
        Response [/usr/local/apache2/bin/httpd:27987:30]: { "id": 30, "result":
        { "status": { "code": -10, "message": "Backup password must be set"}}}
        
     With a previous version, you should see a different error message.
     For instance with FortiManager 7.4.2/7.4.3:

     .. code-block:: text

        Request [/usr/local/apache2/bin/httpd:16351:483]: { "__from_rest": 1, "client": "\/usr\/local\/apache2\/bin\/httpd:16351", "id": 483, "method": "get", "params": [{ "target start": 1, "url": "\/sys\/backup"}], "session": "N8UFAhji78TkDBMYRcDBPbsHF94iwoTxCYyI2woGWD6YQ3vqx5e\/kmhsVzApTfMvWY7tES2Mt\/Sq0O164+UEaQ==", "src": "172.26.128.5"}
        Chkperm Response [/usr/local/apache2/bin/httpd:16351:483]: { "id": 483, "result": [{ "status": { "code": 0, "message": "OK"}, "url": "\/sys\/backup"}], "session": 49192}
        Response [/usr/local/apache2/bin/httpd:16351:483]: { "id": 483, "result": { "status": { "code": -1, "message": "runtime error 0: invalid
        value"}}}

Should you want to encrypt your backup file:

.. code-block:: shell

   curl --silent --user devops:fortinet --insecure -o fmg_backup_002.dat https://10.210.35.112/jsonrpc/sys/backup?passwd=abc123

In this case, resulting backup file ``fmg_backup_002.dat`` will be encrypted
with password ``abc123``.

Using FortiManager JSON RPC API
_______________________________

Starting with FortiManager 7.2.3 (#0875702), it is possible to use the
FortiManager JSON RPC API to trigger a backup operation.

The following example shows how to backup your FortiManager system to an external FTP server; backup file will be encrypted:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "filename": "tmp/fmg_backup.dat",
                 "passwd": "fortinet",
                 "port": 21,
                 "server": "10.210.35.207",
                 "service": "ftp",
                 "username": "tiger",
                 "userpasswd": "fortinet"
               },
               "url": "/sys/backup"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json         

         {
           "id": 3,
           "result": {
             "status": {
               "code": 0,
               "message": "OK"
             },
             "taskid": 837
           }
         }

      .. note::

         - Once the task is completed, you can get your ``fmg_backup.dat`` 
           FortiManger backup file, from the ``tmp`` folder of your
           ``10.210.35.207`` FTP server

.. warning::

   - Starting with FortiManager 7.0.11, 7.2.5 and 7.4.2 (#0959025), it is no 
     longer possible to generate a non encrypted backup file.

How to restore the FortiManager?
++++++++++++++++++++++++++++++++

Caught in #621300.

Using REST API to restore the FortiManager
__________________________________________

FortiManager restore operation could be triggered:

- For the non-encrypted backup file:

  .. code-block:: shell

     curl --silent --user devops:fortinet --insecure --data-binary @fmg_backup_001.dat https://10.210.35.112/jsonrpc/sys/restore

- For the encrypted backup file:

  .. code-block:: shell
  
     curl --silent --user devops:fortinet --insecure --data-binary @fmg_backup_002.dat https://10.210.35.112/jsonrpc/sys/restore?passwd=abc123
     
Using |fmg_api| to restore FortiManager
_______________________________________

Caught in #0746154.

It is possible to restore a FortiManager system using the |fmg_api| form,
provided the FortiManager backup file has been uploaded in an external FTP, SCP
or SFTP server:

.. tab-set:: 
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "filename": "tmp/fmg_backup.dat",
                 "port": 21,
                 "server": "10.210.35.207",
                 "service": "ftp",
                 "username": "tiger",
                 "userpasswd": "fortinet"
               },
               "url": "/sys/restore"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json      

         {
           "id": 3,
           "result": {
             "status": {
               "code": 0,
               "message": "OK"
             }
           }
         }
   
How to upgrade the FortiManager?
++++++++++++++++++++++++++++++++

Using the FortiManager API
__________________________

Caught in #1100531 (FMG 7.6.3).

The following example shows how to upgrade the FortiManager. FortiManager will
fetch the ``image.out`` firmware using the ``10.0.0.1`` TFTP server.

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method":"exec",
           "params": [
             {
               "url": "/sys/upgrade",
               "data": {
                 "service": "tftp",
                 "server":"10.0.0.1",
                 "filename": "image.out"
               }
             }
           ],
           "session":"{{session}}"
         }

      .. note::
         
         You can also use ``scp``, ``ftp`` and ``sftp`` as the ``service``.
         In this case, you need to provide the following details:

         - ``username``: The username
         - ``userpasswd``: The password
         - ``port``: (Optional) He port number.

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": {
             "status": {
               "code": 0,
               "message": "OK"
             },
           "url": "/sys/upgrade"
         }

Using REST API to upgrade your FortiManager unit
________________________________________________

Caught in #0600185.

The following example shows how to upgrade your FortiManager unit:

.. tab-set:: 

   .. tab-item:: REQUEST
 
      .. code-block:: shell

         curl --silent --user devops:fortinet --header "Content-Type: application/octet-stream" --insecure --data-binary '@Downloads/FMG_VM64-v7-build3372-FORTINET.out' https://10.210.34.120/jsonrpc/sys/upgrade

   .. tab-item:: RESPONSE

      .. code-block:: json

         { 
           "result": { 
             "status": { 
               "code": 0, 
               "message": "OK" 
             } 
           } 
         }

How to get CPU, Memory and Disk usage of FortiManager?
++++++++++++++++++++++++++++++++++++++++++++++++++++++

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/cli/global/system/performance"
       }
     ],
     "session": "PAFlmA6mEMYGylgdrwY7hj2F1/w3li5OzRZrbD6D7+kr6kSPBtTCJBSgYBxau9KZp5jlw7HvUWMeaOa4PrQfhw==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json
  
   {
     "id": 3,
     "result": [
       {
         "data": {
           "CPU": {
             "CPU[0] usage": {
               "Details": {
                 "%idle": "93.66",
                 "%iowait": "4.50",
                 "%irq": "0.00",
                 "%nice": "0.00",
                 "%softirq": "0.00",
                 "%sys": "0.61",
                 "%user": "1.23"
               },
               "Usage": "6.34%"
             },
             "CPU[1] usage": {
               "Details": {
                 "%idle": "97.15",
                 "%iowait": "0.00",
                 "%irq": "0.00",
                 "%nice": "0.00",
                 "%softirq": "0.20",
                 "%sys": "0.61",
                 "%user": "2.03"
               },
               "Usage": "2.85%"
             },
             "CPU[2] usage": {
               "Details": {
                 "%idle": "98.57",
                 "%iowait": "0.00",
                 "%irq": "0.00",
                 "%nice": "0.00",
                 "%softirq": "0.00",
                 "%sys": "0.41",
                 "%user": "1.02"
               },
               "Usage": "1.43%"
             },
             "CPU[3] usage": {
               "Details": {
                 "%idle": "97.96",
                 "%iowait": "0.00",
                 "%irq": "0.00",
                 "%nice": "0.00",
                 "%softirq": "0.00",
                 "%sys": "0.81",
                 "%user": "1.22"
               },
               "Usage": "2.04%"
             },
             "CPU_num": 4,
             "Used": "2.0%",
             "Used(Excluded NICE)": "2.0%"
           },
           "Flash Disk": {
             "IOStat": {
               "%util": "0.0",
               "queue": "0.0",
               "r_kB/s": "1.2",
               "r_tps": "0.0",
               "sampling_sec": "199754.29",
               "svc_ms": "0.0",
               "tps": "0.0",
               "w_kB/s": "0.0",
               "w_tps": "0.0",
               "wait_ms": "0.7"
             },
             "Total": "1,007,512 KB",
             "Used": "234,648 KB 23.3%"
           },
           "Hard Disk": {
             "IOStat": {
               "%util": "0.0",
               "queue": "0.0",
               "r_kB/s": "3.5",
               "r_tps": "0.1",
               "sampling_sec": "199754.28",
               "svc_ms": "0.1",
               "tps": "3.0",
               "w_kB/s": "71.4",
               "w_tps": "2.8",
               "wait_ms": "5.5"
             },
             "Total": "83,663,256 KB",
             "Used": "26,416,368 KB 31.6%"
           },
           "Memory": {
             "Total": "10,264,044 KB",
             "Used": "4,817,012 KB 46.9%"
           }
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/cli/global/system/performance"
       }
     ]
   }

How to `execute top` or `execute iotop`?
++++++++++++++++++++++++++++++++++++++++

`execute top`
_____________

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json
         
         {
           "method": "exec",
           "params": [
             {
               "url": "/cli/global/exec/top",
               "data": {
                 "top-n": 50,
                 "order-by": "cpu-usage"
               }
             }
           ],
           "id": "{{ session }}"
         }

`execute iotop`
_______________

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json
         
         {
           "method": "exec",
           "params": [
             {
               "url": "/cli/global/exec/iotop",
               "data": {
                 "top-n": 50,
               }
             }
           ],
           "id": "{{ session }}"
         }

Task Management
---------------

How to get the latest task?
+++++++++++++++++++++++++++

In other words, how do you retrieve the newest (most recently created) task using the FortiManager API?

The following example demonstrates how to fetch the latest task by querying the
``/task/task/`` endpoint, limiting the result to a single entry, and sorting by
ID in descending order:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "loadsub": 0,
               "range": [
                 0,
                 1
               ],
               "sortings": [
                 {
                   "id": -1
                 }
               ],
               "url": "/task/task/",
               "verbose": 1
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

      .. note::

         The key elements of this requests are:

         - ``range: [0, 1]``: Get results from index 0 to 1, meaning only the 
           first item will be returned (pagination-like behavior).

         - ``sortings: [{"id": -1}]``: Sort by the ``id`` field in descending 
           order (likely to get the most recent task first).

         - ``loadsub: 0``: Don't load sub-objects. Omit it if you need the
           details of the task.

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": [
                 {
                   "adom": 2073,
                   "end_tm": 1743166837,
                   "flags": 0,
                   "id": 986,
                   "num_done": 1,
                   "num_err": 0,
                   "num_lines": 1,
                   "num_warn": 0,
                   "percent": 100,
                   "pid": 24587,
                   "src": 0,
                   "start_tm": 1743166837,
                   "state": 4,
                   "title": "deldevtitle",
                   "tot_percent": 100,
                   "user": "admin"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/task/task/"
             }
           ]
         }        

How to delete a task?
+++++++++++++++++++++

Deleting a task could be used to delete a completed task or cancelling/stopping a running task.

The following example shows how to delete the ``11111`` task:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "delete",
           "params": [
              {
                "url": "/task/task/11111"
              }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "status": {
             "code": 0,
             "message": "OK"
           },
           "url": "/task/task/11111"
         }            

FortiManager Packet capture
---------------------------

It is possible to make packet capture operations for traffic originating or
destined to the FortiManager using the FortiManager API.

How to get existing packet capture definitions?
+++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to get existing packet capture definitions:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/cli/global/system/sniffer"
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
                   "host": "10.0.0.1",
                   "id": 1,
                   "interface": "port1",
                   "ipv6": "enable",
                   "max-packet-count": 4000,
                   "non-ip": "enable",
                   "port": "80",
                   "protocol": "6",
                   "vlan": "1001"
                 },
                 {
                   "host": "",
                   "id": 2,
                   "interface": "port3",
                   "ipv6": null,
                   "max-packet-count": 4000,
                   "non-ip": null,
                   "port": "1111",
                   "protocol": "",
                   "vlan": ""
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/cli/global/system/sniffer"
             }
           ]
         }

      .. note::

         This output shows two existing packet capture definitions. 

How to add a new packet capture definition?
+++++++++++++++++++++++++++++++++++++++++++

The following example shows how to add a new packet capture definition:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "host": "10.1.2.3",
                 "id": 0,
                 "interface": "port8",
                 "max-packet-count": 300
               },
               "url": "/cli/global/system/sniffer"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         The ``id`` field is mandatory. Setting it to ``0`` prompts 
         FortiManager to automatically assign the next available ID.

   .. tab-item:: REQUEST

      .. code-block:: json   

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "id": 12
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/cli/global/system/sniffer"
             }
           ]
         }

      .. note::

         The ``id`` of the create packet capture definition is ``12``.

How to start a packet capture?
++++++++++++++++++++++++++++++

The following example shows how to start a packet capture from an existing
packet capture definition:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "action": "start",
                 "id": 1
               },
               "url": "/cli/global/system/sniffer"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         ``id`` is the ID of an existing packet capture definition.

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
               "url": "/cli/global/system/sniffer"
             }
           ]
         }

How to restart a packet capture?
++++++++++++++++++++++++++++++++

*Restart* retains packets captured before the stop operation and includes newly captured packets in the final result.

The following example demonstrates restarting a packet capture from an existing definition:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "action": "restart",
                 "id": 1
               },
               "url": "/cli/global/system/sniffer"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         ``id`` is the ID of an existing packet capture definition.

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
               "url": "/cli/global/system/sniffer"
             }
           ]
         }

How to stop a packet capture?
+++++++++++++++++++++++++++++

The following example shows how to stop a packet capture from an existing
packet capture definition:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "action": "stop",
                 "id": 1
               },
               "url": "/cli/global/system/sniffer"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         ``id`` is the ID of an existing packet capture definition.

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
               "url": "/cli/global/system/sniffer"
             }
           ]
         }

How to get the status of the packet captures?
+++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to get the status of the packet captures:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "action": "progress"
               },
               "url": "/cli/global/system/sniffer"
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
                   "id": 1,
                   "max_packets": 4000,
                   "packets": 1308,
                   "running": 0
                 },
                 {
                   "id": 2,
                   "max_packets": 4000,
                   "packets": 407,
                   "running": 1
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/cli/global/system/sniffer"
             }
           ]
         }

      .. note::

         The output shows two packet captures: the one with ID ``1`` is stopped
         (``running`` is ``0``) and the one with ID ``2`` is running
         (``running`` is ``1``).

How to download a packet capture?
+++++++++++++++++++++++++++++++++

Seems doable via the FortiManager GUI API using an URl similar to:

.. code-block:: text

   https://{{fmg_ip}}/flatui/api/gui/sniff/export?filename=sniffer_{{interface}}.{{packet_capture_definition_id}}.pcap&downloadname=sniffer_{{interface}}.{{packet_capture-definition_id}}.pcap

For more details, see the section :ref:`How to download a FortiManager packet capture?`

How to license a FortiManager-VM?
---------------------------------

Captured in #1090271 (FortiManager 7.6.3).

The following example shows how to license a FortiManager-VM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 2,
           "method": "exec",
           "params": [
             {
               "url": "/sys/api/vmlicense",
               "data": {
                 "vmlicense": "-----BEGIN FMG VM LICENSE----- ..... -----END FMG VM LICENSE-----"
               }
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK, System is rebooting"
               },
               "url": "/sys/api/vmlicense"
             }
           ],
           "id": 2
         }