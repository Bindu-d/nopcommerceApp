pytest -v -s -m "sanity" --html=./Reports/report.html testCases/
pytest -v -s -m "sanity" --html=./Reports/report.html testCases/ --browser firefox

rem pytest -v -s -m "sanity or regression" --html=Reports\report.html testCases\

rem pytest -v -s -m "sanity and regression" --html=Reports\report.html testCases\

rem pytest -v -s -m "regression" --html=Reports\report.html testCases\

rem pytest -v -s --html=Reports\report.html testCases/test_searchCustomerByName.py --browser firefox