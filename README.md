# Python Django 4 超入門
書籍に則って進めていきます,Python3.11での作成

## 書籍リンク
[Link](https://www.shuwasystem.co.jp/book/9784798062419.html)

## 学習記事のリンク
[Link](https://Iris-Fla.me/Study-Django)

## Venvに入り、Djangoのサーバーを起動する
0. Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force (※PowerShellでスクリプトが使えない場合)
1. python -m venv venv
2. venv\Scripts\Activate.ps1
3. python -m pip install -r requirements.txt
4. python ./django_app/manage.py runserver