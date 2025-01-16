import logging
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile

import requests
from pytz import timezone
from tqdm import tqdm

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %p %Z",
)
logging.Formatter.converter = lambda *_: datetime.now(
    tz=timezone("America/Sao_Paulo")
).timetuple()
logger = logging.getLogger(__name__)


def download_and_extract_data(url: str, download_path: str, extract_path: str) -> None:
    """Faz o download de um arquivo ZIP do Google Drive e o extrai.

    Args:
        url (str): Link direto do arquivo no Google Drive.
        download_path (str): Caminho para salvar o arquivo baixado.
        extract_path (str): Caminho para extrair os arquivos do ZIP.

    """
    extract_path_dir = Path(extract_path)

    if extract_path_dir.exists() and any(extract_path_dir.iterdir()):
        logger.info("O dataset já foi baixado e está em %s.", extract_path)
        return

    logger.info("Baixando o arquivo ZIP...")
    response = requests.get(url, stream=True, timeout=10)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))
    with (
        Path(download_path).open("wb") as file,
        tqdm(
            desc="Progresso do download",
            total=total_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar,
    ):
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))
    logger.info("Arquivo salvo em: %s", download_path)

    logger.info("Extraindo os dados para %s", extract_path)
    extract_path_dir.mkdir(parents=True, exist_ok=True)
    with ZipFile(download_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)
    logger.info("Dados extraídos para a pasta: %s", extract_path)

    Path(download_path).unlink()
    logger.info("Arquivo ZIP removido.")


url = "https://drive.usercontent.google.com/download?id=13rvnyK5PJADJQgYe-VbdXb7PpLPj7lPr&export=download&confirm=t"
download_path = "challenge-webmedia-e-globo-2023.zip"
extract_path = "data/raw"

download_and_extract_data(url, download_path, extract_path)
