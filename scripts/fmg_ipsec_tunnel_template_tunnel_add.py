"""
Create a new tunnel in an IPsec Tunnel Template
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
    url = f"/pm/config/adom/{ADOM}/template/_ipsec/{MKEY}/action-list"

    # Get the existing tunnels, last one is the one you want to use as a
    # reference

    response = fmg.get(url)

    # Extract the list of tunnels
    tunnels = response[1]

    # Last one is the one to be used as a reference
    tunnel = tunnels[-1].copy()

    # Get rid of seq, and OIDs (you have multiple OIDs)
    del tunnel["oid"]
    del tunnel["seq"]
    del tunnel["value"]["vpn ipsec phase1-interface"]["oid"]
    for p2 in tunnel["value"]["vpn ipsec phase2-interface"]:
        del p2["oid"]

    # Adapt the tunnel configuration
    TUNNEL_NAME = "ol_isp4"
    tunnel["value"]["name"] = TUNNEL_NAME
    tunnel["value"]["vpn ipsec phase1-interface"]["remote-gw"] = "10.4.0.1"
    tunnel["value"]["vpn ipsec phase1-interface"]["name"] = TUNNEL_NAME
    tunnel["value"]["vpn ipsec phase1-interface"]["interface"] = ["port4"]
    tunnel["value"]["vpn ipsec phase1-interface"]["mode-cfg"] = "enable"
    tunnel["value"]["vpn ipsec phase1-interface"]["net-device"] = "enable"
    tunnel["value"]["vpn ipsec phase2-interface"][0]["name"] = TUNNEL_NAME
    tunnel["value"]["vpn ipsec phase2-interface"][0]["phase1name"] = TUNNEL_NAME

    # Add this new tunnel in the IPsec Tunnel Template
    fmg.debug = True
    fmg.add(
        url,
        data=tunnel,
    )
    fmg.debug = False
