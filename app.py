from configs.config import Config

def app():
    configuration = Config(environment="Prod")
    print(f"running in {configuration.get_environment()}")





