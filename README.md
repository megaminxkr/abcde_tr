# 26.3-JM

[Joey-JM版](https://github.com/joeymavv/26.3-JM)をブラウザーで遊ぶためのサイトです。26.2を基に、一部の26.3機能を追加した独自版です。

## 起動

"https://megaminxkr.github.io/abcde_tr"

最新のChromeで開いてください。Chromebookでも、Linux・Python・HTMLの手動ダウンロードは不要です。初回は約82 MBを読み込みます。

1. **Edit Profile**で名前を設定し、**Done**を押します。
2. 確認が表示されたら **Continue Anyway** を選びます。
3. **Singleplayer**からゲームを始めます。

古いページが表示される場合は、**Ctrl＋Shift＋R**で再読み込みしてください。

## ワールドの保存

ワールドはブラウザーに保存され、GitHubには同期されません。同じブラウザープロファイル・URLを使い、ゲーム内の**Export**で定期的にバックアップしてください。

## 構成

- `index.html`：ゲーム本体。配布元の`26.3-fixed.html`と同一。
- `.nojekyll`：GitHub Pagesで静的ファイルを配信する設定。
- `build_pages.py`：HTMLの整合性を検証し、`dist/`へコピーする補助スクリプト。
- `play.py`：PCでローカル起動する補助スクリプト（Python 3.11以降）。

Pagesは **main → / (root)** から公開します。閲覧者は補助スクリプトを実行する必要はありません。

## 配布元

[26.3-JM / v26.3-jm.1](https://github.com/joeymavv/26.3-JM/releases/tag/v26.3-jm.1) の `26.3-fixed.html` を使用しています。ゲーム内のクレジットは原本のままです。
