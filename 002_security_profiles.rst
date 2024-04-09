Security Profiles
=================

URL Filtering
-------------

Webfilter urlfilter
+++++++++++++++++++

This section is for the ``webfilter.urlfilter``  object.

How to add a new entry in a webfilter.urlfilter.entries?
________________________________________________________

Goal is to add a new entry without overwritting the existing ones.

To add a new entry ``www.url-003.com`` in the ``webfilter.urlfilter`` named
``urlfilter_001``, with ID ``1``, in ADOM ``dc_emea``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": {
           "url": "www.url-003.com"
         },
         "url": "/pm/config/adom/dc_emea/obj/webfilter/urlfilter/1/entries"
       }
     ],
     "session": "GcpTJdkN8A0VwkAQF+zBA70wdh7B+Qe3tZoGil4lR+rQlrUhy0nOjNeoJLKyQb/CgdXmuA8i5omm4WV/dE7cQw=="
   }

.. note::

   - The ``webfilter.urlfilter`` ``urlfilter_001`` cannot be used as master key;
     its ID ``1`` has to be used instead

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": {
           "id": 4
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/dc_emea/obj/webfilter/urlfilter/1/entries"
       }
     ]
   }

How to delete an entry in a webfilter.urlfilter. entries?
_________________________________________________________

Goal is to delete an existing entry without overwritting the existing ones.

To delete entry ``www.url-003.com`` with ID ``4``, in the
``webfilter.urlfilter`` named ``urlfilter_001``, with ID ``1``, in ADOM
``dc_emea``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "delete",
     "params": [
       {
         "url": "/pm/config/adom/dc_emea/obj/webfilter/urlfilter/1/entries/4"
       }
     ],
     "session": "GcpTJdkN8A0VwkAQF+zBA70wdh7B+Qe3tZoGil4lR+rQlrUhy0nOjNeoJLKyQb/CgdXmuA8i5omm4WV/dE7cQw=="
   }

.. note::

   - The ``webfilter.urlfilter`` ``urlfilter_001`` cannot be used as master key;
     its ID ``1`` has to be used instead
   - The ``webfilter.urlfilter.entries`` ``www.url-003.com`` cannot be used as a
     master key; its ID ``4`` has to be used instead.

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/dc_emea/obj/webfilter/urlfilter/1/entries/3"
       }
     ]
   }

Web rating overrides
++++++++++++++++++++

This section is for the ``webfilter.ftgd-local-rating`` objects.

How to add a new web rating override?
_____________________________________

To add a new web rating override in ADOM ``dc_amer``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": {
           "comment": "Test #003",
           "rating": [
             "96"
           ],
           "status": "enable",
           "url": "www.url-003.com"
         },
         "url": "/pm/config/adom/dc_amer/obj/webfilter/ftgd-local-rating"
       }
     ],
     "session": "6vRSrzLBbOj1JB0thRDB1/dzUETGtibb3oohHEPXs+ppbcq99CkWp33QZLWPwd9rmYgeRXYozeXNSLjUIb6pjQ=="
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": {
           "url": "www.url-003.com"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/dc_amer/obj/webfilter/ftgd-local-rating"
       }
     ]
   }  

Webfilter profile
+++++++++++++++++

This section is for the ``webfilter.profile``  object.

How to add a new filter in a webfilter profile?
_______________________________________________

Following example add a new filter to block category ``84`` (i.e., *Web-based
Applications*) from webfilter profile ``webfilter_profile_001`` in ADOM
``demo_002``.  

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "add",
     "params": [
       {
         "data": {
           "action": "block",
           "category": 84
         },
         "url": "/pm/config/adom/demo_002/obj/webfilter/profile/webfilter_profile_001/ftgd-wf/filters"
       }
     ],
     "session": "nRrJXLvH/kZVYQ9pnfTwCw3DrMKJENANTdyPjt8MLDBZC3xyuhoWpa2D7LpF1MVhYv7p9RZWPurYlMfLjPgaAw=="
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": {
           "id": 26
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/demo_002/obj/webfilter/profile/webfilter_profile_001/ftgd-wf/filters"
       }
     ]
   }

.. note::

  - Response contains the ``id`` of the created entry.

How to update a single filter in a webfilter profile?
_____________________________________________________

Goal is to just update a single filter from a Web Filter Profile.

For instance we want to update the filter with category *Potentially Liable* > *Extremist Groups* from its default ``warning`` to ``block`` in our Web Filter Profile ``web_filter_profile_001`` located in ADOM ``root``:

