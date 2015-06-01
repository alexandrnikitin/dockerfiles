To build:
```
docker build -t graphite .
```

To stop/start:
```
docker stop graphite
docker rm graphite

docker run -d -p 8080:8080 -p 2003:2003 --name graphite graphite
```