# Install pyenv and python 3.9.1 on ubuntu (qa.guru Jenkins)
В домашних заданиях данный скрипт не пригодится.
```bash
apt update -y && apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

git clone https://github.com/pyenv/pyenv.git /home/jenkins/.pyenv

echo 'export PYENV_ROOT="/home/jenkins/.pyenv"' >> /home/jenkins/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> /home/jenkins/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> /home/jenkins/.bashrc


exec "$SHELL"

pyenv install --list

pyenv install 3.9.1

pyenv versions

pyenv global 3.9.1

python --version

```