Before the change: ``action`` is ``warning``

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "url": "/pm/config/adom/root/obj/webfilter/profile/web_filter_profile_001/ftgd-wf/filters/7"
       }
     ],
     "session": "YW73rbdh9iDVDVh7EEu27igmT7sYZmHKeIli2wfe1NGwDuI+2OU3R1NwoWuID3JGzyfJEbhdyBJVCglYOVScJw==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 3,
     "result": [
       {
         "data": {
           "action": "warning",
           "category": [
             "12"
           ],
           "id": 7,
           "log": "enable",
           "oid": 3693,
           "warn-duration": "5m",
           "warning-prompt": "per-category"
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/root/obj/webfilter/profile/web_filter_profile_001/ftgd-wf/filters/7"
       }
     ]
   }

.. note:: 
  - The master key is the ``id`` attribute.
  - Here it is ``7`` and we used it in the ``get`` request to obtain the detail of this specific filter only
  - We will need it to perform the change as well.

We change the action to ``block``:

**REQUEST:**

.. code-block:: json

   {
     "id": 4,
     "method": "set",
     "params": [
       {
         "data": {
           "action": "block"
         },
         "url": "/pm/config/adom/root/obj/webfilter/profile/web_filter_profile_001/ftgd-wf/filters/7"
       }
     ],
     "session": "YW73rbdh9iDVDVh7EEu27igmT7sYZmHKeIli2wfe1NGwDuI+2OU3R1NwoWuID3JGzyfJEbhdyBJVCglYOVScJw=="
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 4,
     "result": [
       {
         "data": {
           "id": 7
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/root/obj/webfilter/profile/web_filter_profile_001/ftgd-wf/filters/7"
       }
     ]
   }

After the change: action is ``block``:

**REQUEST:**

.. code-block:: json

   {
     "id": 5,
     "method": "get",
     "params": [
       {
         "url": "/pm/config/adom/root/obj/webfilter/profile/web_filter_profile_001/ftgd-wf/filters/7"
       }
     ],
     "session": "YW73rbdh9iDVDVh7EEu27igmT7sYZmHKeIli2wfe1NGwDuI+2OU3R1NwoWuID3JGzyfJEbhdyBJVCglYOVScJw==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json
  
   {
     "id": 5,
     "result": [
       {
         "data": {
           "action": "block",
           "category": [
             "12"
           ],
           "id": 7,
           "log": "enable",
           "oid": 3693
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/root/obj/webfilter/profile/web_filter_profile_001/ftgd-wf/filters/7"
       }
     ]
   }

How to update a multiple categories in a webfilter profile?
___________________________________________________________

Goal is to just update multiple categories from a Web Filter Profile.

For instance we want the categories *Potentially Liable* > *Extremist
Groups* and *Potentially Liable* > *Hacking*  with ``action`` set to ``block``
in our Web Filter Profile ``web_filter_profile_001`` located in ADOM ``root``:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "set",
     "params": [
       {
         "data": [
           {
             "action": "block",
             "id": 7
           },
           {
             "action": "block",
             "id": 25
           }
         ],
         "url": "/pm/config/adom/root/obj/webfilter/profile/web_filter_profile_001/ftgd-wf/filters"
       }
     ],
     "session": "loEYHhY8MscMCCWAaiOzV2mPxJjU1gqDwAP+nnYIKEQFx43vth/D3ZQx4Yg5ZlGjQg1qtdHlctROIwLIDg+XBw=="
   }

**RESPONSE:**

.. code-block:: json
  
   {
     "id": 3,
     "result": [
       {
         "status": {
           "code": 0,  
           "message": "OK"
         },
         "url": "/pm/config/adom/root/obj/webfilter/profile/web_filter_profile_001/ftgd-wf/filters"
       }
     ]
   }

How to get the webfilter categories?
____________________________________

Caught in #0227646.

We can use the ``datasrc`` option as shown below:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "attr": "rating",
         "option": "datasrc",
         "url": "/pm/config/adom/root/obj/webfilter/ftgd-local-rating"
       }
     ],
     "session": "vivfIFW9y+mdCpWMh70rCuRoH8lcRTbRH2Zju7CpxePlzZddsRRp3ctkHlfY2GGWYBGnls3w77nUeLTt0nIZMA=="
   }

**RESPONSE:**

