from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')

robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for f in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for e in range(8):
        robotArm.moveLeft()

robotArm.wait()