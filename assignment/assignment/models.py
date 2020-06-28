from django.db import models
from django.utils import timezone

from datetime import datetime

class YoutubeVideos(models.Model):

   video_id = models.CharField(db_column="VIDEO_ID", max_length = 100, primary_key=True)
   title = models.CharField(db_column="TITLE", max_length=1000, blank=False)
   description = models.TextField(db_column="DESCRIPTION", blank=False)
   published_at = models.DateTimeField(db_column="PUBLISHED_AT")
   default_url = models.CharField(db_column="DEFAULT_URL", max_length = 1000, blank=False)

   class Meta:
      db_table = u'YoutubeVideos'
