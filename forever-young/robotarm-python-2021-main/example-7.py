from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed = 2
for i in range(1,6):
    for r in range(1,7):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for z in range (1,3): 
        robotArm.moveRight()
robotArm.wait()