To build:
```
docker build -t graphite .
```

To stop/start:
```
docker stop graphite
docker rm graphite

sudo docker run -d \
  --name graphite \
  -v /path/to/host/graphite/storage:/opt/graphite/storage \
  -p 8080:8080 \
  -p 2003:2003 \
  graphite
```