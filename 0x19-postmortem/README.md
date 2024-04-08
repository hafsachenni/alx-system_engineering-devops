# Postmortem: Web Stack Debugging Outage

## Issue Summary

- **Duration:**
    - Start Time: April 7, 2024, 11:00 AM
    - End Time: April 7, 2024, 15:00 PM
- **Impact:** 
  - Our website experienced a complete outage during the specified duration. Visitors were unable to access any content or services hosted on the website.
- **Root Cause:** 
  - The outage was caused by a misconfiguration in the server's firewall settings, leading to unintended blocking of incoming traffic.

## Timeline

- **11:15 AM:** 
  - Issue detected as I attempted to access the website and received a connection timeout error.
- **11:30 AM:** 
  - Investigation began to identify potential causes, initially focusing on server health and network connectivity.
- **12:30 PM:** 
  - Noticed abnormal firewall log entries indicating blocked traffic.
- **13:45 PM:** 
  - Realized recent firewall rule changes might have inadvertently caused the outage.
- **14:00 PM:** 
  - Disabled the latest firewall rule changes to restore normal traffic flow.
- **15:00 PM:** 
  - Website service confirmed to be operational again.

## Root Cause and Resolution

- **Root Cause Explanation:**
  - The misconfiguration in the server's firewall settings resulted in the unintended blocking of incoming traffic, effectively rendering the website inaccessible.
- **Resolution Details:**
  - The issue was resolved by reverting the recent firewall rule changes, restoring normal traffic flow to the server.


## Corrective and Preventative Measures

- **Improvement/Fixes:**
  - We implemented stricter change management procedures for firewall rule modifications to prevent inadvertent misconfigurations.
  - We now regularly review and audit firewall settings to ensure they align with security requirements.
- **Tasks to Address the Issue:**
  - Document the incident, including root cause analysis and resolution steps, for future reference.
  - Schedule regular firewall configuration reviews and audits to identify and rectify potential misconfigurations.

By implementing these corrective measures and enhancing preventive actions, We aim to minimize the risk of future outages and ensure the continued availability of our website.
