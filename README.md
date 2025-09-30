## About this project
- Djangoアプリの裏で`Celery`を用いて`Selenium`で情報を取得
- `Selenium`で取得した情報を`Sqlite`に保存
- Djangoアプリで取得した情報を一覧表示
- Seleniumで用いるURLは個人情報を隠すため適当に変更する予定
- ~~githubには`tasks.py`をgitの管理から外して`tasks_sample.py`を管理していく~~

## pip install
```bash
pip install django
pip install "celery[redis]" redis # Celery + Redisサポート, Python用のRedisクライアント
pip install django-celery-results # Celeryの実行結果をDBへ保存
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


## Celery
### ワーカー起動
```bash
celery -A django_selenium_lab worker -l info
```
- Celery Workerでシラバスの収集を行うことができた。Celery関係の設定をいじったら，celery worker を再起動させる必要がある

### workerとの接続確認
```python
# python manage.py shell
from scraper.tasks import add
r = add.delay(40, 2)
r.id, r.status           # （ここで 'PENDING' でもOK）
r.get(timeout=10)        # ← 42 が返れば接続も処理もOK
```

### Celery Woker と django-db の接続確認
```python
from scraper.tasks import store_result_test
t = 'test用textです。'
store_result_test(t)
c = CeleryTestModel.objects.all()
print(c) # 「test用textです。」が表示されたらOk
```
- ※ 管理画面でも確認可能

### django-celery-result
- Celery Woker の処理を Django のDBに保存するには必要らしい 
- `tasks.py`で`models.py`からモデルをインストールしてそのテーブルにtaskの処理を保存しているわけだからあまり必要性を感じない
- 必要なのか？
#### マイグレーション
```python
python manage.py migrate django_celery_results
```


### MEMO
Python Celeryで非同期タスクを実行するには、tasks.pyで定義したタスクをviews.pyなどから呼び出します<br>
以下例([Celery 5.5.3 documentation » Django » First steps with Django](https://docs.celeryq.dev/en/v5.5.3/django/first-steps-with-django.html))より
```python
# views.py
def create_user(request):
    # Note: simplified example, use a form to validate input
    user = User.objects.create(username=request.POST['username'])
    send_email.delay(user.pk) # この行でtasks.pyを呼び出しているってこと？
    return HttpResponse('User created')

# task.py
@shared_task
def send_email(user_pk):
    user = User.objects.get(pk=user_pk)
    # send email ...
```


## Installing requirements
```bash
$ pip install -r requirements.txt
```
## pip freeze
```bash
pip freeze > requirements.txt
```