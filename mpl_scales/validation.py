import re

import matplotlib.ticker as ticker


def _validate_function_format(func):
    if len(func.__code__.co_varnames) != 2:
        print(func.__code__.co_varnames)
        raise TypeError(
            "the number of arguments passed to format function {} must be 2".format(
                str(func)
            )
        )
    return ticker.FuncFormatter(func)


def _validate_string_format(fmt):
    # TODO: 流石に書き直したい
    fmt = fmt.replace("{:", "{x:")
    fmt = fmt.replace(":d}", ":.0f}")
    fmt = fmt.replace(":,d}", ":,.0f}")
    fmt = re.sub('{[a-zA-Z]:', '{x:', fmt)
    return fmt
