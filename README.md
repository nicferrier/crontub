# crontub - a dynamic cron daemon

crontub is a virtual crontab... it abstracts the definition of the
crontab.  Currently the abstraction takes the form of scanning files
for special CRON declarations which are then assembled into a crontab
as if someone had written a text file.

Why? crontub let's your programmers specify how and where a script
should run under cron inside the script itself. This means that you
can place crons under version control and have crontub find them and
run them at whatever time has been specified.

In addition, crontub let's you specify a role checker so that you can
have different crontabs run on different environments (by adjusting
the role checker).

The config file:

`  [cron]
  pidfile = path
  roletest = somecommand`

'pidfile' is a path to a pidfile, where the daemon records it's pid,
by default the pidfile is in /tmp/crontub.pid

'roletest' specifies that somecommand be run to establish whether the
cron should be run here or not.

the roletest command is executed with the %% template variables:

> 'role' set to the role being tested
> 'user' set to the user being tested

for example, setting 'roletest' thusly:

  `roletest = /usr/local/bin/check_is_staging -u %(user)s %(role)s`

with a role of "staging" and a user of "woome" would cause the
following command to be executed:

  `/usr/local/bin/check_is_staging -u woome staging`
