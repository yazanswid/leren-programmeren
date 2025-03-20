from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()

for _ in range(8):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
        


    else:
        robotArm.drop()
        robotArm.moveLeft()

    if color is None:
        break
        
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

