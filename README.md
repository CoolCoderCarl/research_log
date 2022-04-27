# webapp
Logs for logs

##
For launch pull image from here - https://hub.docker.com/repository/docker/h0d0user/flask_web_test  
`podman push docker.io/h0d0user/flask_web_test:3.0`  
`podman run -d -p 5000:5000 -v /var/log/:/webapp/logs_for_logs docker.io/h0d0user/flask_web_test:3.0`
