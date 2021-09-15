from django.db import models

TYPE_GEOMETRY = (
    ('line', 'Line feature'),
    ('point', 'Point feature'),
    ('polygon', 'Polygon feature')
)


class UploadFile(models.Model):
    user_name = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    layer = models.CharField(max_length=255)
    type = models.CharField(choices=TYPE_GEOMETRY, default='None', max_length=50)
    link_to_file = models.FileField(upload_to='.')


class Report(models.Model):
    # delete rap if delete org file (models.Cascade)
    upload_file = models.ForeignKey(UploadFile, on_delete=models.CASCADE)
    upload_link = models.FileField(upload_to='.')
