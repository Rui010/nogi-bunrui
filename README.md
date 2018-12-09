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

## convert_img_csv.py
教師ラベルごとの画像データをnpy形式で訓練データとして保存　 

## cnn_face.py
CNNを実装し、顔画像からモデル学習する  

## model_test.py
学習モデルからテストデータを使って、顔認識とクラス分類を行う

## index.html
TensorFlow.jsを使ったフロント部分

## js/predict_face.js
TensorFlow.jsを使って、顔画像を抽出→クラス分類  
