rm -rf dist
rm -rf build
rm -rf django_chained_autocomplete.egg-info
python3 setup.py sdist bdist_wheel
twine upload dist/*
