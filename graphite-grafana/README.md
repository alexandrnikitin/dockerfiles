To build:
```
docker build -t graphite-grafana .
```

To stop/start:
```
docker stop graphite-grafana
docker rm graphite-grafana

docker run -d -p 3000:3000 -p 8080:8080 -p 2003:2003 --name graphite-grafana graphite-grafana

sudo docker run -d \
  --name graphite-grafana \
  -v /path/to/host/grafana/db:/var/lib/grafana \
  -v /path/to/host/graphite/storage:/opt/graphite/storage \
  -p 3000:3000 \
  -p 8080:8080 \
  -p 2003:2003 \
  graphite-grafana
```