CLI Script management
=====================

.. warning::

   Starting with FortiManager 7.6.5 and 8.0.0 (# 1203111), CLI Scripts operations have 
   been redesigned. CLI Scripts are now saved in the ADOM DB and the main JSON 
   API endpoint is:

   .. code-block:: 

      /pm/config/adom/{adom}/obj/fmg/script

   This chapter hasn't been updated yet with the new details

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

It is best practise to wait for the task completion before ending the FMG JSON
RPC API session. 

Especially when the target is ``remote_device``; the task takes longer to complete and it requires a valid FMG JSON RPC API session.

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

How to add a CLI Script?
------------------------

Add a CLI Script to be executed against a Policy Package or the ADOM database
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to add the ``cli_script_001`` CLI Script into the ``demo`` ADOM; this CLI script targets Policy Package or ADOM database content:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block::
      
         {
           "id": 1,
           "method": "add",
           "params": [
             {
               "data": {
                 "content": "<your content>",
             	   "desc": "A CLI Script description",
                 "name": "cli_script_001",
                 "target": "adom_database",
                 "type": "cli"
               },
               "url": "/dvmdb/adom/demo/script"
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
               "data": {
                 "name": "cli_script_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/script"
             }
           ]
         }

Add a Jinja CLI Script to be executed against the ADOM database
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Starting FortiManager 7.6.4, you can add a Jinja CLI Script to be executed
against the ADOM database (ref: #1133295).

The following example shows how to add the ``cli_script_001`` CLI Script into the ``demo`` ADOM; this CLI script targets Policy Package or ADOM database content:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block::
      
         {
           "id": 1,
           "method": "add",
           "params": [
             {
               "data": {
                 "content": "<your content>",
             	   "desc": "A Jinja CLI Script description",
                 "name": "cli_script_001",
                 "target": "adom_database",
                 "type": "jinja"
               },
               "url": "/dvmdb/adom/demo/script"
             }
           ],
           "session": "{{session}}"
         }
      
   .. tab-item:: RESPONSE

      .. code-block::

         {
           "id": 149,
           "result": [
             {
               "data": {
                 "name": "cli_script_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/script"
             }
           ]
         }

How to run a CLI Script against a Policy Package?
-------------------------------------------------

The following example shows how to run the ``script_001`` CLI Script against the ``pkg_001`` Policy Package in the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
      	   "id": 1,
           "method": "exec",
      		 "params": [
      		   {
      		     "data": {
      		       "adom": "demo",
      			     "package": "pkg_001",
      			     "script": "script_001"
      		     },
      		     "url": "/dvmdb/adom/demo/script/execute"
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
                 "task": 452
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/script/execute"
             }
           ]
         }

How to run a Jinja CLI Script against a Policy Package?
-------------------------------------------------------

The following example shows how to run the ``cli_script_001`` CLI Script against the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
      	   "id": 1,
           "method": "exec",
      		 "params": [
      		   {
      		     "data": {
      		       "adom": "demo",
      			     "script": "cli_script_001"
      		     },
      		     "url": "/dvmdb/adom/demo/script/execute"
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
                 "task": 1217
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/script/execute"
             }
           ]
         }

How to run a CLI Script against a device?
-----------------------------------------

The following example shows how to run the ``script_001`` CLI Script against 
the ``dev_001`` device in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
         
         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "demo",
                 "scope": [
                   {
                     "name": "dev_001",
                     "vdom": "global"
                   }
                 ],
                 "script": "script_001"
               },
               "url": "/dvmdb/adom/demo/script/execute"
             }
           ],
           "session": "{{session}}"
         }
      
      .. note:: 
      
         - A CLI Script cannot be run against a VDOM scope; this is why we set 
           the ``vdom`` attribute to ``global``
         - But why don't you simply omit the ``vdom`` attribute in this case?
         - Because when you don't specify the ``vdom`` attribute, FortiManager 
           considers that you're targeting a Device Group
  
   .. tab-item:: RESPONSE

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
      	       "url": "/dvmdb/adom/demo/script/execute"
      	     }
      	   ]
      	 }
      
      .. warning:: 
      
         - If your CLI Script is with the *Remote FortiGate Directly (via CLI)*
           target and if you're getting a sucessful API response (as shown 
           above with the returned task ID), but the task itself fails with an 
           error message like *Error while reading script from database*, then 
           please make sure you maintain the API session open during the CLI 
           script execution (just follow the task progress using a ``get`` on 
           ``/task/task/{task_id}``)
      
