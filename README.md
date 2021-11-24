# docker_whatsmyip

determines what ip you're requesting from and other user agent information.

```bash
 docker build -t docker_whatsmyip .
 export URL="http://google.com"
 docker run --name docker_whatsmyip -d -p --env URL=$URL 8000:8000 -i dockerip:latest 
 ``` 

```
{
  "access_routes": [
    "24.157.60.110"
  ],
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Early-Data": "1",
    "Forwarded": "for=\"24.157.60.110\";proto=https",
    "Host": "hello-mj3f2owm7a-uc.a.run.app",
    "Referer": "https://console.cloud.google.com/",
    "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Traceparent": "00-9712bc9a929aefdc34785a45075ee4e5-17aa6ae0bde8cb25-01",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
    "X-Client-Data": "CgSL6ZsV",
    "X-Cloud-Trace-Context": "9712bc9a929aefdc34785a45075ee4e5/1705292922404522789;o=1",
    "X-Forwarded-For": "24.157.60.110",
    "X-Forwarded-Proto": "https"
  }
}
```

