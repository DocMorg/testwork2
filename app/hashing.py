from app import app,db
from app.models import Data
import os
import sys
import hashlib
import requests
import shutil


def md5(uuid, url):
    fname = 'file_' + uuid
    filepath = 'app/tmp/' + fname
    try:
        file_download = requests.post(url, stream=True, timeout=60 * 2)
        with open(filepath,"wb") as f1:
            file_download.raw.decode_content = True
            shutil.copyfileobj(file_download.raw, f1)
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        if os.path.isfile(filepath):
            os.remove(filepath)
        md5_hash = hash_md5.hexdigest()
        state = "finished"
    except Exception:
        state = "failed"
    upd = Data.query.filter_by(id = uuid).update({'state': state, 'md5_hash': md5_hash})
    db.session.commit()
    


if __name__ == '__main__':
    uuid, url = sys.argv[1:]
    md5(uuid, url)