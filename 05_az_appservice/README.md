# auzre appservice へデプロイ

Flaskアプリとしてデプロイする

## Azure App Service
```
# プランを作成 (--is-linux)
az appservice plan create --name my-example-appsrv-plan --resource-group $RG_NAME --is-linux

# App Serviceへデプロイ
az webapp up -n my-example-flask-app -g $RG_NAME -l $LOCATION -p my-example-appsrv-plan --runtime 'PYTHON:3.9'
```

localで確認
```
FLASK_APP=app.py
flask run --host=0.0.0.0
curl localhost:5000/hello
```
※--host=0.0.0.0 外部からの接続を可能にする

Azureで確認
```
curl https://my-example-flask-app.azurewebsites.net/hello
```

appserviceでサポートしているversion確認
```
az webapp list-runtimes --os linux | grep PYTHON
  "PYTHON:3.9",
  "PYTHON:3.8",
  "PYTHON:3.7",
```

## Azure App Service (カスタムコンテナ)

Buildしてローカルで確認
```
docker build -t tokym/my-flask-app:v1 .
docker run --rm -d -p 8080:5000 tokym/my-flask-app:v1 
curl localhost:8080
```

RegistoryへPush　※ACR or DockerHub
ACR
```
```
DockerHub
```
```



