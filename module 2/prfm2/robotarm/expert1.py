from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

# your code starts here:
for i in range(1):
    robotArm.grab()
    for j in range(5):
        robotArm.moveRight()
    robotArm.drop()
for i in range(4):
    robotArm.moveLeft()
for i in range(2):
    robotArm.grab()
    for j in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()

robotArm.moveRight()
for i in range(3):
    robotArm.grab()
    for j in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for k in range(5):
        robotArm.moveLeft()

robotArm.moveRight()

for w in range(4):
    robotArm.grab()
    for j in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for k in range(5):
            robotArm.moveLeft()

    



# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

