from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
colorColumns = {"blue": 10, "red": 8, "green": 9, "white": 0, "yellow": 0}
spot = 1
max_position = 10  

for column in range(6):
    robotArm.grab()
    scannedColor = robotArm.scan()
    
    returnHere = spot
    target_position = colorColumns[scannedColor]

    
    while spot < target_position and spot < max_position:
        robotArm.moveRight()
        spot += 1

    
    robotArm.drop()

    
    while spot > returnHere:
        robotArm.moveLeft()
        spot -= 1

    
    if spot < max_position:
        robotArm.moveRight()
        spot += 1

    
    


# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

