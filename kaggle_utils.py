import os
import kaggle
import zipfile


def download_and_extract_competition_files():
    download_path = os.path.abspath('data')
    print(f'downloading files to {download_path}')
    kaggle.api.competition_download_files(
        'AI4Code',
        path=download_path
    )
    zip_filepath = os.path.join(download_path, 'AI4Code.zip')
    print(f'extracting files from {zip_filepath} to {download_path}')
    with zipfile.ZipFile(zip_filepath) as zip_ref:
        zip_ref.extractall(download_path)
    os.remove(zip_filepath)
