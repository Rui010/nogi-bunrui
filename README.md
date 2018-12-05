# nogi-bunrui
乃木坂46・2期生のCNNによる顔認識アプリケーション

## image_getter.py
設定ファイルに従って、該当URL内のJPGファイルを一括ダウンロード

## url_list.json
image_getter.pyの設定ファイル  
URL: 画像ファイルが複数あるURL  
Path: 画像保存先  
selector: URL内のimgタグが複数あるCSSセレクター  

## config.ini
dirs: trim_face_image.pyで顔検出する画像の格納フォルダ

## trim_face_image.py
ディレクトリ内の画像ファイルから顔検出  
その配下の'face'ディレクトリに顔部分を抽出した画像を格納  