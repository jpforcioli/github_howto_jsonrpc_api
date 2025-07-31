Security Profiles
=================

URL Filtering
-------------

Webfilter urlfilter
+++++++++++++++++++

This section is for the ``webfilter.urlfilter`` object.

How to add a new entry in a webfilter.urlfilter.entries?
________________________________________________________

Goal is to add a new entry without overwritting the existing ones.

The following example shows how to add a new entry ``www.url-001.com`` in the
``webfilter.urlfilter`` with ID ``1`` in the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "url": "www.url-001.com"
               },
               "url": "/pm/config/adom/demo/obj/webfilter/urlfilter/1/entries"
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
                 "id": 1
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/webfilter/urlfilter/1/entries"
             }
           ]
         }

      .. note::

         ``1`` is the ID of the newly created URL entry.

How to add multiple entries in a webfilter.urlfilter.entries?
_____________________________________________________________

Goal is to add multiple new entries without overwritting the existing ones.

The following example shows how to add multiple new entries (``www.url-002.com``
to ``www.url-004.com``) in the ``webfilter.urlfilter`` with ID ``1`` in the ``demo`` ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": [
                 {
                   "url": "www.url-002.com"
                 },
                 {
                   "url": "www.url-003.com"
                 },
                 {
                   "url": "www.url-004.com"
                 }
               ],
               "url": "/pm/config/adom/demo/obj/webfilter/urlfilter/1/entries"
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
               "url": "pm/config/adom/dc_amer/obj/webfilter/urlfilter/1/entries"
             }
           ]
         }      

      .. note::

         In this case, no ID are returned.

How to replace the entire list of webfilter.urlfilter.entries?
___________________________________________________________________

Sometimes, you receive a new list of URLs and don’t want to go through the
tedious process of comparing which ones are present or missing from your
existing ``webfilter.urlfilter.entries``, then updating accordingly. 

It is much simpler and faster to just ignore the existing ``webfilter.urlfilter.entries`` list and replace it with the new one.

The example below shows how to replace the contents of the
``webfilter.urlfilter.entries`` sub-table of the URL Filter with ID ``1`` in the
``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "set",
           "params": [
             {
               "data": {
                 "entries": [
                   {
                     "action": "block",
                     "url": "www.host-001.com"
                   },
                   {
                     "action": "block",
                     "url": "www.host-002.com"
                   },
                   {
                     "action": "block",
                     "url": "www.host-003.com"
                   },
                   {
                     "action": "block",
                     "url": "www.host-004.com"
                   },
                   {
                     "action": "block",
                     "url": "www.host-005.com"
                   },
                   {
                     "action": "block",
                     "url": "www.host-006.com"
                   }
                 ]
               },
               "revision note": "URL List v20250607-002.",
               "url": "pm/config/adom/demo/obj/webfilter/urlfilter/1"
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
                 "id": 1
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "pm/config/adom/demo/obj/webfilter/urlfilter/1"
             }
           ]
         }
         
How to delete an entry in a webfilter.urlfilter.entries?
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

This section is for operating the ``webfilter profile`` object.

How to add a new filter in a webfilter profile?
_______________________________________________

*filter* wording is used because of the CLI syntax used to add a new category and its corresponding action. You have to update a table named ``filters`` as 
shown below:

.. code-block:: text
   :caption: CLI syntax for a webfilter profile filter
   :emphasize-lines: 4-9

   config webfilter profile
       edit <wfp_name>
           config ftgd-wf
               config filters
                   edit <filter>
                       set category <id>
                       set action <action>
                   next
               end
           end
       next
   end

The following example shows how to add the ``wfp_001`` webfilter profile in the 
``demo`` ADOM. It will block web traffic to URLs categorized as *Web-based 
Applications* (i.e. category ID is ``84``):

.. tab-set::

   .. tab-item:: REQUEST

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
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - See section :ref:`How to get the webfilter categories?` for how to 
           get the category ID used in the attribute ``category``

   .. tab-item:: RESPONSE

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
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
             }
           ]
         }

      .. note::
      
        - Response contains the ``id`` of the created entry
      
      .. warning::
      
        - You can't use same ``category`` value in a different filter entry

   .. tab-item:: pyFMG

      .. code-block:: python

         """
         Create a new ftgd-wf.filter in an existing webfilter profile
         """
         
         from pyFMG.fortimgr import FortiManager
         
         IP = "10.210.34.120"
         USERNAME = "devops"
         PASSWORD = "fortinet"
         
         with FortiManager(
             IP,
             USERNAME,
             PASSWORD,
             disable_request_warnings=True,
         ) as fmg:
         
             ADOM = "demo"
             MKEY = "wfp_001"
             url = f"/pm/config/adom/{ADOM}/obj/webfilter/profile/{MKEY}/ftgd-wf/filters"
         
             data = {
                 "category": 84,
                 "action": "block"
             } 
         
             fmg.debug = True
             fmg.add(url, data=data)
             fmg.debug = False        


