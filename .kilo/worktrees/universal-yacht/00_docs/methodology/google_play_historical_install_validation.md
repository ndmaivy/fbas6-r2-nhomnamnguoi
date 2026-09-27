# Google Play Historical Install Validation

## Research purpose

Attempt to obtain historical public Google Play cumulative install signals for TCInvest from archived store pages between Sep 2024 and Aug 2025.

## Data source

Wayback Machine archived copies of the public Google Play listing for package `com.fss.tcbs.mobiletrading`. The collector queried both the Vietnam-localized URL (`hl=vi&gl=VN`) and the canonical listing URL. It found 0 unique CDX snapshot records in the diagnostic query window.

CDX/query notes:

- localized exact — https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: 0 snapshots; CDX returned no rows
- canonical exact — https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: 0 snapshots; CDX returned no rows
- canonical prefix — https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: 0 snapshots; CDX returned no rows
- package wildcard — play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading*: 0 snapshots; CDX returned no rows
- Availability 2024-09 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2024-09 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture
- Availability 2024-10 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2024-10 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture
- Availability 2024-11 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2024-11 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture
- Availability 2024-12 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2024-12 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture
- Availability 2025-01 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2025-01 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture
- Availability 2025-02 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2025-02 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture
- Availability 2025-03 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2025-03 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture
- Availability 2025-04 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2025-04 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture
- Availability 2025-05 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2025-05 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture
- Availability 2025-06 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2025-06 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture
- Availability 2025-07 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2025-07 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture
- Availability 2025-08 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading&hl=vi&gl=VN: no capture
- Availability 2025-08 https://play.google.com/store/apps/details?id=com.fss.tcbs.mobiletrading: no capture

## Snapshot selection

For each target month, the collector selected the latest available snapshot within that month. When a month had no snapshot, it considered the closest snapshot within 15 days of that month-end. It did not carry observations forward and did not interpolate missing values.

## What the metric means

Historical installs extracted from archived Google Play pages are cumulative public install bands/signals.

They are **not**:

- exact monthly downloads;
- Google Play Console first-party acquisition data;
- App Store downloads;
- TCBS internal analytics.

## Extraction and QA result

- Target months: 12
- Months with a usable install signal: 0
- Usable months: None
- Months without an extracted install signal: 2024-09, 2024-10, 2024-11, 2024-12, 2025-01, 2025-02, 2025-03, 2025-04, 2025-05, 2025-06, 2025-07, 2025-08
- Extracted public install bands: None
- Archived HTML files downloaded and inspectable: 0
- Overall usability: **NOT_USABLE**

Extraction required an install-like numeric token to occur near an explicit Google Play install/download label. Ambiguous or context-free numbers were not assigned to install fields. Raw archived HTML was retained for every successfully downloaded selected snapshot.

The requested inspection of at least two archived HTML snapshots could not be performed because Wayback returned no captures for the tested exact, prefix, wildcard, or month-end availability queries. No placeholder HTML was created.

## Why it is useful

When observations exist, archived cumulative public install bands can be used as an independent, coarse sanity check for third-party estimated downloads such as Similarweb. A change between observations is reported only as an **observed cumulative install lower-bound change**, never as official monthly downloads.

## Important limitation

Google Play public install counts are usually coarse thresholds, so they may remain unchanged despite substantial new downloads. An unchanged band does not imply zero new downloads.

Wayback coverage may also be incomplete or inconsistent. Archived pages can contain consent/interstitial responses, dynamically rendered content, or incomplete replay assets. Missing extraction therefore does not establish that the live listing lacked an install signal at that time.