.. code-block:: 

   {
     "id": 3,
     "result": [
       {
         "data": {
           "webfilter categories": [
             {
               "id": "all",
               "obj description": "All Categories"
             },
             {
               "id": "g01",
               "obj description": "Potentially Liable"
             },
             {
               "id": "1",
               "obj description": "Drug Abuse"
             },
             [...],
                       {
               "id": "g21",
               "obj description": "Unrated"
             },
             {
               "id": "0",
               "obj description": "Unrated"
             },
             {
               "id": "g22",
               "obj description": "Local Categories"
             }
           ],
           "webfilter ftgd-local-cat": [
             {
               "desc": "custom1",
               "id": 140,
               "status": 1
             },
             {
               "desc": "custom2",
               "id": 141,
               "status": 1
             }
           ]
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/root/obj/webfilter/ftgd-local-rating"
       }
     ]
   }   

We can also use the ``get reserved`` option as shown below:

**REQUEST:**

.. code-block:: json

   {
     "id": 3,
     "method": "get",
     "params": [
       {
         "option": "get reserved",
         "url": "/pm/config/adom/root/obj/webfilter/categories"
       }
     ],
     "session": "jkdpxOcqKU/tuzAMPxljkMYY1/swAnbapm8MfdVOF+ME13i40+8v+63DQhX8KHSBK7+v2lqCcNSlSVYlwDzgTw=="
   }

**RESPONSE:**

.. code-block:: 

   {
     "id": 3,
     "result": [
       {
         "data": [
           {
             "id": "all",
             "obj description": "All Categories"
           },
           {
             "id": "g01",
             "obj description": "Potentially Liable"
           },
           {
             "id": "1",
             "obj description": "Drug Abuse"
           },
           [...]
           {
             "id": "g21",
             "obj description": "Unrated"
           },
           {
             "id": "0",
             "obj description": "Unrated"
           },
           {
             "id": "g22",
             "obj description": "Local Categories"
           }
         ],
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/root/obj/webfilter/categories"
       }
     ]
   }

The dnsfilter domain-filter object
++++++++++++++++++++++++++++++++++

The ``dnsfilter.domain-filter`` used by the ``dnsfilter.profile`` is the
counterpart of the ``webfilter.urlfilter`` used by the ``webfilter.profile``.

How to empty the ``dnsfilter.domain-filter.entries`` table?
___________________________________________________________

You can use the |json_rpc_m| ``update`` or ``set`` as shown below:

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "update",
           "params": [
             {
               "data": {
                 "entries": []
               },
               "url": "/pm/config/adom/dc_amer/obj/dnsfilter/domain-filter/2"
             }
           ],
           "session": "{{ session }}"
         }        

   .. tab:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "id": 2
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/dc_amer/obj/dnsfilter/domain-filter/2"
             }
           ]
         }
              
Application Control Management
------------------------------

How to get the list of all applications?
++++++++++++++++++++++++++++++++++++++++

We can use any of those URL

.. code-block::

   pm/config/global/_application/list
   pm/config/global/obj/_application/list
   pm/config/adom/<adom>/_application/list
   pm/config/adom/<adom>/obj/_application/list
   pm/config/device/<device>/global/_application/list
   pm/config/device/<device>/_application/list
   pm/config/device/<device>/vdom/<vdom>/_application/list

For instance:

**REQUEST**:

.. code-block:: json

   {
     "id": 1, 
     "jsonrpc": "1.0", 
     "method": "get", 
     "params": [
       {
         "url": "/pm/config/adom/CM-LAB-001/_application/list"
       }
     ], 
     "session": "NFqDRmsSz8tdxPZ7TPLdPCewoXS8Tz/vvZyOXera6CVntGsNHbElddvtyW/gAdmacfrYsoyaQsAaIktFwQm2dmRfUocs1u4B", 
     "verbose": 1
   }

**RESPONSE**:

