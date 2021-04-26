# Readme


### Command line options

_CleanQL_ doesn't provide many options. You can list them by running `cleanql --help`:


```text
Usage: cleanql [OPTIONS] [PATHS]...

  The uncompromising SQL formatter.

  Pass path(s) to SQL file(s) or folder(s) that contain(s) SQL files.

Options:
  -f, --flavor [COMMON|HQL|ORACLE|POSTGRESQL]
                                  Specify the favor of SQL syntax.
  -v, --verbose                   Print verbose output.
  --help                          Show this message and exit.
```

_CleanQL_ is a Unix-style command-line tool:

- it does nothing if no paths are passed to it;
