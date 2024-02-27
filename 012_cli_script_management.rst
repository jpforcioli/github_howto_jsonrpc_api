Script management
=================

A FortiManager CLI script could be defined with different targets:

+-------------------------+---------------------------------------+
| FMG JSON RPC API *type* | FMG GUI equivalent                    |
+=========================+=======================================+
| ``device_database``     | *Device Database*                     |
+-------------------------+---------------------------------------+
| ``adom_database``       | *Policy Package or ADOM Database*     |
+-------------------------+---------------------------------------+
| ``remote_device``       | *Remote FortiGate Directly (via CLI)* |
+-------------------------+---------------------------------------+

CLI script execution triggers a task.

It is best practise to end for the task completion before ending the FMG JSON
RPC API session. Especially when the target is ``remote_device``; the task
takes longer to complete and it requires a valid FMG JSON RPC API session.

All script execution outputs are saved by FortiManager using a log ID. The log
ID is generated using the following logic:

1. If script run against Device DB or Policy & Object/ADOM DB:

   .. code-block::

      log_id = concat(task_id, 1)

   For instance, if created task is ``123`` then corresponding log ID will be
   ``1231``.

2. If script run against real device:

   .. code-block::

      log_id = concat(task_id, 0)

   For instance, if created task is ``123`` then corresponding log ID will be
   ``1230``.	  

How to add a script?
--------------------

We add script ``overlays.site_7`` into adom ``demo``. This script target adom db
content.

**REQUEST:**

.. code-block::

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "add",
     "params": [
       {
         "data": {
           "content": "<your content>",
     	   "desc": "Script to add site_7 to the overlays",
           "name": "overlays.site_7",
           "target": "adom_database",
           "type": "cli"
         },
         "url": "/dvmdb/adom/demo/script"
       }
     ],
     "session": "M9hhF11FuiehMbImEjrhv6jEC9Rq6Mwr145bzby1f3zPRhJdYaiSU0nFfs15hW/NSJTmyacjkRZY0g/FKSPV3A==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block::

   {
     "id": 1,
     "result": [
       {
         "data": {
           "name": "overlays.site_7"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/dvmdb/adom/fastweb/script"
       }
     ]
   }

How to run a script against a Policy Package?
---------------------------------------------

Below is the request to run script ``script-002`` against policy
package ``default`` in ADOM ``DEMO``:

**REQUEST:**

.. code-block:: json

		{
		  "id": 1,
		  "jsonrpc": "1.0",
		  "method": "exec",
		  "params": [
		    {
		      "data": {
		        "adom": "DEMO",
			"package": "default",
			"script": "script-002"
		      },
		      "url": "/dvmdb/adom/DEMO/script/execute"
		    }
		  ],
		  "session": "tWy6iKRmT+C2obiyVpAz6c0tSel3RnNroUhqIeko0SLQD0lz1dSJ5iB0XbW4DcTb/w/bFkt6XuLLSz5AkyA9UA==",
		  "verbose": 1
		}

**RESPONSE:**

.. code-block:: json

		{
		  "id": 1,
		  "result": [
		    {
		      "data": {
		        "task": 452
		      },
		      "status": {
		        "code": 0,
			"message": "OK"
		      },
		      "url": "/dvmdb/adom/DEMO/script/execute"
		    }
		  ]
		}

How to run a script against a device/vdom?
------------------------------------------

**REQUEST:**

.. code-block:: json

		{
		  "id": 1,
		  "jsonrpc": "1.0",
		  "method": "exec",
		  "params": [
		    {
		      "data": {
		        "adom": "DEMO",
			"scope": [
			  {
			    "name": "peer11",
			    "vdom": "global"
			  }
			],
			"script": "script-003"
		      },
		      "url": "/dvmdb/adom/DEMO/script/execute"
		    }
		  ],
		  "session": "YaFeM8Wmxq0utrb31MuYjdLi+wKYSxs0urm0YmDgjMhCehyWiHI2HMk7jzm4E48WgNJ1iV7lS4Yj3MyWbnfv8Q==",
		  "verbose": 1
		}

.. note:: 

   - A CLI Script cannot be run against in VDOM scope; this is why we set the
     ``vdom`` attribute to ``global``.
   - For instance, if you run a CLI script against each member of a Model HA
     cluster, using ``root`` VDOM will work for the primary member, but will
     fail for the secondary members (which is weird; it should fail for all
     members). This is why we recommend to always use ``global``.
    
**RESPONSE:**

.. code-block:: json

		{
		  "id": 1,
		  "result": [
		    {
		      "data": {
		        "task": 457
		      },
		      "status": {
		        "code": 0,
			"message": "OK"
		      },
		      "url": "/dvmdb/adom/DEMO/script/execute"
		    }
		  ]
		}

.. warning:: 

   - If your CLI Script is with target *Remote FortiGate Directly (via CLI)* and
     ...
   - If you're getting a sucessful API response (as shown above with the
     returned task ID), but the task itself fails with an error message like
     *Error while reading script from database*, then please make sure you
     maintain the API session open during the CLI script execution (just follow
     the task progress using a ``get``  on ``/task/task/{task_id}``)

