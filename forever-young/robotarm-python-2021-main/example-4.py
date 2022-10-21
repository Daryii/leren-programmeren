from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

robotArm.speed = 3


robotArm.grab()
for e in range(1,10):
    robotArm.moveRight()
robotArm.drop()
for e in range(1,10):
    robotArm.moveLeft()

robotArm.grab()
for e in range(1,10):
    robotArm.moveRight()
robotArm.drop()
for e in range(1,10):
    robotArm.moveLeft()

robotArm.grab()
for e in range(1,10):
    robotArm.moveRight()
robotArm.drop()
for e in range(1,10):
    robotArm.moveLeft()

robotArm.grab()
for e in range(1,10):
    robotArm.moveRight()
robotArm.drop()
for e in range(1,10):
    robotArm.moveLeft()

robotArm.grab()
for e in range(1,10):
    robotArm.moveRight()
robotArm.drop()

robotArm.grab()
for f in range(1,9):
    robotArm.moveLeft()
robotArm.drop()
for d in range(1,9):
    robotArm.moveRight()

robotArm.grab()
for f in range(1,9):
    robotArm.moveLeft()
robotArm.drop()
for d in range(1,9):
    robotArm.moveRight()

robotArm.grab()
for f in range(1,9):
    robotArm.moveLeft()
robotArm.drop()
for d in range(1,9):
    robotArm.moveRight()

robotArm.grab()
for f in range(1,9):
    robotArm.moveLeft()
robotArm.drop()
for d in range(1,9):
    robotArm.moveRight()

robotArm.grab()
for f in range(1,9):
    robotArm.moveLeft()
robotArm.drop()
for d in range(1):
    robotArm.moveRight()


robotArm.wait()