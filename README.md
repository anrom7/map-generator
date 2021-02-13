# MAP GENERATOR

## Description
This program generates a map with locations where films were filmed. The user
enters 3 values, which are year, longitute and latitude. The map shows 10 films
of only that year, locations of which are the closest ones to the current
location of the user.

## Usage
``` python
import main.py
```
Enter requested values. Wait for the map to be generated.

## Example of running
When the program is run, it asks the user to enter the year of a film, and
after the year being entered, the program asks the user to enter his/her
coordinates in 'latitude longitude' format.
For example, user enters this values
![Input](input.jpg?raw=true "User's input")

Then, he/she gots the next output, saying to wait while the map is being
generated. Messages appear with a delay, defined by the end of the work of the
functions that are called.
![Output1](output1.jpg?raw=true "Output in command line")

When all data processing is done and the map is generated, the user is
welcomed to see the 'map.html' file on his/her directory. After opening it, the
following map is shown in the web browser.
![Output2](output2.png?raw=true "Generated map screenshot")

The program ends its work.

## Description of html file structure and markup tags
map.html file has a basic html structure.

<!DOCTYPE html> at the beginning of the file defines the file's markup
language.

Between the <head> </head> tags there is main information of the file. It has
<script> </script> tags that define some important information, and <style>
</style> tags that define css style of the file.

Between <body> </body> tags there are main tags, which create the html file
and contain information that is displayed in the web browser (in this case it
is the map Class).

Inside the <script> </script> tags there are all actions called in the main.py
module, but written in js. That variables, their attributes and methods
correspond to the ones written in the build_map() function in the main.py
module.

For example, var map_b2a2377d73b44da19522618323881680 = L.map() line (with all
the attributes inside it) creates a map itself, and corresponds to the
map = folium.Map(location=user_coords, zoom_start=10) line in main.py module.

Another example, var marker_8ba866f9464a48b2abfb23fd4da05a1c = L.marker()
(with all the attributes inside it) create a marker of the user's input
location and correspond to the fg_user.add_child() method in main.py module.

## Results
The result of the work of the program is a map with locations of 10 films,
which have the closest location to the user's current location. The map
displays information on current user's location, film locations, which
contain the film names, and lines that connect user's location to every film's
location on the map.

## License
[MIT](https://github.com/linvieson/map-generator/blob/main/LICENSE.txt)