from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 3


robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()


robotArm.moveRight()
robotArm.grab()
for i in range (1):
    robotArm.moveRight()
robotArm.drop()
for i in range (1):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()

robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

robotArm.moveLeft()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()

robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

robotArm.moveLeft()


robotArm.wait()