from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

robotArm.speed = 4

for i in range(7):
    robotArm.moveRight()
robotArm.grab()
for i in range(1):
    robotArm.moveRight()
robotArm.drop()

for r in range(7):
    for i in range(2):
        robotArm.moveLeft()
    robotArm.grab()
    for i in range(1):
        robotArm.moveRight()
    robotArm.drop()




robotArm.wait()