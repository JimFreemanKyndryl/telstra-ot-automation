# OSS Architecture and Device Integration

## Overview
This diagram illustrates how Telstra's Operational Support Systems (OSS) integrate with various device categories for centralized management.

```mermaid
graph TB
    subgraph "Telstra OSS Operations"
        OSS[Network Management Systems]
        INV[Inventory Management]
        PROV[Provisioning System]
        PERF[Performance Monitoring]
        FAULT[Fault Management]
        SEC[Security Management]
    end
    
    subgraph "Telstra Network"
        subgraph "Mobile Network"
            RAN[Mobile Network Devices<br/>- eNodeB/gNodeB<br/>- Small Cells]
        end
        
        subgraph "Core Network"
            CORE[Core Routers & Switches<br/>- Cisco ASR<br/>- Juniper MX]
        end
        
        subgraph "Transport Network"
            OPT[Optical Transport<br/>- Ciena DWDM<br/>- Nokia Photonic]
        end
        
        subgraph "Access Network"
            ACCESS[Access Devices<br/>- DSLAMs<br/>- OLTs<br/>- CMTS]
        end
        
        subgraph "Customer Layer"
            CPE[Customer Premises<br/>- Smart Modems<br/>- Business Routers]
        end
    end
    
    OSS --> INV
    OSS --> PROV
    OSS --> PERF
    OSS --> FAULT
    OSS --> SEC
    
    INV -.->|Inventory Data| RAN
    INV -.->|Inventory Data| CORE
    INV -.->|Inventory Data| OPT
    INV -.->|Inventory Data| ACCESS
    INV -.->|Inventory Data| CPE
    
    PROV -->|Configuration| RAN
    PROV -->|Configuration| CORE
    PROV -->|Configuration| OPT
    PROV -->|Configuration| ACCESS
    PROV -->|Configuration| CPE
    
    PERF <--|Telemetry| RAN
    PERF <--|Telemetry| CORE
    PERF <--|Telemetry| OPT
    PERF <--|Telemetry| ACCESS
    PERF <--|Telemetry| CPE
    
    FAULT <--|Alarms| RAN
    FAULT <--|Alarms| CORE
    FAULT <--|Alarms| OPT
    FAULT <--|Alarms| ACCESS
    FAULT <--|Alarms| CPE
    
    RAN <-->|Backhaul| CORE
    CORE <-->|Transport| OPT
    CORE <-->|Distribution| ACCESS
    ACCESS <-->|Last Mile| CPE
```

## Key Integration Points

### Management Protocols
- **NETCONF/RESTCONF**: Modern configuration management
- **SNMP**: Traditional monitoring and basic configuration
- **TR-069/TR-369**: CPE management protocols
- **gRPC**: Streaming telemetry for real-time data

### Data Flows
1. **Northbound** (Device → OSS): Alarms, performance metrics, status updates
2. **Southbound** (OSS → Device): Configuration changes, software updates, control commands

### Security Layers
- Centralized authentication (TACACS+/RADIUS)
- Encrypted management channels
- Role-based access control
- Automated compliance auditing
