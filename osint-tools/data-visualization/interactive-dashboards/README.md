# Interactive Dashboards

## Overview

Interactive, browser-based dashboards let a stakeholder explore findings themselves (filtering, hovering for detail, switching between views) rather than reading a static document. See `findings_dashboard_template.html` in this folder for a ready-to-use, self-contained HTML template that renders an interactive dashboard from embedded findings data, requiring no server or installation.

---

## Dashboard Platforms

| Tool | Description | Best For | Cost |
|---|---|---|---|
| Tableau | Leading commercial business intelligence and dashboard platform | Enterprise-grade interactive dashboards with extensive data source connectivity | Paid (Tableau Public free tier available for public dashboards) |
| Microsoft Power BI | Commercial business intelligence platform, strong integration with Microsoft data sources | Organizations already using the Microsoft ecosystem | Freemium/Paid |
| Google Looker Studio | Free, web-based dashboard and reporting platform | Free, quick dashboards connected to Google data sources (Sheets, Analytics, BigQuery) | Free |
| Observable | Browser-based platform for building interactive data visualizations and notebooks with JavaScript | Custom, code-driven interactive visualizations shareable via a link | Freemium/Paid |
| Streamlit / Dash (Python) | Python frameworks for building interactive data apps and dashboards | Analysts comfortable in Python who want a custom interactive tool without heavy JavaScript | Free, open source (hosting may incur cost) |

---

## Using the Included Dashboard Template

`findings_dashboard_template.html` is a single, self-contained HTML file (using Chart.js loaded from a public CDN) that renders an interactive dashboard — summary statistics, a findings-by-category chart, a confidence-level breakdown, and a filterable findings table — directly from a JSON data block embedded in the file. No installation, server, or build step is required; simply open the file in any modern web browser.

To use it with your own data:

1. Open `findings_dashboard_template.html` in a text editor.
2. Locate the `const findingsData = { ... }` block near the top of the `<script>` section.
3. Replace the sample data with your own findings, following the same structure.
4. Save and open the file in a browser (or share the file directly — everything needed is embedded in it).

---

## Usage Notes

- Because this template embeds its data directly in the HTML file, treat the resulting file with the same classification and handling requirements as any other report containing your findings; sharing the file shares the underlying data.
- This template uses a Chart.js library loaded from a public CDN, which requires an internet connection to render charts; for a fully offline-capable version, download the Chart.js library file and reference it locally instead of via CDN.
- For very large datasets (hundreds of findings), consider a dedicated platform (Tableau, Power BI, Looker Studio) rather than this lightweight template, which is designed for a single investigation's findings rather than large-scale data exploration.

---

## Legal and Ethical Notes

- Apply the same classification and distribution controls to a generated dashboard file as you would to the underlying report; an interactive HTML file is as easy to forward or copy as any other document.
- Where a dashboard presents findings about identifiable private individuals, apply the elevated standard in `people-investigation/README.md` to what is included and to whom the file is distributed.

---

**Version:** 1.0
**Last Updated:** 2026-07-25