.. code-block::

   {
     "id": 1, 
     "result": [
       {
         "data": [
           {
             "behavior": "", 
             "cat-id": "21", 
             "category": "Email", 
             "id": "16554", 
             "language": "Chinese", 
             "name": "126.Mail", 
             "parameter": "", 
             "popularity": "4.low", 
             "protocol": "1.TCP, 9.HTTP, 26.SSL", 
             "require_ssl_di": "No", 
             "risk": "3.low", 
             "shaping": "0", 
             "sub-cat-id": "0", 
             "sub-category": "(null)", 
             "technology": "1.Browser-Based", 
             "vendor": "9.Netease", 
             "weight": "10"
           }, 
   [...]

How to get the list of Application Categories?
++++++++++++++++++++++++++++++++++++++++++++++

Caught in #0278734.

We can use either of those URLs:

- ``pm/config/adom/<adom>/_category/list``
- ``pm/config/adom/<adom>/obj/_category/list``

To get some output, the ADOM has to contains a real device.

If your ADOM doesn't have yet any real devices or only has Model
Devices, the output will be null. 

**REQUEST:**

.. code:: json
	  
	  {
	    "id": 1, 
	    "method": "get", 
	    "params": [
	      {
	        "url": "pm/config/adom/ADOM_54_001/obj/_category/list"
	      }
	    ], 
	    "session": "xkULr1ot8oq+HnVLlrxVC9KafsiO+ZvtU0Uot+LlueIqDegtqIw9W0lYSF1YkyUgCHLH/PxwnSmCjnfuLPoZrQ==", 
	    "verbose": 1
	  }

**RESPONSE:**

.. code:: json

	  {
	    "id": 1, 
	    "result": [
	      {
	        "data": [
		  {
		    "id": 19, 
		    "name": "\"Botnet\""
		  }, 
		  {
		    "id": 29, 
		    "name": "\"Business\""
		  }, 
		  {
		    "id": 30, 
		    "name": "\"Cloud.IT\""
		  }, 
	          {
		    "id": 5, 
		    "name": "\"Video/Audio\""
		  }, 
		  {
		    "id": 3, 
		    "name": "\"VoIP\""
		  }, 
		  {
		    "id": 25, 
		    "name": "\"Web.Client\""
		  }
	        ], 
		"status": {
		  "code": 0, 
		  "message": "OK"
		}, 
		"url": "pm/config/adom/ADOM_54_001/_category/list"
	      }
	    ]
	  }

Please also consider the new information from #0370036.

.. code::

   1) JSON API changes:
   a) The following 3 JSON API:
   firewall/service/predefined (this one should be deleted)
   ips/sensor/entries/protocol
   ips/sensor/entries/application
   Will merge into one:
   _data/reserved/<mapping_name>
   b) New category: application/categories,
   also "webfilter/categories", etc...
   can be get by the new JSON API:
   _data/reserved/application/categories
   _data/reserved/webfilter/categories
   c) The old JSON API:
   _category/list
   will be kept which will return the DB calculated category list.

How to create a new Custom Application Signature?
+++++++++++++++++++++++++++++++++++++++++++++++++

To add a new ``APP_SIG_002`` Custom Application Signature in ``dc_africa`` ADOM:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "set",
           "params": [
             {
               "data": {
                 "comment": null,
                 "signature": "F-SBID (--app_cat 36; --name \"Front.FP30reg.Chunked.Overflow TEst\"; --protocol tcp; --service HTTP; --flow from_client; --parsed_type HTTP_POST; --pattern \"/vti_bin/_vti_aut/fp30reg.dll\"; --context uri; --no_case; --parsed_type HTTP_CHUNKED; )",
                 "tag": "APP_SIG_002"
               },
               "url": "pm/config/adom/dc_africa/obj/application/custom"
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
                 "tag": "APP_SIG_002"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "pm/config/adom/dc_africa/obj/application/custom"
             }
           ]
         }        

DLP Profile Management
----------------------

How to add a new DLP File Pattern?
++++++++++++++++++++++++++++++++++

Caught in #594984.

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "add",
           "params": [
             {
               "url": "pm/config/adom/root/obj/dlp/filepattern",
               "data": {
                 "name": "test",
                 "id": 0,
                 "entries": [
                   {
                     "file-type": 64,
                     "filter-type": 1,
                     "pattern": "Test"
                   }
                 ]
               }
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
                 "id": 3
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "pm/config/adom/root/obj/dlp/filepattern"
             }
           ]
         }

How to get DLP elements from FortiGuard DB?
+++++++++++++++++++++++++++++++++++++++++++

Caught in #0966060.

