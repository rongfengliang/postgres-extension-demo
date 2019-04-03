# create my demo postgresql extension

> this extension expose one fucntion just like oracle nvl

## how to use

* install

> use docker for build please note the location for extension

```code
docker-compose build
```

* useage

```code
CREATE EXTENSION nvlfunc;
SELECT NVL(NULL::SMALLINT, 121::SMALLINT);
```