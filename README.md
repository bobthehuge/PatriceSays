# Patrice Says
<img src="https://github.com/bobthehuge/PatriceSays/blob/main/demo.gif" width="256" height="256" />
Patrice template GIF maker

## HTUI
1. install Pillow (tested only with 10.3.0)
2. (Optionnal) make script executable
3. Run script. By default, you only need to provide the wanted text

## Options
- `<text>`: wanted text
- `-f, --font [PATH]`: font file path. By default, it takes the provided `impact.ttf`
- `-o, --output [PATH]`: output file path. By default, it formats the given text
- `-s, --size [SIZE]`: text size. By default or if provided isn't valid (negative or null), it tries to automaticaly max-fit to the destination
