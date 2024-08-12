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
                   "\"-----BEGIN CERTIFICATE-----\nMIIKLDCCBhSgAwIBAgIBADANBgkqhkiG9w0BAQsFADCBpTELMAkGA1UEBhMCVVMx\nEzARBgNVBAgTCkNhbGlmb3JuaWExEjAQBgNVBAcTCVN1bm55dmFsZTERMA8GA1UE\nChMIRm9ydGluZXQxHjAcBgNVBAsTFUNlcnRpZmljYXRlIEF1dGhvcml0eTEVMBMG\nA1UEAxMMZm9ydGluZXQtY2EyMSMwIQYJKoZIhvcNAQkBFhRzdXBwb3J0QGZvcnRp\nbmV0LmNvbTAgFw0xNjA2MDYyMDI3MzlaGA8yMDU2MDUyNzIwMjczOVowgaUxCzAJ\nBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRIwEAYDVQQHEwlTdW5ueXZh\nbGUxETAPBgNVBAoTCEZvcnRpbmV0MR4wHAYDVQQLExVDZXJ0aWZpY2F0ZSBBdXRo\nb3JpdHkxFTATBgNVBAMTDGZvcnRpbmV0LWNhMjEjMCEGCSqGSIb3DQEJARYUc3Vw\ncG9ydEBmb3J0aW5ldC5jb20wggQiMA0GCSqGSIb3DQEBAQUAA4IEDwAwggQKAoIE\nAQC9YkiEs7iwMQVeJuZyV5hYi8RGwE5N8X8I8jLo1BI/r/HD/RbbtmPBkyWVgPpa\nRQnAgnupxy06qJcWNrinZBxZyqKJrqke2RIBstV3lfoevSP7pmjF2raDZqL7EaDG\nkvRzaLyei5pifzcBzpoY8TpBk6upDD2pjkU60MqgWY/0Eo7SsiTKAukWvEqK3mL0\nK05+UNcEYzboWi0tIMBgXIYgIDDmYvOqUbDnPFYRTZQ6eltSFWrU+TvR4wEhBcwg\nDxlFQHY02Ee9UxEav4Ej02KzdjDKq3ZKMHaczGLiam4N/5TwtLG5+7il2TZ309Uf\n4Tjr5aWvEKMvHNTI4/hLDd+DsUs43qf0yD8HQ4kzpkyEEzdfXxPjbt6UNX7Dlz2T\nDQXvcqESs27kRxcEQ3gmVeL3cyDC4R4G3DhyBQQxNi22rROOX5DRMNC0TIrLslld\nRBMZfDbSUOrLZobfuOE4bMDHGz7pzJWxqkfBI/GoO9G4ZMFxC5JYr2/3lzod5K4P\nlGRyWUJ9vax2JIeF5DM/UgfBdqhZetTXLKnKCOxT85cseAeYT335vlHNo/YVnYg5\nLFfCpqAJMJYjFz9EG6oOBXeT34GHwtXOxpaib1uYqM6REzhiqSRLvwYdlQtXM7Tn\nse4HqiYATflFv5ZUj4087YrG0ok6zjQaIleqbeLLciMpYIvUxcsrMM/BHPwZH/xE\nWx4uau7oTdeSZQOj9okUYWPCf2Id5f9aOpHoGbwn5Y7FvE+y1VmQNw46UpBYLFJO\nhWtE2ZCx2sIDbH6sfQnPTG2gUqDkATHdZv5gLnFVQ2PRdL0465WCnrjIZHdJ7Isy\nk/QfubQCWKnM4aPJmsxQl9I38BkxVAZk9Txgw0i/9HjD9FPO3b9K2+te0oifxPav\nHqGfLKsU6TQE0GAJvsq3cYhGrqRUeD3fUTsmFypXw51Pr/Ka7O29Zt1kVZkf65J4\n1xH+XxkTp594ffr47EP80j44jsILa8M66CBV9MpCYoNJSZz0Q6TZkSEfSnwO0Dek\nuPmRwuVEcR18iCzpdhkqAIc+kalZbTJTsCBbZ1QNPxyEAzmjPLGFbQ00fH2o1nnW\nik4V4vtPgUCjJYomroF4U6I9J3FAtTnwejTiLMd4NMdbTibQQcM6706VnKvR7Z11\nKMKDlCLEzoVaPnAItg1bVnsK6uwHDisAc1bfysTR7DRUPDI7b69CptrEqN+Gljnp\nfJT+rhus/0RjUFVd/Z+2tGeLUVB+SYqaZgrWHhklaB1TKE38u8i4o6/V8sbCCUrJ\nad/nWvVY4lNYsxTrZbeAv+BPRy9SJMp7fWownkx8anhis5uVbR/w/nmJZK8TJ8RZ\n7Z9v2duLk/T8vUOcpfAKnSS5AgMBAAGjYzBhMB0GA1UdDgQWBBSjMa+jSO6h4l+x\n8v3W+0FIUBs6dTAfBgNVHSMEGDAWgBSjMa+jSO6h4l+x8v3W+0FIUBs6dTAPBgNV\nHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIBhjANBgkqhkiG9w0BAQsFAAOCBAEA\nPXG+lVec2WJGOZmb66q3isr/92spI8HvTUBp6nF8vbLmVgfWsctSKzF27+HhSkX1\nxPhdmoBHVFASwfgcqdrLdDBOqb8Nm07iVYElPdiufTq3NzI2wIS5m8egAagILGQ+\nV3IwGay67kUrH4MMwLqB3vR9YbNEAS/xq89RUZkPe9t5nvYm1WfXCkzLT3Poz8I8\n0nP+FZGkBEz+pg05/rPfujU0DwQsIqds5IQBzmd4TcQm12UVxkBM9z4NEAZiII5a\nKeo0vRbBnmaflBNUxeRaiPyLSncvlSNxUv5Q1rL4jUaDE4Ybqif1QQzB05jwLZbt\nzUB7vppn0VSEBwnbaWwcVAtcBExY8YwJEEuhhZ7beYjQQ7TE4Jf1mwHD28nPT+B0\n1DntS6+q+fIMG/4UzmF936sB8XicVGcscLmvGMtOoGTiCtXX9J1/E9+Qeb7Isu/W\njzQXXllgQTuK3F0K/M58eM4GjXSOY2KuLHclC+1jEusHKvXfwAYuIFLYm/mTlVAs\npqIRmg0ZFDhea6t1hu7U7G0JNMyPhS9DA7RpiTUUCbMJdAHGPIt9b+j/ggrI1t0N\n1EHpKvViulIoHxH/wtQUEAkEYXH9Y011KF9mqeXP6w1pz1j3QERzxqmmslWB7jO7\nKNcw0OjSlDQX5IkQ4py1IQj8jBuwzTZIuRSWnGDUZx6MeGd9JWcZeg/osMbBD2dc\nNiUg84Zc2sZbN2+ma1br/YjcFVRfjjWG8JRo3Y4WevLeClJJCTD/3zb9pd9imPhQ\npS3M5vqEHlO4V6RVmCyugEWamEkdAc6LRBxcvs0V1328JQ0X9edJjn0FTPoY788w\n2rY4akEPViJ9Ew2N3ZgG5ELxI5jrgd7AStdagwAj5ykIAHcQAPi2oz0ADl8YAgTM\n2yJj5GiEkADU8s3Cyhf6Qf6WPWWiRVmYtlCwXjp+bUl5Sgiy+dZaPv6GwXTKPsoc\n3vAHdh2/Md0Jtv8ZqM6RgBHTMrewkkh7u7kjGjCFKS1VVtZ4lhDRZbTOEKdjYbQe\nvGAieiYwArAFXBFyqMN6vQq8B/oZwmCPXuUL+y7vMvRsM8YXgy/vnJ6+B8NBwfEj\nI6PFB1wur2zO/42AUBhndEIRX/k4I07WbX+Rwn+zKfVuic2v9mVv2R9oc95qV4NQ\njvk1EYUQvZ+H4BYAX8CxhU/SmLfaZOi/ysV/WD5J1IxZCd5qLNkmLwiWyoFwcCzO\n18jp/3AG//GRZurh6xKUqylNUFGkTxHUI72lTDQKLBBYo0M16ij1JCZIz03Uno2A\nIhTNSJ8pkXDrWBXUcQb26GWPyeQ4jSXTSgqWuaXM0PsMEqVg3hbJhGa1p2wFXiHg\nx+nkkKoLQHPUczTwYRxQUQ==\n-----END CERTIFICATE-----\""
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
                     "account": "jpforcioli@fortinet.com",
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
                     "rawdata": "Contract=ADOM-1-06-20260525:0:5000:5000:0*AVDB-1-99-20221001:0:1:1:0*AVEN-1-99-20221001:0:1:1:0*COMP-1-20-20260525:0:1:1:0*ENHN-1-20-20260525:0:1:1:0*FMWR-1-06-20260525:0:1:1:0*FRVS-1-06-20260525:0:1:1:0*NIDS-1-99-20221001:0:1:1:0*SPRT-1-20-20260525:0:1:1:0*VMLS-1-06-20260525:0:5000:5000:0|AccountID=jpforcioli@fortinet.com|Industry=Technology|Company=Fortinet|UserID=106728",
                     "serial": "FMVMMLTM22123079"
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
     "jsonrpc": "1.0",
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
     "session": "+iLuqr601/V0Yd3hCt405kHSd0gnFbDrsv6EcLd7WoG1IJE+edzYsPDLVDXkwgEh8GVvvEScpoCQwZkdicjpfA==",
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

