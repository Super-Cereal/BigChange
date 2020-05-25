import os
from werkzeug.utils import secure_filename

from data.model_files import File

from blueprints.macros.convert_ru_to_eng import convert_ru_to_eng


def save_file(model, file):
    path = f'static/wp-content/{ model.__class__.__name__.lower() }_{ model.id }'
    if not os.path.exists(path):
        os.mkdir(path)
    filename = secure_filename(convert_ru_to_eng(file.data.filename))
    file.data.save(os.path.join(path, filename))
    file = File(path=os.path.join(path, filename))
    return file
