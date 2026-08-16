# Bounded Task Pipeline

I implemented this dependency-free Python producer/worker/consumer pipeline to
practise coordination semantics. The bounded queue applies back-pressure,
workers process tasks concurrently, and I restore input order explicitly after
completion.

```bash
python3 -m unittest discover -s tests -v
python3 pipeline.py --items 100 --workers 4 --queue-size 8
```

I use sentinels for shutdown, propagate worker exceptions to the caller, and
test empty input, invalid configuration, and output ordering.
