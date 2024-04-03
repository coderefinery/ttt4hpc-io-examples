# ttt4hpc-io-examples
Examples for disk input and output operations

1. Generate files

``` python
python generate_files.py
```

2. Create an archive

``` bash
zip -r data.zip data
```

3. Test reading individual files

``` python
time python aggregate_files.py
```

4. Test reading continuously from an archive

``` python
time python aggregate_zip.py
```
