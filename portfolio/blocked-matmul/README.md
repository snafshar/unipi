# Blocked Matrix Multiply

I implemented tiled matrix multiplication in dependency-free Python. I made
the tile size configurable so I can explore how loop blocking affects cache
behaviour and compare it with a straightforward implementation.

```bash
python3 matmul.py --size 32 --tile 8
```

My next step would be to add a NumPy baseline and collect measurements for
different matrix sizes and tile sizes.