Workspace normal mode
---------------------

Locking
+++++++

ADOM Lock
_________

Following example is showing how to lock the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lock"
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
               "url": "/dvmdb/adom/demo/workspace/lock"
             }
           ]
         }

Policy Package Lock
___________________

The following example shows how to lock the ``ppkg_001`` Policy Package from the ``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lock/pkg/ppkg_001"
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
               "url": "/dvmdb/adom/demo/workspace/lock/pkg/ppkg_001"
             }
           ]
         }

Firewall Policy Lock
____________________

Following example is showing how to lock firewall policy with ``policyid`` ``1`` in the ``ppkg_001`` Policy Package from the ``demo`` ADOM:

.. tab-set:: 
  
   .. tab-item:: REQUEST

      .. code-block:: json
  
         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lock/pkg/ppkg_001/firewall/policy/1"
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
               "url": "/dvmdb/adom/demo/workspace/lock/pkg/ppkg_001/firewall/policy/1"
             }
           ]
         }
      
Object Lock
___________

To lock an object, you need first to lock a Policy Package (see :ref:`Policy Package Lock`) or a firewall policy (see :ref:`Firewall Policy Lock`).

The endpoint to lock an object is:

.. code-block:: text

   /dvmdb/adom/{adom}/workspace/obj/{path_to_the_object}

