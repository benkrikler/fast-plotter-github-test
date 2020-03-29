import pytest
import string
import numpy as np
import pandas as pd
from fast_plotter.postproc import functions as funcs


def _make_string(index):
    chars = string.printable
    start = index % len(chars)
    stop = (index + 28) % len(chars)
    return chars[start] + chars[stop]


@pytest.fixture
def binned_df():
    anInt = list(range(4))
    aCat = ["foo", "bar"]
    anInterval = pd.IntervalIndex.from_breaks(np.linspace(100, 104, 6))
    index = pd.MultiIndex.from_product([anInt, aCat, anInterval],
                                       names=["int", "cat", "interval"])
    data = dict(a=np.arange(len(index)), b=map(_make_string, range(len(index))))
    df = pd.DataFrame(data, index=index)
    return df


def test_query(binned_df):
    result = funcs.query(binned_df, "cat=='bar'")
    assert len(result) == 20

    result = funcs.query(binned_df, "cat=='bar' and int > 2")
    assert len(result) == 5


def test_rebin(binned_df):
    result = funcs.rebin(binned_df.copy(), axis="int", mapping=dict(zip(range(4), [0, 2] * 2)))
    assert len(result) == 20
    assert list(result.index.unique("int")) == [0, 2]

    mapping = {0: dict(bar="foo"), 2: dict(foo="bar"), 3: dict(foo="BAZ", bar="BAZ")}
    result = funcs.rebin(binned_df.copy(), axis=["int", 'cat'], mapping=mapping)
    assert len(result) == 25
    assert set(result.index.unique("cat")) == {"bar", "BAZ", "foo"}


# def test_keep_bins():
#     #def keep_bins(df, axis, keep):
#     pass

# def test_keep_specific_bins():
#     #def keep_specific_bins(df, axis, keep, expansions={}):
#     pass

def test_combine_cols_AND_split_dimension(binned_df):
    result = funcs.combine_cols(binned_df, {"a;b": "{a};{b}"})
    assert len(result.columns) == 3
    assert all(result.columns == ["a", "b", "a;b"])
    assert len(result) == 40

# def test_split_dimension(binned_df):
#     #def split_dimension(df, axis, delimeter=";"):
#     result = funcs.split_dimension(binned_df, ["interval"], ",")
#     pass

# def test_regex_split_dimension():
#     #def regex_split_dimension(df, axis, regex):
#     pass

# def test_rename_cols():
#     #def rename_cols(df, mapping):
#     pass

# def test_rename_dim():
#     #def rename_dim(df, mapping):
#     pass

# def test_split():
#     #def split(df, axis, keep_split_dim, return_meta=True):
#     pass

# def test_reorder_dimensions():
#     #def reorder_dimensions(df, order):
#     pass

# def test_densify():
#     #def densify(df, known={}):
#     pass

# def test_stack_weights():
#     #def stack_weights(df, drop_n_col=False):
#     pass

# def test_to_datacard_inputs():
#     #def to_datacard_inputs(df, select_data, rename_syst_vars=False):
#     pass

# def test_assign_col():
#     #def assign_col(df, assignments={}, evals={}, drop_cols=[]):
#     pass

# def test_assign_dim():
#     #def assign_dim(df, assignments={}, evals={}, drop_cols=[]):
#     pass

# def test_merge():
#     #def merge(dfs):
#     pass

# def test_multiply_values():
#     #def multiply_values(df, constant=0, mapping={}, weight_by_dataframes=[], apply_if=None):
#     pass

# def test_multiply_dataframe():
#     #def multiply_dataframe(df, multiply_df, use_column=None):
#     pass

# def test_normalise_group():
#     #def normalise_group(df, groupby_dimensions, apply_if=None, use_column=None):
#     pass

# def test_open_many():
#     #def open_many(file_list, return_meta=True):
#     pass

# def test_write_out():
#     #def write_out(df, meta, filename="tbl_{dims}--{name}.csv", out_dir=None):
#     pass
