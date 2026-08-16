# Bounded Task Pipeline

A dependency-free Python example of a producer/worker/consumer pipeline. The
bounded queue applies back-pressure, workers perform CPU-style work, and the
consumer preserves input order even though tasks finish out of order.

```bash
python3 -m unittest discover -s tests -v
python3 pipeline.py --items 100 --workers 4 --queue-size 8
```

The project focuses on coordination semantics: shutdown uses sentinels,
exceptions are propagated to the caller, and output ordering is explicit.
