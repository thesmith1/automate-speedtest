# Periodic Internet SpeedTest on Linux

## Prerequisites
- [Speedtest.net CLI](https://www.speedtest.net/apps/cli)
- `cron`
- `git`
- Python 3.6 or later (only to plot results)

## Setting Up
1. Set up `cron` by launching `crontab -e`.
2. Add the following line:

```
* * * * * speedtest -f csv >> <out_file>
```

where `<out_file>` is the absolute path to `out.csv` in this repository.

To reset the history of recorded data, run
```
git checkout out.csv
```

## Plot Results
Create a virtual environment:
```
python3 -m venv <venv_name>
```

Activate the virtual environment (`source <venv_name>/bin/activate`), then install dependencies:

```
pip3 install numpy plotly
```

Finally, execute the script to generate the plots:

```
python3 plot.py
```

This will produce the files `speed.html` and `latency.html`, containing the desired plots.