How to get DLP sensors from FortiGuard DB?
__________________________________________

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "pm/config/adom/root/_fdsdb/dlp/sensor"
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
                   "comment": "Canadian Health Information Act (HIA) Sensor",
                   "entries": "[ { \"dictionary\": \"can-pass-dict\", \"count\": 5 }, { \"dictionary\": \"can-natl_id-sin-dict\", \"count\": 5 }, { \"dictionary\": \"can-phin-dict\", \"count\": 5 }, { \"dictionary\": \"can-health_service-dict\", \"count\": 5 } ]",
                   "eval": "",
                   "match-type": "any",
                   "name": "can-hia"
                 },
                 {
                   "comment": "Canadian Personal Identifiable Information (PII) Sensor",
                   "entries": "[ { \"dictionary\": \"can-dl-dict\", \"count\": 5 }, { \"dictionary\": \"can-natl_id-sin-dict\", \"count\": 5 }, { \"dictionary\": \"can-pass-dict\", \"count\": 5 }, { \"dictionary\": \"can-health_service-dict\", \"count\": 5 }, { \"dictionary\": \"can-bank_account-dict\", \"count\": 5 }, { \"dictionary\": \"can-phin-dict\", \"count\": 5 } ]",
                   "eval": "",
                   "match-type": "any",
                   "name": "can-pii"
                 },
                 {
                   "comment": "Source Code Sensor",
                   "entries": "[ { \"dictionary\": \"source_code-python\", \"count\": 5 }, { \"dictionary\": \"source_code-c\", \"count\": 5 }, { \"dictionary\": \"source_code-java\", \"count\": 5 } ]",
                   "eval": "",
                   "match-type": "any",
                   "name": "source_code"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "pm/config/adom/root/_fdsdb/dlp/sensor",
               "version": "1.41"
             }
           ]
         }

How to get DLP dictionnaries from FortiGuard DB?
________________________________________________

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "pm/config/adom/root/_fdsdb/dlp/dictionary"
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
                   "comment": "EICAR Test File for DLP",
                   "entries": "[ { \"type\": \"keyword\", \"pattern\": \"X5O!P%@AP[4\\\\PZX54(P^)7CC)7}$EICAR-STANDARD-DLP-TEST-FILE!$H+H*\", \"ignore-case\": 0, \"repeat\": 1 } ]",
                   "match-type": "any",
                   "name": "EICAR-TEST-FILE"
                 },
                 {
                   "comment": "",
                   "entries": "[ { \"type\": \"regex\", \"pattern\": \"Social Insurance (Number|Card)\", \"ignore-case\": 1, \"repeat\": 0 }, { \"type\": \"keyword\", \"pattern\": \"sin\", \"ignore-case\": 1, \"repeat\": 0 }, { \"type\": \"keyword\", \"pattern\": \"sic\", \"ignore-case\": 1, \"repeat\": 0 }, { \"type\": \"keyword\", \"pattern\": \"sin#\", \"ignore-case\": 1, \"repeat\": 0 }, { \"type\": \"keyword\", \"pattern\": \"social insurance\", \"ignore-case\": 1, \"repeat\": 0 } ]",
                   "match-type": "any",
                   "name": "can-natl_id-pk"
                 },
                 {
                   "comment": "Canadian SIN Card Number Dictionary",
                   "entries": "[ { \"type\": \"can-natl_id-sin\", \"pattern\": \"\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"can-natl_id-prox\", \"pattern\": \"\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"luhn-algo\", \"pattern\": \"\\\\b\\\\d{3}[- ]?\\\\d{3}[- ]?\\\\d{3}\\\\b\", \"ignore-case\": 0, \"repeat\": 1 } ]",
                   "match-type": "all",
                   "name": "can-natl_id-sin-dict"
                 },
                 {"...": "..."},
                 {
                   "comment": "Python Source Code Dictionary",
                   "entries": "[ { \"type\": \"keyword\", \"pattern\": \"@staticmethod\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^from\\\\s(\\\\w.+)\\\\simport\\\\s\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"lambda\\\\s(.+):\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \":\\\\s*(continue|yield|await)\\\\s\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*class\\\\s(\\\\w+?):$\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*(try|finally)\\\\s*:$\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*except\\\\s*(Exception|\\\\w+Error\\\\sas\\\\s\\\\w+)\\\\s*:$\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^import\\\\s[\\\\w,]+$\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^if\\\\s__name__\\\\s*==\\\\s*[\\\"']__main__[\\\"']\\\\s*:$\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*(async\\\\s)?def\\\\s*(\\\\w+?)\\\\(([\\\\w,*\\\\s=\\\"']*?)\\\\):$\\/m\", \"ignore-case\": 0, \"repeat\": 1 } ]",
                   "match-type": "any",
                   "name": "source_code-python"
                 },
                 {
                   "comment": "C Source Code Dictionary",
                   "entries": "[ { \"type\": \"regex\", \"pattern\": \"^\\\\s*(int|void|double|float|char)\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"^\\\\s*(class|struct|interface)\\\\s\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*using\\\\s+(namespace|\\\\w+)\\\\s*(=|::)?\\\\s*[\\\\w*:<>]+;\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*typedef\\\\s+((int|void|float|double|char|short|long)\\\\*{0,2}|(struct|enum|union)\\\\s+)\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*#include\\\\s*[<\\\"][^>\\\"]+[>\\\"]\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*(public|private|protected)\\\\:\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*namespace\\\\s+(.+?)\\\\s*\\\\{\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*#define\\\\s\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*int\\\\s+main\\\\s*\\\\(\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*switch\\\\b\\\\s*\\\\([^)]*\\\\)\\\\s*\\\\{\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*#ifndef\\\\s\\/m\", \"ignore-case\": 0, \"repeat\": 1 } ]",
                   "match-type": "any",
                   "name": "source_code-c"
                 },
                 {
                   "comment": "Java Source Code Dictionary",
                   "entries": "[ { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*@(Override|Deprecated|SuppressWarnings|FunctionalInterface|Entity|RequestMapping|Autowired|)\\\\s*$\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*(public\\\\s|private\\\\s|protected\\\\s)?(static\\\\s)?(final\\\\s)?(int(\\\\[\\\\])*|String(\\\\[\\\\])*|Runnable|double|float|long|char|boolean|byte|short)\\\\s(.+?);$\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*(public\\\\s+|private\\\\s+|protected\\\\s+)?((abstract\\\\s+|final\\\\s+|static\\\\s+)?class|(abstract\\\\s+|static\\\\s+)?void|enum|interface)\\\\s+(.+?){\\/m\", \"ignore-case\": 0, \"repeat\": 1 }, { \"type\": \"regex\", \"pattern\": \"\\/^\\\\s*(import|package)\\\\s(static\\\\s)?(javax?|com|org)\\\\..*?;\\/m\", \"ignore-case\": 0, \"repeat\": 1 } ]",
                   "match-type": "any",
                   "name": "source_code-java"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "pm/config/adom/root/_fdsdb/dlp/dictionary",
               "version": "1.41"
             }
           ]
         }