where ``path_to_the_object`` is the usual path used to refer to objects.

For instance:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - To lock...
     - ``path_to_the_object`` is

   * - the ``host_001`` firewall address
     - ``/firewall/address/host_001``

   * - the ``grp_001`` firewall address
     - ``/firewall/addrgrp/grp_001``

   * - the ``tcp_8080`` TCP service
     - ``/firewall/service/custom/tcp_8080``

The following exemple shows how to lock the ``host_001`` firewall address from the ``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 4,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lock/obj/firewall/address/host_001"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 4,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/lock/obj/firewall/address/host_001"
             }
           ]
         }

Device Lock
___________

Device lock has been introduced in #0544637 (FMG 6.0.5/6.2.0).

The following example show how to tock the ``dev_001`` device from the ``demo`` ADOM:

.. tab-set:: 
   
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lock/dev/dev_001"
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
               "url": "/dvmdb/adom/demo/workspace/lock/dev/dev_001"
             }
           ]
         }

Comitting changes
+++++++++++++++++

ADOM Commit
___________

Before unlocking an ADOM, a Policy Package or a firewall policy, a *save* operation is required in order have all pending changes applied to the running 
ADOM database.

If you unlock without saving, all changes will be lost.

To save changes made in the ``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block::

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/commit"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: 

         {
           "id": 1,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "taskid": 3332,
               "url": "/dvmdb/adom/demo/workspace/commit"
             }
           ]
         }

Device commit
_____________

The following example shows how to commit changes made to the locked ``dev_001`` device from the ``demo`` ADOM:

.. tab-set:: 
   
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/commit/dev/dev_001"
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
               "url": "/dvmdb/adom/demo/workspace/commit/dev/dev_001"
             }
           ]
         }

Policy Package Commit
_____________________

The following example shows how to commit changes made to the locked ``ppkg_001`` Policy Package from the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 9,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/commit/pkg/ppkg_001"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json         

         {
           "id": 9,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/commit/pkg/ppkg_001"
             }
           ]
         }

How to detect unsaved changes?
______________________________

How do you know when a save operation is required?

It is important to answer that question otherwise you may lose all of your unsaved changes when unlocking your resource.

FortiManager is maintaining a ``dirty`` flag.

When it is ``0``, it means there's no unsaved changes.

When it is ``1``, it means it is required to trigger a save operation before 
unlocking the ADOM.

To understand the process, review the following complete sequence of operations
performed in the ``demo`` ADOM:

