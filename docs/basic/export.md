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
So, execute f.e.

    pyroll input-py solve export-json -f my-results.json

Which leads to a file similar to this

```json
{
    "label": "",
    "units": [
        {
            "label": "Oval I",
            "roll": {
                "nominal_radius": 0.16,
                "rotational_frequency": 1,
                "groove": {
                    "r1": 0.006,
                    "r2": 0.04,
                    "alpha1": 0.5986680528355425,
                    "alpha2": 0.5986680528355425,
                    "depth": 0.008,
                    "usable_width": 0.04814264518817268,
                    "types": "oval, circular_oval"
                },
                "roll_torque": 3492.976239911318,
                "max_radius": 0.16,
                "contour_line": {
                    "width": 0.05703051814598918,
                    "depth": 0.008,
                    "length": 0.06025975303951582
                },
                "min_radius": 0.152,
                "contact_length": 0.04228474902373194,
                "contact_area": 0.0016521210699162083
            },
            "gap": 0.002,
            "in_profile": {
                "cross_section": {
                    "width": 0.03,
                    "height": 0.03,
                    "perimeter": 0.09420993470864258
                },
                "types": "round",
                "temperature": 1473.15,
                "strain": 0,
                "material": "C45, steel",
                "flow_stress": 100000000.0,
                "width": 0.03,
                "height": 0.03,
                "length": 0
            },
            "out_profile": {
                "types": "oval, circular_oval",
                "temperature": 1473.15,
                "strain": 0.12967679498342286,
                "material": "C45, steel",
                "flow_stress": 100000000.0,
                "cross_section": {
                    "width": 0.04814264518817268,
                    "height": 0.018000000000000002,
                    "perimeter": 0.10779462546810438
                },
                "length": 0.0,
                "width": 0.04814264518817268
            },
            "roll_force": 165212.10699162082,
            "mean_flow_stress": 100000000.0,
            "height": 0.018000000000000002,
            "elongation": 1.1384603677535539,
            "log_elongation": 0.12967679498342286
        },
        {
            "label": "I => II",
            "duration": 1,
            "in_profile": {
                "types": "oval, circular_oval",
                "temperature": 1473.15,
                "strain": 0.12967679498342286,
                "material": "C45, steel",
                "flow_stress": 100000000.0,
                "cross_section": {
                    "width": 0.04814264518817268,
                    "height": 0.018000000000000002,
                    "perimeter": 0.10779462546810438
                },
                "length": 0.0
            },
            "out_profile": {
                "types": "oval, circular_oval",
                "temperature": 1473.15,
                "strain": 0,
                "material": "C45, steel",
                "flow_stress": 100000000.0,
                "cross_section": {
                    "width": 0.04814264518817268,
                    "height": 0.018000000000000002,
                    "perimeter": 0.10779462546810438
                },
                "length": 0.0
            }
        },
        {
            "label": "Round II",
            "roll": {
                "nominal_radius": 0.16,
                "rotational_frequency": 1,
                "groove": {
                    "r1": 0.001,
                    "r2": 0.0125,
                    "alpha1": 1.422100832527334,
                    "alpha2": 1.422100832527334,
                    "depth": 0.0115,
                    "usable_width": 0.02497934630720916,
                    "types": "round"
                },
                "roll_torque": 3548.7909827990825,
                "max_radius": 0.16,
                "contour_line": {
                    "width": 0.029372265830201118,
                    "depth": 0.0115,
                    "length": 0.04104864528285382
                },
                "min_radius": 0.1485,
                "contact_length": 0.0574698817109208,
                "contact_area": 0.0012350089741440056
            },
            "gap": 0.002,
            "in_profile": {
                "types": "oval, circular_oval",
                "temperature": 1473.15,
                "strain": 0,
                "material": "C45, steel",
                "flow_stress": 100000000.0,
                "cross_section": {
                    "width": 0.018000000000000002,
                    "height": 0.04814264518817268,
                    "perimeter": 0.10779462546810438
                },
                "length": 0.0,
                "width": 0.018000000000000002,
                "height": 0.04814264518817268
            },
            "out_profile": {
                "types": "round",
                "temperature": 1473.15,
                "strain": 0.23476395237851164,
                "material": "C45, steel",
                "flow_stress": 100000000.0,
                "length": 0.0,
                "cross_section": {
                    "width": 0.02497934630720916,
                    "height": 0.025,
                    "perimeter": 0.07857532958642108
                },
                "width": 0.02497934630720916
            },
            "roll_force": 123500.89741440056,
            "mean_flow_stress": 100000000.0,
            "height": 0.025,
            "elongation": 1.2646102252632567,
            "log_elongation": 0.23476395237851164
        }
    ],
    "in_profile": {
        "cross_section": {
            "width": 0.03,
            "height": 0.03,
            "perimeter": 0.09420993470864258
        },
        "types": "round",
        "temperature": 1473.15,
        "strain": 0,
        "material": "C45, steel",
        "flow_stress": 100000000.0
    },
    "out_profile": {
        "types": "round",
        "temperature": 1473.15,
        "strain": 0.23476395237851164,
        "material": "C45, steel",
        "flow_stress": 100000000.0,
        "length": 0.0,
        "cross_section": {
            "width": 0.02497934630720916,
            "height": 0.025,
            "perimeter": 0.07857532958642108
        }
    }
}
```

