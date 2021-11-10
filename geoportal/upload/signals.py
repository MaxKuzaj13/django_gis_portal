from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver
from .models import UploadFile
from geoportal.settings import MEDIA_URL
import fiona
import os
import uuid
import pandas as pd


@receiver(post_save, sender=UploadFile)
def post_save_update_fields(sender, instance, **kwargs):
    default_value = sender.objects.get(pk=instance.id)
    if default_value.file == '':
        set_value(default_value)


def set_value(default_value):
    # Create unique id
    default_value.uuid = str(uuid.uuid4())
    # Define layer name and file name
    layer, default_value.file = fill_layer_and_file(default_value.link_to_file)
    format_of_file, path = find_extension(str(default_value.link_to_file))
    default_value.format_of_file = format_of_file.replace('.', '').upper()
    save_value_field_and_layer(default_value, layer)
    check_if_contain_more_then_one_layer(default_value, layer)


def check_if_contain_more_then_one_layer(default_value, layer):
    if len(layer) > 1 and type(layer) == list:
        for i in range(1, len(layer)):
            default_value.pk = None
            default_value.layer = layer[i]
            default_value.save()


def save_value_field_and_layer(default_value, layer):
    if type(layer) == list:
        default_value.layer = layer[0]
    else:
        default_value.layer = layer
    default_value.save()


def fill_layer_and_file(path):
    layer = file = 'Error with loading file'
    extension, full_path = find_extension(MEDIA_URL + str(path))
    file, layer = check_depend_on_extension(extension, file, full_path, layer, path)
    return layer, file


def check_depend_on_extension(extension, file, full_path, layer, path):
    print(extension)
    if extension in ['.csv', '.txt']:
        file = path
        layer = str(path).replace(extension, '')
    elif extension in ['.gpkg', 'gdb']:
        layer = fiona.listlayers(full_path)
        file = path
    elif extension in ['.xls', '.xlsx']:
        file = path
        layer = pd.ExcelFile(path).sheet_names

    print(layer)
    return file, layer


def find_extension(file_path):
    path = os.getcwd() + file_path
    extension = os.path.splitext(file_path)[1]
    return extension, path


