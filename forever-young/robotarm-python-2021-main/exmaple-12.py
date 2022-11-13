from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

u = 0

while u < 5:
    robotArm.grab()
    if robotArm.scan() == "red":
        u =  u + 1
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for t in range(9):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
robotArm.wait()