from django.apps import AppConfig
from joblib import load
import os

class BaseAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Base_App"
    label = "base_app"

    def ready(self):
        # Define the path to the 'SaveModels' directory
        save_models_dir = os.path.join('D:\\My_Docs\\Sentiment_Analysis\\backend', 'SaveModels')

        # Construct the full paths to the model and vector files
        model_path = os.path.join(save_models_dir, 'model.joblib')
        vector_path = os.path.join(save_models_dir, 'vector.joblib')

        # Load the model and vectorizer
        if os.path.exists(model_path):
            self.model = load(model_path)
        else:
            raise FileNotFoundError(f"Model file not found at {model_path}")

        if os.path.exists(vector_path):
            self.vector = load(vector_path)
        else:
            raise FileNotFoundError(f"Vector file not found at {vector_path}")
