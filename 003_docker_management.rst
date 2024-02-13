Docker Management
=================

How to get docker status?
-------------------------

Caught in #0600260.

**REQUEST:**

.. code:: json

	  {
	    "id": 2,
	    "method": "exec",
	    "params": [
	      {
	        "url": "/sys/api/docker/status"
	      }
            ]
          }

**RESPONSE**:

.. code:: json

	  {
	    "result": [
	      {
	        "data": {
		  "fortiportal": {
		    "status": 0
		  },
		  "fortiwlm": {
		    "status": 0
		  },
		  "sdwancontroller": {
		    "status": 3
		  }
		},
		"status": {
		  "code": 0,
		  "message": "OK"
		},
		"url": "/sys/api/docker/status"
	      }
	    ]
	  }

This is the response you could get at the time you enable SD-WAN
Orchestrator and the fortimanager is downloading it:

.. code-block:: json

		{
		  "id": "198a1e36-64f5-4106-bbb8-ba3bd606641e",
		  "result": [
		    {
		      "data": {
		        "fortiportal": {
			  "status": 0
			},
			"fortiwlm": {
		          "status": 0
			},
			"sdwancontroller": {
			  "progress": 84,
			  "status": 1
			}
		      },
		      "status": {
		        "code": 0,
			"message": "OK"
		      },
		      "url": "/sys/api/docker/status"
		    }
		  ]
		}

How to upgrade a docker component?
----------------------------------

Caught in PMDB #9360

**REQUEST**:

.. code:: json

	  {
	    "id": 2,
	    "method": "exec",
	    "params": [
	      {
	        "url": "/sys/api/docker/upgrade",
		"data": [
		  {
		    "docker": "fortiwlm"
		  }
		]
	      }
	    ],
	    "session": "{{session}}"
	  }

``docker`` could have following values: ``sdwancontroller``, ``fortiportal``, or ``fortiwlm``.
