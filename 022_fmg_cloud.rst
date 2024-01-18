FortiManager Cloud
==================

How to create an IAM API user
-----------------------------

1. Navigate to ``https://support.fortinet.com``
2. Login using your FortiCloud account
3. Click *Services* > *IAM (Beta)*
4. Click *API Users* > *ADD API USER*
5. In *1. API User Details* enter a description (for instance ``FortiManager
   API user``) then click *NEXT* 
6. In *2. Permissions* manage to get the following table:

   +----------------------------+---------+-------------+-----------------------+
   |*Cloud Management & Service*|*Access* |*Access Type*|*Additional Permission*|
   +============================+=========+=============+=======================+
   | *FortiManager Cloud*       | checked | *Customer*  | *-*                   |
   +----------------------------+---------+-------------+-----------------------+

   Then click *NEXT*

7. In *3. Confirmation* click *CONFIRM*
8. In *4. Successful API User Registration* click *DOWNLOAD CREDENTIALS*
9. We obtain the file ``API_Credential_E8766032-7319-409F-902A-REDACTEDD045_12_10_2021.txt``

   .. literalinclude:: datas/API_Credential_E8766032-7309-409F-902A-REDACTEDD045_12_10_2021.txt

How to generate the access token?
---------------------------------

You will have to build the following JSON block using the information returned
in the credentials file:

.. code-block:: json

   {
       "username": "{apiId}>",
       "password": "{password}",
       "client_id": "{clientId}",
       "grant_type": "password"
   }

For instance:

**REQUEST:**

.. code-block::

   curl -H 'Content-Type: application/json' -X POST 'https://customerapiauth.fortinet.com/api/v1/oauth/token/' -d '{"username": "E8766032-7319-409F-902A-96376117D045", "password": "7b6593822fcc9860f81fb05d82ca3131!1Aa", "client_id": "FortiManager", "grant_type": "password"}'

**RESPONSE:**

.. code-block:: json

   {"access_token": "0cVmxFd3fQJsYThFxDuHaKY2HGKLW4", "expires_in": 14400, "message": "successfully authenticated", "refresh_token": "GVqCZ3F15xTSUZuOAZq5RF0Jfx3Ns3", "scope": "read write", "status": "success", "token_type": "Bearer"}

You now have to conserve somewhere the returned ``access_token``.

How to issue a FMG JSON RPC API call?
-------------------------------------

1. Authenticate to the FortiManager Cloud instance

   **REQUEST:**

   .. code-block::

      curl -k -H "Content-Type: application/json" "https://106728.ca-west-1.fortimanager.forticloud.com/p/forticloud_jsonrpc_login/" -d '{"access_token": "0cVmxFd3fQJsYThFxDuHaKY2HGKLW4"}'

   **RESPONSE:**

   .. code-block:: json

      {"session":"08sjyDDgwgtAqFfcZ8gzD7RwRn1lr9T4UKjJ4B8w2ElTDjuTWXPOnssVP+w6B+obkPrtGwXchs92XvoG7QCBkg=="}
      
2. Use the returned ``session`` ID for your sub-sequent calls

   **REQUEST:**

   .. code-block:: 

      curl -k -H "Content-Type: application/json" "https://106728.ca-west-1.fortimanager.forticloud.com/jsonrpc" -d '{"method": "get", "params": [{"url": "/sys/status"}], "session": "08sjyDDgwgtAqFfcZ8gzD7RwRn1lr9T4UKjJ4B8w2ElTDjuTWXPOnssVP+w6B+obkPrtGwXchs92XvoG7QCBkg==", "id": 1}'

   **RESPONSE:**

   .. code-block::

      { "id": 1, "result": [ { "data": { "Admin Domain Configuration": "Disabled", "BIOS version": "04000002", "Branch Point": "0113", "Build": "4661", "Current Time": "Tue Oct 12 13:11:54 CEST 2021", "Daylight Time Saving": "Yes", "FIPS Mode": "Disabled", "HA Mode": "Stand Alone", "Hostname": "FMG-VM64-VIO-CLOUD", "License Status": "Valid", "Major": 7, "Max Number of Admin Domains": 10000, "Max Number of Device Groups": 10000, "Minor": 0, "Offline Mode": "Disabled", "Patch": 1, "Platform Full Name": "FortiManager-VM64-VIO-CLOUD", "Platform Type": "FMG-VM64-VIO-CLOUD", "Release Version Information": " (GA)", "Serial Number": "FMGVCLTM19000055", "TZ": "Europe\/Brussels", "Time Zone": "(GMT+1:00) Brussels, Copenhagen, Madrid, Paris.", "Version": "v7.0.1-build4661 210831 (GA)", "x86-64 Applications": "Yes" }, "status": { "code": 0, "message": "OK" }, "url": "\/sys\/status" } ] }