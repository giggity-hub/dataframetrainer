### todo: write a generic script how to test the challenge classes
from ..challenges.challenge1 import SumSpendings
from ..challenges.challenge2 import ChangeDependingOfOthers
from ..challenges.challenge3 import ChangeAtIndex
from ..challenges.challenge4 import MonthIndex
from ..challenges.challenge5 import RenameColumn
from ..challenges.challenge6 import AddTriangularDataFrame
from ..challenges.challenge7 import AddPseudoTriangularDataFrame
from ..challenges.challenge8 import GroupTerms
from ..challenges.challenge9 import MapValues
from ..challenges.challenge10 import TransformWithConditions
from ..challenges.challenge11 import TransformWithConditions2
from ..challenges.challenge12 import TransformWithMultipleConditions
from ..challenges.challenge12 import TransformWithMultipleConditions
from ..challenges.challenge13 import GroupbyTransform
from ..challenges.challenge14 import Pivot1
from ..challenges.challenge15 import Pivot2
import pandas as pd
import pandas.testing as tm
import pytest
import json
from ..challenges.compile_challenges import _load_from_json


def test_challenge1():
    challenge = SumSpendings()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    tm.assert_frame_equal(
        df.reset_index(drop=True), _load_from_json(df.to_json()).reset_index(drop=True)
    )


def test_challenge2():
    challenge = ChangeDependingOfOthers()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    tm.assert_frame_equal(
        df.reset_index(drop=True), _load_from_json(df.to_json()).reset_index(drop=True)
    )


def test_challenge3():
    challenge = ChangeAtIndex()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


@pytest.mark.xfail(reason="Datetimes are somehow difficult to handle.")
def test_challenge4():
    challenge = MonthIndex()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)
    # todo: this does not yet work
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


def test_challenge5():
    challenge = RenameColumn()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


def test_challenge6():
    challenge = AddTriangularDataFrame()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


def test_challenge7():
    challenge = AddPseudoTriangularDataFrame()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)
    # test if this works
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


def test_challenge8():
    challenge = GroupTerms()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)
    # test if this works
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


def test_challenge9():
    challenge = MapValues()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


def test_challenge10():
    challenge = TransformWithConditions()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


def test_challenge11():
    challenge = TransformWithConditions2()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


def test_challenge12():
    challenge = TransformWithMultipleConditions()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


def test_challenge13():
    challenge = GroupbyTransform()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


def test_challenge14():
    challenge = Pivot1()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected, check_names=False)
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))


def test_challenge15():
    challenge = Pivot2()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected, check_names=False)
    tm.assert_frame_equal(df, _load_from_json(df.to_json()).reset_index(drop=True))