#. Lock the ADOM

   .. tab-set::
    
      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 3,
              "method": "exec",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/lock"
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
                  "url": "/dvmdb/adom/demo/workspace/lock"
                }
              ]
            }
      
#. Observe the ``dirty`` flag

   .. tab-set::
    
      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 4,
              "method": "get",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/dirty"
                }
              ],
              "session": "{{session}}",
              "verbose": 1
            }

      .. tab-item:: RESPONSE

         .. code-block:: json            

            {
              "id": 4,
              "result": [
                {
                  "data": {
                    "dirty": 0
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/dirty"
                }
              ]

            }

   This is expected: ``dirty`` flag is ``0`` since no change were done yet.

#. Do a change

   Modify the ``comment`` of an existing ``host_001`` firewall address in the  
   ``demo`` ADOM:
   
   .. tab-set::
    
      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 5,
              "method": "set",
              "params": [
                {
                  "data": {
                    "comment": "New comment #001"
                  },
                  "url": "/pm/config/adom/demo/obj/firewall/address/host_001"
                }
              ],
              "session": "{{session}}"
            }

      .. tab-item:: RESPONSE

         .. code-block:: json

            {
              "id": 5,
              "result": [
                {
                  "data": {
                    "name": "host_001"
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/pm/config/adom/demo/obj/firewall/address/host_001"
                }
              ]
            }
      
#. Observe the ``dirty`` flag

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 6,
              "method": "get",
              "params": [
                {
                  "url": "/dvmdb/adom/dc_us/workspace/dirty"
                }
              ],
              "session": "{{session}}",
              "verbose": 1
            }

      .. tab-item:: RESPONSE

         .. code-block:: json      

            {
              "id": 6,
              "result": [
                {
                  "data": {
                    "dirty": 1
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/dirty"
                }
              ]
            }

         Now the ``dirty`` flag is ``1``.

         It indicates there are unsaved changes!

   You could have use the ``lockinfo`` to observe the *dirty* status (see 
   :ref:`How to figure out there is a lock?`).

   For instance:

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json

            {
              "id": 6,
              "method": "get",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/lockinfo"
                }
              ],
              "session": "{{session}}",
              "verbose": 1
            }

      .. tab-item:: RESPONSE

         .. code-block:: json
            :emphasize-lines: 7,10

            {
              "id": 6,
              "result": [
                {
                  "data": [
                    {
                      "adom_dirty": 1,
                      "db_mode": 1,
                      "dev_oid": 399,
                      "dirty": 1,
                      "flags": 1,
                      "lock_sid": 31952,
                      "lock_time": 1721801037,
                      "lock_user": "devops",
                      "obj_cat": 0,
                      "obj_oid": 0,
                      "obj_url": "",
                      "type": 1,
                      "wfsid": 0
                    }
                  ],
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/lockinfo"
                }
              ]
            }
   
         You can see that the ``adom_dirty`` attribute is ``1``.

         There's also another ``dirty`` flag with value ``1``.

#. Save the change

   .. tab-set::
    
      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 7,
              "method": "exec",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/commit"
                }
              ],
              "session": "{{session}}"
            }

      .. tab-item:: RESPONSE

         .. code-block:: json

            {
              "id": 7,
              "result": [
                {
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/commit"
                }
              ]
            }
      
