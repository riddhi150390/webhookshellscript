secret_token = 'password12345'  # Some secret string
projects_to_scripts = {'project_name_1': 'webhook_handler.sh'}
# PLEASE, NOTE, that values of `projects_to_scripts` are just `path.join`ed with `'scripts/'` and the resulting string
# is ran. Be careful, with giving access to this file