### `export-csv`

Exports the data to a CSV file via the {py:meth}`pandas.DataFrame.to_csv` method, using {py:func}`pyroll.export.to_pandas`.
The file can be specified by the `-f`/`--file` option, which defaults to `./export.csv`.
So, execute f.e.

    pyroll input-py solve export-csv -f my-results.csv

Which leads to a file similar to this

```csv
,duration,elongation,gap,height,in_profile.cross_section.height,in_profile.cross_section.perimeter,in_profile.cross_section.width,in_profile.flow_stress,in_profile.height,in_profile.length,in_profile.material,in_profile.strain,in_profile.temperature,in_profile.types,in_profile.width,label,log_elongation,mean_flow_stress,out_profile.cross_section.height,out_profile.cross_section.perimeter,out_profile.cross_section.width,out_profile.flow_stress,out_profile.length,out_profile.material,out_profile.strain,out_profile.temperature,out_profile.types,out_profile.width,roll.contact_area,roll.contact_length,roll.contour_line.depth,roll.contour_line.length,roll.contour_line.width,roll.groove.alpha1,roll.groove.alpha2,roll.groove.depth,roll.groove.r1,roll.groove.r2,roll.groove.types,roll.groove.usable_width,roll.max_radius,roll.min_radius,roll.nominal_radius,roll.roll_torque,roll.rotational_frequency,roll_force
0,,1.1384603677535539,0.002,0.018000000000000002,0.03,0.09420993470864258,0.03,100000000,0.03,0,"C45, steel",0.0,1473.15,round,0.03,Oval I,0.12967679498342286,100000000,0.018000000000000002,0.10779462546810438,0.04814264518817268,100000000,0,"C45, steel",0.12967679498342286,1473.15,"oval, circular_oval",0.04814264518817268,0.0016521210699162083,0.04228474902373194,0.008,0.06025975303951582,0.05703051814598918,0.5986680528355425,0.5986680528355425,0.008,0.006,0.04,"oval, circular_oval",0.04814264518817268,0.16,0.152,0.16,3492.976239911318,1,165212.10699162082
1,1,,,,0.018000000000000002,0.10779462546810438,0.04814264518817268,100000000,,0,"C45, steel",0.12967679498342286,1473.15,"oval, circular_oval",,I => II,,,0.018000000000000002,0.10779462546810438,0.04814264518817268,100000000,0,"C45, steel",0.0,1473.15,"oval, circular_oval",,,,,,,,,,,,,,,,,,,
2,,1.2646102252632567,0.002,0.025,0.04814264518817268,0.10779462546810438,0.018000000000000002,100000000,0.04814264518817268,0,"C45, steel",0.0,1473.15,"oval, circular_oval",0.018000000000000002,Round II,0.23476395237851164,100000000,0.025,0.07857532958642108,0.02497934630720916,100000000,0,"C45, steel",0.23476395237851164,1473.15,round,0.02497934630720916,0.0012350089741440056,0.0574698817109208,0.0115,0.04104864528285382,0.029372265830201118,1.422100832527334,1.422100832527334,0.0115,0.001,0.0125,round,0.02497934630720916,0.16,0.1485,0.16,3548.7909827990825,1,123500.89741440056
```