How to get existing filters in a webfilter profile?
___________________________________________________

The following example shows how to get the configured filters for the ``wfp_001`` in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
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
                   "action": "monitor",
                   "category": [
                     "1"
                   ],
                   "id": 1,
                   "log": "enable",
                   "oid": 6639
                 },
                 {
                   "action": "warning",
                   "category": [
                     "2"
                   ],
                   "id": 2,
                   "log": "enable",
                   "oid": 6640,
                   "warn-duration": "5m",
                   "warning-prompt": "per-category"
                 },
                 {"...", "..."},
                 {
                   "action": "block",
                   "category": [
                     "99"
                   ],
                   "id": 33,
                   "log": "enable",
                   "oid": 6671
                 },
                 {
                   "action": "block",
                   "category": [
                     "84"
                   ],
                   "id": 34,
                   "log": "enable",
                   "oid": 6672
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
             }
           ]
         }

   .. tab-item:: pyFMG

      .. code-block:: python

         """
         Get configured filters in a webfilter profile
         """
         
         from pyFMG.fortimgr import FortiManager
         
         IP = "10.210.34.120"
         USERNAME = "devops"
         PASSWORD = "fortinet"
         
         with FortiManager(
             IP,
             USERNAME,
             PASSWORD,
             disable_request_warnings=True,
             verbose=True,
         ) as fmg:
         
             ADOM = "demo"
             MKEY = "wfp_001"
             url = f"/pm/config/adom/{ADOM}/obj/webfilter/profile/{MKEY}/ftgd-wf/filters"
         
             fmg.debug = True
             fmg.get(url)
             fmg.debug = False
 
In the above example, the information you're getting from the existing filters isn't very meaningful: ``action`` is quite explicit, but you don't get the symbolic name associated with the returned ``category``...

The following example shows how to obtain a more meaningful output by leveraging the ``expand datasrc`` mechaism:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "expand datasrc": [
                 {
                   "datasrc": [
                     {
                       "obj type": "webfilter categories"
                     }
                   ],
                   "name": "category"
                 }
               ],
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
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
                   "action": "monitor",
                   "category": [
                     {
                       "id": "1",
                       "obj description": "Drug Abuse",
                       "obj type": "webfilter categories",
                       "oid": 0
                     }
                   ],
                   "id": 1,
                   "log": "enable",
                   "oid": 6639
                 },
                 {
                   "action": "warning",
                   "category": [
                     {
                       "id": "2",
                       "obj description": "Alternative Beliefs",
                       "obj type": "webfilter categories",
                       "oid": 0
                     }
                   ],
                   "id": 2,
                   "log": "enable",
                   "oid": 6640,
                   "warn-duration": "5m",
                   "warning-prompt": "per-category"
                 },
                 {"...", "..."},
                 {
                   "action": "block",
                   "category": [
                     {
                       "id": "84",
                       "obj description": "Web-based Applications",
                       "obj type": "webfilter categories",
                       "oid": 0
                     }
                   ],
                   "id": 34,
                   "log": "enable",
                   "oid": 6672
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
             }
           ]
         }        

   .. tab-item:: pyFMG

      .. code-block:: python

         """
         Get configured filters in a webfilter profile showing categories
         symbolic names
         """
         
         from pyFMG.fortimgr import FortiManager
         
         IP = "10.210.34.120"
         USERNAME = "devops"
         PASSWORD = "fortinet"
         
         with FortiManager(
             IP,
             USERNAME,
             PASSWORD,
             disable_request_warnings=True,
             verbose=True,
         ) as fmg:
         
             ADOM = "demo"
             MKEY = "wfp_001"
             url = f"/pm/config/adom/{ADOM}/obj/webfilter/profile/{MKEY}/ftgd-wf/filters"
         
             params = [
                 {
                     "expand datasrc": [
                         {
                             "datasrc": [
                                 {
                                     "obj type": "webfilter categories",
                                 },
                             ],
                             "name": "category",
                         }
                     ],
                     "url": url,
                 }
             ]
         
             fmg.debug = True
             fmg.free_form(
                 "get",
                 data=params,
             )
             fmg.debug = False

