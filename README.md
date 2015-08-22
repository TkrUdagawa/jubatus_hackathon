## Yomiuriデータをレコメンダにつっこんでモデルをダンプするサンプル

###なにするもの？
- 読売新聞の記事データを読み込んでDatum化してJubarecommenderに学習させる
- 学習させたモデルファイルをSaveする
- Saveしたモデルファイルをダンプして特徴ごとの重みをみる

###必要なもの
- Jubatus
   - --enable-mecabオプションが必要
- python 2.7
- mecab

###とりあえず動かす

```
jubarecommender -f recommender.json &
python train_and_save.py articles.json
jubadump -i /tmp/192.168.80.139_9199_recommender_jubatus_hackathon.jubatus > dumped_model.dat
python print_model.py dumped_model.dat
```

###注意
- python2.7でしか動かしていない