#. Observe the ``dirty`` flag

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 8,
              "method": "get",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/dirty"
                }
              ],
              "session": "{{session}}",
              "verbose": 1
            }

      .. tab-item:: RESPONSE

         .. code-block:: json

            {
              "id": 8,
              "result": [
                {
                  "data": {
                    "dirty": 0
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/dirty"
                }
              ]
            }

   Changes were saved in previous operation step.

   The ``dirty`` flag is back to ``0`` to indicate there's no unsaved change
   anymore.

#. Unlock the ADOM

   See :ref:`ADOM Unlock`

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json
      
            {
              "id": 9,
              "method": "exec",
              "params": [
                {
                  "url": "/dvmdb/adom/demo/workspace/unlock"
                }
              ],
              "session": "{{session}}"
            }
    
      .. tab-item:: RESPONSE

         .. code-block:: json

            {
              "id": 9,
              "result": [
                {
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/workspace/unlock"
                }
              ]
            }

   .. note:: 
   
      - You can only get the ``dirty`` flag of your own workspace session

Unlocking
+++++++++

ADOM Unlock
___________

.. warning::

   - If you unlock without a ``commit`` operation then unsaved changes will be 
     lost

   - See :ref:`ADOM Commit`

The following example shows how to unlock the locked ``demo`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block::

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/unlock"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block::

         {
           "id": 1,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/unlock"
             }
           ]
         }  

Device Unlock
_____________

The following example shows how to unlock the locked ``dev_001`` device from 
the ``demo`` ADOM:

.. tab-set:: 
   
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/unlock/dev/dev_001"
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
               "url": "/dvmdb/adom/demo/workspace/unlock/dev/dev_001"
             }
           ]
         }

Policy Package Unlock
_____________________

The following example shows how to unlock the locked ``ppkg_001`` Policy 
Package from the ``demo`` ADOM:

.. tab-set:: 
   
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 12,
           "method": "exec",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/unlock/pkg/ppkg_001"
             }
           ],
           "session": "{{session}}"
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 12,
           "result": [
             {
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/unlock/pkg/ppkg_001"
             }
           ]
         }

How to figure out there is a lock?
++++++++++++++++++++++++++++++++++

``lockinfo`` can be used to obtain information about an existing lock.

ADOM lockinfo
_____________

When ADOM isn't locked
@@@@@@@@@@@@@@@@@@@@@@

The following example shows how to get the lock details for the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
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
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
             }
           ]
         }

      .. note::

         - When the ADOM isn't locked, nothing special is returned

When ADOM is locked
@@@@@@@@@@@@@@@@@@@

The following example shows how to get the lock details for the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
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
                   "adom_dirty": 0,
                   "db_mode": 1,
                   "dev_oid": 399,
                   "dirty": 0,
                   "flags": 0,
                   "lock_sid": 37154,
                   "lock_time": 1714077048,
                   "lock_user": "devops",
                   "obj_cat": 0,
                   "obj_oid": 0,
                   "obj_url": "",
                   "type": 1,
                   "wfsid": 0
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
             }
           ]
         }
      .. note::

         - When the ADOM is locked, FortiManager returns multiple information 
           like the owner of the lock (``lock_user``) and the lock time 
           (``lock_time``)

Policy Package lockinfo
_______________________

When Policy Package isn't locked
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The following example shows how to get the lock details for the ``ppkg_001`` Policy Package in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
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
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/workspace/lockinfo"
             }
           ]
         }

      .. note::

         - When the ADOM isn't locked, nothing special is returned

When Policy Package is locked
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The following example shows how to get the lock details for the ``ppkg_001`` Policy Package in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 5,
           "method": "get",
           "params": [
             {
               "url": "/dvmdb/adom/demo/workspace/lockinfo/pkg/ppkg_001"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

   .. tab-item:: RESPONSE

      .. code-block:: json
         
         {
           "id": 5,
           "result": [
             {
               "data": [
                 {
                   "db_mode": 1,
                   "dev_oid": 399,
                   "dirty": 0,
                   "flags": 0,
                   "lock_sid": 39089,
                   "lock_time": 1721802745,
                   "lock_user": "devops",
                   "obj_cat": 0,
                   "obj_oid": 6079,
                   "obj_url": "ppkg_001",
                   "type": 2,
                   "wfsid": 0
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/dc_emea/workspace/lockinfo/pkg/ppkg_001"
             }
           ]
         }

      .. note::

         - When the Policy Package is locked, FortiManager returns multiple 
           information like the owner of the lock (``lock_user``), the lock 
           time (``lock_time``) and the locked resource (``obj_url``).

         - The ``adom_dirty`` flag (see :ref:`ADOM lockinfo`) isn't visible, 
           since you're getting the ``lockinfo`` for a Policy Package
        
         - However, the ``dirty`` attribute is visible - ``1`` means there are
           pending changes in this Policy Package; ``0`` means there's no such 
           pending changes.

         - ``dev_oid`` is the ID of the ``demo`` ADOM
         - ``obj_oid`` is the ID of the ``ppkg_001`` Policy Package

Per-ADOM workspace mode
+++++++++++++++++++++++

How to figure out whether an ADOM is with or without workspace mode?
____________________________________________________________________

The following example shows how to figure out whether the ``demo`` ADOM is with
workspace mode enable or disable:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "fields": [
                 "workspace_mode"
               ],
               "loadsub": 0,
               "url": "/dvmdb/adom/demo"
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
                 "name": "demo",
                 "oid": 311,
                 "workspace_mode": 0
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo"
             }
           ]
         }  

      .. note::

         - ``0`` means workspace mode is not enabled
         - ``1`` means workspace mode is enabled      

Workflow mode
-------------

We describe here the operations required to perform a change when FortiManager
operates in workflow mode.

This section isn't describing all of the possible workflow mode operations. 

To get additional API details, we can use the fortimanager GUI and observe the
output produced by the following fortimanager CLI debug commands:

.. code-block::

   diagnose debug service dvmdb 255
   diagnose debug enable
   diagnose debug timestamp enable

How to lock an adom in workflow mode?
+++++++++++++++++++++++++++++++++++++

We lock adom ``ZTP_SINGLE``.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workspace/lock"
       }
     ],
     "session": "McJZs8SpFtjHte+FFcNDbb9KPVg5bvIh9fkUAsvq5cDAPB6R0PF+AV+5YpiJ0fTye5Z07LJR7b/60k2c/ZkRA/oa3KAJPKwJ",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workspace/lock"
       }
     ]
   }

How to create a workflow session?
+++++++++++++++++++++++++++++++++

We want to start a new session.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/start"
       }
     ],
     "session": "M1CzeItUayZBbsftqkyBXetQJTKB1nm7X7+/QknqiLR9vbCuIkLW/qSDK/TwtCDuarPbEXc1taOnLzOzg0rD4dX5qqYOrmOB",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "new_session": 1,
           "sessionid": 1
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/start"
       }
     ]
   }

.. note::

   - ``new_session``: ``1`` indicates it's a new session, ``0`` indicates it's
     an existing session (we can re-enter an existing session provided it hasn't
     been submitted yet).

     To start an existing session, we just have to use same method as above but
     with this url:

     .. code-block::

        /dvmdb/adom/ZTP_SINGLE/workflow/start/<session_id>

   - ``session_id`` will have to be used to reference that specific session for
     other workflow operations (for instance to save or approve it).

How to get existing sessions?
+++++++++++++++++++++++++++++

It could be required to get the list of existing sessions to perform additional
workspace workflow operations on them.

To get the list of sessions:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "get",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow"
       }
     ],
     "session": "3AyIKOdJl27+OoZj8TJsHMqBovc4x031AuPFIl1r7pl616x/ewMTaqEmmEMwWow9O4Q45tRP+Dfv85e+WIyAXGL01M0xfw/c",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": [
           {
             "audit_time": "",
             "audit_user": "",
             "create_time": "2020-07-22 18:37:38",
             "create_user": "devops",
             "desc": "Workflow session",
             "flags": 1,
             "name": "Workflow session",
             "oid": 616,
             "revid": 0,
             "sessionid": 1,
             "state": 1,
             "submit_time": "",
             "submit_user": "",
             "wflog": null
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow"
       }
     ]
   }

We can use the returned ``sessionid`` to perform other workspace workflow mode
operation on that particular session.

How to save changes made in a session?
++++++++++++++++++++++++++++++++++++++

We assume that some changes have been made.
We now want to save them.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/save/1"
       }
     ],
     "session": "MOhyT02bbKOCrqqwt0X2OH3G27LifDHr/5AZ3cwg2ySRYvAi2jHZZl9veO61BgM1Inbu/mHsBuBDEIK1fK4zH/ZovswIBCCO",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/save/1"
       }
     ]
   }

How to discard saved changes?
+++++++++++++++++++++++++++++

We're in a situation where we have an existing session with some saved changes
and our session is still not submitted.

We want to discard the changes.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/discard/1"
       }
     ],
     "session": "nkv/vQ8R9/zwnrP/Vp+f+LzjzsspQUe0a2u9LS74BgCScsQOekgPhJEJ3So/D5zCCGHvwSdfdINiR36P4fi0QV2BR9QVnkD8",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/discard/1"
       }
     ]
   }

.. note::

   Session ``1`` still exists in the system. Hence it is possible to re-open it
   and perform new changes.

How to submit a session?
++++++++++++++++++++++++

We submit a session when we want the saved changes to be approved.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/submit/1",
         "workflow": {
           "desc": "We have finished our changes.",
           "fmgip": "10.210.35.200",
           "no_diff": 0
         }
       }
     ],
     "session": "eaXr97ungqgR31ecapTPnt5hiDhqmegidS1668ZxEsgEJjgnR/yAdGzoBOVg7ndaAnWcsozbd9rCczPvf42cYJ8U8jckwCMJ",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/submit/1"
       }
     ]
   }

.. note::

   It is no longer possible to add extra changes to a submitted session. If we
   try to start a submitted session, a brand new session will be created.

How to delete a session?
++++++++++++++++++++++++

This operation can only be performed by an approver.
If we receive this error:

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "status": {
           "code": -20020,
           "message": "No permission"
         },
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/drop/1"
       }
     ]
   }

it is probably because our API session has been created with the credentials of a
non approver user.

We want to delete session 1.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/drop/1"
       }
     ],
     "session": "avGakSAPiuvAfqvIIaYMFjEIOz2GymtIzFYMGJNuR05mxgYUgGyS1ILDuJOg/QTOP5An32HahKIEnh2hySXw7Lbf+JLxdIK4",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/drop/1"
       }
     ]
   }

Deleting a non approved session will also delete all other sessions made on top
of this one (which are by essence also not approved).

How to reject a session?
++++++++++++++++++++++++

This operation can only be performed by an approver.
A rejected session could be repaired.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/reject/1",
         "workflow": {
           "desc": "Wrong changes. Please repair",
           "user": "admin"
         }
       }
     ],
     "session": "NMTPFix6qkkKFJ7bDLFpjhVMSMcPfJKv61aH928174/xMOro+aZYBAg6zdJxxTmMnDglPxp81mKqwQd4nCv6DQ==",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/reject/1"
       }
     ]
   }

How to repair a rejected session?
+++++++++++++++++++++++++++++++++

Repairing a rejected session consists just in creating a new session.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/repair/1"
       }
     ],
     "session": "sai90w4hlWdSWOzn5sqVHmhxWPRFTtZ2R08pyW352avvqGxc1C167nkGNtjvHXEJ6XAT4sCnfCkHWeZRC/cLtw==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": {
           "sessionid": 2
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/repair/1"
       }
     ]
   }

How to approve a submitted session?
+++++++++++++++++++++++++++++++++++

This operation can only be performed by an approver.
Once approved, a submitted session can't be deleted anymore.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/approve/2",
         "workflow": {
           "desc": "Good!. I approve.",
           "user": "admin"
         }
       }
     ],
     "session": "FfBwDLjz5g23TIiAXg6OI6d3Re7qrERN+EaojGzRg5eN0ArKUflPs6YZabrKaGT++y87fDPGuXuFRI3stlfQKcj4/HTmIwyP",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workflow/approve/2"
       }
     ]
   }

How to unlock an adom in workflow mode?
+++++++++++++++++++++++++++++++++++++++

When we no longer need to perform any workflow mode operations we have to
release the ADOM since it could be needed by another administrator.

We unlock adom ``ZTP_SINGLE``.

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "exec",
     "params": [
       {
         "url": "/dvmdb/adom/ZTP_SINGLE/workspace/unlock"
       }
     ],
     "session": "X8ccl04rmuhRIdZo/VgArjUwWQylAmUYcbRG5h1xz49yBW0j/fCH6M6PbkPJAt726osTNIFg++gEivQi1isIqx5l6tlZd57r",
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
         "url": "/dvmdb/adom/ZTP_SINGLE/workspace/unlock"
       }
     ]
   }

How to CLI diff?
++++++++++++++++

This feature has been introduced in FortiManager 7.4.0 (Internal Reference:
0893188).

#. Trigger the diff taskid

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "dst": "adom/adom70/revision/2",
                 "flags": 16,
                 "src": "adom/adom70/revision/1"
               },
               "url": "cache/diff/start"
             }
           ],
           "session": 62273
         }  

   .. tab:: RESPONSE

      .. code-block:: json
      
         {
           "id": 1,
           "result": [
             {
               "data": {
                 "token": "AhZp8ro+ACZD81lbXa7pQpiP8MHpi0rG"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "cache\/diff\/start"
             }
           ]
         }      

#. Conserve the returned ``token``

#. Get the Policy Package diff

   .. tabs::

      .. tab:: REQUEST

         .. code-block:: json

            { 
              "method": "exec", 
              "params": [
                { 
                  "token": "AhZp8ro+ACZD81lbXa7pQpiP8MHpi0rG", 
                  "url": "cache/diff/get/cli/pkg/{pkg}"
                }
              ]
            }          

#. Get the objects diff

   .. tabs::

      .. tab:: REQUEST

         .. code-block:: json

            {
              "method": "exec",
              "params": [
                {
                  "token": "AhZp8ro+ACZD81lbXa7pQpiP8MHpi0rG",
                  "url": "cache/diff/get/cli/obj"
                }
              ]
            }

      .. tab:: RESPONSE

         .. code-block:: json

            {
              "result": [
                {
                  "data": {
                    "script": "config firewall address\nedit \"test_addr1\"\nset uuid 3de73c20-c80d-51ed-032d-099a7a5215d7\nset comment \"my test firewall address\"\nset subnet 192.168.100.100 255.255.255.255\nnext\nedit \"test_addr2\"\nset uuid 551925ac-c80d-51ed-bfbb-366b7966cba7\nset comment \"my test firewall address2\"\nset subnet 192.168.100.200 255.255.255.255\nnext\nend\n",
                    "percent": 100
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "cache/diff/get/cli/obj"
                }
              ]
            }




How to keep the session idle?
-----------------------------

Caught in #0643153.

Sometimes, we need to perform some actions but we don't want to reset the
idle_timeout timer. This is making sense from the GUI where some background
requests shouldn't reset the connected user idle_timeout (otherwise he will stay
connected forever).

FMG API comes with the attribute *keep_session_idle*. When set, the idle_timeout
timer won't be reset by the API call.

For instance:

**REQUEST:**

.. code-block:: json

                {
                  "id": 1,
                  "method": "get",
                  "params": [
                    {
                      "fields": [
                        "name",
                        "flags"
                      ],
                      "filter": [
                        "name",
                        "in",
                        "dut_fgt1"
                      ],
                      "keep_session_idle": 1,
                      "sub fetch": {
                        "vdom": {
                          "fields": [
                            "name",
                            "flags",
                            "status"
                          ]
                        }
                      },
                      "url": "/dvmdb/device"
                    }
                  ],
                  "session": 19874,
                  "verbose": 1
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

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json
      
      		{
      		  "id": 1,
      		  "jsonrpc": "1.0",
      		  "method": "exec",
      		  "params": [
      		    {
      		      "url": "/sys/reboot",
                "message": "We're rebooting!"
      		    }
      		  ],
      		  "session": "85cKXer0wv9g/YjLuGqgo2JeEDlUW+u0SAPEx6zkt+ToV2CpnbwOj5PDmYj2uKAN7KX0R3ATVk+D9OFsNq2mi44n1901XU4d",
      		  "verbose": 1
      		}

.. tabs::

   .. tab:: REQUEST

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

Backup, restore, upgrade and reboot have been caught in #0600185

How to backup the FortiManager?
+++++++++++++++++++++++++++++++

Using REST API
______________

FortiManager backup could be trigger with this simple API:

.. code-block:: shell

   curl --silent --user devops:fortinet --insecure -o fmg_backup_001.dat https://10.210.35.112/jsonrpc/sys/backup

This is generating a non encrypted protected archive named
``fmg_backup_001.dat``.

Should you want to encrypt your backup file:

.. code-block:: shell

   curl --silent --user devops:fortinet --insecure -o fmg_backup_002.dat https://10.210.35.112/jsonrpc/sys/backup?passwd=abc123

In this case, resulting backup file ``fmg_backup_002.dat`` will be encrypted
with password ``abc123``.


Using |fmg_api|
_______________

Starting with FortiManager 7.2.3 (#0875702).

To backup to an external FTP server; backup file will be encrypted:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "exec",
     "params": [
       {
         "data": {
           "filename": "tmp/fmg_backup_3.dat",
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
     "session": "33dYaeEVQm7SljnJGTSGPTvbE+bPws/PTlvJdPMYcW44I4oU6ZDJlLDHzriAC2CG3yD5yem0FodxkBpPAvulxw=="
   }

**RESPONSE:**

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

How to restore the FortiManager?
++++++++++++++++++++++++++++++++

Using REST API to restore the FortiManager
__________________________________________

FMG/FAZ restore could be triggered with this one:

- With the non-encrypted file:

  .. code-block:: shell

     curl --silent --user devops:fortinet --insecure --data-binary @fmg_backup_001.dat https://10.210.35.112/jsonrpc/sys/restore

- With the encrypted backup file:

  .. code-block:: shell
  
     curl --silent --user devops:fortinet --insecure --data-binary @fmg_backup_002.dat https://10.210.35.112/jsonrpc/sys/restore?passwd=abc123
     

Using |fmg_api| to restore FortiManager
_______________________________________

Caught in #0746154.

It is possible to restore a FortiManager system using the |fmg_api| form,
provided the FortiManager backup file has been uploaded in an external FTP, SCP
or SFTP server:

**REQUEST:**

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
     "session": "DHWAgr6Qk/iHPJOyl7s44pvfPogWiJokZf637NWDNBL1m8js1cA+3F+j2zvjLTvKnlzPaLNknVFUVc6O9RNEOpjhOAAYPD6p"
   }

**RESPONSE:**

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

Todo based on NFR #0600185

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