You can run a CLI script against multiple devices using a single API call.

The following example shows how to run the ``script_001`` CLI Script against the ``dev_001`` and ``dev_002`` devices in the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
      	 {
      	   "id": 1,
      		  "method": "exec",
      		  "params": [
      		    {
      		      "data": {
      		        "adom": "demo",
            			"scope": [
            			  {
      			          "name": "dev_001",
            			    "vdom": "global"
            			  },
      			        {
      			          "name": "dev_002",
            			    "vdom": "global"
             			  }
            			],
            			"script": "script_001"
      		      },
      		      "url": "/dvmdb/adom/demo/script/execute"
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
                 "task": 458
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/script/execute"
             }
           ]
         }

You can run a CLI Script against one or multiple Device Groups.

By convention, if a ``scope`` entry only contains a ``name`` and no ``vdom`` attribute, then the ``name`` is considered as a Device Group name.

The following example shows how to run the ``script_001`` against the ``dev_grp_001`` and ``dev_grp_002`` in the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "demo",
                 "scope": [
                   {
                     "name": "dev_grp_001"
                   },
                   {
                     "name": "dev_grp_002"
                   }
                 ],
                 "script": "script_001"
               },
               "url": "/dvmdb/adom/demo/script/execute"
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
      
How to run a CLI Script against a Provisioning Template?
--------------------------------------------------------

Captured in #0209576.

You can run a CLI Script against any Provisioning Template.

However, this operation is only supported via the API.

For example, you can execute a CLI Script on a System Template or a FortiSwitch
Template.

How to run a CLI script against an IPsec Tunnel Template?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. Create a CLI Script (target = *Policy & Objects or ADOM Database*)

   This is the CLI Script used in this example:

   .. code-block:: text

      config vpn ipsec phase1-interface
          edit "HUB1-VPN1"
              set interface "port1"
              set ike-version 2
              set proposal aes256-sha256
              set peertype any
              set mode-cfg enable
              set localid "local_id_001"
              set remote-gw 10.0.0.3
              set net-device enable
              set add-route disable
              set psksecret foobar
              set network-overlay enable
              set network-id 1
          next
      end

   .. note::

      This CLI script appears to include all the required attributes. For 
      example, if the ``psksecret`` attribute is not specified, the script will 
      fail.

      If you're unsure which attributes are mandatory, you can use the
      FortiManager GUI to create a new IPsec Tunnel Template. Then, use the
      FortiManager CLI to view the corresponding CLI version with the following
      command:

      .. tab-set::
         
         .. tab-item:: CLI command
          
            .. code-block:: text

               execute fmpolicy print-adom-package demo 23 6076 all HUB1-VPN1

         .. tab-item:: CLI output

            .. code-block:: text

               Dump object [HUB1-VPN1] of category [vpn ipsec phase1-interface] in adom [demo] package [6076]:
               ---------------
               config vpn ipsec phase1-interface
               edit "HUB1-VPN1"
               set interface "port1"
               set ike-version 2
               set proposal aes256-sha256
               set peertype any
               set mode-cfg enable
               set localid "local_id_001"
               set remote-gw 10.0.0.3
               set net-device enable
               set add-route disable
               set psksecret ********
               set network-overlay enable
               set network-id 1
               
               next
               
               end
               
               Dump object [HUB1-VPN1] of category [vpn ipsec phase2-interface] in adom [demo] package [6076]:
               ---------------
               config vpn ipsec phase2-interface
               edit "HUB1-VPN1"
               set phase1name "HUB1-VPN1"
               set proposal aes256-sha256
               set auto-negotiate enable
               
               next
               
               end         

