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
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file


class Report(models.Model):
    # delete rap if delete org file (models.Cascade)
    upload_file = models.ForeignKey(UploadFile, on_delete=models.CASCADE)
    upload_link = models.FileField(upload_to='.', blank=True, null=True)
    calculate_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"ID: {self.id}"
