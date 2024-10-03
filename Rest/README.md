# DJANGO REST Framework

- API Server wiht JSON format

```
# install package
pip install djangorestframework

DJANGO_APPS = [
    ...,
    'rest_framework',  # resigst rest app
]
```

### Request wiht '@api_view'
```
@api_view(['GET'])
def hello_api(request: Request):
    return Response({'hello': 'world'})
```
- view 정의 : function, class 두 방법 가능
- serializer를 이용해 직렬화/역직렬화 