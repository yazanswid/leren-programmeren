from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from basic import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:
robotArm.moveRight()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.drop()


# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