#. Find the *oid* of the destination IPsec Tunnel Template

   It will be used as the target of the CLI Script execution.

   Following example shows how to get the *oid* of the    
   ``ipsec_tunnel_template_001`` IPsec Tunnel Template in the ``demo`` ADOM:

   - Enter following FortiManager CLI command:

     .. code-block:: text

        execute fmpolicy print-adom-package demo 23 ?

   - You should get the following output:

     .. code-block:: text

              ID        <package name>
            5950        name=IPsec_Fortinet_Recommended, pathname=IPsec_Fortinet_Recommended
            5954        name=BRANCH_IPsec_Recommended, pathname=BRANCH_IPsec_Recommended
            5960        name=HUB_IPsec_Recommended, pathname=HUB_IPsec_Recommended
            6076        name=ipsec_tunnel_template_001, pathname=ipsec_tunnel_template_001
        
   .. note::

      - The *oid* of the ``ipsec_tunnel_template_001`` IPsec Tunnel Template 
        is ``6076``

#. Put the ADOM name, package oid (IPsec Tunnel Template oid) and CLI script 
   name into your |fmg_api| request:

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json

            {
              "id": 3,
              "method": "exec",
              "params": [
                {
                  "data": {
                    "adom": "demo",
                    "package": 6076,
                    "script": "script_001"
                  },
                  "url": "/dvmdb/adom/demo/script/execute"
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
                    "task": 1120
                  },
                  "status": {
                    "code": 0,
                    "message": "OK"
                  },
                  "url": "/dvmdb/adom/demo/script/execute"
                }
              ]
            }

#. Check script log for its execution history

   .. code-block:: text

      -------Executing time: Thu Apr 24 07:41:12 2025-----------
      
      
      
      Starting log (Run on database)
      
      config vpn ipsec phase1-interface
      edit "HUB1-VPN1"
      set interface "port1"
      set ike-version 2
      set proposal aes256-sha256
      set peertype any
      set mode-cfg enable
      set localid local_id_001
      set remote-gw 10.0.0.3
      set net-device enable
      set add-route disable
      set psksecret ******
      set network-overlay enable
      set network-id 1
      next
      end
      Running script(script_001) on DB success
      
      ----------------End of Log-------------------------

How to run a CLI script against a SD-WAN Template?
++++++++++++++++++++++++++++++++++++++++++++++++++

#. Create a CLI Script (target = *Policy & Objects or ADOM Database*)

   This is the CLI Script used in this example:

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

#. Find the *oid* of the destination SD-WAN Template

   It will be used as the target of the CLI Script execution.

   Following example shows how to get the *oid* of the ``sdwan_template_001`` 
   SD-WAN Template in the ``demo`` ADOM:

   - Enter following FortiManager CLI command:

     .. code-block:: text

        execute fmpolicy print-adom-package demo 11 ?

   - You should get the following output:

     .. code-block:: text

          ID	<package name>
        5168	name=sdwan_template_001, pathname=sdwan_template_001

   .. note::

      - The *oid* of the ``sdwan_template_001`` SD-WAN Template is ``5168``

#. Put the ADOM name, package oid (SD-WAN Template oid) and CLI script name into
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
                  "url": "/dvmdb/adom/demo/script/execute"
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
                  "url": "/dvmdb/adom/demo/script/execute"
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

How to run a CLI Script against a System Template?
++++++++++++++++++++++++++++++++++++++++++++++++++

#. Create a CLI Script (target = *Policy & Objects or ADOM Database*)

   This is the CLI Script used in this example:

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

#. Find the *oid* of the target System Template

   - Enter the following FortiManager CLI command:

     .. code-block:: text
    
        executee fmpolicy print-adom-package demo 5 ?

   - You should get the following output:

     .. code-block:: text

          ID        <package name>
        3059        name=system_template_001, pathname=system_template_001

     .. note::
  
        - The *oid* of the ``system_template_001`` System Template is ``3059``

