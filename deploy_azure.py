import azureml.core
from azureml.core.webservice import LocalWebservice
from azureml.core import Workspace
from azureml.core import Environment
from azureml.core.model import InferenceConfig
from azureml.core.model import Model

print('SDK version:', azureml.core.VERSION)

ws = Workspace.from_config()
print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep='\n')

envname='AzureML-TensorFlow-2.3-CPU'
envname='AzureML-TensorFlow2.4-Cuda11-OpenMpi4.1.0-py36'


env = Environment(name=envname)
inf_config = InferenceConfig(environment=env, source_directory='./source_dir', entry_script='./score.py')

deploy_config = LocalWebservice.deploy_configuration(port=6788)
model=Model(ws,'stadnamn_model1')
service = Model.deploy(ws, "stadnamn", [model], inf_config, deploy_config)
service.wait_for_deployment(show_output=True)
print(service.get_logs())