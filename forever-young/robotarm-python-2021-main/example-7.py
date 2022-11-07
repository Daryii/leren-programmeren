from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for i in range(5):
    for r in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for g in range(2):
        robotArm.moveRight()
robotArm.wait()