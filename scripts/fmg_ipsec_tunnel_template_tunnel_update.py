"""
Update an existing tunnel in an IPsec Tunnel Template
"""

from pyFMG.fortimgr import FortiManager

IP = "10.210.34.120"
USERNAME = "devops"
PASSWORD = "fortinet"

with FortiManager(
    IP,
    USERNAME,
    PASSWORD,
    verbose=True,
    disable_request_warnings=True,
) as fmg:

    ADOM = "demo"
    MKEY = "ipsec_tunnel_template_001"
    SEQ = 4
    url = f"/pm/config/adom/{ADOM}/template/_ipsec/{MKEY}/action-list/{SEQ}"

    # Get the tunnel you wan to modify
    response = fmg.get(url)
    tunnel = response[1].copy()

    # Get rid of seq, and OIDs (you have multiple OIDs)
    del tunnel["oid"]
    del tunnel["seq"]
    del tunnel["value"]["vpn ipsec phase1-interface"]["oid"]
    for p2 in tunnel["value"]["vpn ipsec phase2-interface"]:
        del p2["oid"]

    # Modify your tunnel
    tunnel["value"]["vpn ipsec phase1-interface"]["remote-gw"] = "10.6.0.1"

    # Update your tunnel
    fmg.debug = True
    fmg.update(
        url,
        data=tunnel,
    )
    fmg.debug = False