How to update an existing filter in a webfilter profile?
________________________________________________________

Goal is to change the ``action`` attribute value of an webfilter profile filter.

The following example shows how to update the ``action``, for the *Potentially 
Unwanted Program* category, from ``block`` to ``warning`` in the ``wfp_001`` 
webfilter profile of the ``demo`` ADOM:

Current ``action`` is ``block``:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "expand datasrc": [
                 {
                   "datasrc": [
                     {
                       "obj type": "webfilter categories"
                     }
                   ],
                   "name": "category"
                 }
               ],
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters/33"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

      .. note::

         - How do you know that you have to use the ``33`` ID for the filter 
           entry?  See ref:`How to get existing filters in a webfilter profile?`

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "action": "block",
                 "category": [
                   {
                     "id": "99",
                     "obj description": "Potentially Unwanted Program",
                     "obj type": "webfilter categories",
                     "oid": 0
                   }
                 ],
                 "id": 33,
                 "log": "enable",
                 "oid": 6671
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters/33"
             }
           ]
         }        

   .. tab-item:: pyFMG

      .. code-block:: python

         """
         Get a specific filter entry in a webfilter profile
         """
         
         from pyFMG.fortimgr import FortiManager
         
         IP = "10.210.34.120"
         USERNAME = "devops"
         PASSWORD = "fortinet"
         
         with FortiManager(
             IP,
             USERNAME,
             PASSWORD,
             disable_request_warnings=True,
             verbose=True,
         ) as fmg:
         
             ADOM = "demo"
             MKEY = "wfp_001"
             url = f"/pm/config/adom/{ADOM}/obj/webfilter/profile/{MKEY}/ftgd-wf/filters/33"
         
             params = [
                 {
                     "expand datasrc": [
                         {
                             "datasrc": [
                                 {
                                     "obj type": "webfilter categories",
                                 }
                             ],
                             "name": "category",
                         }
                     ],
                     "url": url,
                 }
             ]
         
             fmg.debug = True
             fmg.free_form(
                 "get",
                 data=params,
             )
             fmg.debug = False
                     

Change it to ``warning``:

.. tab-set::

    .. tab-item:: REQUEST

       .. code-block:: json

          {
            "id": 3,
            "method": "set",
            "params": [
              {
                "data": {
                  "action": "warning"
                },
                "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters/33"
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
                  "id": 33
                },
                "status": {
                  "code": 0,
                  "message": "OK"
                },
                "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters/33"
              }
            ]
          }

    .. tab-item:: pyFMG

       .. code-block:: python

          """
          Update an existing filter in a webfilter profile
          """
          
          from pyFMG.fortimgr import FortiManager
          
          IP = "10.210.34.120"
          USERNAME = "devops"
          PASSWORD = "fortinet"
          
          with FortiManager(
              IP,
              USERNAME,
              PASSWORD,
              disable_request_warnings=True,
              verbose=True,
          ) as fmg:
          
              ADOM = "demo"
              MKEY = "wfp_001"
              url = f"/pm/config/adom/{ADOM}/obj/webfilter/profile/{MKEY}/ftgd-wf/filters/33"
          
              fmg.debug = True
              fmg.set(
                  url,
                  action="warning"
              )
              fmg.debug = False
          
          
After the change, ``action`` is ``warning``:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "expand datasrc": [
                 {
                   "datasrc": [
                     {
                       "obj type": "webfilter categories"
                     }
                   ],
                   "name": "category"
                 }
               ],
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters/33"
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
                 "action": "warning",
                 "category": [
                   {
                     "id": "99",
                     "obj description": "Potentially Unwanted Program",
                     "obj type": "webfilter categories",
                     "oid": 0
                   }
                 ],
                 "id": 33,
                 "log": "enable",
                 "oid": 6671,
                 "warn-duration": "5m",
                 "warning-prompt": "per-category"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters/33"
             }
           ]
         }

How to update multiple filters in a webfilter profile?
______________________________________________________

Goal is to change the ``action`` attribute values of multiple webfilter profile filters.

