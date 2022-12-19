# Data Export

The `pyroll-export` package provide several routines for exporting the data in PyRolL's object structure to well known data formats and objects.

```{eval-rst}
.. autofunction:: pyroll.export.to_dict
```

```{eval-rst}
.. autofunction:: pyroll.export.to_json
```

```{eval-rst}
.. autofunction:: pyroll.export.to_pandas
```

## Command Line Usage

If the `pyroll-cli` package is also installed, the `pyroll-export` package provides additional CLI commands.

### `export-json`

Exports the data to a JSON file via the {py:func}`pyroll.export.to_json` function.
The file can be specified by the `-f`/`--file` option, which defaults to `./export.json`.

### `export-csv`

Exports the data to a CSV file via the {py:meth}`pandas.DataFrame.to_csv` method, using {py:func}`pyroll.export.to_pandas`.
The file can be specified by the `-f`/`--file` option, which defaults to `./export.csv`.