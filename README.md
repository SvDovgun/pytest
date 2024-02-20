# pytest
project with pytest cases



# pytest commands:
# run tests
pytest -v 

# run tests with mark "smoke"
pytest -m smoke -v

# run tests with both marks "smoke" and "regression"
pytest -m "smoke and regression" -v

# run tests with marks "smoke" or "regression"
pytest -m "smoke or regression" -v

# run tests without mark "regression"
pytest -m "not regression" -v

# run total numbers of tests without details, shows only details for failed test
pytest -q

# run tests without details, shows only dot (.) for passed test and F for failed ones
pytest -qq

# run test with "qa" in the name
pytest -k "qa" -v

# run failed test first, then others
pytest --ff -v 

# stop run after 2 failed tests
pytest --maxfail=2 -v 

# show 2 slowest tests
pytest --durations=2 -v 

# show result in xml file 
pytest --junitxml=report.xml