from pathlib import Path
import subprocess
import pandas as pd


def download_kaggle_dataset(
    dataset_slug: str = "rabieelkharoua/alzheimers-disease-dataset",
    destination: str = "data/raw/alzheimers_disease_data.csv",
) -> Path:
    '''Descarga un dataset de Kaggle usando la API oficial.

    Requiere autenticacion previa mediante la variable de entorno
    KAGGLE_API_TOKEN o el archivo ~/.kaggle/kaggle.json.
    Documentacion: https://www.kaggle.com/docs/api
    '''
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        subprocess.run(
            [
                "kaggle", "datasets", "download",
                "-d", dataset_slug,
                "-p", str(path.parent),
                "--unzip",
            ],
            check=True,
        )

    frame = pd.read_csv(path)
    if frame.empty:
        raise ValueError("El dataset descargado esta vacio")
    return path