#. Put the ADOM name, package oid (System Template oid) and CLI Script name 
   into your |fmg_api| request:
   
   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json
         	
            {
              "id": 16,
              "method": "exec",
              "params": [
                {
                  "data": {
                    "adom": "demo",
                    "package": 3059,
                    "script": "script_001"
                  },
                  "url": "dvmdb/adom/demo/script/execute"
                }
              ],
              "session": "{{session}}"
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
                  "url": "dvmdb/adom/demo/script/execute"
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
      Running script(script_001) on DB success
   
      ----------------End of Log-------------------------

How to run a CLI Script against a FortiSwitch Template?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. Create a CLI Script (target = *Policy & Objects or ADOM Database*)

   This is the CLI Script used in this example:

   .. code-block:: text
   
      config fsp managed-switch
          edit "S248DF3X15000011"
              set name "S248DF3X15000011"
              set platform "FortiSwitch-248D-FPOE"
              set template "managed_fsw1"
          next
      end
   
#. Find the *oid* of the target FortiSwitch Template

   - Run the following FortiManager CLI command:

     .. code-block:: text
      
        execute fmpolicy print-adom-package demo 12 ?

   - You should get the following output:

     .. code-block:: text

          ID        <package name>
        3714        name=fsw_template_001, pathname=fsw_template_001

     .. note::
  
        - The *oid* of the ``fsw_template_001`` FortiSwitch Template is 
          ``3714``

#. Put the ADOM name, package oid (FortiSwitch Template oid) and CLI Script 
   name into your |fmg_api| request:

   .. tab-set::
     
      .. tab-item:: REQUEST

         .. code-block:: json
         	
            {
              "id": 16,
              "method": "exec",
              "params": [
                {
                  "data": {
                    "adom": "demo",
                    "package": 3714,
                    "script": "script_001"
                  },
                  "url": "dvmdb/adom/demo/script/execute"
                }
              ],
              "session": "{{session}}"
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
                  "url": "dvmdb/adom/demo/script/execute"
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
      Running script(script_001) on DB success
   
      ----------------End of Log-------------------------

How to run a CLI Script against a FortiAP Profile?
++++++++++++++++++++++++++++++++++++++++++++++++++

#. Create a CLI Script (target = *Policy & Objects or ADOM Database*)

   This is the CLI Script used in this example:

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
   
#. Find the *oid* of the target FortiAP Profile

   - Enter the following FortiManager CLI command:

     .. code-block:: text
     
        execute fmpolicy print-adom-package demo 10 ?

   - You should get the following output:

     .. code-block:: text
              
          ID        <package name>
        3065        name=fap_template_001, pathname=fap_template_001

     .. note::
  
        - The *oid* of the ``fap_template_001`` FortiAP Template is 
          ``3065``

#. Put the ADOM name, package oid (FortiAP Template oid) and CLI Script name 
   into your |fmg_api| request:

   .. tab-set::

      .. tab-item:: REQUEST

         .. code-block:: json
         	
            {
              "id": 16,
              "method": "exec",
              "params": [
                {
                  "data": {
                    "adom": "demo",
                    "package": 3065,
                    "script": "script_001"
                  },
                  "url": "dvmdb/adom/demo/script/execute"
                }
              ],
              "session": "{{session}}"
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
                  "url": "dvmdb/adom/demo/script/execute"
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
      Running script(script_001) on DB success
      
      ----------------End of Log-------------------------

How To get the latest CLI Script execution output?
--------------------------------------------------

For a CLI Script executed against a Policy Package
++++++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to get the latest CLI Script execution output in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
      		{
      		  "id": 1,
      		  "method": "get",
      		  "params": [
      		    {
      		      "url": "/dvmdb/adom/demo/script/log/latest"
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
                 "content": "\n\nStarting log (Run on database)\n\n config firewall policy\n edit \"2\"\n set _scope \"demo_device1\"-\"root\"\n next\n end\nRunning script(test-001) on DB success\n",
                 "exec_time": "Wed Apr 15 13:48:07 2020",
                 "log_id": 41,
                 "script_name": "script_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/script/log/latest"
             }
           ]
         }
                        
For a CLI Script executed against a specific device
+++++++++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to get the latest CLI Script execution output for the ``dev_001`` device in the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
      		{
      		  "id": 1,
      		  "method": "get",
      		  "params": [
      		    {
      		      "url": "/dvmdb/adom/demo/script/log/latest/device/dev_001"
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
                 "content": "\n\nStarting log (Run on database)\n\n config system global\n set hostname demo_device1\n end\nRunning script(test-002) on DB success\n",
                 "exec_time": "Thu Apr 16 07:58:49 2020",
                 "log_id": 71,
                 "script_name": "script_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/script/log/latest/device/dev_001"
             }
           ]
         }        

How to get a specific CLI Script execution output?
--------------------------------------------------

#. First you need to get its corresponding ``log_id`` by retrieving a
   summary of the execution list

   - For CLI Scripts run against *Policy Packages*:

     .. tab-set::

        .. tab-item:: REQUEST

           .. code-block:: json
      
      		     {
      		       "id": 1,
         	       "method": "get",
      		       "params": [
      		         {
      		           "url": "/dvmdb/adom/demo/script/log/summary"
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
                    "data": [
                      {
                        "exec_time": "Wed Apr 15 13:48:07 2020",
                        "log_id": 41,
                        "script_name": "script_001",
                        "seq": 1
                      },
                      {
                        "exec_time": "Wed Apr 15 13:44:50 2020",
                        "log_id": 31,
                        "script_name": "script_002",
                        "seq": 2
                      }
                    ],
                    "status": {
                      "code": 0,
                      "message": "OK"
                    },
                    "url": "/dvmdb/adom/demo/script/log/summary"
                  }
                ]
              }

   - For CLI Scripts run against a specific device:

     .. tab-set::

        .. tab-item:: REQUEST

           .. code-block:: json
      
      		     {
      		       "id": 1,
      		       "method": "get",
      		       "params": [
      		         {
      			         "url": "/dvmdb/adom/demo/script/log/summary/device/dev_001"
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
                    "data": [
                      {
                        "exec_time": "Thu Apr 16 07:58:49 2020",
                        "log_id": 71,
                        "script_name": "script_001",
                        "seq": 1
                      }
                    ],
                    "status": {
                      "code": 0,
                      "message": "OK"
                    },
                    "url": "/dvmdb/adom/demo/script/log/summary/device/demo_device1"
                  }
                ]
              }

   .. note::

      Note that the returned ``log_id`` will have the following format:

      - If CLI Script is executed against Device DB or Policy Package:

      	.. code-block::
      
      	   log_id = str(task_id) + "1"

      - If CLI Script is executed against the remote device:
	
      	.. code-block::
      
      	   log_id = str(task_id) + "0"

      where ``task_id`` is the task ID returned at the time the CLI Script 
      execution was triggered.
	 
#. Now you can retrieve the CLI Script output using one of the returned 
   ``log_id``

   - For a CLI Script run against a Policy Package

     .. tab-set::

        .. tab-item:: REQUEST

           .. code-block:: json

              {
                "id": 1,
                "method": "get",
                "params": [
                  {
                    "url": "/dvmdb/adom/demo/script/log/output/logid/41"
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
                      "content": "\n\nStarting log (Run on database)\n\n config firewall policy\n edit \"2\"\n set _scope \"demo_device1\"-\"root\"\n next\n end\nRunning script(test-001) on DB success\n",
                      "exec_time": "Wed Apr 15 13:48:07 2020",
                      "log_id": 41,
                      "script_name": "script_001"
                    },
                    "status": {
                      "code": 0,
                      "message": "OK"
                    },
                    "url": "/dvmdb/adom/demo/script/log/output/logid/41"
                  }
                ]
              }                

   - For a CLI script run against a specific device

     .. tab-set::

        .. tab-item:: REQUEST

           .. code-block:: json

              {
                "id": 1,
                "method": "get",
                "params": [
                  {
                    "url": "/dvmdb/adom/demo/script/log/output/device/dev_001/logid/71"
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
                      "content": "\n\nStarting log (Run on database)\n\n config system global\n set hostname demo_device1\n end\nRunning script(test-002) on DB success\n",
                      "exec_time": "Thu Apr 16 07:58:49 2020",
                      "log_id": 71,
                      "script_name": "script_001"
                    },
                    "status": {
                      "code": 0,
                      "message": "OK"
                    },
                    "url": "/dvmdb/adom/demo/script/log/output/device/dev_001/logid/71"
                  }
                ]
              }            

#. If you have the feeling that your resulting script output is truncated, then
   this is normal!

   - By default, FortiManager enforces a per-device limit of 100K:

     .. code-block:: text
  
        config system dm
            set script-logsize 100
        end

   - You can change the max to up 10000K

How to create a CLI Script Group?
---------------------------------

The following example shows how to create the ``cli_script_grp_001`` CLI Script 
Group in the ``demo`` ADOM. 

It contains the ``script_001`` and ``script_001`` CLI Script members:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "set",
           "params": [
             {
               "data": {
                 "name": "cli_script_grp_001",
                 "object member": [
                   {
                     "key": "script_001",
                     "oid": 454
                   },
                   {
                     "key": "script_002",
                     "oid": 455
                   }
                 ],
                 "target": "device_database",
                 "type": "cligrp"
               },
               "url": "/dvmdb/adom/demo/script"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - You have to get the ``oid`` first for each CLI Script member
         - For instance:
         
           .. dropdown:: Click to expand
              :color: primary
              :icon: chevron-up

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
                               "script_%"
                             ],
                             "url": "/dvmdb/adom/demo/script"
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
                                 "name": "script_001",
                                 "oid": 454,
                                 "script_schedule": null
                               },
                               {
                                 "name": "script_002",
                                 "oid": 455,
                                 "script_schedule": null
                               }
                             ],
                             "status": {
                               "code": 0,
                               "message": "OK"
                             },
                             "url": "/dvmdb/adom/demo/script"
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
                 "name": "cli_script_grp_001"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/script"
             }
           ]
         }

