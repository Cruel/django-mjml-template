[![CI](https://github.com/Cruel/django-mjml-template/actions/workflows/ci.yml/badge.svg)](https://github.com/Cruel/django-mjml-template/actions/workflows/ci.yml) [![pypi](https://img.shields.io/pypi/v/django-mjml-template.svg)](https://pypi.org/project/django-mjml-template/)

# Django MJML Template

Use MJML in your Django templates. A very small and fast implementation.

## About

This
package leverages [MRML](https://github.com/jdrouet/mrml), a Rust implementation
of [MJML](https://github.com/mjmlio/mjml) using bindings provided by [mjml-python](https://github.com/mgd020/mjml-python).

If you want to run `MJML` itself as a separate HTTP server endpoint for conversion, use [django-mjml](https://github.com/liminspace/django-mjml) instead. It uses the same `mjml` template tag.

## What is MJML?

From the [documentation](https://documentation.mjml.io/) of the project:

> MJML is a markup language designed to reduce the pain of coding a responsive
> email. Its semantic syntax makes it easy and straightforward and its rich
> standard components library speeds up your development time and lightens your
> email codebase. MJML’s open-source engine generates high quality responsive
> HTML compliant with best practices.

## Requirements

- Python >= 3.7
- Django >= 1.11

## Installation

To install the package, run the following command:

```bash
pip install django-mjml-template
```

Then update your `settings.py`:

```python
INSTALLED_APPS = (
    ...
    'django_mjml_template',
)
```

## Usage

Load `mjml` in your django template and use `mjml` tag that will compile MJML to HTML:

```html
{% load mjml %}

{% mjml %}
  <mjml>
    <mj-body>
      <mj-section>
        <mj-column>
          <mj-text>Hello {{ user_name }}!</mj-text>
        </mj-column>
      </mj-section>
    </mj-body>
  </mjml>
{% endmjml %}
```

## Contributions

Contributions, bug reports, and suggestions are welcome! Feel free to open an
issue or submit a pull request.
