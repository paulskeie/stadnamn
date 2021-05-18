from azureml.core.model import Model
from azureml.core import Workspace

ws = Workspace.from_config()

# Register model
model = Model.register(ws, model_name="stadnamn_model1", model_path="./model2.tf")
