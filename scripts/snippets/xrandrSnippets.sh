##To enable a monitor that is currently disabled:
xrandr -d :0 --output LVDS1 --auto 
##To specify a monitor in relation to another monitor
xrandr --output VGA1 --auto --left-of LVDS1 