The following example shows how to set the ``action``, for the *Potentially 
Unwanted Program* and *Web-based Applications* categories, to ``monitor`` in the ``wfp_001`` webfilter profile of the ``demo`` ADOM:

Current ``action`` are ``warning`` and ``block`` respectively:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "expand datasrc": [
                 {
                   "datasrc": [
                     {
                       "obj type": "webfilter categories"
                     }
                   ],
                   "name": "category"
                 }
               ],
               "filter": [
                 "id",
                 "in",
                 33,
                 34
               ],
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
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
                   "action": "warning",
                   "category": [
                     {
                       "id": "99",
                       "obj description": "Potentially Unwanted Program",
                       "obj type": "webfilter categories",
                       "oid": 0
                     }
                   ],
                   "id": 33,
                   "log": "enable",
                   "oid": 6671,
                   "warn-duration": "5m",
                   "warning-prompt": "per-category"
                 },
                 {
                   "action": "block",
                   "category": [
                     {
                       "id": "84",
                       "obj description": "Web-based Applications",
                       "obj type": "webfilter categories",
                       "oid": 0
                     }
                   ],
                   "id": 34,
                   "log": "enable",
                   "oid": 6672
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
             }
           ]
         }

   .. tab-item:: pyFMG

      .. code-block:: python

         """
         Get configured filters in a webfilter profile
         """
         
         from pyFMG.fortimgr import FortiManager
         
         IP = "10.210.34.120"
         USERNAME = "devops"
         PASSWORD = "fortinet"
         
         with FortiManager(
             IP,
             USERNAME,
             PASSWORD,
             disable_request_warnings=True,
             verbose=True,
         ) as fmg:
         
             ADOM = "demo"
             MKEY = "wfp_001"
             url = f"/pm/config/adom/{ADOM}/obj/webfilter/profile/{MKEY}/ftgd-wf/filters"
         
             params = [
                 {
                     "expand datasrc": [
                         {
                             "datasrc": [
                                 {
                                     "obj type": "webfilter categories",
                                 },
                             ],
                             "name": "category",
                         }
                     ],
                     "url": url,
                     "filter": [
                         "id",
                         "in",
                         33, 
                         34,
                     ]
                 }
             ]
         
             fmg.debug = True
             fmg.free_form(
                 "get",
                 data=params,
             )
             fmg.debug = False

Change them to ``warning``:

.. tab-set::

    .. tab-item:: REQUEST

       .. code-block:: json

          {
            "id": 3,
            "method": "set",
            "params": [
              {
                "data": [
                  {
                    "action": "monitor",
                    "id": 33
                  },
                  {
                    "action": "monitor",
                    "id": 34
                  }
                ],
                "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
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
                "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
              }
            ]
          }

    .. tab-item:: pyFMG

       .. code-block:: python

          """
          Update configured filters in a webfilter profile
          """
          
          from pyFMG.fortimgr import FortiManager
          
          IP = "10.210.34.120"
          USERNAME = "devops"
          PASSWORD = "fortinet"
          
          with FortiManager(
              IP,
              USERNAME,
              PASSWORD,
              disable_request_warnings=True,
              verbose=True,
          ) as fmg:
          
              ADOM = "demo"
              MKEY = "wfp_001"
              url = f"/pm/config/adom/{ADOM}/obj/webfilter/profile/{MKEY}/ftgd-wf/filters"
          
              data = [
                  {
                      "id": 33,  
                      "action": "monitor",
                  },
                  {
                      "id": 34,  
                      "action": "monitor",            
                  },
              ]
          
              fmg.debug = True
              fmg.set(
                  url,
                  data=data
              )
              fmg.debug = False
          
After the change, ``action`` is ``monitor`` for both filter entries:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "expand datasrc": [
                 {
                   "datasrc": [
                     {
                       "obj type": "webfilter categories"
                     }
                   ],
                   "name": "category"
                 }
               ],
               "filter": [
                 "id",
                 "in",
                 33,
                 34
               ],
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
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
                   "action": "monitor",
                   "category": [
                     {
                       "id": "99",
                       "obj description": "Potentially Unwanted Program",
                       "obj type": "webfilter categories",
                       "oid": 0
                     }
                   ],
                   "id": 33,
                   "log": "enable",
                   "oid": 6671
                 },
                 {
                   "action": "monitor",
                   "category": [
                     {
                       "id": "84",
                       "obj description": "Web-based Applications",
                       "obj type": "webfilter categories",
                       "oid": 0
                     }
                   ],
                   "id": 34,
                   "log": "enable",
                   "oid": 6672
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/webfilter/profile/wfp_001/ftgd-wf/filters"
             }
           ]
         }

