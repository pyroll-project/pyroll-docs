# Extension Packages for PyRolL

Extensions are additional packages that extend the functionality of PyRolL, f.e. by adding user interfaces.
They have to be distinguished from plugins, which provide modelling approaches by implementing hooks (see [here](../plugins/index)).

In the following available extension packages for PyRolL will be listed.
The list will be extended continuously.

## Official Extension Packages

{% for p in official | sort(attribute="name")%} 

### `{{- p.name -}}`

[[Docs]]({{p.docs}}) [[Source]]({{p.source}}) [[PyPI]]({{p.pypi}})

{{p.description}}

{% endfor %}

## Unofficial Extension Packages

```{note}
If you want your package listed here, please contact the maintainers.
```

{% for p in unofficial | sort(attribute="name") %} 

### `{{- p.name -}}`

[[Docs]]({{p.docs}}) [[Source]]({{p.source}}) [[PyPI]]({{p.pypi}})

{{p.description}}

{% endfor %}