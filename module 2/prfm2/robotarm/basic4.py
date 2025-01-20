from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.basic import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

