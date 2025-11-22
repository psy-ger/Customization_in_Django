default_app_config = 'core.apps.CoreConfig'

# Signals are imported in CoreConfig.ready() to avoid importing models
# before the app registry is fully populated.
