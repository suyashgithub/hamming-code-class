# hamming-code-class

# Installation Envirnment on Linux 
### python@3.8 <a href="https://docs.python-guide.org/starting/install3/linux/">Python help</a>
```shell
$sudo apt-get update
$sudo apt-get install python3.8
$python --version
```
### install pip and virtual environment with virtualenvwrapper

```shell
$pip --version
$pip install --user pipenv
$pip install virtualenv
$virtualenv --version
$pip install virtualenvwrapper
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh
$mkvirtualenv hc (hc is the environment name refer to hamming code)
$workon hc
```

### Create a project dir:

```shell
$mkdir hc
$pip freeze > requirements.txt
```

## Usage
```
data = '1011001' # input string
import HammingCode(data)
h = HammingCode(data)
hc = h.calc_parity_bits()
print("Hamming code generated would be:", hc)
print("The position of error  " + str(h.detect_error(hc)))
```