How to get DLP data-type from FortiGuard DB?
____________________________________________

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "pm/config/adom/root/_fdsdb/dlp/data-type"
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
                   "comment": "",
                   "look-ahead": 0,
                   "look-back": 0,
                   "match-ahead": 0,
                   "match-around": "",
                   "match-back": 0,
                   "name": "uk-iban",
                   "pattern": "\\bGB\\d{2}[A-Z]{4}\\d{6}\\d{8}\\b",
                   "verify": ""
                 },
                 {
                   "comment": "",
                   "look-ahead": 1,
                   "look-back": 12,
                   "match-ahead": 0,
                   "match-around": "",
                   "match-back": 0,
                   "name": "can-natl_id-sin",
                   "pattern": "\\b\\d{3}[- ]?\\d{3}[- ]?\\d{3}\\b",
                   "verify": "\\b(?!0\\d{2}|8\\d{2})\\d{3}([ -]?)?\\d{3}\\1\\d{3}\\b"
                 },
                 {
                   "comment": "",
                   "look-ahead": 0,
                   "look-back": 20,
                   "match-ahead": 0,
                   "match-around": "",
                   "match-back": 0,
                   "name": "luhn-algo",
                   "pattern": "",
                   "verify": "builtin)luhn"
                 },
                 {"...": "..."},
                 {
                   "comment": "France SWIFT Code",
                   "look-ahead": 100,
                   "look-back": 100,
                   "match-ahead": 100,
                   "match-around": "glb-swift-pk",
                   "match-back": 100,
                   "name": "fra-swift",
                   "pattern": "\\b[A-Z]{4}FR[A-Z0-9]{2}(?:[A-Z0-9]{3})?\\b",
                   "verify": ""
                 },
                 {
                   "comment": "Australia SWIFT Code",
                   "look-ahead": 100,
                   "look-back": 100,
                   "match-ahead": 100,
                   "match-around": "glb-swift-pk",
                   "match-back": 100,
                   "name": "aus-swift",
                   "pattern": "\\b[A-Z]{4}AU[A-Z0-9]{2}(?:[A-Z0-9]{3})?\\b",
                   "verify": ""
                 },
                 {
                   "comment": "China SWIFT Code",
                   "look-ahead": 100,
                   "look-back": 100,
                   "match-ahead": 100,
                   "match-around": "glb-swift-pk",
                   "match-back": 100,
                   "name": "chn-swift",
                   "pattern": "\\b[A-Z]{4}CN[A-Z0-9]{2}(?:[A-Z0-9]{3})?\\b",
                   "verify": ""
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "pm/config/adom/root/_fdsdb/dlp/data-type",
               "version": "1.41"
             }
           ]
         }        


