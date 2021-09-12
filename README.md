# Aldabra

## Running managegment scripts

 The script robot-arm provides an easy way to run commands such as django managegment
 commands and more cli tools such as git interactivetly... To set it up

- set your project root path: by exporting "PROJECT_ROOT=/FULL_PATH/" as an environmental
  variable (best to add to your venv activate script)

- add robot-arm startup script to PATH:
  ```
  export PATH=$PATH:/FULL_PATH/TO/startup_script/
  ```

## Running The arm
After the above setup, run...
```
robot-arm
```

## make migrations and migrate data models
the followign command carries out desires task
```
*makemigrations* -> to make migrations
*migrate* -> to migrate database tables

```
for more info of commands to run in django a app visit: djangoproject.org

## start dev server
  ````
  runserver: to start developement server
  ````

**Happy Hacking (o_o)**
