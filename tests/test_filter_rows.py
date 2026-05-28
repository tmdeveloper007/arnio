import pandas as pd
import pytest
import arnio as ar


def test_filter_rows_gt():
    df = pd.DataFrame({"age": [10, 20, 30, 40], "name": ["a", "b", "c", "d"]})
    frame = ar.from_pandas(df)
    result = ar.filter_rows(frame, column="age", op=">", value=20)
    assert len(result) == 2
    assert list(result["age"]) == [30, 40]


def test_filter_rows_lt():
    df = pd.DataFrame({"age": [10, 20, 30, 40], "name": ["a", "b", "c", "d"]})
    frame = ar.from_pandas(df)
    result = ar.filter_rows(frame, column="age", op="<", value=30)
    assert len(result) == 2
    assert list(result["age"]) == [10, 20]


def test_filter_rows_ge():
    df = pd.DataFrame({"age": [10, 20, 30, 40], "name": ["a", "b", "c", "d"]})
    frame = ar.from_pandas(df)
    result = ar.filter_rows(frame, column="age", op=">=", value=20)
    assert len(result) == 3
    assert list(result["age"]) == [20, 30, 40]


def test_filter_rows_le():
    df = pd.DataFrame({"age": [10, 20, 30, 40], "name": ["a", "b", "c", "d"]})
    frame = ar.from_pandas(df)
    result = ar.filter_rows(frame, column="age", op="<=", value=30)
    assert len(result) == 3
    assert list(result["age"]) == [10, 20, 30]


def test_filter_rows_eq():
    df = pd.DataFrame({"age": [10, 20, 30, 20], "name": ["a", "b", "c", "d"]})
    frame = ar.from_pandas(df)
    result = ar.filter_rows(frame, column="age", op="==", value=20)
    assert len(result) == 2


def test_filter_rows_ne():
    df = pd.DataFrame({"age": [10, 20, 30, 20], "name": ["a", "b", "c", "d"]})
    frame = ar.from_pandas(df)
    result = ar.filter_rows(frame, column="age", op="!=", value=20)
    assert len(result) == 2
    assert list(result["age"]) == [10, 30]


def test_filter_rows_invalid_operator():
    df = pd.DataFrame({"age": [10, 20, 30]})
    frame = ar.from_pandas(df)
    with pytest.raises(ValueError, match="Unsupported operator"):
        ar.filter_rows(frame, column="age", op="invalid", value=20)


def test_filter_rows_invalid_column():
    df = pd.DataFrame({"age": [10, 20, 30]})
    frame = ar.from_pandas(df)
    with pytest.raises(ValueError, match="Unknown column"):
        ar.filter_rows(frame, column="nonexistent", op=">", value=20)


def test_filter_rows_non_scalar_value():
    df = pd.DataFrame({"age": [10, 20, 30]})
    frame = ar.from_pandas(df)
    with pytest.raises(TypeError, match="filter_rows value must be a scalar"):
        ar.filter_rows(frame, column="age", op=">", value=[20, 30])


def test_filter_rows_returns_same_type_as_input():
    df = pd.DataFrame({"age": [10, 20, 30]})
    frame = ar.from_pandas(df)
    result = ar.filter_rows(frame, column="age", op=">", value=5)
    assert isinstance(result, ar.ArFrame)

    result_pd = ar.filter_rows(df, column="age", op=">", value=5)
    assert isinstance(result_pd, pd.DataFrame)


def test_filter_rows_with_string_column():
    df = pd.DataFrame({"name": ["alice", "bob", "charlie"], "age": [25, 30, 35]})
    frame = ar.from_pandas(df)
    result = ar.filter_rows(frame, column="name", op="==", value="bob")
    assert len(result) == 1
    assert list(result["name"]) == ["bob"]


def test_filter_rows_no_matches():
    df = pd.DataFrame({"age": [10, 20, 30]})
    frame = ar.from_pandas(df)
    result = ar.filter_rows(frame, column="age", op=">", value=100)
    assert len(result) == 0