IPS Profiles Management
-----------------------

How to add an IPS signature in an IPS profile?
++++++++++++++++++++++++++++++++++++++++++++++

**REQUEST:**

.. code-block::

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "add",
     "params": [
       {
         "data": {
           "action": "default",
           "exempt-ip": null,
           "log": "enable",
           "log-attack-context": "disable",
           "log-packet": "disable",
           "quarantine": "none",
           "rate-count": 0,
           "rule": [
             "1002"
           ],
           "status": "default"
         },
         "url": "/pm/config/adom/root/obj/ips/sensor/ips-sensor-001/entries"
       }
     ],
     "session": "OTSxkSZMaLvhsyve32Gq+1mRMAuEA0FAzVxJL1OpzGIOtdPNPNwosmp7hvVD/u+QlkGn+Q5cGfotR4witaxC5Q==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block::

   {
     "id": 1,
     "result": [
       {
         "data": {
           "id": 2
         },
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/root/obj/ips/sensor/ips-sensor-001/entries"
       }
     ]
   }
   
How to get list of IPS signatures?
++++++++++++++++++++++++++++++++++

The following example shows how to get the list of IPS signatures using the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/_data/reserved/ips/sensor/entries/protocol"
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
                   "action": "block",
                   "application": "SCADA",
                   "cve": "",
                   "cve_lf": "",
                   "database": 4,
                   "date": "20220502",
                   "group": "SCADA",
                   "location": "server,client",
                   "log": "",
                   "log-packet": "",
                   "name": "10-Strike.LANState.Local.Buffer.Overflow.Exploit",
                   "objver": "13.518",
                   "os": "Windows",
                   "rate-count": "",
                   "rate-duration": "",
                   "rate-mode": "",
                   "rate-track": "",
                   "rev": "13518",
                   "rule-id": 47306,
                   "service": "TCP,HTTP,FTP,SMTP,POP3,IMAP,NNTP",
                   "severity": "medium",
                   "status": "enable",
                   "vuln_type": "Buffer Errors"
                 },
                 {
                   "...": "..."
                 },
                 {
                   "action": "block",
                   "application": "Other",
                   "cve": "202237434",
                   "cve_lf": "",
                   "database": 11,
                   "date": "20221104",
                   "group": "applications3",
                   "location": "server,client",
                   "log": "",
                   "log-packet": "",
                   "name": "zlib.Library.inflateGetHeader.Handling.Buffer.Overflow",
                   "objver": "22.423",
                   "os": "Windows,Linux,MacOS",
                   "rate-count": "",
                   "rate-duration": "",
                   "rate-mode": "",
                   "rate-track": "",
                   "rev": "22423",
                   "rule-id": 52146,
                   "service": "TCP,HTTP,FTP,SMTP,POP3,IMAP,NNTP",
                   "severity": "high",
                   "status": "enable",
                   "vuln_type": "Buffer Errors"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/_rule/list",
               "version": "26.740"
             }
           ]
         }        

.. note::

   - The obtained signatures are from the IPS package version indicated in the 
     output of this command:

     .. code-block:: text

        diagnose dvm adom list demo

   - You should get an output similar to the following one:

     .. code-block:: text

        OID      STATE    PRODUCT OSVER MR  LIC NAME MODE    VPN MANAGEMENT        IPS     ISDB
        3        enabled  FOS     7.0   4       demo Normal  Policy & Device VPNs  26.740  7.3585
        ---End ADOM list---
                
   - In this above output, the IPS package version is given by the ``IPS`` column: ``26.740``

How to get list of IPS protocols?
+++++++++++++++++++++++++++++++++

The following example shows how to get the list of IPS protocols using the 
``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/_data/reserved/ips/sensor/entries/protocol"
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
                   "_flags": "+H",
                   "name": "BO"
                 },
                 {
                   "_flags": "+H",
                   "name": "DCERPC"
                 },
                 {
                   "_flags": "+H",
                   "name": "DHCP"
                 },
                 {
                   "...": "..."
                 },
                 {
                   "_flags": "+H",
                   "name": "TELNET"
                 },
                 {
                   "_flags": "+H",
                   "name": "TFN"
                 },
                 {
                   "_flags": "+H",
                   "name": "UDP"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/_data/reserved/ips/sensor/entries/protocol"
             }
           ]
         }

