# Python Django 4 超入門
書籍に則って進めていきます

## 書籍リンク
[Link](https://www.shuwasystem.co.jp/book/9784798062419.html)

## Venvに入り、Djangoのサーバーを起動する
0. Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force (※PowerShellでスクリプトが使えない場合)
1. python -m venv venv
2. venv\Scripts\Activate.ps1
3. python -m pip install -r requirements.txt
4. python ./django_app/manage.py runserver

## 一章まとめ
- Djangoのインストール
- ローカルサーバーの立て方

## 二章まとめ
- templatesの利用
> 1.settings.pyの編集
> 2.templatesフォルダの作成,フォルダの中にHelloフォルダを作成
> 3.index.htmlの作成,urlpatternsを修正する
- staticの利用
> staticでCSSやIMGを保管する