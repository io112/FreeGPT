from g4f.models import ModelUtils

working_providers = ModelUtils.convert

print("\nWorking providers by model:")
for model, provider in working_providers.items():
    print(f"{model}: {provider.name}")