How to get list of IPS applications?
++++++++++++++++++++++++++++++++++++

The following example shows how to get the list of IPS applications using the 
``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/_data/reserved/ips/sensor/entries/application"
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
                   "_flags": "+H",
                   "name": "ASP_app"
                 },
                 {
                   "_flags": "+H",
                   "name": "Adobe"
                 },
                 {
                   "_flags": "+H",
                   "name": "Apache"
                 },
                 {
                   "...": "..."
                 },
                 {
                   "_flags": "+H",
                   "name": "Sun"
                 },
                 {
                   "_flags": "+H",
                   "name": "Veritas"
                 },
                 {
                   "_flags": "+H",
                   "name": "Winamp"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/_data/reserved/ips/sensor/entries/application"
             }
           ]
         }         

How to get IPS Profile Usage?
+++++++++++++++++++++++++++++

Caught in #0955276.

IPS Profile Usage is a tool that lets the FortiManager administror knows about
global IPS sensor usage.

You trigger it using the *More* > *IPS Profile Usages* from the *Intrusion Prevention* page:

.. thumbnail:: images/image_007.png

For each managed device using IPS sensors, You can review the *Installed Timestamp*, the *Modified Timestamp* and most importantly the IPS sensor *Status* (whether it is in sync with the one used by the managed device):abbr:

.. thumbnail:: images/image_008.png

In the above example, the ``default`` IPS sensor was installed on the two 
``site_1`` and ``site_2`` managed devices at the indicated *Installed 
Timestamp*.
The example is also confirming that for the moment, the ``default`` IPS sensor
is still in sync with the one currently enforced by the two managed devices 
since the *Status* is green for them.

You can trigger the *IPS Profile Usages* operation using the |fmg_api| as shown 
below:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/production/_objstatus/ips/sensor"
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
                   "device": "site_1",
                   "objects": [
                     {
                       "category": 288,
                       "copied_timestamp": 1699030383,
                       "latest_timestamp": 1699030383,
                       "name": "default",
                       "status": 0
                     }
                   ],
                   "vdom": "root"
                 },
                 {
                   "device": "site_2",
                   "objects": [
                     {
                       "category": 288,
                       "copied_timestamp": 1699030383,
                       "latest_timestamp": 1699030383,
                       "name": "default",
                       "status": 0
                     }
                   ],
                   "vdom": "root"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/production/_objstatus/ips/sensor"
             }
           ]
         }

      .. note::

         - Value ``0`` for the ``status`` attribute correspond to the green 
           status

Virtual Patching
----------------

How to get the Virtual Patching Signatures list?
++++++++++++++++++++++++++++++++++++++++++++++++

Caught in #0983425.

Following example shows how to get the Virtual Patching Signatures list using 
the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/_fdsdb/rule/otvp"
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
               "data": [
                 {
                   "act": "1",
                   "app": "Other",
                   "date": "20240215",
                   "group": "vPatch",
                   "location": "server",
                   "name": "OpenSSL.Heartbleed.Attack.",
                   "os": "All",
                   "rev": "26735",
                   "rule-id": 38315,
                   "service": "TCP",
                   "sev": "4",
                   "status": "1"
                 }, 
                 {
                   "act": "0",
                   "app": "Other",
                   "date": "20240213",
                   "group": "vPatch",
                   "location": "server",
                   "name": "HTTP.Chunk.Length.Invalid.",
                   "os": "All",
                   "rev": "24020",
                   "rule-id": 39122,
                   "service": "TCP,HTTP",
                   "sev": "0",
                   "status": "0"
                 },
                 {"...": "..."},
                 {
                   "act": "1",
                   "app": "PHP_app",
                   "date": "20240312",
                   "group": "vPatch",
                   "location": "server",
                   "name": "Advantech.R-SeeNet.Options.PHP.Local.File.Inclusion.",
                   "os": "All",
                   "rev": "21353",
                   "rule-id": 10005254,
                   "service": "TCP,HTTP",
                   "sev": "4",
                   "status": "1"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/_fdsdb/rule/otvp",
               "version": "27.748"
             }
           ]
         }