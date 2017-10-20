# Quitting a running screen, if its running
screen -X -S server quit

# Starting selfbot in new screen
# -L  ->  Writing console output in file 'screenlog.0'
# -S  ->  Set name of screen so you can resume it or stop it
cd src
screen -L -S self python3 main.py
