# Snowflake to Chronosphere Integration Demo
- [Snowflake to Chronosphere Integration Demo](#snowflake-to-chronosphere-integration-demo)
  - [Overview](#overview)
  - [Potential Target vs Simulated Approach](#potential-target-vs-simulated-approach)
    - [Components](#components)
    - [Target Production Model](#target-production-model)
    - [Simulated Demo Model](#simulated-demo-model)
  - [Native Snowflake Monitoring vs Chronosphere Capabilities](#native-snowflake-monitoring-vs-chronosphere-capabilities)
  - [Architecture](#architecture)

## Overview
This demo simulates exporting metrics from Snowflake and sending them into the Chronosphere Observability Platform using OpenTelemetry Collector.

Since access to Snowflake and Chronosphere is unavailable, mock data is generated and logged to demonstrate data flow.

Steps:
1. Python script generates fake Snowflake metrics and writes to a log file
2. OTel Collector reads the log file, parses metric lines, and outputs structured logs
3. `debug` exporter shows what would be sent to Chronosphere as output in the command line

## Potential Target vs Simulated Approach
### Components

| Real Component       | Simulated Substitute                         |
|----------------------|----------------------------------------------|
| Snowflake            | Python script generating mock metrics        |
| OTel Collector       | OTel Collector container                     |
| Chronosphere         | Logging exporter (prints to console)         |

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


## Architecture
There are many ways to integrate Snowflake with Chronosphere's Telemetry Pipeline and Observability Platform. This diagram shows some potential integration paths depending on a variety of use cases.

![arch](./diagrams/arch-diagram.png)
