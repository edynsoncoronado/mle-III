import dagshub  # Importa la librería dagshub para integrar el seguimiento de experimentos con DagsHub
import mlflow   # Importa la librería mlflow para el seguimiento de experimentos de machine learning
from functools import wraps
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def mlflow_setup(repo_name: str):
    """Configuración inicial de MLflow"""
    # Inicializa la integración con DagsHub, especificando el propietario y nombre del repositorio,
    # y habilita la integración con MLflow para registrar experimentos en DagsHub
    dagshub.init(
        repo_owner='edynsoncoronado',
        repo_name=f'{repo_name}',
        mlflow=True
    )

    # Establece la URI de seguimiento de MLflow para que apunte al servidor remoto de DagsHub,
    # permitiendo así registrar y visualizar experimentos de MLflow en esa plataforma.
    mlflow.set_tracking_uri(f"https://dagshub.com/edynsoncoronado/{repo_name}.mlflow")

    # Configura MLflow para registrar experimentos
    mlflow.set_experiment(f"{repo_name}")
    return True


def with_mlflow_autolog(func):
    """Decorador para habilitar y deshabilitar mlflow.autolog automáticamente."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        mlflow.autolog()
        try:
            result = func(*args, **kwargs)  # ejecuta la función decorada
            for model_name in result:
                logger.info(f"💯🚀🎯 Modelo registrado en MLflow: {model_name}")
        finally:
            mlflow.autolog(disable=True)   # siempre se deshabilita al final
        return result
    return wrapper