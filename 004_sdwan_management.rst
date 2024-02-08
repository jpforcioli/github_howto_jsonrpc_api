SD-WAN Management
=================

SD-WAN Monitoring
-----------------

How to get SD-WAN Monitoring data?
++++++++++++++++++++++++++++++++++

This is to collect the data that allows FortiManager to produce this per-device
SD-WAN Monitoring view via the *SD-WAN* widget:

.. thumbnail:: images/image_010.png
   :title: Per-device SD-WAN Monitoring via the SD-WAN widget (FMG 7.4.
           3-INTERIM build 2430)

You can get the data directly from the managed FortiGate devices using the 
FortiOS REST API over the FortiManager API via the ``sys/proxy/json`` endpoint.

But FortiManager is already doing that on a periodic basis and is saving the
collected data in local Real Time Monitor (RTM) databases in order to provide 
longer period of monitoring in FortiManager GUI.

The following examples show how to get two SD-WAN Monitoring indicators for the ``dev_001`` device: ``sd-wan-sla-log`` and ``sd-wan-intf-log``.

.. tab-set::

   .. tab-item:: sd-wan-sla-log

      .. tab-set::

         .. tab-item:: REQUEST

            .. code-block:: json

               {
                 "id": 3,
                 "method": "get",
                 "params": [
                   {
                     "filter": {
                       "key": [
                         [
                           "name"
                         ],
                         [
                           "interface"
                         ]
                       ],
                       "timestamp": [
                         [
                           "start",
                           "==",
                           1707250119
                         ],
                         [
                           "end",
                           "==",
                           1707253719
                         ]
                       ]
                     },
                     "url": "/rtm/global/rhistory/monitor/sd-wan-sla-log/device/dev_001"
                   }
                 ],
                 "session": "{{session}}"
               }

         .. tab-item:: RESPONSE

            .. code-block:: text

               {
                 "id": 3,
                 "result": [
                   {
                     "data": [
                       {
                         "interface": "port1",
                         "log": [
                           {
                             "timestamp": 1707250158,
                             "value": {
                               "jitter": 0.1982,
                               "latency": 6.003067,
                               "link": "up",
                               "packetloss": 0.0
                             }
                           },
                           {
                             "timestamp": 1707250218,
                             "value": {
                               "jitter": 0.230633,
                               "latency": 9.498699,
                               "link": "up",
                               "packetloss": 0.0
                             }
                           },
                           {
                             "timestamp": 1707250278,
                             "value": {
                               "jitter": 0.378133,
                               "latency": 9.459866,
                               "link": "up",
                               "packetloss": 0.0
                             }
                           },               
               [...]

   .. tab-item:: sd-wan-intf-log

      .. tab-set:: 
         
         .. tab-item:: REQUEST

            .. code-block:: json

               {
                 "id": 3,
                 "method": "get",
                 "params": [
                   {
                     "filter": {
                       "key": [
                         [
                           "interface"
                         ]
                       ],
                       "timestamp": [
                         [
                           "start",
                           "==",
                           1707250119
                         ],
                         [
                           "end",
                           "==",
                           1707253719
                         ]
                       ]
                     },
                     "url": "/rtm/global/rhistory/monitor/sd-wan-intf-log/device/dev_001"
                   }
                 ],
                 "session": "{{session}}"
               }

         .. tab-item:: RESPONSE
   
            .. code-block:: text
   
               {
                 "id": 3,
                 "result": [
                   {
                     "data": [
                       {
                         "interface": "HUB1-VPN1",
                         "log": [
                           {
                             "timestamp": 1707250149,
                             "value": {
                               "bi_bandwidth": 1318,
                               "egress_queue": [],
                               "rx_bandwidth": 659,
                               "rx_bytes": 88247589,
                               "tx_bandwidth": 659,
                               "tx_bytes": 88247420
                             }
                           },
                           {
                             "timestamp": 1707250209,
                             "value": {
                               "bi_bandwidth": 1318,
                               "egress_queue": [],
                               "rx_bandwidth": 659,
                               "rx_bytes": 88252512,
                               "tx_bandwidth": 659,
                               "tx_bytes": 88252343
                             }
                           },
                           {
                             "timestamp": 1707250279,
                             "value": {
                               "bi_bandwidth": 1318,
                               "egress_queue": [],
                               "rx_bandwidth": 659,
                               "rx_bytes": 88258306,
                               "tx_bandwidth": 659,
                               "tx_bytes": 88258118
                             }
                           },            
               [...]
   
SD-WAN Orchestrator API
-----------------------

Caught in PMDB #10801

How to get a token (ie. how to login)
+++++++++++++++++++++++++++++++++++++

**REQUEST:**

.. code::

   curl 'http://10.106.18.100/fortiwan/' -v -H 'Cookie: csrftoken=m6Dd8N5GsweAPqvnFVcVP7Tyrsvh063brby96GaywngEIgxewZ5XK2Xsvqpm0829; CURRENT_SESSION=B5hYrmsvgo17EBTTyOf1lF8Ci28eQZP2MPopBcE7iwSS7os78nnXhU/aNkfRvrswYUTm+KN36sAWQPgUAs5ICBXo4JPm85tS; HTTP_CSRF_TOKEN=d5O0XWc6eLuc5GaN7hqI3sbfSkpWShe; XSRF-TOKEN=d5O0XWc6eLuc5GaN7hqI3sbfSkpWShe'

Cookies in above call are acquired from FMG request after user login.


**RESPONSE:**

.. code::

   * Trying 10.106.18.100...
   * TCP_NODELAY set
   * Connected to 10.106.18.100 (10.106.18.100) port 80 (#0)
   > GET /fortiwan/ HTTP/1.1
   > Host: 10.106.18.100
   > User-Agent: curl/7.58.0
   > Accept: */*
   > Cookie: csrftoken=m6Dd8N5GsweAPqvnFVcVP7Tyrsvh063brby96GaywngEIgxewZ5XK2Xsvqpm0829; auth_state=; remoteauth=; CURRENT_SESSION=B5hYrmsvgo17EBTTyOf1lF8Ci28eQZP2MPopBcE7iwSS7os78nnXhU/aNkfRvrswYUTm+KN36sAWQPgUAs5ICBXo4JPm85tS; HTTP_CSRF_TOKEN=d5O0XWc6eLuc5GaN7hqI3sbfSkpWShe; XSRF-TOKEN=d5O0XWc6eLuc5GaN7hqI3sbfSkpWShe
   >
   < HTTP/1.1 200 OK
   < Date: Fri, 20 Dec 2019 01:06:39 GMT
   < X-Frame-Options: SAMEORIGIN
   < Expires: Thu, 01 Jan 1970 00:00:00 GMT
   < ETag: 1576520236129
   < Content-Type: text/html
   < Content-Length: 737
   < Server: Jetty(9.4.18.v20190429)
   < Set-Cookie: token=36dbccea-384f-4fe4-9df4-ed6bd737b0a8;Path=/
   < Vary: Accept-Encoding
   < X-UA-Compatible: IE=Edge
   < X-XSS-Protection: 1; mode=block
   < X-Content-Type-Options: nosniff
   ......

How to backup SD-WAN Orchestrator
+++++++++++++++++++++++++++++++++

**REQUEST:**

.. code::

   curl -H 'Cookie:token=a8013337-b388-4649-bd31-103a6c28b456' 'http://fmg-ip/fortiwan/rest/v1/controller_config/download'

How to restore a SD-WAN Orchestrator
++++++++++++++++++++++++++++++++++++

**REQUEST:**

.. code::

   curl -v -F file=@/location/of/backup/file/controller-store.config -H 'Cookie: token=a8013337-b388-4649-bd31-103a6c28b456' http://127.0.0.1/fortiwan/rest/v1/controller_config/upload

