from django.db import models

# Create your models here.

class Parent(models.Model):
    """
    ネストの親側のmodel
    """
    parent_column = models.CharField(
        max_length=10, verbose_name='親モデルのカラム')

    def __self__(self):
        return self.parent_column

class Child1(models.Model):
    """
    ネストする子供側のmodel1
    """
    # related_nameとserializerのfield名を合わせる
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='child1s')
    child1_column = models.CharField(
        max_length=10, verbose_name='子モデル１のカラム')

    def __self__(self):
        return self.Child1_column

class Child2(models.Model):
    """
    ネストする子供側のmodel2
    """
    # related_nameとserializerのfield名を合わせる
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='child2s')
    child2_column = models.CharField(
        max_length=10, verbose_name='子モデル２のカラム')

    def __self__(self):
        return self.Child2_column
