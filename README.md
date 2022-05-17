# tch_search

## Developer Setup
1. make a virtualenv
   
   ```sh
   virtualenv venv
   ```

2. Activate virtual env
    ```sh
    . venv/bin/activate
    ```

3. Clone the repo
```
git clone https://github.com/saivarala/tch_search.git 
```

4. change directory 
``` 
cd tch_search
```
5. install requirements
```
pip install -r requirements.txt
```
6. Usage on command line
```
python search.py <<filter>>
```

### Sample Usage

1. To find the records with city=New York
```
python search.py "city=New York"
```
2. To find the records with zip code 10018

```
python search.py "zip code = 10018"
```
3. To find the records with state as NY
```
python search.py "state=NY"
```
4. To find the records with transaction type as ATM
```
python search.py "type=ATM"
```
5. To find city and state

```
python search.py "city=New York & state = NY"
```

#### For Help
```
python search.py --help
```


## TODO add the setup.py for the installing the command on mac or windows. Instead of 'python search.py <<filter>>' user can use 'search <<filter>>'
