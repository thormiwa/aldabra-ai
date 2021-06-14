# Aldabra

## Virtual environment setup
  ## For Windows  
  
  cd into **.\cli-scripts** in project root and run:
  **assuming you have python3 installed on your system**
  ````
  .\envset.ps1
  ````
  
  to activate environment run:
  ````
  .\envactive.ps1
  ````
  deactive environment using
  ````
  deactive
  ````
  
  ## For Linux(Ubuntu)
  ```
    ./envset
  ```
 ## Database setup
  ## Windows
  Run following scripts in admin windows **powershell**
  
  In .\cli-scripts run:
  ````
  .\dbset.ps1
  ````
  
  run migration to see if db is correctly installed
  ````
  .\migration.ps1
  ````
  
## start dev server
  ## Windows
  in **.\cli-scripts** run:
  ````
  .\runserver.ps1
  ````
  
  ## Linux(Ubuntu)
  ````
  ./runserver
  ````

**Happy Hacking (o_o)**
   
   
