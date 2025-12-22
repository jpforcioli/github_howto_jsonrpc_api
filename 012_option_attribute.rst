The *option* attribute
======================

This section describe all the possible options that could be passed when using the FMG JSON API.

To pass an option, we need to use the ``option`` attribute:

.. code-block:: 

		"option": "option1",
		
It's possible to pass multiple options; in that case we need to place them in a list:

.. code-block:: 

		"option": ["option1", "option2"],

It's also possible to pass a single option via a list:

.. code-block:: 

		"option": ["option1"],

Sometime the option is having a direct counterpart attribute.
For instance:

.. code-block:: 

		"option": "loadsub",

and

.. code-block:: 

		"loadsub": 1,

are two possible ways to enable the ``loadsub`` option.

*extra info*
------------

As its name implies, it is used to return extra information.

For instance, it can be used to get the *Last Modified* timestamp information
when retrieving objects (see :ref:`How to get the Last Modified timestamp?`) or
to get the *Packages* assignment information (Policy Package, Provisioning
Templates, FortiAP/FortiSwitch Template, etc.) for the managed devices (see
:ref:`Device status`).

.. code-block:: json

   "option": [
	   "extra info"
   ]

To disable it:

.. code-block:: json

   "option": [
	   "no extra info"
   ]

*loadsub*
---------

When enabled, this option is used to instruct the FortiManager to return sub
table information.

To enable it:

.. code-block:: json

   "option": [
	   "loadsub"
   ]

To disable it:

.. code-block:: json

   "option": [
	   "no loadsub"
   ]

It is also possible to use the ``loadsub`` as a standalone attribute:

- To enable it:

  .. code-block::

     "loadsub": 1,

- To disable it:

  .. code-block::

     "loadsub": 0,

For instance:


*count*
-------

This option is used to return the number of entries in a given table.

For instance to get the number of firewall addresses for ADOM ``400K``:

**REQUEST:**

.. code-block:: json

   {
     "id": 1,
     "jsonrpc": "1.0",
     "method": "get",
     "params": [
       {
         "option": [
           "count"
         ],
         "url": "/pm/config/adom/400K/obj/firewall/address"
       }
     ],
     "session": "M9tBdRa0ifwpNhzh2nED+PTfzqTc3DMwJhX4kIY57ezZXvuYpAF+Qy8q4Gb3MPEpX+xpWxHJXzMDxgzY5iq9qw==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": 400000,
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "/pm/config/adom/400K/obj/firewall/address"
       }
     ]
   }

This ADOM ``400K`` is having 400000 firewall addresses as returned by the
attribute ``data``.

*syntax*
--------

It is used to return the schema of a table or object.

For instance, if you want to get the schema of a firewall address you can add
the ``syntax`` option when the firewall address table/object from any ADOMs: 

.. tab-set:: 
   
   .. tab-item:: REQUEST

      .. code-block:: json
      
      		{
      		  "id": 1,
      		  "method": "get",
      		  "params": [
      		    {
      		      "option": [
      		        "syntax"
      		      ],
      		      "url": "/pm/config/adom/demo/obj/firewall/address"
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
                 "firewall address": {
               		"alimit": 400000,
             			"attr": {
             			  "_image-base64": {
               			  "max": 5120,
               			  "sz": 5120,
               			  "type": "string"
                     },
                   },
             			"allow-routing": {
             			  "default": "disable",
             			  "excluded": true,
             			  "help": "Enable/disable use of this address in the static route configuration.",
             			  "opts": {
             			    "disable": 0,
             			    "enable": 1
             			  },
             			  "sz": 4,
             			  "type": "uint32"
         		    	},
                   "...": "...",
                 }
               }
             }
           ]
         }

