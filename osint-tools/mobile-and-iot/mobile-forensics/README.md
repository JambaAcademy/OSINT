# Mobile Forensics

## Overview

This section covers analysis of mobile device data obtained through a lawful, authorized, or consented process — most commonly a chat export, call log export, or full device backup extraction. See `chat_export_analyzer.py` in this folder for a ready-to-use script that parses a common chat export format (WhatsApp-style plain text export) and produces participant activity statistics, a timeline summary, and basic entity extraction.

**Authorization requirement:** Only analyze mobile device data that you own, that you have the device owner's informed consent to analyze, or that you are authorized to examine under a documented legal process. This category does not cover techniques for extracting data from a device without the owner's knowledge or authorization.

---

## Mobile Forensics Platforms

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Cellebrite UFED | Widely used commercial mobile forensics platform for law enforcement and authorized corporate investigations | Full device extraction and analysis under proper legal authority | Paid, enterprise/government licensing |
| Magnet AXIOM | Commercial digital forensics platform covering mobile, computer, and cloud data sources | Cross-source forensic analysis in an authorized investigation | Paid, enterprise |
| Autopsy / The Sleuth Kit | Open-source digital forensics platform | Authorized forensic analysis on a budget, including some mobile backup support | Free, open source |
| Android/iOS native backup tools | Standard device backup mechanisms (e.g., Android backup, iTunes/Finder encrypted backup) | Basic, consented data extraction without specialized forensic hardware | Free, built-in |

---

## Using the Included Chat Export Analyzer

`chat_export_analyzer.py` parses a WhatsApp-style plain text chat export (the format produced by the "Export Chat" feature available to any chat participant) and produces:

- Message count per participant
- Activity timeline (messages per day)
- Basic entity extraction (reusing the pattern-matching approach from `ai-powered-tools/natural-language-processing/extract_entities.py`) across all messages combined

```bash
python chat_export_analyzer.py --file chat_export.txt
```

See `sample_chat_export.txt` in this folder for the expected input format.

---

## Usage Notes

- Chat export formats vary slightly between platforms and even between app versions; this script is written for the common WhatsApp export format (`[date, time] Sender: Message` or similar) and may need adjustment for other platforms' export formats.
- Always confirm the authenticity and completeness of a chat export before relying on it; exports can be edited before being shared with you, and a partial export can omit relevant context. Corroborate significant findings against other evidence where possible.

---

## Legal and Ethical Notes

- Only analyze chat exports and other mobile data you have lawfully obtained access to, per the authorization requirement stated above.
- Where a chat export is provided by one participant in a conversation, be aware that it reflects only that participant's device copy and may not include messages deleted on their device before export, or content from participants who have left a group.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
