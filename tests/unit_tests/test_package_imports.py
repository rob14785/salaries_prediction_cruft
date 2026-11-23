def test_package_imports():
    import salaries_prediction_cruft

from salaries_prediction_cruft.commons.utils import normalize_project_name


def test_package_imports():
    import salaries_prediction_cruft


def test_normalize_project_name():
    assert normalize_project_name(" Salary Prediction ") == "salary_prediction"