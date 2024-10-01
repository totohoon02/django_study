# Photo App

### Model

```
class Photo(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    description = models.TextField()
    price = models.IntegerField()

```

- admin.py에 등록한다.

### MVT

- Model
  - 데이터베이스 스키마 정의
  - ORM 모델 사용
- View
  - Template에 정보 제공
  - 단순 렌더
  - API로도 사용
- Template
  - 데이터를 받아서 화면 그리기
- CRUD
- Form
