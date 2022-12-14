# Planet tracks
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/vb64/planet_tracks/pep257?label=Pep257&style=plastic)](https://github.com/vb64/planet_tracks/actions?query=workflow%3A%22pep257%22)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/vb64/planet_tracks/tests?label=Python%203.7-3.10&style=plastic)](https://github.com/vb64/planet_tracks/actions?query=workflow%3A%22tests%22)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/3829500c25364fd6ba18ed025d0f1be5)](https://www.codacy.com/gh/vb64/planet_tracks/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vb64/planet_tracks&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/3829500c25364fd6ba18ed025d0f1be5)](https://www.codacy.com/gh/vb64/planet_tracks/dashboard?utm_source=github.com&utm_medium=referral&utm_content=vb64/planet_tracks&utm_campaign=Badge_Coverage)

Console app for calculating Sun, Moon, etc coordinates for given point at the Earth with skyfield library.

Next call saves to file `sun_xxxx.csv` in current dir the track of the Sun for location at latitude 51.551750 north degrees and longitude 45.964380 eastern degrees (Russia, Saratov).

```
source/main.py sun 51.551750 45.964380
```

If you want location with south latitude / west longitude, use negative values. For example, Rio de Janeiro, Brazil.

```
source/main.py moon -22.908333 -43.196388
```

You can use next options to change output.

`--step`: Track points step in seconds. Default is 20.

`--length`: Track length in seconds. Default is 432000 (5 days).

`--min_elevation`: Minimal planet elevation in degrees above horizon. Default is 1.

`--utc`: Sets UTC time for start calculating. Format: 2022-01-31:23:00 Default is now.

`--output`: Sets file name for output data in CSV format. Default file name construct automatically.