How to get the webfilter categories?
____________________________________

Caught in #0227646.

It is about describing how to obtain a category ID along with its corresponding symbolic name.

The following example shows how to get the categories ID along with their symbolic names, by combining the ``datasrc`` option with the ``attr`` attribute:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "attr": "rating",
               "option": "datasrc",
               "url": "/pm/config/adom/demo/obj/webfilter/ftgd-local-rating"
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
                   {"...", "..."},
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
      
   .. tab-item:: pyFMG

      .. code-block:: python
  
         """
         Get categories ID along with their symbolic names.
         """
         
         from pyFMG.fortimgr import FortiManager
         
         IP = "10.210.34.120"
         USERNAME = "devops"
         PASSWORD = "fortinet"
         
         with FortiManager(
             IP,
             USERNAME,
             PASSWORD,
             disable_request_warnings=True,
             verbose=True,
         ) as fmg:
         
             ADOM = "demo"
             url = f"/pm/config/adom/{ADOM}/obj/webfilter/ftgd-local-rating"
         
             params = [
                 {
                     "attr": "rating",
                     "option": "datasrc",
                      "url": url,
                 }
             ]
         
             fmg.debug = True
             fmg.free_form(
                 "get",
                 data=params,
             )
             fmg.debug = False

You could leverage the ``datasrc`` option and the ``attr`` attribute for all ``url`` leading to a configuration element referencing a category ID.

The following example will produce a similar output but with a different ``url`` and ``attr`` values:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "attr": "ftgd-wf/filters/category",
               "option": "datasrc",
               "url": "/pm/config/adom/demo/obj/webfilter/profile"
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
                 "webfilter categories": [
                   {
                     "id": "all",
                     "obj description": "All Categories",
                     "oid": 0
                   },
                   {
                     "id": "g01",
                     "obj description": "Potentially Liable",
                     "oid": 0
                   },
                   {
                     "id": "1",
                     "obj description": "Drug Abuse",
                     "oid": 0
                   },
                   {"...", "..."},
                   {
                     "id": "0",
                     "obj description": "Unrated",
                     "oid": 0
                   },
                   {
                     "id": "g22",
                     "obj description": "Local Categories",
                     "oid": 0
                   }
                 ],
                 "webfilter ftgd-local-cat": [
                   {
                     "desc": "custom1",
                     "id": 140,
                     "oid": 3716,
                     "status": "enable"
                   },
                   {
                     "desc": "custom2",
                     "id": 141,
                     "oid": 3717,
                     "status": "enable"
                   }
                 ]
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/webfilter/profile"
             }
           ]
         }

   .. tab-item:: pyFMG

      .. code-block:: python

         """
         Get categories ID along with their symbolic names.
         """
         
         from pyFMG.fortimgr import FortiManager
         
         IP = "10.210.34.120"
         USERNAME = "devops"
         PASSWORD = "fortinet"
         
         with FortiManager(
             IP,
             USERNAME,
             PASSWORD,
             disable_request_warnings=True,
             verbose=True,
         ) as fmg:
         
             ADOM = "demo"
             url = f"/pm/config/adom/{ADOM}/obj/webfilter/profile"
         
             params = [
                 {
                     "attr": "ftgd-wf/filters/category",
                     "option": "datasrc",
                      "url": url,
                 }
             ]
         
             fmg.debug = True
             fmg.free_form(
                 "get",
                 data=params,
             )
             fmg.debug = False


There is a second alternative which consists in using the ``get reserved`` option as shown below:
      
.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "option": "get reserved",
               "url": "/pm/config/adom/demo/obj/webfilter/categories"
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
                 {"...": "..."},
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

   .. tab-item:: pyFMG

      .. code-block:: python

         """
         Get categories ID along with their symbolic names.
         """
         
         from pyFMG.fortimgr import FortiManager
         
         IP = "10.210.34.120"
         USERNAME = "devops"
         PASSWORD = "fortinet"
         
         with FortiManager(
             IP,
             USERNAME,
             PASSWORD,
             disable_request_warnings=True,
             verbose=True,
         ) as fmg:
         
             ADOM = "demo"
             url = f"/pm/config/adom/{ADOM}/obj/webfilter/categories"
         
             fmg.debug = True
             fmg.get(
                 url,
                 option="get reserved"
             )
             fmg.debug = False


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


