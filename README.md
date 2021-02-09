### Install

```bash
$ pip install PyGithub
```

### How to use
Use parameter passing through system envs.
```shell script
TOKEN="{your github token}" \
REPOS_FILE="repos.txt" \
USERS_FILE="users.txt" \
BEGIN_DATE="11/01/20" \ 
END_DATE="01/01/21" \
OUTPUT_FILE="issues.csv" \
python3 main.py
```
Format of date -- %m/%d/%y

### Example of output
[issues.csv](issues.csv)

### Sample files for input

- repos.txt
```text
tarantool/tarantool
tarantool/cartridge
```

- users.txt
```text
sharonovd
akudiyar
amitichev
filonenko-mikhail
```
