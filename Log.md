```python
def barplot(bars, title='', upColor='blue', downColor='red'):
    """
    Create candlestick plot for the given bars. The bars can be given as
    a DataFrame or as a list of bar objects.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.patches import Rectangle

    if isinstance(bars, pd.DataFrame):
        ohlcTups = [
            tuple(v) for v in bars[['open', 'high', 'low', 'close']].values]
    elif bars and hasattr(bars[0], 'open_'):
        ohlcTups = [(b.open_, b.high, b.low, b.close) for b in bars]
    else:
        ohlcTups = [(b.open, b.high, b.low, b.close) for b in bars]

    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.grid(True)
    fig.set_size_inches(10, 6)
    for n, (open_, high, low, close) in enumerate(ohlcTups):
        if close >= open_:
            color = upColor
            bodyHi, bodyLo = close, open_
        else:
            color = downColor
            bodyHi, bodyLo = open_, close
        line = Line2D(
            xdata=(n, n),
            ydata=(low, bodyLo),
            color=color,
            linewidth=1)
        ax.add_line(line)
        line = Line2D(
            xdata=(n, n),
            ydata=(high, bodyHi),
            color=color,
            linewidth=1)
        ax.add_line(line)
        rect = Rectangle(
            xy=(n - 0.3, bodyLo),
            width=0.6,
            height=bodyHi - bodyLo,
            edgecolor=color,
            facecolor=color,
            alpha=0.4,
            antialiased=True
        )
        ax.add_patch(rect)

    ax.autoscale_view()
    return fig


def allowCtrlC():
    """Allow Control-C to end program."""
    signal.signal(signal.SIGINT, signal.SIG_DFL)


def logToFile(path, level=logging.INFO):
    """Create a log handler that logs to the given file."""
    logger = logging.getLogger()
    logger.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s %(message)s')
    handler = logging.FileHandler(path)
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def logToConsole(level=logging.INFO):
    """Create a log handler that logs to the console."""
    logger = logging.getLogger()
    logger.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.handlers = [
        h for h in logger.handlers
        if type(h) is not logging.StreamHandler]
    logger.addHandler(handler)
```

