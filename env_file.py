import os


def setup_env_from_file(file_name='.env', file_dir=None):
    if file_dir is None:
        file_dir = os.getcwd()

    file_path = os.path.join(file_dir, file_name)
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r') as f:
        for line in f.readlines():
            x = line.strip()
            if not x:
                continue

            i = x.find('=')
            if i > 0:
                param = x[:i].strip()
                val = x[i+1:].strip()
            else:
                param = x
                val = ''

            os.environ[param] = val
