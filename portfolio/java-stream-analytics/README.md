# Java Stream Analytics

I built this Java 17 example to practise stream-based analytics. It groups
measurements by device and computes a per-device average without manually
managing aggregation maps.

```bash
javac Measurements.java && java Measurements
```

I would extend it next with CSV input, validation for missing measurements,
and unit tests for the aggregation rules.
