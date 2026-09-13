# Remote Patient Monitoring

## Interview Answer: How would you design a data pipeline for remote patient monitoring?

I would design the pipeline around reliability, security, data integrity, and
clinical usefulness. The important thing is not just moving data from a device
to the cloud, but making sure the data is trustworthy, protected, and useful
for patient care.

High-level design:

1. Sensors collect patient data on the device.
2. Firmware validates the data, timestamps it, and checks for invalid or
missing samples.
3. The device buffers data locally if connectivity is unavailable.
4. Data is encrypted and sent over a secure communication channel.
5. A cloud ingestion service authenticates the device and receives the data.
6. Processing services check for alerts, trends, and data quality issues.
7. Data is stored securely with audit trails.
8. Clinician or patient dashboards display summaries, trends, alerts, and
device status.

Key considerations:

- Safety: define what happens when readings are missing, delayed, duplicated,
or outside valid range.
- Security: encryption in transit and at rest, authentication, access control,
and audit logging.
- Reliability: retries, local buffering, duplicate detection, and idempotent
uploads.
- Traceability: include timestamps, device ID, firmware version, hardware
revision, and calibration/status metadata.
- Scalability: support many devices sending data at different intervals.
- Clinical value: alerts should be actionable and avoid unnecessary noise.
- Maintainability: monitor the pipeline and log failures clearly.

Possible architecture:

```text
Sensors
  -> Embedded firmware validation
  -> Local secure buffer
  -> Secure upload
  -> Cloud ingestion API
  -> Stream processing and alert rules
  -> Secure database
  -> Clinician/patient dashboard
```

Medical-device angle:

For remote patient monitoring, I would be especially careful about false
confidence. If data is late or missing, the system should show that clearly
rather than presenting stale values as current. The pipeline should also make
it possible to audit what happened, when it happened, which device sent the
data, and which software version was running.

## Short Version

I would collect and validate data on the device, timestamp it, buffer it during
connectivity loss, transmit it securely, process it in the cloud for trends and
alerts, store it with audit trails, and present it through a dashboard. The key
engineering concerns are safety, security, reliability, data integrity,
traceability, and clinically useful alerts.
