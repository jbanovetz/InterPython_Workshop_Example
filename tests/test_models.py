"""Tests for statistics functions within the Model layer."""

import pandas as pd

@pytest.mark.parameterize(
        'test_df,test_colname,expected',
        [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        7),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
        ]
                          )

def test_max_mag_integers():
    # Test that max_mag function works for integers
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 7

    assert max_mag(test_input_df, test_input_colname) == test_output

def test_max_mag_():
    # Test that max_mag function works for zeros and positive integerts
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[0, 0, 0], 
                                       [0, 0, 0], 
                                       [0, 0, 0]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 0

    assert max_mag(test_df, test_colname) == expected

@pytest.mark.parameterize(
        'test_df,test_colname,expected',
        [
        (pd.DataFrame(data=[[0, 1, 2], 
                            [3, 4, 5], 
                            [6, 7, 8]], 
                      columns=list("abc")),
        "b",
        1),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
        ]
                          )

def test_min_mag_zeros():
    # Test that min_mag function works for zeros and integers
    from lcanalyzer.models import min_mag
    assert min_mag(test_input_df, test_input_colname) == test_output

@pytest.mark.parameterize(
        'test_df,test_colname,expected',
        [
        (pd.DataFrame(data=[[0, 1, 2], 
                            [3, 4, 5], 
                            [6, 7, 8]], 
                      columns=list("abc")),
        "b",
        4),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
        ]
                          )

def test_mean_mag_zeros():
    # Test that max_mag function works for zeros and integers
    from lcanalyzer.models import mean_mag
    assert mean_mag(test_input_df, test_input_colname) == test_output