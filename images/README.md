gbm-perf
-------

Build and run docker image. Requires a decent amount of RAM (8GB+).
```
cd images/gbm-perf/cpu
docker build --build-arg CACHE_DATE=$(date +%Y-%m-%d) -t gbmperf_cpu .
docker run --rm gbmperf_cpu
```

Build AMI:
```
```