IPS Sensors Management
----------------------

How to add an IPS rule in an IPS sensor?
++++++++++++++++++++++++++++++++++++++++

The following example shows how to add a new IPS rule in the ``ips_sensor_001``
IPS sensor in the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block::

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "action": "default",
                 "application": [
                   "all"
                 ],
                 "cve": [],
                 "default-action": "all",
                 "default-status": "all",
                 "exempt-ip": null,
                 "last-modified": [],
                 "location": [
                   "all"
                 ],
                 "log": "disable",
                 "log-attack-context": "disable",
                 "log-packet": "disable",
                 "os": [
                   "all"
                 ],
                 "protocol": [
                   "all"
                 ],
                 "quarantine": "none",
                 "rule": [],
                 "severity": [
                   "info"
                 ],
                 "status": "default",
                 "vuln-type": []
               },
               "url": "/pm/config/adom/demo/obj/ips/sensor/ips_sensor_001/entries"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - Using the ``add`` preserves the existing items in the ``entries`` 
           sub-table

         - New item is added at the end of the list of existing items

   .. tab-item:: RESPONSE

      .. code-block::

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "id": 3
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/ips/sensor/ips_sensor_001/entries"
             }
           ]
         }

How to insert an IPS rule in an IPS sensor?
+++++++++++++++++++++++++++++++++++++++++++

The following example shows how to insert a new IPS rule in the
``ips_sensor_001`` IPS sensor in the ``demo`` ADOM. 

This new IPS rule will be inserted after the IPS rule with ID ``1``:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": {
                 "action": "default",
                 "application": [
                   "all"
                 ],
                 "cve": [],
                 "default-action": "all",
                 "default-status": "all",
                 "exempt-ip": null,
                 "last-modified": [],
                 "location": [
                   "all"
                 ],
                 "log": "enable",
                 "log-attack-context": "enable",
                 "log-packet": "enable",
                 "object position": [
                   "after",
                   "1"
                 ],
                 "os": [
                   "all"
                 ],
                 "protocol": [
                   "HTTP",
                   "FTP"
                 ],
                 "quarantine": "none",
                 "rule": [],
                 "severity": [
                   "high"
                 ],
                 "status": "default",
                 "vuln-type": []
               },
               "url": "/pm/config/adom/demo/obj/ips/sensor/ips_sensor_001/entries"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - ``object position`` mechanism seen in :ref:`How to insert a policy?`
           is used to insert the new IPS rule

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "id": 6
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/demo/obj/ips/sensor/ips_sensor_001/entries"
             }
           ]
         }        

How to delete an IPS rule from an IPS sensor?
+++++++++++++++++++++++++++++++++++++++++++++

The following example shows how to delete the IPS rule with ID ``5`` from the
``ips_sensor_001`` in the ``demo`` ADOM:

.. tab-set:: 
   
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "delete",
           "params": [
             {
               "url": "/pm/config/adom/demo/obj/ips/sensor/ips_sensor_001/entries/5"
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
               "url": "/pm/config/adom/demo/obj/ips/sensor/ips_sensor_001/entries/5"
             }
           ]
         }

How to get list of IPS signatures?
++++++++++++++++++++++++++++++++++

The following example shows how to get the list of IPS signatures available in
the ``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "url": "/pm/config/adom/demo/_rule/list"
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

For each managed device using IPS sensors, You can review the *Installed Timestamp*, the *Modified Timestamp* and most importantly the IPS sensor *Status* (whether it is in sync with the one used by the managed device):

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

Global IPS sensor
+++++++++++++++++

The Global IPS Sensor allows you to create baseline IPS sensors composed of header and footer IPS rules.

In the FortiManager GUI, you can find it under *Policy & Objects* > Header/Footer IPS.

.. note::

   - The Global IPS sensor defining header/footer IPS rules has nothing to do 
     with the normal Global IPS sensor that you can find under *Policy & 
     Objects* > *Security Profile* > *Intrusion Prevention*

How to create a Global IPS sensor
_________________________________

