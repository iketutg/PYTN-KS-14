Install Python Multi Version 

1. Download dan Install pyenv 
2. Install Python sesuai dengan yang tuju :
 pyenv install 3.10.8
python-build: definition not found: 3.10.8

See all available versions with `pyenv install --list'.

If the version you need is missing, try upgrading pyenv:
cd /Users/iketutg/.pyenv/plugins/python-build/../.. && git pull && cd -

# List Python yang di laptop kita 
pyenv verions 

# Set python version di laptop
pyenv global 3.10.8

#untuk mengecek 
pyenv version
atau 
python -V

Membuat Environment Python 

python3 -m venv heloflask    

Activate 

# untuk di linux atau mac 
source heloflask/bin/activate   

windows 
./heloflask/bin/activate.bat 

Install Flask 
pip install flask 




