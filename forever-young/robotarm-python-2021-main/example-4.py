from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

robotArm.speed = 3

for r in range(5):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    if r != 4:
        for i in range(2): 
            robotArm.moveLeft()

for u in range(5):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()


robotArm.wait()