Since FMG 6.2.4/6.4.0 (#0603847, this option is also returning the table limit
with attribute ``alimit``. For instance, from the above output, we can see it
is possible to have up to 400000 firewall addresses.

You can also ask for the schemo of all objects at once (captured in #1229558):

.. tab-set::

   .. tab-item:: REQUEST

      .. code-block:: json
      
         {
           "id": 1,
           "method": "get",
           "params": [
             {
               "option": [
                 "syntax"
               ],
               "url": "/pm/config/adom/demo/obj"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

How to get default values?
++++++++++++++++++++++++++

The *syntax* option provides default values **ONLY** for attributes whose
values are not from others data source.

Let me give an example for when I *syntax* a firewall policy:

- The following firewall policy  ``ztna-status`` attribute is of type
  ``uint32`` and has a static list of values,  either *disable* or *enable* and
  in that case the default value will be *disable*: 

  .. code-block:: json

     "ztna-status": {
         "default": "disable",
         "excluded": true,
         "help": "Enable/disable zero trust access.",
         "opts": {
             "disable": 0,
             "enable": 1
         },
         "sz": 4,
         "type": "uint32"
     }

- However, the following firewall policy ``ztna-geo-tag`` attribute is of type
  ``datasrc``. it means it **references** (I used this verb on purpose to refer
  to the ``ref`` list in below output) values coming from another table (or to
  use proper FMG API wording, ***from another data source***); in that case it
  could be any objects from table ``firewall address`` or ``firewall addrgrp``:
  
  .. code-block:: json
    
     "ztna-geo-tag": {
        "help": "Source ztna-geo-tag names.",
        "max_argv": -1,
        "ref": [
            {
                "category": "firewall address",
                "mkey": "name"
            },
            {
                "category": "firewall addrgrp",
                "mkey": "name"
            }
        ],
        "type": "datasrc"
     }

  In that case, as you can see in above output, there's no proposed default
  value.  
  
**The syntax call works will all kind of FortiManager objects (device db or
adom db).**

For instance, we can apply it against the firewall policy from policy package
``foobar`` of adom ``demo`` (i.e. adom db):  

**REQUEST:**

.. code-block::
     
   {
   [...]
       "method": "get",
       "params": [
           {
               "option": [
                   "syntax"
               ],
               "url": "/pm/config/adom/demo/pkg/foobar/firewall/policy"
           }
       ],
   [...]
   }

.. note::
  
   Whatever is the chosen policy package name, you'll get the same syntax
   output. 

We can also apply it against the system global table of any managed devices;
like in the following example my managed device ``device1`` (i.e. ``device1``'s
device db):  

**REQUEST:**
  
.. code-block::
  
   {
   [...]
       "method": "get",
       "params": [
           {
               "option": [
                   "syntax"
               ],
               "url": "/pm/config/device/device1/global/system/global"
           }
       ],
   [...]
   }

The *syntax* call could target a specific leaf table using the url attribute or
a set of tables by shortening the path given to the ``url`` attribute: 

.. code-block::

   ADOM DB:

   # Syntax for the firewall policy table
   "url": "/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy"

   # Syntax for all kind of policies we could have in a policy package:
   "url": "/pm/config/adom/{adom}/pkg/{pkg}"

   # Syntax for the firewall address table
   "url": "/pm/config/adom/{adom}/obj/firewall/address"

   # Syntax for all kind of objects tables:
   "url": "/pm/config/adom/{adom}/obj"

   DEVICE DB:

   # Syntax for firewall policy table in a device 
   "url": "/pm/config/device/{device}/vdom/{vdom}/firewall/policy"

   # Syntax for all tables in a device
   "url": "/pm/config/device/{device}/vdom/{vdom}"

*object template* and *devicetemplate* mechanisms are just offering default
values but without the syntax details. It might be easier when the calling
script has to parse the output. 

For instance those are the default values for firewall policy:

**REQUEST:**

.. code-block::

   {
   [...]
       "method": "get",
       "params": [
           {
               "object template": 1,
               "url": "/pm/config/adom/demo/pkg/default/firewall/policy"
           }
       ],
   [...]
   }

**RESPONSE:**

.. code-block::

   {
       "id": 1,
       "result": [
           {
               "data": {
                   "action": "deny",
                   "anti-replay": "enable",
                   "auth-path": "disable",
                   "auto-asic-offload": "enable",
                   "block-notification": "disable",
                   "captive-portal-exempt": "disable",
                   "capture-packet": "disable",
                   "delay-tcp-npu-session": "disable",
                   "diffserv-forward": "disable",
                   "diffserv-reverse": "disable",
                   "diffservcode-forward": "000000",
                   "diffservcode-rev": "000000",
                   [...]
                   "tos": "0x00",
                   "tos-mask": "0x00",
                   "tos-negate": "disable",
                   "utm-status": "disable",
                   "uuid": "00000000-0000-0000-0000-000000000000",
                   "vlan-cos-fwd": 255,
                   "vlan-cos-rev": 255,
                   "vpn_dst_node": {},
                   "vpn_src_node": {},
                   "wanopt": "disable",
                   "wanopt-detection": "active",
                   "wanopt-passive-opt": "default",
                   "wccp": "disable",
                   "webcache": "disable",
                   "webcache-https": "disable",
                   "ztna-status": "disable"
               },
               "status": {
                   "code": 0,
                   "message": "OK"
               },
               "url": "/pm/config/adom/demo_001_70/pkg/default/firewall/policy"
           }
       ]
   }

We can recognize the ``ztna-status`` attribute with its default disable value
(as indicated when using the ``syntax`` option). Furthermore, this output is
easier to parse since it respects the firewall policy format. 

The above output isn't showing the attributes like ``srcintf``, ``dstintf``,
``srcaddr``, ``dstaddr``, etc. This is because their values come from different
data sources (``system interface``, ``firewall address``, etc.) 

When you get **existing** objects from adom db (everything behind Policy &
Objects) or from device db (everything behind Device Manager), you get ALL
possible attributes; the modified ones (hence overridden by the admin using
GUI, API, CLI) along with the untouched ones. The untouched ones will show up
with their default values. 

To give an example, if you get ``firewall policy`` 1 either from ``device1``'s
device db or from policy package ``foobar`` (i.e. adom db, policy package
``foobar`` is assigned to ``device1``):

- external data source attributes  like ``srcintf``, ``dstintf``, ``srcaddr``,
  ``dstaddr``, ``service``, ``schedule``, etc. will necessarily show up  with
  values **picked** by the admin since there's no default values for such type
  of attributes. 
- Other attributes will either show up with overridden-by-admin values or their
  default values. 

When you offer to create a new object, you can present a form where all
non-external-data-source attributes show up with their default values. Easy. 

However, for external-data-source attributes, you have to decide by yourself
whether you keep the field blank or if you pre-fill it with custom default
values. 

But in this case, the custom default values have to be generated using
your own internal logic; if your program knows it is creating a new firewall
policy, it can for instance pre-fill the ``srcaddr`` with firewall address
``all``. This is what FMG GUI is doing for instance... 

When building a tool which presents a create a new object mechanism, to figure
out what are the minimum list of attributes to set, we just need to get from
the *syntax* all the external-data-source attributes  (i.e. type is
``datasrc``). 

.. note::

  ``object template`` is not documented. 
  It was originally intended for GUI use.

  It returns the value of an object and all child table/objects with default
  values as if it was created new.
  For child tables, it will include one default entry.

  This is used for GUI to auto-fill in the form with default values when user
  tries to create a new object.

*devinfo*
---------

This option could be used to obtain a kind of ADOM checksum used to detect
whether a change was made.

For instance, you can obtain the checksum of the object database for the
``TEST`` ADOM using the following request:

.. tabs::

   .. tab:: REQUEST

      .. code-block:: json
      
         {
      	   "id": 1,
      		 "jsonrpc": "1.0",
      		 "method": "get",
      		 "params": [
      		   {
      		     "option": [
      		       "devinfo"
               ],
     		      "url": "/pm/config/adom/TEST/obj"
             }
           ],
      		 "session": "c/6nIFsDE8+lkYaSnhgXfXFrbL5dJmdpSJpg1AurwydHDivLHDt9MkAHoYtjyac7aLDkr6P4BWlI5Ro3Q2YuwEGqESEeewR8",
      		 "verbose": 1
         }

   .. tab:: RESPONSE

      .. code-block:: json
      		
         {
           "id": 1,
           "result": [
             {
               "data": {
                 "uuid": "203111b8-6395-51ea-56da-3ddaf129148e"
               },
               "status": {
                 "code": 0,
                 "message": "OK"
               },
               "url": "/pm/config/adom/TEST/obj"
             }
           ]
         }

      .. note::

         - The returned ``uuid`` could be considered as a checksum
         - You can save it and compare it with the one returned by a sub-sequent request
         - If they are different, it means something has been modified in the
           objects database of the ``TEST`` ADOM
      

*obj flags*
-----------

Not very clear.

Few explanation in #0305108.

*datasrc*
---------

Caught in #0622870.

This option is generally used to get list of possible object types and the
objects themselves that could be used within an object you want to create or
update.

For instance, if you create a new address group, you might want to know what are
all the possible object types that could be placed as ``member``. 

You know that a firewall address group could regroup firewall addresses or other
firewall address groups.

Let's take an example wih the Internet Service Group object.
What could be the object types and the objects that you could use as members?

To present the list of available internet service group member objects, you can
just ask to get its ``datasrc``:

.. tab-set:: 

   .. tab-item:: REQUEST

      .. code-block:: json

         {
           "id": 1,
           "method": "get",
           "params": [
             {
               "attr": "member",
               "option": "datasrc",
               "url": "/pm/config/adom/DEMO/obj/firewall/internet-service-group"
             }
           ],
           "session": "{{session}}",
           "verbose": 1
         }

      .. note::

         Note the usage of the attribute ``attr`` which is specifying for which
         part of the internet service group (here ``member``) you need the
         ``datasrc``.

   .. tab-item:: RESPONSE

      .. code-block::

         {
           "id": 1,
           "result": [
             {
               "data": {
                 "firewall internet-service": [
                   {
                     "database": "isdb",
                     "direction": "both",
                     "extra-ip-range-number": 0,
                     "icon-id": 0,
                     "id": 10027174,
                     "ip-number": 0,
                     "ip-range-number": 0,
                     "jitter-threshold": 0,
                     "latency-threshold": 0,
                     "obj description": "Censys.Scanner",
                     "obsolete": 0,
                     "packetloss-threshold": 0,
                     "reputation": 0,
                     "singularity": 0,
                     "sld-id": 0
                   },
      	     [...]
                   {
                     "database": "isdb",
                     "direction": "both",
                     "extra-ip-range-number": 0,
                     "icon-id": 0,
                     "id": 9961638,
                     "ip-number": 0,
                     "ip-range-number": 0,
                     "jitter-threshold": 0,
                     "latency-threshold": 0,
                     "obj description": "Shodan.Scanner",
                     "obsolete": 0,
                     "packetloss-threshold": 0,
      	       "reputation": 0,
                     "singularity": 0,
                     "sld-id": 0
                   }
                 ]
      	 },
      	 "status": {
                 "code": 0,
                 "message": "OK"
      	 },
      	 "url": "/pm/config/adom/DEMO/obj/firewall/internet-service-group"
             }
           ]
         }
      .. note::

         As shown in the above output, you can only use ``firewall
         internet-service`` objects as member of an Internet Service Group.
         
*chksum*
--------

Caught in #0254612.

This option is used to retrieve the version or checksum of a specific table.

It helps to figure out whether a table has been changed. 

For instance, if you modify a particular policy, then you can use the
``chksum`` option to get the new version of the policy package by using the
following request: 

**REQUEST:**

.. code-block:: json
  
   {
     "id": 1,
     "method": "get",
     "params": [
       {
         "option": "chksum",
         "url": "pm/config/adom/root/pkg/default/firewall/policy"
       }
     ],
     "session": "cCyFgkiB/UbhXXxm2bYvSsHQtNAQ88Px7BlivPEyQqZy4p62VYEzLj9RHpin8Gf8JU/pZLyFypbTXafQprS+RQ==",
     "verbose": 1
   }

**RESPONSE:**

.. code-block:: json

   {
     "id": 1,
     "result": [
       {
         "data": 6,
         "status": {
           "code": 0,
           "message": "OK"
         },
         "url": "pm/config/adom/root/pkg/default/firewall/policy"
       }
     ]
   }

The version/checksum is returned with the ``data`` attribute. 
In the above response, the version of my policy package is ``6``.

With FMG 6.2.1-INTERIM build 1099, the option ``chksum`` seems also to work at
the object level (ie. not only at the table level).