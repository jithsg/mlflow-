from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("552580c50d064285b43d7f88f84fbbed", path="model")
print(f"Placed model in: {my_model}")
