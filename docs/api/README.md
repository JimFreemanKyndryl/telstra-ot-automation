# Telstra Network API Documentation

## Overview
Telstra provides programmatic access to network services through RESTful APIs, enabling customers and internal systems to interact with the network infrastructure.

## API Categories

### 1. Service Management APIs
- Service ordering
- Service modification
- Service status query
- Bandwidth on demand

### 2. Network Information APIs
- Topology discovery
- Port availability
- Performance metrics
- Fault status

### 3. Device Management APIs
- Configuration management
- Software management
- Inventory queries
- Status monitoring

## Authentication
All APIs use OAuth 2.0 for authentication with JWT tokens.

```
Authorization: Bearer <token>
```

## Common Endpoints

### Service Provisioning
```
POST /api/v1/services
GET /api/v1/services/{serviceId}
PUT /api/v1/services/{serviceId}
DELETE /api/v1/services/{serviceId}
```

### Network Status
```
GET /api/v1/network/topology
GET /api/v1/network/devices
GET /api/v1/network/links
GET /api/v1/network/performance
```

### Device Operations
```
GET /api/v1/devices/{deviceId}
POST /api/v1/devices/{deviceId}/config
GET /api/v1/devices/{deviceId}/status
POST /api/v1/devices/{deviceId}/reboot
```

## Example Usage

### Create VPN Service
```bash
curl -X POST https://api.telstra.com/network/v1/services \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "serviceType": "L3VPN",
    "bandwidth": "1000",
    "endpoints": [
      {"location": "Sydney", "vlan": 100},
      {"location": "Melbourne", "vlan": 200}
    ]
  }'
```

### Query Device Status
```bash
curl -X GET https://api.telstra.com/network/v1/devices/router-syd-001/status \
  -H "Authorization: Bearer $TOKEN"
```

## Rate Limiting
- 1000 requests per hour per API key
- Burst allowance: 50 requests per minute

## Error Handling
Standard HTTP status codes with detailed error messages in JSON format.

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Device with ID router-xyz-001 not found",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```
