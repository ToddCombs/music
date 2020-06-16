
# index的models.py 用于定义4张数据表
from django.db import models

# Create your models here.
# 歌曲分类表label
class Label(models.Model):
    label_id = models.AutoField('序号', primary_key=True)
    label_name = models.CharField('分类标签', max_length=10)
    def __str__(self):
        return self.label_name
    class Meta:
        '''设置Admin界面的显示内容'''
        verbose_name = '歌曲分类'
        verbose_name_plural = '歌曲分类'

# 歌曲信息表song
class Song(models.Model):
    song_id = models.AutoField('序号', primary_key=True)
    song_name = models.CharField('歌名', max_length=50)
    song_singer = models.CharField('歌手', max_length=50)
    song_time = models.CharField('时长', max_length=10)
    song_album = models.CharField('专辑', max_length=50)
    song_languages = models.CharField('语种', max_length=20)
    song_type = models.CharField('类型', max_length=20)
    song_release = models.CharField('发布时间', max_length=20)
    song_img = models.CharField('歌曲图片', max_length=20)
    song_lyrics = models.CharField('歌词', max_length=50, default='暂无歌词')