The following example shows how to add the ``g_ips_sensor_001`` Global IPS sensor made of one header and one footer rules in the Global ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         { 
           "id": 3,
           "method": "add", 
           "params": [
             { 
               "data": { 
                 "block-malicious-url": 0, 
                 "entries": [
                   { 
                     "action": 5, 
                     "application": ["all"], 
                     "default-action": 34, 
                     "default-status": 34, 
                     "exempt-ip": [], 
                     "last-modified": null, 
                     "location": ["all"], 
                     "log": true, 
                     "log-attack-context": 0, 
                     "log-packet": 0, 
                     "os": ["all"], 
                     "position": "header",
                     "protocol": ["all"], 
                     "quarantine": 0, 
                     "quarantine-expiry": "5m", 
                     "quarantine-log": 1, 
                     "rate-count": 0, 
                     "rate-duration": 60, 
                     "rate-mode": 9, 
                     "rate-track": 0, 
                     "severity": ["all"], 
                     "status": 3
                   }, 
                   { 
                     "action": 5, 
                     "application": ["all"], 
                     "default-action": 34, 
                     "default-status": 34, 
                     "exempt-ip": [], 
                     "last-modified": null,
                     "location": ["all"], 
                     "log": true, 
                     "log-attack-context": 0, 
                     "log-packet": 0, 
                     "os": ["all"], 
                     "position": "footer", 
                     "protocol": ["all"], 
                     "quarantine": 0, 
                     "quarantine-expiry": "5m", 
                     "quarantine-log": 1, 
                     "rate-count": 0, 
                     "rate-duration": 60, 
                     "rate-mode": 9, 
                     "rate-track": 0, 
                     "severity": ["all"], 
                     "status": 3
                   }
                 ], 
                 "extended-log": 0, 
                 "name": "g_ips_sensor_001",
                 "scan-botnet-connections": 0
               }, 
               "url": "/pm/config/global/obj/global/ips/sensor"
             }
           ], 
           "session": "{{session}}"
         }

      .. note::

         - The ``entries`` attribute contains the IPS header and footer rules
         - The ``position`` attribute determines whether the IPS rule is in the 
           header (value is ``header``) of footer (``footer``) rule block

   .. tab-item:: RESPONSE

      .. code-block:: json

         { 
           "id": 3,
           "data": { 
             "name": "g_ips_sensor_001"
           }, 
           "status": { 
             "code": 0, 
             "message": "OK"
           }, 
           "url": "/pm/config/global/obj/global/ips/sensor"
         }

How to delete a Global IPS sensor?
__________________________________

The following example shows how to delete the ``g_ips_sensor_001`` Global IPS 
sensor from the Global ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "delete",
           "params": [
             {
               "url": "/pm/config/global/obj/global/ips/sensor/g_ips_sensor_001",
             }
           ]
         }
      
   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "data": null,
           "id": 3,
           "status": {
             "code": 0,
             "message": "OK"
           },
           "url": "/pm/config/global/obj/global/ips/sensor/g_ips_sensor_001"
         }

How to add ADOMs to a Global IPS sensor?
________________________________________

The following example shows how to add the ``demo_001`` and ``demo_002`` to the 
``g_ips_sensor_001`` Global IPS sensor in the Global ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "add",
           "params": [
             {
               "data": [
                 {
                   "name": "demo_001"
                 },
                 {
                   "name": "demo_002"
                 }
               ],
               "url": "/pm/config/global/obj/global/ips/sensor/g_ips_sensor_001/scope member"
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
               "url": "/pm/config/global/obj/global/ips/sensor/g_ips_sensor_001/scope member"
             }
           ]
         }

How to delete ADOMs from a Global IPS sensor?
_____________________________________________

The following example shows how to delete the ``demo_001`` and ``demo_002`` 
from the ``g_ips_sensor_001`` Global IPS sensor in the Global ADOM:

.. tab-set::
  
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "delete",
           "params": [
             {
               "data": [
                 {
                   "name": "demo_001"
                 },
                 {
                   "name": "demo_002"
                 }
               ],
               "url": "/pm/config/global/obj/global/ips/sensor/g_ips_sensor_001/scope member"
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
               "url": "/pm/config/global/obj/global/ips/sensor/g_ips_sensor_001/scope member"
             }
           ]
         }

How to assign a Global IPS sensor?
__________________________________

The following example shows how to assign the ``g_ips_sensor_001`` Global IPS sensor to the ``demo_001`` and ``demo_002`` ADOMs:

