# Device-Specific API Examples

## Cisco Router APIs (IOS-XR)

### NETCONF Example
```xml
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get-config>
    <source>
      <running/>
    </source>
    <filter>
      <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"/>
    </filter>
  </get-config>
</rpc>
```

### RESTCONF Example
```bash
curl -X GET https://router1.telstra.com/restconf/data/Cisco-IOS-XR-ifmgr-cfg:interfaces \
  -H "Accept: application/yang-data+json" \
  -u admin:password
```

## Ericsson RAN APIs

### Configuration API
```bash
POST /ericsson/ran/v1/nodes/{nodeId}/configuration
{
  "cellConfiguration": {
    "cellId": "12345",
    "frequencyBand": "n78",
    "bandwidth": "100MHz",
    "transmitPower": "40"
  }
}
```

### Performance API
```bash
GET /ericsson/ran/v1/nodes/{nodeId}/performance?metrics=throughput,latency&interval=5m
```

## Ciena Optical APIs

### Wavelength Provisioning
```bash
POST /ciena/waveserver/v1/wavelengths
{
  "wavelength": {
    "frequency": "193.1THz",
    "modulation": "16QAM",
    "fec": "enhanced",
    "power": "-10dBm"
  }
}
```

## CPE Management (TR-069)

### Get Parameter Values
```xml
<cwmp:GetParameterValues>
  <ParameterNames arrayType="xsd:string[1]">
    <string>Device.WiFi.AccessPoint.1.</string>
  </ParameterNames>
</cwmp:GetParameterValues>
```

### Set Parameter Values
```xml
<cwmp:SetParameterValues>
  <ParameterList arrayType="cwmp:ParameterValueStruct[1]">
    <ParameterValueStruct>
      <Name>Device.WiFi.AccessPoint.1.Enable</Name>
      <Value xsi:type="xsd:boolean">true</Value>
    </ParameterValueStruct>
  </ParameterList>
</cwmp:SetParameterValues>
```