How to get the CLI Script scheduling details for a given managed FortiGate?
---------------------------------------------------------------------------

Caught in #1222086 (FortiManager 8.0.0).

The following example shows how to get the CLI Script scheduling details for the
``dev_00`` managed FortiGate in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/dvmdb/adom/demo/script/schedule/device/dev_001"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 44,
           "result": [
             {
               "data": [
                 {
                   "filter_build": -1,
                   "filter_device": 0,
                   "filter_ostype": 0,
                   "filter_osver": -1,
                   "members": [],
                   "name": "cli_script_001",
                   "oid": 42683,
                   "schedules": [
                     {
                       "datetime": "",
                       "day_of_week": 0,
                       "device": 6583,
                       "run_on_db": 0,
                       "timestamp": 1764595475,
                       "type": 1,
                       "user": "admin"
                     }
                   ],
                   "target": 1,
                   "timestamp": 1764595475,
                   "type": 1
                 },
                 {
                   "filter_build": -1,
                   "filter_device": 0,
                   "filter_ostype": 0,
                   "filter_osver": -1,
                   "members": [],
                   "name": "cli_script_002",
                   "oid": 42685,
                   "schedules": [
                     {
                       "datetime": "",
                       "day_of_week": 0,
                       "device": 6583,
                       "run_on_db": 0,
                       "timestamp": 1764768766,
                       "type": 4,
                       "user": "admin"
                     }
                   ],
                   "target": 1,
                   "timestamp": 1764595974,
                   "type": 1
                 },
                 {
                   "filter_build": -1,
                   "filter_device": 0,
                   "filter_ostype": 0,
                   "filter_osver": -1,
                   "members": [],
                   "name": "cli_script_003",
                   "oid": 42687,
                   "schedules": [
                     {
                       "datetime": "",
                       "day_of_week": 0,
                       "device": 6583,
                       "run_on_db": 0,
                       "timestamp": 1765546258,
                       "type": 2,
                       "user": "admin"
                     }
                   ],
                   "target": 1,
                   "timestamp": 1764596005,
                   "type": 1
                 },
                 {
                   "filter_build": -1,
                   "filter_device": 0,
                   "filter_ostype": 0,
                   "filter_osver": -1,
                   "members": [],
                   "name": "cli_script_004",
                   "oid": 42689,
                   "schedules": [
                     {
                       "datetime": "",
                       "day_of_week": 0,
                       "device": 6583,
                       "run_on_db": 0,
                       "timestamp": 1765028180,
                       "type": 5,
                       "user": "admin"
                     }
                   ],
                   "target": 0,
                   "timestamp": 1764596186,
                   "type": 1
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/dvmdb/adom/demo/script/schedule/device/dev_001"
             }
           ]
         }

      .. note::

         By testing multiple schedule types, the following meanings for the 
         ``type`` field in the returned ``schedules`` dictionary have been 
         identified: 

         - ``1``: Install schedule; the CLI script is executed at each 
           installation. 
         - ``2``: One-time schedule. 
         - ``3``: Recurring daily schedule.
	       - ``4``: Recurring weekly schedule.
         - ``5``: Recurring monthly schedule.