.. tab-set::
   
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "global",
                 "category": 1908,
                 "flags": "none",
                 "objs": [
                   "g_ips_sensor_001"
                 ],
                 "target": [
                   {
                     "adom": "demo_001"
                   },
                   {
                     "adom": "demo_002"
                   }
                 ]
               },
               "url": "/securityconsole/assign/objs"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - The ``category`` attribute is the number of the table ``global ips 
           sensor``

         - You can get this number by issuing following command:

           .. code-block:: text

              execute fmpolicy print-adom-object Global ?

           In the output, you will see this line:

           .. code-block:: text

              [...]
              1908	"global ips sensor"
              [...]         

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "task": 1558
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/securityconsole/assign/objs"
             }
           ]
         }

How to unassign a Global IPS sensor?
____________________________________

The following example shows how to unassign the ``g_ips_sensor_001`` Global IPS sensor from the ``demo_001`` and ``demo_002`` ADOMs:

.. tab-set::
   
   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "exec",
           "params": [
             {
               "data": {
                 "adom": "global",
                 "category": 1908,
                 "flags": "unassign",
                 "objs": [
                   "g_ips_sensor_001"
                 ],
                 "target": [
                   {
                     "adom": "demo_001"
                   },
                   {
                     "adom": "demo_002"
                   }
                 ]
               },
               "url": "/securityconsole/assign/objs"
             }
           ],
           "session": "{{session}}"
         }

      .. note::

         - The ``category`` attribute is the number of the table ``global ips 
           sensor``

         - You can get this number by issuing following command:

           .. code-block:: text

              execute fmpolicy print-adom-object Global ?

           In the output, you will see this line:

           .. code-block:: text

              [...]
              1908	"global ips sensor"
              [...]         

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 3,
           "result": [
             {
               "data": {
                 "task": 1562
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/securityconsole/assign/objs"
             }
           ]
         }         

How to get the assign status for Global IPS sensors?
____________________________________________________

Caught in #1051174.

This is to get the information exposed in the following screenshot:

.. thumbnail:: images/security_profiles/image_001.png

The screenshot above shows two global IPS sensor, ``g_ips_sensor_001`` and
``g_ips_sensor_002``, along with their *assignement* status.

You can see that:

- The ``g_ips_sensor_001`` global IPS sensor isn't assigned to the ``dc_amer``
  ADOM; its status is *Never installed*
- The ``g_ips_sensor_001`` global IPS sensor is assigned to the ``dc_africa``
  ADOM but it has pending changes; its status is *Modified*
- The ``g_ips_sensor_002`` has been assigned to its ``dc_emea`` ADOM; its status
  is *Synced*

The following example shows how to get the same information using the
FortiManager API:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 2,
           "method": "get",
           "params": [
             {
               "stype": "gl_ips_sensor",
               "type": "template",
               "url": "/pm/config/global/_package/status"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

   .. tab-item:: RESPONSE

      .. code-block:: json

         {
           "id": 2,
           "result": [
             {
               "data": [
                 {
                   "adom": "dc_africa",
                   "pkg": "g_ips_sensor_001",
                   "status": "modified",
                   "stype": "gl_ips_sensor",
                   "type": "template"
                 },
                 {
                   "adom": "dc_emea",
                   "pkg": "g_ips_sensor_002",
                   "status": "installed",
                   "stype": "gl_ips_sensor",
                   "type": "template"
                 }
               ],
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/global/_package/status"
             }
           ]
         }

      .. note::

         - You can see that FortiManager doesn't return details for the global
           IPS sensors which aren't assigned

         - In this output above, FortiManager didn't return anything about the
           ``dc_amer`` ADOM since its global IPS sensor isn't assigned yet


Virtual Patching
----------------

How to get the Virtual Patching Signatures list?
++++++++++++++++++++++++++++++++++++++++++++++++

Caught in #0983425 and #1103218

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

Inline CASB Profile
-------------------

How to get list of SaaS Applications?
+++++++++++++++++++++++++++++++++++++

Caught in #1094160.

The following example shows how to get the list of SaaS applications using the 
``demo`` ADOM:

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 3,
           "method": "get",
           "params": [
             {
               "attr": "saas-application/name",
               "option": "datasrc",
               "url": "/pm/config/adom/demo/obj/casb/profile"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

   .. tab-item:: RESPONSE

      .. literalinclude:: datas/security_profiles/output_001.json
         :language: json
