# Producer Consumer

I implemented a bounded producer-consumer queue with explicit sentinel-based
shutdown. The bounded capacity lets me demonstrate back-pressure, while the
sentinels give workers a predictable termination protocol.

```bash
python3 producer_consumer.py
```

I would add cancellation and exception propagation in the next iteration.
