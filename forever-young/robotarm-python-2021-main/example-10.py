from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
for i in range(5):
    robotArm.grab()
    for s in range(9):
        robotArm.moveRight()
    robotArm.drop()
    for r in range(8):
        robotArm.moveLeft() 


robotArm.wait()