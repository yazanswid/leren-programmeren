from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:
robotArm.moveRight()  

for _ in range(6):  
    robotArm.grab() 
    color = robotArm.scan()  

    if color == "blue":  
        robotArm.moveLeft()  
        robotArm.drop()  
        robotArm.moveRight()  
    elif color == "green":  
        robotArm.moveRight() 
        robotArm.drop()  
        robotArm.moveLeft()  
    elif color is None:  
        break  
# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

