from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed=4
for e in range(11):
    robotArm.grab()
    for u in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for h in range(5):
        robotArm.moveLeft()
    if robotArm.grab() == False:
        robotArm.moveRight()


robotArm.wait()