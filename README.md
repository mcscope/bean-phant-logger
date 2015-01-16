# Very Simple LightBlueBean Logger

Use the [LightBlue Bean](http://punchthrough.com/bean/) to log data over time.

This logs the data right to stdout, where you can capture it, save it, put it into other programs, etc.
This is just a bare-bones implementation, to build off of.

It's a simplification of mplewis's bean-phant-logger, which logged to the phant service.

# Setup

1. Copy `sample_config.py` to `config.py`.
2. Edit `config.py`, set your desired logging interval. If you want to log any additional data fields, you can specify them there (and also edit the bean sketch to send them.)
3. Install the Python script's requirements with `pip install -r requirements.txt`.
4. Connect to your Bean with the Bean Loader App.
5. Program your Bean with `logger_sketch/logger_sketch.ino`.
6. Use your Bean as a Virtual Serial device by right-clicking on it and selecting the menu option. It'll look like this when you're done:

![Bean as Virtual Serial menu](http://i.imgur.com/dKpgldI.png =512x)

# Usage

1. Run the script with `python logger.py`.
2. Data will print to stdout.

# Contributions

Bug reports, fixes, or features? Feel free to open an issue or pull request any time.

# Written

Written in a greek cafe, two hours out of Las Vegas, in the middle of a 7 day road trip. :-P
Originally used to log the acceleration of the lightbluebean when it was strapped to fireworks.

# Thanks

Thanks to mplewis for the original code, and to AlexGlow (www.alexglow.com) for being a wonderful cohacker and roadtrip-companion.

# License
Original bean-phant-logger license
Copyright (c) 2014 Matthew Lewis. Licensed under [the MIT License](http://opensource.org/licenses/MIT).

Modifications to make it bean-simple-logger license
Copyright (c) 2015 Christopher Beacham. Licensed under [the MIT License](http://opensource.org/licenses/MIT).