We can run the script on multiple devices:

**REQUEST:**

.. code-block:: json

		{
		  "id": 1,
		  "jsonrpc": "1.0",
		  "method": "exec",
		  "params": [
		    {
		      "data": {
		        "adom": "DEMO",
			"scope": [
			  {
			    "name": "peer11",
			    "vdom": "global"
			  },
			  {
			    "name": "peer12",
			    "vdom": "global"
			  }
			],
			"script": "script-003"
		      },
		      "url": "/dvmdb/adom/DEMO/script/execute"
		    }
		  ],
		  "session": "GvcXK7JTnPnXAJZQT+nTk1GEkAv3VR55rJiSxob0IwaQYIIN/FkiHLeLtjjrcHghoQOtlQbkDcL7U/pU9eYwSg==",
		  "verbose": 1
		}

**RESPONSE:**

.. code-block:: json

		{
		  "id": 1,
		  "result": [
		    {
		      "data": {
		        "task": 458
		      },
		      "status": {
		        "code": 0,
			"message": "OK"
		      },
		      "url": "/dvmdb/adom/DEMO/script/execute"
		    }
		  ]
		}

How to run a script against one or multiple device group(s)?
------------------------------------------------------------

By convention, if the ``scope`` entry only contains a ``name``, then
it is considered a device group.

In the below example, we're running script ``script-003`` against two
device groups ``apac`` and ``amer``.

**REQUEST:**

.. code-block:: json

		{
		  "id": 1,
		  "jsonrpc": "1.0",
		  "method": "exec",
		  "params": [
		    {
		      "data": {
		        "adom": "DEMO",
			"scope": [
			  {
			    "name": "apac"
			  },
			  {
			    "name": "amer"
			  }
			],
			"script": "script-003"
		      },
		      "url": "/dvmdb/adom/DEMO/script/execute"
		    }
		  ],
		  "session": "PX+BnOklcNAuIwWhF4wc0BLMUr9OQXiHPI46ZHCJzXkrrlSwV5GfxhDJIl6rwPjfVU+NqsDTRg7s1EbQFRgYzA==",
		  "verbose": 1
		}

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
	     "data": {
		   "task": 459
		 },
         "status": {
		   "code": 0,
	       "message": "OK"
		 },
		 "url": "/dvmdb/adom/DEMO/script/execute"
	   }
	 ]
   }

How to run a script against a FortiManager template?
----------------------------------------------------

For instance a system template, a fortiswitch template, etc.?

Caught in #0209576.

Run a script against a SD-WAN template
++++++++++++++++++++++++++++++++++++++

.. note:: 
  
   - Caught in #0209576.

#. Create a CLI Script (target = ADOM Database)

   In this example, I created a script named ``script_001`` with below content: 

   .. code-block:: text

      config system sdwan
          set status enable
          config zone
              edit virtual-wan-link
              next
          end
          config members
              edit 1
                  set interface port1
              next
              edit 2
                  set interface port2
              next        
          end
      end

#. Find the SD-WAN Template oid

   It will be used as the target of the CLI Script execution

   .. code-block:: text
      :emphasize-lines: 8,24

      # execute fmpolicy print-adom-package dc_amiens ?
      <policy package/template name>
      1	Policy Packages
      5	System Templates
      8	FortiClient Templates
      9	Threat Weight Templates
      10	WTP Packages
      11	SD-WAN Templates
      12	FortiSwitch Packages
      14	FortiExtender Packages
      18	Firmware Templates
      20	Template Groups
      22	All Non-policy Packages
      23	IPsec Tunnel Templates
      24	Static Route Templates
      26	SD-WAN Overlay Templates
      27	IPS Templates
      1262	BGP Templates
      
      
      
      # execute fmpolicy print-adom-package dc_amiens 11 ?
            ID	<package name>
          5168	name=test_001, pathname=test_001

   .. note::

      - The ``test_001`` SD-WAN Template is in the ``dc_amiens`` ADOM
      - The ``test_001`` SD-WAN Template oid is ``5168``

