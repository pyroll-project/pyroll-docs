# Plugin Packages for PyRolL

Plugins are additional packages that provide model approaches to PyRolL by implementing hooks.
They have to be distinguished from extensions, which provide extended functionality (see [here](../extensions/index)).

In the following available plugin packages for PyRolL will be listed.
The list will be extended continuously.

```{note}
Read [here](../core/plugins) for details on hooks and plugins.
```

## Official Plugin Packages

{% for p in official | sort(attribute="name") %} 

### `{{- p.name -}}`

[[Docs]]({{p.docs}}) [[Source]]({{p.source}}) [[PyPI]]({{p.pypi}})

{{p.description}} 

{% endfor %}

## Unofficial Plugin Packages

```{note}
If you want your package listed here, please contact the maintainers.
```

{% for p in unofficial | sort(attribute="name") %} 

### `{{- p.name -}}`

[[Docs]]({{p.docs}}) [[Source]]({{p.source}}) [[PyPI]]({{p.pypi}})

{{p.description}}

{% endfor %}