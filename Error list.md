# Error list

## 1. 개요

애로사항을 겪었던 에러를 모았다.

## 2. Error

`django.db.utils.IntegrityError: FOREIGN KEY constraint failed`

- JSON을 loaddata할 때 JSON 안에 model에 없는 FOREIGN KEY가 있을 때 발생
  - FOREIGN KEY에 해당하는 model을 먼저 JSON을 import 하거나 JSON에 있는 model에는 없는 FOREIGN KEY 값을 제거해야함

`django.core.serializers.base.DeserializationError: Problem installing fixture 'C:\...': 'ManyToManyRel' object has no bute 'to_python'`

- ManyToManyField가 없는 model에 JSON을 loaddata할 때 발생
  - ManyToManyField가 선언된 model에 import 되어야 함

