import os


def delete_file_if_exists(file, session):
    if file:
        if os.path.exists(file.path):
            os.remove(file.path)
        session.delete(file)
        session.commit()
