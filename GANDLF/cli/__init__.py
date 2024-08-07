from .patch_extraction import patch_extraction
from .main_run import main_run
from .preprocess_and_save import preprocess_and_save
from .config_generator import config_generator
from .deploy import deploy_targets, mlcube_types, run_deployment
from .recover_config import recover_config
from .post_training_model_optimization import post_training_model_optimization
from .generate_metrics import generate_metrics_dict
from .data_split_saver import split_data_and_save_csvs
from .generate_Competition_metrics import generate_metrics_dict_competition

__all__ = [
    "patch_extraction",
    "main_run",
    "preprocess_and_save",
    "config_generator",
    "deploy_targets",
    "mlcube_types",
    "run_deployment",
    "recover_config",
    "post_training_model_optimization",
    "generate_metrics_dict",
    "split_data_and_save_csvs",
    "generate_metrics_dict_competition",
]

from datetime import date

copyrightMessage = (
    "Contact: gandlf@mlcommons.org\n\n"
    + "This program is NOT FDA/CE approved and NOT intended for clinical use.\nCopyright (c) "
    + str(date.today().year)
    + " MLCommons. All rights reserved.\n\nCitation: https://doi.org/10.1038/s44172-023-00066-3"
)
