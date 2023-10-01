# Smart Home description to JSON
Smart Home description convertion to JSON type file.
### How you can describe your house:
``` Python
description = """
kitchen: microwaves2, lights2            # two microwaves, two lights
Livingroom: 2lights, thermostats2        # two lights, two thermostats
bedroom: thermostat light                # one thermostat, one light
LIBRARY: lights5 and microwave           # five lights, one microwave
Garage: light1                           # one light
"""
```
More extreme example
``` Python
description = """
kitchen: 2microwave,  2lights             # two microwaves, two lights
Livingroom: sssslight2, 2thermostatkkkkk  # two lights, two thermostats
bedroom: elaseeethermostat light          # one thermostat, one light
LIBRARY: 5lights and microwave on         # five lights, one microwave
Garage: 1light                            # one light
"""
```

### Input custom names:
```
Enter a custom name for the microwave in the Kitchen: 3
Enter a custom name for the microwave in the Kitchen: 4
Enter a custom name for the light in the Kitchen: 4
Enter a custom name for the light in the Kitchen: 5
Enter a custom name for the light in the Livingroom: 6
Enter a custom name for the light in the Livingroom: 7
Enter a custom name for the thermostat in the Livingroom: 8
Enter a custom name for the thermostat in the Livingroom: 3
Enter a custom name for the thermostat in the Bedroom: 2
Enter a custom name for the light in the Bedroom: 1
Enter a custom name for the light in the Library: 3
Enter a custom name for the light in the Library: 45
Enter a custom name for the light in the Library: 6
Enter a custom name for the light in the Library: 7
Enter a custom name for the light in the Library: 8
Enter a custom name for the microwave in the Library: 5
Enter a custom name for the light in the Garage: 3
```
### Output JSON
```
{
    "kitchen": [
        {
            "name": "3",
            "type": "microwave",
            "state": "off"
        },
        {
            "name": "4",
            "type": "microwave",
            "state": "off"
        },
        {
            "name": "4",
            "type": "light",
            "state": "off"
        },
        {
            "name": "5",
            "type": "light",
            "state": "off"
        }
    ],
    "livingroom": [
        {
            "name": "6",
            "type": "light",
            "state": "off"
        },
        {
            "name": "7",
            "type": "light",
            "state": "off"
        },
        {
            "name": "8",
            "type": "thermostat",
            "state": "off"
        },
        {
            "name": "3",
            "type": "thermostat",
            "state": "off"
        }
    ],
    "bedroom": [
        {
            "name": "2",
            "type": "thermostat",
            "state": "off"
        },
        {
            "name": "1",
            "type": "light",
            "state": "off"
        }
    ],
    "library": [
        {
            "name": "3",
            "type": "light",
            "state": "off"
        },
        {
            "name": "45",
            "type": "light",
            "state": "off"
        },
        {
            "name": "6",
            "type": "light",
            "state": "off"
        },
        {
            "name": "7",
            "type": "light",
            "state": "off"
        },
        {
            "name": "8",
            "type": "light",
            "state": "off"
        },
        {
            "name": "5",
            "type": "microwave",
            "state": "off"
        }
    ],
    "garage": [
        {
            "name": "3",
            "type": "light",
            "state": "off"
        }
    ]
}
```

## Task list
* make different properties for different devices types 
* add more devices
## How to Contribute
1. Fork the Project
2. Clone repo with your GitHub username instead of ```YOUR-USERNAME```:<br>
```
$ git clone https://github.com/YOUR-USERNAME/description-to-JSON
```
3. Create new branch:<br>
```
$ git branch BRANCH-NAME 
$ git checkout BRANCH-NAME
```
4. Make changes and test<br>
5. Submit Pull Request with comprehensive description of change
## License 
[MIT license](LICENSE)