#. Put the ADOM name, package oid (SD-WAN Template oid) and script name into
   your |fmg_api| request:

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json

            {
              "id": 3,
              "method": "exec",
              "params": [
                {
                  "data": {
                    "adom": "dc_amiens",
                    "package": 5168,
                    "script": "script_001"
                  },
                  "url": "/dvmdb/adom/dc_amiens/script/execute"
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
                    "task": 1312
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/dc_amiens/script/execute"
                }
              ]
            }

#. Check script log for its execution history

   .. code-block:: text
   
      -------Executing time: Fri Jun 16 19:00:15 2023-----------
      
      
      
      Starting log (Run on database)
      
      config system sdwan
      set status enable
      config zone
      edit virtual-wan-link
      next
      end
      config members
      edit 1
      set interface port1
      next
      edit 2
      set interface port2
      next
      end
      end
      Running script(script_001) on DB success
      
      ----------------End of Log-------------------------

Run a script against a System Template
++++++++++++++++++++++++++++++++++++++

#. Create a ClI script (target = ADOM Database)

   In this example, I created a script named ``system1`` with below content:

   .. code-block:: text

      config system global
          set gui-ipv6 enable
          set admintimeout 30
          set admin-scp enable
      end
      config system email-server
          set server "15.5.5.55"
          set username "qa111"
          set password qa123456
          set authenticate enable
      end

#. Find the System Template id that you want your script run on

   .. code-block:: text
      :emphasize-lines: 4,14
   	   
      fmg # execute fmpolicy print-adom-package 136 ?
      <policy package/template name>
      1       Policy Packages
      5       System Templates
      8       FortiClient Templates
      9       Threat Weight Templates
      10      WTP Packages
      11      WAN Templates
      12      FortiSwitch Packages
      18      All Non-policy Packages
   
      fmg # executee fmpolicy print-adom-package 136 5 ?
      ID        <package name>
      3059        name=default, pathname=default
   

