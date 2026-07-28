# VPN and Tor Setup

## Overview

This section covers VPN and Tor configuration for investigative browsing, where masking the analyst's originating IP address and network identity reduces the risk of an investigation subject detecting research activity before appropriate, and reduces the analyst's exposure to network-level surveillance. See `opsec-verification-checklist.md` in this folder for a ready-to-use checklist confirming a VPN/Tor setup is actually working as intended before relying on it.

---

## VPN Services

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Commercial no-logs VPN providers | Numerous commercial VPN providers offer encrypted tunneling with a stated no-logging policy | General-purpose IP masking for investigative browsing | Paid, subscription |
| Organizational/corporate VPN | Many organizations provide their own VPN infrastructure for staff | Investigative browsing under organizational network policy and support | Typically provided by employer |
| Self-hosted VPN (e.g., WireGuard on a personal cloud server) | Running your own VPN server rather than using a commercial provider | Full control over logging and configuration, at the cost of needing to manage the infrastructure yourself | Cost of cloud hosting |

## Tor

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Tor Browser | Official browser bundle routing traffic through the Tor anonymity network | Strong anonymity for sensitive research, at the cost of slower browsing speed and some site compatibility issues | Free |
| Tails OS | A live, amnesic operating system that routes all traffic through Tor by default and leaves no trace on the host machine | High-sensitivity investigative work requiring strong anonymity and no persistent local trace | Free |
| Whonix | A Tor-focused operating system split into a gateway and workstation virtual machine for additional isolation | Advanced users wanting strong Tor-based isolation within a persistent VM setup | Free |

---

## Using the Included OPSEC Verification Checklist

`opsec-verification-checklist.md` provides a step-by-step checklist for confirming that a VPN or Tor setup is actually functioning as intended — checking for IP leaks, DNS leaks, WebRTC leaks, and kill-switch behavior — before relying on it for sensitive investigative work. A misconfigured VPN or browser can leak your real IP address or DNS queries even while appearing to be connected.

---

## Usage Notes

- **Test before you rely on it.** A VPN or Tor connection that appears active can still leak your real IP address through DNS leaks, WebRTC, or an inactive kill switch; always run the leak tests in the included checklist before beginning sensitive work, not just once at initial setup.
- **VPN choice affects your threat model.** A commercial VPN provider can, in principle, see your traffic and be compelled to produce logs it retains; choose a provider and logging policy appropriate to the sensitivity of your work, and consider Tor for the highest-sensitivity research.
- **Tor is not always the right tool.** Tor's exit-node traffic is sometimes blocked or heavily challenged (CAPTCHAs) by mainstream websites, and its lower speed can be impractical for routine browsing; reserve it for research where its stronger anonymity properties are actually needed.

---

## Legal and Ethical Notes

- VPN and Tor use is lawful in most jurisdictions for general privacy purposes, though a small number of countries restrict or ban VPN/Tor use; confirm the legal status in your jurisdiction and the jurisdiction you are researching from if traveling.
- These tools protect the confidentiality of lawful investigative research; they should not be used to circumvent a platform's explicit ban on the investigator personally, evade law enforcement, or facilitate unauthorized access to any system.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
