To build:
```
docker build -t graphite .
```

To stop/start:
```
docker stop graphite
docker rm graphite

docker run -d -p 80:80 -p 2003:2003 --name graphite graphite
```