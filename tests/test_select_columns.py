import pandas as pd
import pytest
import arnio as ar


def test_select_columns_basic():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    frame = ar.from_pandas(df)
    result = ar.select_columns(frame, ["a", "c"])
    assert list(result.columns) == ["a", "c"]
    assert len(result) == 2


def test_select_columns_single():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    frame = ar.from_pandas(df)
    result = ar.select_columns(frame, ["a"])
    assert list(result.columns) == ["a"]
    assert len(result) == 2


def test_select_columns_preserves_order():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    frame = ar.from_pandas(df)
    result = ar.select_columns(frame, ["c", "a"])
    assert list(result.columns) == ["c", "a"]


def test_select_columns_missing_column():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    frame = ar.from_pandas(df)
    with pytest.raises((KeyError, ValueError), match="Unknown"):
        ar.select_columns(frame, ["a", "nonexistent"])


def test_select_columns_type_error():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    frame = ar.from_pandas(df)
    with pytest.raises(TypeError):
        ar.select_columns(frame, "a")


def test_select_columns_not_empty():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    frame = ar.from_pandas(df)
    with pytest.raises(ValueError, match="cannot be empty"):
        ar.select_columns(frame, [])


def test_select_columns_method():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    frame = ar.from_pandas(df)
    result = frame.select_columns(["b", "c"])
    assert list(result.columns) == ["b", "c"]


def test_select_columns_all():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    frame = ar.from_pandas(df)
    result = ar.select_columns(frame, ["a", "b"])
    assert list(result.columns) == ["a", "b"]