# GV-Crawler

An Api endpoint for the GVSU sports analytics web applicattion <br>
When it recieves a post request from the app, it will retrieve <br>
the latest roster data and statistics from the gvsu website, thus <br>
updating the websites data.

### Container Setup
`sudo docker build -t rosterdata .` <br>
`sudo docker run --network="host" rosterdata` <br>
