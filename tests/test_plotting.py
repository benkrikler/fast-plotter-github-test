import numpy as np
from fast_plotter import plotting


def test_replace_inf():
    x = np.arange(5)
    replaced = plotting.replace_infs(x)
    assert np.array_equal(replaced, x)

    x = np.concatenate(([-np.inf], x, [np.inf]), axis=0)
    replaced = plotting.replace_infs(x)
    assert np.array_equal(replaced, np.arange(-1, 6))

    x = np.arange(2, 4)
    replaced = plotting.replace_infs(x)
    assert np.array_equal(replaced, np.arange(2, 4))

    x = np.concatenate(([-np.inf], x), axis=0)
    replaced = plotting.replace_infs(x)
    assert np.array_equal(replaced, np.arange(1, 4))


def test_pad_zero_noYs():
    x = np.arange(5)
    padded, = plotting.standardize_values(x)
    assert np.array_equal(padded, np.arange(-1, 6))

    x = np.concatenate(([-np.inf], x, [np.inf]), axis=0)
    padded, = plotting.standardize_values(x)
    assert np.array_equal(padded, np.arange(-2, 7))

    x = np.arange(2, 4)
    padded, = plotting.standardize_values(x)
    assert np.array_equal(padded, np.arange(1, 5))

    x = np.concatenate(([-np.inf], x), axis=0)
    padded, = plotting.standardize_values(x)
    assert np.array_equal(padded, np.arange(0, 5, dtype=float))


def test_pad_zero_oneY():
    x = np.arange(5)
    y = np.arange(5, 0, -1)
    expected_y = np.concatenate(([0], y, [0]), axis=0)
    pad_x, pad_y = plotting.standardize_values(x, [y])
    assert np.array_equal(pad_x, np.arange(-1, 6))
    assert np.array_equal(pad_y, expected_y)

    x = np.concatenate(([-np.inf], x, [np.inf]), axis=0)
    y = np.arange(len(x), 0, -1)
    expected_y = np.concatenate(([0], y, [0]), axis=0)
    pad_x, pad_y = plotting.standardize_values(x, [y])
    assert np.array_equal(pad_x, np.arange(-2, 7))
    assert np.array_equal(pad_y, expected_y)

    x = np.arange(2, 4)
    y = np.arange(len(x), 0, -1)
    expected_y = np.concatenate(([0], y, [0]), axis=0)
    pad_x, pad_y = plotting.standardize_values(x, [y])
    assert np.array_equal(pad_x, np.arange(1, 5))
    assert np.array_equal(pad_y, expected_y)

    x = np.concatenate(([-np.inf], x), axis=0)
    y = np.arange(len(x), 0, -1)
    expected_y = np.concatenate(([0], y, [0]), axis=0)
    pad_x, pad_y = plotting.standardize_values(x, [y])
    assert np.array_equal(pad_x, np.arange(0, 5))
    assert np.array_equal(pad_y, expected_y)
