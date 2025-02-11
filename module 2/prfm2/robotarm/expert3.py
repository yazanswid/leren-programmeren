from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:
position = 1

while True:
    robotArm.grab()
    color = robotArm.scan()

    if color is '':
        break
    

    for i in range(position):
        robotArm.moveRight()

    robotArm.drop()


    for  i in range(position):
        robotArm.moveLeft()

    position += 1
        


# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

