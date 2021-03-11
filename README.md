# Periodic Internet SpeedTest on Linux

## Prerequisites
- [Speedtest.net CLI](https://www.speedtest.net/apps/cli)
- `cron`
- `git`

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
