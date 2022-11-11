from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

i = 0

while i < 9:
    robotArm.grab()
    if robotArm.scan() == "white":
        i = i +1
        robotArm.moveRight()
    robotArm.drop()
    robotArm.moveRight()
    i = i +1

   


robotArm.wait()