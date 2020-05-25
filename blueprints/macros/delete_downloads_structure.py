import os


def delete_downloads_structure(model):
    path = f'static/wp-content/{ model.__class__.__name__.lower() }_{ model.id }'
    if os.path.exists(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
