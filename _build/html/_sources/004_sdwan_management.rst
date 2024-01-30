SD-WAN Management
=================

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

