def get_upload_path(instance, path):
    app_name = instance._meta.app_label
    path = "images/" + app_name + path
    konum = path.split("-")[0]
    return path