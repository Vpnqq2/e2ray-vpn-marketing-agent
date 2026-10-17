from datetime import date
from pathlib import Path

OUT = Path("outputs")
OUT.mkdir(exist_ok=True)

ideas = [
    {
        "angle": "Simple connection walkthrough",
        "hook": "Need a simple way to connect to a VPN?",
        "script": [
            "Show the E2ray VPN home screen.",
            "Show the available server list.",
            "Choose a server and tap Connect.",
            "Show the real connection status. Avoid promising that every server is always available or fastest."
        ],
        "caption": "Meet E2ray VPN: a simple way to explore VPN server options and connect. Availability and performance can vary by network and location.",
        "hashtags": "#E2rayVPN #VPN #AndroidApps #TechTips"
    },
    {
        "angle": "Protocol options",
        "hook": "One app, multiple VPN protocol options.",
        "script": [
            "Open the protocol or configuration area in E2ray VPN.",
            "Show only protocol options that are present in the current app version.",
            "Briefly explain that options suit different network conditions.",
            "Do not claim that any protocol bypasses every restriction or guarantees privacy."
        ],
        "caption": "Take a look at the protocol options available in E2ray VPN. Results depend on your network, server and configuration.",
        "hashtags": "#E2rayVPN #VPNProtocol #Android #Tech"
    },
    {
        "angle": "Real-world server test",
        "hook": "Let's compare VPN server connections.",
        "script": [
            "Show the server list.",
            "Choose one server and show the actual connection result.",
            "If you show a speed or ping test, display the real measurement and test conditions.",
            "Avoid implying that one result applies to all users."
        ],
        "caption": "A quick look at testing VPN server connections with E2ray VPN. Your results may differ by location, device and network.",
        "hashtags": "#E2rayVPN #VPNTest #MobileInternet #AndroidApps"
    },
]

# Rotate content by calendar day so the daily pack changes.
item = ideas[date.today().toordinal() % len(ideas)]
today = date.today().isoformat()

pack = f"""# E2ray VPN TikTok Content Pack

**Date:** {today}
**Content angle:** {item['angle']}

## Hook (first seconds)
{item['hook']}

## Suggested screen-recording sequence
""" + "\n".join(f"{i}. {line}" for i, line in enumerate(item["script"], 1)) + f"""

## Caption
{item['caption']}

## Hashtags
{item['hashtags']}

## Before posting
- Confirm the recording matches the current public version of E2ray VPN.
- Remove private notifications and sensitive information from the recording.
- Use only footage, music and other assets you have permission to publish.
- Review all technical claims. Do not promise guaranteed speed, anonymity, or access.
- Add the official Google Play link to your profile or an allowed link field; do not assume links are clickable in every caption.
- This pack was generated from local templates, not from an AI model.
"""

(OUT / "content-pack.md").write_text(pack, encoding="utf-8")
(OUT / "on_screen_hook.txt").write_text(item["hook"] + "\n", encoding="utf-8")
(OUT / "caption.txt").write_text(item["caption"] + "\n\n" + item["hashtags"] + "\n", encoding="utf-8")
print(f"Created content pack for {today}: {item['angle']}")