#. Put the ADOM name, package id (template id) and script name into your
   |fmg_api| request:
   
   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json
         	
            {
              "id": 16,
              "method": "exec",
              "params": [
                {
                  "data": {
                    "adom": "taj-adom",
                    "package": 3059,
                    "script": "system1"
                  },
                  "url": "dvmdb/adom/taj-adom/script/execute"
                }
              ],
              "session": "..."
            }

      .. tab-item:: RESPONSE

         .. code-block:: json
         
            {
              "id": 16,
              "result": [
                {
                  "data": {
                    "task": 766
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "dvmdb/adom/taj-adom/script/execute"
                }
              ]
            }
         
#. Check script log for its execution history

   .. code-block:: text
	
      -------Executing time: Wed Oct 28 16:09:31 2020-----------
   
      Starting log (Run on database)
      config system global
      set gui-ipv6 enable
      set admintimeout 30
      set admin-scp enable
      end
      config system email-server
      set server 15.5.5.55
      set username qa111
      set password ********
      set authenticate enable
      end
      Running script(system1) on DB success
   
      ----------------End of Log-------------------------

Run a script against a FortiSwitch System Template
++++++++++++++++++++++++++++++++++++++++++++++++++

#. Create a ClI script (target = ADOM Database)

   In this example, I created a script named ``fsw1`` with below content:

   .. code-block:: text
   
      config fsp managed-switch
          edit "S248DF3X15000011"
              set name "S248DF3X15000011"
              set platform "FortiSwitch-248D-FPOE"
              set template "managed_fsw1"
          next
      end
   
#. Find the FortiSwitch Template id that you want your script run on

   .. code-block:: text
      :emphasize-lines: 9,14
   
      fmg # execute fmpolicy print-adom-package 136 ?
      <policy package/template name>
      1       Policy Packages
      5       System Templates
      8       FortiClient Templates
      9       Threat Weight Templates
      10      WTP Packages
      11      WAN Templates
      12      FortiSwitch Packages
      18      All Non-policy Packages
   
      fmg # execute fmpolicy print-adom-package 136 12 ?
      ID        <package name>
      3714        name=138-3, pathname=138-3
   
#. Put the ADOM name, package id (template id) and script name into your
   |fmg_api| request:

   .. tab-set::
     
      .. tab-item:: REQUEST

         .. code-block:: json
         	
            {
              "id": 16,
              "method": "exec",
              "params": [
                {
                  "data": {
                    "adom": "taj-adom",
                    "package": 3714,
                    "script": "fsw1"
                  },
                  "url": "dvmdb/adom/taj-adom/script/execute"
                }
              ],
              "session": "..."
            }

      .. tab-item:: RESPONSE

         .. code-block:: json
         
            {
              "id": 16,
              "result": [
                {
                  "data": {
                    "task": 765
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "dvmdb/adom/taj-adom/script/execute"
                }
              ]
            }
         
#. Check script log for its execution history

   .. code-block:: text
   
      -------Executing time: Wed Oct 28 15:52:06 2020-----------
   
      Starting log (Run on database)
   
      config fsp managed-switch
      edit "S248DF3X15000011"
      set name S248DF3X15000011
      set platform FortiSwitch-248D-FPOE
      set template "managed_fsw1"
      next
      end
      Running script(fsw1) on DB success
   
      ----------------End of Log-------------------------

Run a script against a FortiAP Profile
++++++++++++++++++++++++++++++++++++++

#. Create a ClI script (target = ADOM Database)

   In this example, I created a script named ``wtp1`` with below content:
   
   .. code-block:: text
   
      config wireless-controller wtp
          edit "FAP11C3X12000488"
              set admin enable
              set name "FAP11C3X12000488"
              set wtp-profile "11C_cus1"
              config radio-1
                  set _mode 2
                  set _country-name "NA"
              end
          next
      end
   
#. Find the FortiAP Profile id that you want your script run on

   .. code-block:: text
      :emphasize-lines: 7,14
   
      fmg # execute fmpolicy print-adom-package 206 ?
      <policy package/template name>
      1       Policy Packages
      5       System Templates
      8       FortiClient Templates
      9       Threat Weight Templates
      10      WTP Packages
      11      WAN Templates
      12      FortiSwitch Packages
      18      All Non-policy Packages
   
      fmgB # execute fmpolicy print-adom-package 206 10 ?
      ID        <package name>
      3065        name=293-3, pathname=293-3     
      3092        name=293-102, pathname=293-102
      3093        name=293-103, pathname=293-103
   
#. Put the ADOM name, package id (template id) and script name into your
   |fmg_api| request:

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json
         	
            {
              "id": 16,
              "method": "exec",
              "params": [
                {
                  "data": {
                    "adom": "64-RACHEL-root",
                    "package": 3065,
                    "script": "wtp1"
                  },
                  "url": "dvmdb/adom/64-RACHEL-root/script/execute"
                }
              ],
              "session": "..."
            }

      .. tab-item:: RESPONSE

         .. code-block:: json
         
            {
              "id": 16,
              "result": [
                {
                  "data": {
                    "task": 767
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "dvmdb/adom/64-RACHEL-root/script/execute"
                }
              ]
            }
         
#. Check script log for its execution history

   .. code-block:: text
   
      -------Executing time: Wed Oct 28 17:14:47 2020-----------
      Starting log (Run on database)
   
      config wireless-controller wtp
      edit "FAP11C3X12000488"
      set admin enable
      config radio-1
      unset band
      #WARN: attribute [band] object invisible
      end
      config radio-2
      unset band
      end
      config radio-3
      unset band
      end
      config radio-4
      unset band
      end
      set admin enable
      set name FAP11C3X12000488
      set wtp-profile "11C_cus1"
      config radio-1
      set _mode 2
      set _country-name NA
      #WARN: attribute [band] object invisible
      end
      next
      end
      Running script(wtp1) on DB success
      
      ----------------End of Log-------------------------

How To get the latest script output executed in a particular ADOM?
------------------------------------------------------------------

For a script run against a policy package
+++++++++++++++++++++++++++++++++++++++++

**REQUEST**:

.. code-block:: json

		{
		  "id": 1,
		  "jsonrpc": "1.0",
		  "method": "get",
		  "params": [
		    {
		      "url": "/dvmdb/adom/DEMO/script/log/latest"
		    }
		  ],
		  "session": "RoXa5xoGrAlOMnCLC2vx4lprjwC/T97STtm7kevs6cnoVg+e4IBVSlSS1FlgVL3kL7DTtrFHDBocJGLsAQZSWA==",
		  "verbose": 1
		}

**RESPONSE**:

.. code-block:: json

		{
		  "id": 1,
		  "result": [
		    {
		      "data": {
		        "content": "\n\nStarting log (Run on database)\n\n config firewall policy\n edit \"2\"\n set _scope \"demo_device1\"-\"root\"\n next\n end\nRunning script(test-001) on DB success\n",
			"exec_time": "Wed Apr 15 13:48:07 2020",
			"log_id": 41,
			"script_name": "test-001"
		      },
		      "status": {
		        "code": 0,
			"message": "OK"
		      },
		      "url": "/dvmdb/adom/DEMO/script/log/latest"
		    }
		  ]
		}

For a script run against a specific device
++++++++++++++++++++++++++++++++++++++++++

**REQUEST:**

.. code-block:: json

		{
		  "id": 1,
		  "jsonrpc": "1.0",
		  "method": "get",
		  "params": [
		    {
		      "url": "/dvmdb/adom/DEMO/script/log/latest/device/demo_device1"
		    }
		  ],
		  "session": "jt7dv3N1X+GNdw9Wy9Vs+pitwFH8DjsV/xy4E2KV/OTE35nltYVmPd/GvGBXGv27E2L/WKvjW5HCx89EXsEVpA==",
		  "verbose": 1
		}

**RESPONSE:**

.. code-block:: json

		{
		  "id": 1,
		  "result": [
		    {
		      "data": {
		        "content": "\n\nStarting log (Run on database)\n\n config system global\n set hostname demo_device1\n end\nRunning script(test-002) on DB success\n",
			"exec_time": "Thu Apr 16 07:58:49 2020",
			"log_id": 71,
			"script_name": "test-002"
		      },
		      "status": {
		        "code": 0,
			"message": "OK"
		      },
		      "url": "/dvmdb/adom/DEMO/script/log/latest/device/demo_device1"
		    }
		  ]
		}

How to get the script output of a particular script execution in a particular ADOM?
-----------------------------------------------------------------------------------

1. First you need to get its corresponding ``log_id`` by retrieving a
   summary of the execution list

   - For scripts run against policy packages:

     **REQUESTS:**

     .. code-block:: json

		     {
		       "id": 1,
		       "jsonrpc": "1.0",
        	       "method": "get",
		       "params": [
		         {
		           "url": "/dvmdb/adom/DEMO/script/log/summary"
		         }
		       ],
		       "session": "Iv3oia2d+q2E5TUG/IsdSFJ175AQMQrD1+4V1TeOejjx48XXOp2fUNY2FMOf0ZmjGK81k5g+CUwImb+02Quasw==",
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
			       "exec_time": "Wed Apr 15 13:48:07 2020",
			       "log_id": 41,
			       "script_name": "test-001",
			       "seq": 1
			     },
			     {
			       "exec_time": "Wed Apr 15 13:44:50 2020",
			       "log_id": 31,
			       "script_name": "50_config.firewall.policy-54-adomdb",
			       "seq": 2
			     }
			   ],
			   "status": {
			     "code": 0,
			     "message": "OK"
			   },
			   "url": "/dvmdb/adom/DEMO/script/log/summary"
		         }
		       ]
		     }		   

   - For scripts run against a specific device:

     **REQUEST:**

     .. code-block:: json

		     {
		       "id": 1,
		       "jsonrpc": "1.0",
		       "method": "get",
		       "params": [
		         {
			   "url": "/dvmdb/adom/DEMO/script/log/summary/device/demo_device1"
			 }
		       ],
		       "session": "P/l8udT6BPTSZPcvy2BQfbK2C0cHsahvevn6ogzOqVnb7r1DmmG6RevKN5uc1ilTyhckBVFStF2V/A/vqcPbiQ==",
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
			       "exec_time": "Thu Apr 16 07:58:49 2020",
			       "log_id": 71,
			       "script_name": "test-002",
			       "seq": 1
			     }
			   ],
			   "status": {
			     "code": 0,
			     "message": "OK"
			   },
			   "url": "/dvmdb/adom/DEMO/script/log/summary/device/demo_device1"
			 }
		       ]
		     }		     


   .. note::

      Note that the ``log_id`` will have the following format:

      - If script executed against DB:

	.. code-block::

	   log_id = str(task_id) + "1"

      - If script executed against the remote device:
	
	.. code-block::

	   log_id = str(task_id) + "0"
	 
   2. Now you can retrieve the script output for the selected
      ``log_id``

      - For a script run against a policy package

	**REQUEST:**

	.. code-block:: json

			{
			  "id": 1,
			  "jsonrpc": "1.0",
			  "method": "get",
			  "params": [
			    {
			      "url": "/dvmdb/adom/DEMO/script/log/output/logid/41"
			    }
			  ],
			  "session": "3jspS4e/z5uVhqGIg0QrLSt1TkZAreTp93vFYOvbUiADH+LKVLAcwaSVrNV6q0yzUZx4MhMRgT91XNrAViwHfQ==",
			  "verbose": 1
			}			
			
	**RESPONSE:**

	.. code-block:: json

			{
			  "id": 1,
			  "result": [
			    {
			      "data": {
			        "content": "\n\nStarting log (Run on database)\n\n config firewall policy\n edit \"2\"\n set _scope \"demo_device1\"-\"root\"\n next\n end\nRunning script(test-001) on DB success\n",
				"exec_time": "Wed Apr 15 13:48:07 2020",
				"log_id": 41,
				"script_name": "test-001"
			      },
			      "status": {
			        "code": 0,
				"message": "OK"
			      },
			      "url": "/dvmdb/adom/DEMO/script/log/output/logid/41"
			    }
			  ]
			}

      - For a script run against a specific device

	**REQUEST:**

	.. code-block:: json

			{
			  "id": 1,
			  "jsonrpc": "1.0",
			  "method": "get",
			  "params": [
			    {
			      "url": "/dvmdb/adom/DEMO/script/log/output/device/demo_device1/logid/71"
			    }
			  ],
			  "session": "Qo8bH+n6sebjQy8VMlHSF3N3myGO8reekbaD6Z5ICeRDGSJkE5sOqORcTawwMX67U6KaK/VUukqw/J77OMLU/A==",
			  "verbose": 1
			}
			
	**RESPONSE:**

	.. code-block:: json

			{
			  "id": 1,
			  "result": [
			    {
			      "data": {
			        "content": "\n\nStarting log (Run on database)\n\n config system global\n set hostname demo_device1\n end\nRunning script(test-002) on DB success\n",
				"exec_time": "Thu Apr 16 07:58:49 2020",
				"log_id": 71,
				"script_name": "test-002"
			      },
			      "status": {
			        "code": 0,
				"message": "OK"
			      },
			      "url": "/dvmdb/adom/DEMO/script/log/output/device/demo_device1/logid/71"
			    }
			  ]
			}
      
