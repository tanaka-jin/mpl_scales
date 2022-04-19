from typing import List, Callable, Union

import matplotlib
import matplotlib.ticker as ticker

from .validation import _validate_function_format, _validate_string_format


class MplTickScaler:
    def __init__(self, ax, direction: str):
        self._ax = ax
        self._direction = direction

        if self._direction == "x":
            self._axis = self._ax.xaxis
        elif self._direction == "y":
            self._axis = self._ax.yaxis

        self._is_date = isinstance(
            self._axis.get_major_locator(), matplotlib.dates.AutoDateLocator
        )

    def set_ticks(
        self,
        diff: int = None,
        n: int = None,
        ticks: List[int] = None,
        format: Union[str, Callable] = None,
        labels: List = None,
        label_off: bool = None,
        labelsize: Union[int, float] = None,
        rot: Union[int, float] = None,
        off: bool = None,
    ):
        """customize axis tick"""
        self._set_labelstyle(labelsize, rot)

        if off:
            self._axis.set_major_locator(ticker.NullLocator())
            return self._return()
        else:
            self._set_locations(diff, n, ticks)

        if label_off:
            self._axis.set_major_formatter(ticker.NullFormatter())
            return self._return()
        else:
            self._set_labels(format, labels)

        return self._return()

    def _return(self):
        """return時に行う処理"""
        matplotlib.pyplot.close()
        self._ax.figure.tight_layout()
        return self._ax.figure

    def _set_labelstyle(self, labelsize, rot):
        """update ticklabel's style"""
        self._ax.tick_params(
            axis=self._direction, labelsize=labelsize, labelrotation=rot
        )

    def _set_locations(self, diff: int = None, n: int = None, ticks: List[int] = None):
        if diff:
            # 幅の指定
            self._axis.set_major_locator(ticker.MultipleLocator(diff))
        elif n:
            # 数の指定
            self._axis.set_major_locator(ticker.MaxNLocator(n, min_n_ticks=n))
        elif ticks:
            # リストで指定
            self._axis.set_major_locator(ticker.FixedLocator(ticks))

    def _set_labels(self, format: Union[str, Callable], labels: List[str]):
        if format:
            if callable(format):
                format = _validate_function_format(format)
                self._axis.set_major_formatter(format)
            elif self._is_date:
                self._axis.set_major_formatter(
                    matplotlib.dates.DateFormatter(fmt=format)
                )
            else:
                format = _validate_string_format(format)
                self._axis.set_major_formatter(ticker.StrMethodFormatter(format))
        elif labels:
            # リストで指定
            self._axis.set_major_formatter(ticker.FixedFormatter(labels))


def set_xticks(ax, **kwargs):
    tickscaler = MplTickScaler(ax, direction="x")
    fig = tickscaler.set_ticks(**kwargs)
    return fig


def set_yticks(ax, **kwargs):
    tickscaler = MplTickScaler(ax, direction="y")
    fig = tickscaler.set_ticks(**kwargs)
    return fig


def set_bothticks(ax, **kwargs):
    tickscaler = MplTickScaler(ax, direction="x")
    fig = tickscaler.set_ticks(**kwargs)
    tickscaler = MplTickScaler(ax, direction="y")
    fig = tickscaler.set_ticks(**kwargs)
    return fig
