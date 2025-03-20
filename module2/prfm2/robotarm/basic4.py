from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.basic import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
robotArm.grab()
for i in range(9):
    robotArm.moveRight()

robotArm.drop()
for y in range(2):
    robotArm.moveLeft()

robotArm.grab()
for i in range(2):
    robotArm.moveRight()

robotArm.drop()
for y in range(5):
    robotArm.moveLeft()

robotArm.grab()
for u in range(5):
    robotArm.moveRight()

robotArm.drop()

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

