# Chronosphere + Snowflake Integration Demo
- [Chronosphere + Snowflake Integration Demo](#chronosphere--snowflake-integration-demo)
  - [Overview](#overview)
  - [Potential Target vs Simulated Approach](#potential-target-vs-simulated-approach)
    - [Components](#components)
    - [Target Production Model](#target-production-model)
    - [Simulated Demo Model](#simulated-demo-model)
  - [Native Snowflake Monitoring vs Chronosphere Capabilities](#native-snowflake-monitoring-vs-chronosphere-capabilities)
  - [Technical Challenges](#technical-challenges)
    - [1. Transforming Structured Data into Telemetry Format](#1-transforming-structured-data-into-telemetry-format)
    - [2. Running a Collector with Access to Snowflake](#2-running-a-collector-with-access-to-snowflake)
    - [3. Scheduling, Rate-Limiting, and Data Freshness](#3-scheduling-rate-limiting-and-data-freshness)
  - [Architecture](#architecture)



## Overview
This demo simulates exporting metrics from Snowflake and sending them into the Chronosphere Observability Platform using OpenTelemetry Collector.

Since access to Snowflake and Chronosphere is unavailable, mock data is generated and logged to demonstrate data flow.

Steps:
1. Python script generates fake Snowflake metrics and writes to a log file
2. OTel Collector reads the log file, parses metric lines, and outputs structured metrics
3. `debug` exporter shows what would be sent to Chronosphere as output in the command line

## Potential Target vs Simulated Approach
### Components

| Real Component       | Simulated Substitute                         |
|----------------------|----------------------------------------------|
| Snowflake            | Python script generating mock metrics        |
| OTel Collector       | OTel Collector container                     |
| Chronosphere         | Metrics exporter (prints to console)         |

### <center>Target Production Model
![integration](./diagrams/integration.png)

### <center>Simulated Demo Model
![integration](./diagrams/demo-integration.png)

## Native Snowflake Monitoring vs Chronosphere Capabilities

| Feature                    | Snowflake Monitoring                | Monitoring via Chronosphere               |
|----------------------------|-------------------------------------|-------------------------------------------|
| Unified Observability      | Limited to Snowflake                | Integrates with other systems             |
| Custom Dashboards          | Predefined, less flexible           | Highly customizable                       |
| Query-Level Insights       | Available                           | Available with detailed metrics           |
| Alerting and Notifications | Basic                               | Advanced with custom rules                |
| Scalability                | Good                                | Excellent for hybrid environments         |
| Multi-Source Integration   | No                                  | Yes                                       |
| Cost Optimization Metrics  | Limited                             | Extensive                                 |

## Technical Challenges

### 1. Transforming Structured Data into Telemetry Format
**Challenge**:
Chronosphere expects certain telemetry in an OTLP or Prometheus format. Snowflake doesn’t emit native OTLP or Prometheus metrics for certain data.

**Details**:
Some of Snowflake's data is tabular; converting it to time-series metrics with dimensions/labels will require additional logic.
- E.g., transforming:
  
  `SELECT warehouse_name, avg(credits_used) FROM ...`

  into:

  `snowflake_credits_used{warehouse="analytics_wh"} 41.2`

**Impact**:
May require custom ETL logic, scheduled Snowflake tasks, or use of Chronosphere's telemetry pipeline to extract and reshape this data.

### 2. Running a Collector with Access to Snowflake
**Challenge**:
While Snowflake provides the option for an OTel Collector internally, additional setup of an external OTel or Chronosphere collector may be necessary depending on configuration.

**Details**:

When using an external collector one must:
- Run a collector in your own infrastructure
- Securely authenticate to Snowflake via OAuth/keys
- Schedule polling without overloading query quotas

### 3. Scheduling, Rate-Limiting, and Data Freshness
**Challenge**:
Deciding how frequently to extract and send metrics

**Details**:
Snowflake’s data is not real-time by nature, as it is generally updated every X minutes. Some things to keep in mind:
- Needs careful time-windowing and deduplication
- Hitting Snowflake rate limits or warehouse costs
- Sending stale or duplicated data



## Architecture
There are many ways to integrate Snowflake with Chronosphere's Telemetry Pipeline and Observability Platform. This diagram shows some potential integration paths depending on a variety of use cases.

![arch](./diagrams/arch-diagram.png)
