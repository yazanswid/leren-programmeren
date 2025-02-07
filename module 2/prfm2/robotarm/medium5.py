from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
robotArm.grab()

for _ in range(9):
    robotArm.moveRight()
    
robotArm.drop()

for _ in range(8):
    robotArm.moveLeft()


robotArm.grab()

for _ in range(7):
    robotArm.moveRight()
robotArm.drop()

for _ in range(6):
    robotArm.moveLeft()

robotArm.grab()

for _ in range(5):
    robotArm.moveRight()

robotArm.drop()

for _ in range(4):
    robotArm.moveLeft()

robotArm.grab()

for _ in range(3):
    robotArm.moveRight()

robotArm.drop()

for _ in range(2):
    robotArm.moveLeft()

robotArm.grab()

for _ in range(1):
    robotArm.moveRight()

robotArm.drop()

for _ in range(1):
    robotArm.showSolution()


# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

