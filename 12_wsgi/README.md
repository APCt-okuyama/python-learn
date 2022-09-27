# wsgi (web server gateway interface)

PythonのWEBアプリ(Flask, djangoなど)では、本番環境では web server と web アプリ を別で用意して利用するのが一般的。
※Flaskなどに含まれている開発用のサーバーは利用しない

## Azureでの利用
Azure App Service や　Azure Functions でFlaskを利用する場合は標準で対応される。

※ App Service では、既定で Gunicorn Web サーバーを使用します。

自分自身でコンテナ化する場合は注意が必要