## About this project
- Djangoアプリの裏で`Celery`を用いて`Selenium`で情報を取得
- `Selenium`で取得した情報を`Sqlite`に保存
- Djangoアプリで取得した情報を一覧表示

## pip install
```bash
pip install django
pip install "celery[redis]" redis # Celery + Redisサポート, Python用のRedisクライアント
pip install selenium 
pip install webdriver-manager # ChromeDriverを自動ダウンロードツール
```

## Redis
- Docker で起動する
```bash
docker run -d --name redis -p 6379:6379 redis:7
```
- Redis 動作確認
```bash
python manage.py shell
import redis
r = redis.Redis(host="localhost", port=6379, db=0)
print("PING:", r.ping())
exit()
```

## pip freeze
```bash
pip freeze > requirements.txt
```