How to create a CLI Script Group?
---------------------------------

To create the ``cli_group_001`` CLI Script Group in the ``dc_emea`` ADOM and
with the ``cli_script_001`` and ``cli_script_002`` members:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "set",
           "params": [
             {
               "data": {
                 "name": "cli_group_001",
                 "object member": [
                   {
                     "key": "cli_script_001",
                     "oid": 454
                   },
                   {
                     "key": "cli_script_002",
                     "oid": 455
                   }
                 ],
                 "target": "device_database",
                 "type": "cligrp"
               },
               "url": "/dvmdb/adom/dc_emea/script"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - You have to get the ``oid`` first for each CLI Script member
         
           .. dropdown:: Click to expand
              :color: info 
              :icon: chevron-down

              .. tab-set::
   
                 .. tab-item:: REQUEST
   
                    .. code-block:: json
   
                       {
                         "id": 3,
                         "method": "get",
                         "params": [
                           {
                             "fields": [
                               "name",
                               "oid"
                             ],
                             "filter": [
                               "name",
                               "like",
                               "cli_script_%"
                             ],
                             "url": "/dvmdb/adom/dc_emea/script"
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
                                 "name": "cli_script_001",
                                 "oid": 454,
                                 "script_schedule": null
                               },
                               {
                                 "name": "cli_script_002",
                                 "oid": 455,
                                 "script_schedule": null
                               }
                             ],
                             "status": {
                               "code": 0,
                               "message": "OK"
                             },
                             "url": "/dvmdb/adom/dc_emea/script"
                           }
                         ]
                       }
   
   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "name": "cli_group_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/dc_emea/script"
             }
           ]
         }