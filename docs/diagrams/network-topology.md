# Telstra Network Topology Overview

## High-Level Network Architecture

```mermaid
graph TD
    subgraph "International"
        INT[International<br/>Gateways]
    end
    
    subgraph "National Core"
        SYD[Sydney<br/>Core PoP]
        MEL[Melbourne<br/>Core PoP]
        BNE[Brisbane<br/>Core PoP]
        PER[Perth<br/>Core PoP]
        ADL[Adelaide<br/>Core PoP]
    end
    
    subgraph "Metro Networks"
        MSYD[Sydney<br/>Metro Ring]
        MMEL[Melbourne<br/>Metro Ring]
        MBNE[Brisbane<br/>Metro Ring]
    end
    
    subgraph "Access Layer"
        EXCH1[Exchange 1<br/>DSLAMs/OLTs]
        EXCH2[Exchange 2<br/>DSLAMs/OLTs]
        CELL1[Cell Site 1<br/>4G/5G RAN]
        CELL2[Cell Site 2<br/>4G/5G RAN]
    end
    
    subgraph "Customer Edge"
        BUS1[Business<br/>Customer]
        RES1[Residential<br/>Customer]
        IOT1[IoT<br/>Devices]
    end
    
    INT <==> SYD
    INT <==> MEL
    
    SYD <==> MEL
    MEL <==> ADL
    ADL <==> PER
    PER <==> BNE
    BNE <==> SYD
    
    SYD ==> MSYD
    MEL ==> MMEL
    BNE ==> MBNE
    
    MSYD ==> EXCH1
    MSYD ==> CELL1
    MMEL ==> EXCH2
    MMEL ==> CELL2
    
    EXCH1 --> BUS1
    EXCH2 --> RES1
    CELL1 -.-> IOT1
    CELL2 -.-> RES1
    
    style INT fill:#ff9999
    style SYD fill:#9999ff
    style MEL fill:#9999ff
    style BNE fill:#9999ff
    style PER fill:#9999ff
    style ADL fill:#9999ff
```

## Network Layers

### 1. International Layer
- Submarine cable landings
- International peering points
- Global content delivery networks

### 2. National Core
- High-capacity optical backbone
- Core IP/MPLS routers
- Inter-capital city links

### 3. Metro Networks
- City-wide fiber rings
- Metro Ethernet services
- Mobile backhaul networks

### 4. Access Layer
- Local exchanges
- Cell tower sites
- Street cabinets
- Distribution networks

### 5. Customer Edge
- Business premises
- Residential connections
- IoT and M2M devices
