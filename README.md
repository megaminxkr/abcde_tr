# 26.3-JM — GitHub Pages / ローカル起動

[Joey-JM / 26.3-JM](https://github.com/joeymavv/26.3-JM) の配布済みHTMLを、GitHub Pagesまたは手元のPCで起動するための構成です。作者によれば26.2を基に一部の26.3機能を追加した独自版です。

## GitHub Pagesでブラウザーから起動

公開先（デプロイ成功後）: **https://megaminxkr.github.io/abcde_tr/**

Chromebookも、WebAssembly GCに対応する最新のChromeで上記URLを開けます。PythonやLinux環境は閲覧側には不要です。初回読み込みは約82 MBです。

### 所有者による初回設定

1. リポジトリの **Settings → Pages** を開きます。
2. **Build and deployment → Source → GitHub Actions** を選びます。
3. **Actions → Deploy game to GitHub Pages → Run workflow** で `main` を選んで実行します。
4. `build` と `deploy` の両方が成功したら、公開先URLをChromeで開きます。
5. Edit Profileで名前を設定してDoneを押し、Singleplayerへ進みます。

Pages設定にプランのアップグレード案内が出る場合、現在のプランではPrivateリポジトリからの公開が使えない可能性があります。必要なプランへ変更するか、リポジトリをPublicへ変更するかを所有者が選択してください。ワークフローはリポジトリの公開範囲を変更しません。

### 自動公開の仕組み

`main` へのpushまたは手動実行で、GitHub Actionsが作者の固定リリースを取得し、SHA-256を検証して `dist/index.html` を作ります。検証成功後に、そのHTMLと `.nojekyll` のみをPagesへ配信します。公開するHTMLは作者の配布物と同一で、Git管理には追加しません。取得・チェックサム検証に失敗した場合は公開処理へ進みません。

ローカルで同じ成果物を作る場合:

```sh
python3 build_pages.py
```

ブラウザーに保存したワールドはPCやブラウザープロファイルごとに異なり、GitHubへ同期されません。ローカル起動からPagesへ切り替える場合は、ゲーム内のExport/Importで移行してください。

## 最も簡単な起動方法（Python不要）

1. [作者のリリースページ](https://github.com/joeymavv/26.3-JM/releases/tag/v26.3-jm.1) から **26.3-fixed.html** をダウンロードします。
2. 最新のChromeでそのHTMLファイルを開きます。「プログラムから開く」でChromeを指定できます。
3. 初回のEdit Profile画面でUsernameを設定してDoneを押します。自動生成名の確認が出た場合は、変更するかContinue Anywayで続行します。
4. タイトル画面からシングルプレイを選びます。

## 固定のローカルURLで起動（推奨）

Python 3.11以降と最新のChromeを使用します。追加のPythonパッケージは不要です。

1. GitHubにログインし、このリポジトリの **Code → Download ZIP** を選びます。
2. ダウンロードしたZIPを展開します。ZIP内から直接起動せず、通常のフォルダーへ展開してください。
3. 展開した `play.py` があるフォルダーでターミナルを開き、以下のコマンドを実行します。

Windows:

```powershell
py -3 play.py
```

macOS / Linux:

```sh
python3 play.py
```

初回は約82 MBのHTMLを作者のGitHub Releaseから取得し、固定のSHA-256と照合します。2回目以降は保存済みファイルを照合して使用します。ブラウザーが自動で開かなければ、Chromeで `http://127.0.0.1:8765/` を開きます。終了時はターミナルで Ctrl+C を押します。

サーバーは127.0.0.1だけで待ち受けます。ポート開放や外部公開は不要です。このURLは起動したPCだけで利用できます。別のWebサービスが8765番ポートを使用している場合は、そのサービスを確認して終了してから起動してください。

取得だけ行う場合:

```sh
python3 play.py --download-only
```

ゲームは `.private/index.html` に保存され、Git管理対象から除外されます。ワールドの保存場所はこのフォルダーではなくブラウザー側です。

## 保存とバックアップ

通常ウィンドウを使い、毎回同じChromeプロファイル・URLで開いてください。file URLとlocalhost、localhostと127.0.0.1、異なるポートの間では保存データが共有されない場合があります。ゲーム内のExport機能でワールドを定期的に保存してください。ブラウザーのサイトデータ削除やシークレットモードの終了でワールドを失う可能性があります。

## 配布物の固定情報

- 配布元: https://github.com/joeymavv/26.3-JM
- Release: `v26.3-jm.1`
- Asset: `26.3-fixed.html`
- SHA-256: `1716c4673de4ab5b03ac9ac6ebe8d4db1358f6008825b84fcb4bb05c7228a610`
- 照合元: リリースの `26.3-fixed.sha256.txt`

チェックサムは同じ配布物であることの確認であり、コードの安全性や権利の保証ではありません。独自にHTMLやクレジットを変更しません。

## 公開範囲と権利確認

GitHub Pagesのサイトは一般公開する構成です。リポジトリをPrivateにしても、通常のPagesサイトはURLを知る第三者が閲覧できます。PrivateリポジトリからのPages公開は、GitHubの契約プランによって利用できない場合があります。

配布元はMinecraft由来のコンテンツ・アセットを含むと説明しています。第三者による再配布の許諾は未確認です。この構成やチェックサムの一致は、再配布の適法性を保証しません。配布物のクレジットは原本のまま維持します。

## クラウド環境での検証範囲

- リリース付属のチェックサムとダウンロード実体のSHA-256が一致。
- 再実行で既存HTMLを再利用し、再度整合性を検証。
- HTTP配信内容も同じSHA-256で、ソースコード・Git設定へのHTTPアクセスは404。
- Chromium 154で初回プロフィール画面からタイトルメニュー（26.3-JM表示）までの描画・操作を確認。
- ワールド生成・長時間プレイ・保存復元・音声・マルチプレイは未検証。

ブラウザーのログにはassets.epkの独自URLへのCORSエラー、追加エンティティのdata fixer未登録、メニュー音楽の警告が出ました。画面表示と操作は進みましたが、配布物全体が無不具合という確認ではありません。ゲームHTMLはチェックサムが一致する原本を使用しています。
