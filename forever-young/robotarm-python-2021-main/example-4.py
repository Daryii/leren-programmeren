from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

robotArm.speed = 5

for i in range(9):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
for z in range(9):
    robotArm.moveLeft()
for i in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
for z in range(8):
    robotArm.moveLeft()
for i in range(7):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
for z in range(7):
    robotArm.moveLeft()
for i in range(6):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    
for z in range(6):
    robotArm.moveLeft()
for i in range(5):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
for z in range(5):
    robotArm.moveLeft()
for e in range(5):
    robotArm.moveRight()
robotArm.grab()
for e in range(4):
    robotArm.moveLeft()
robotArm.drop()

for e in range(5):
    robotArm.moveRight()
robotArm.grab()
for e in range(5):
    robotArm.moveLeft()
robotArm.drop()

for z in range(6):
    robotArm.moveRight()
robotArm.grab()
for e in range(6):
    robotArm.moveLeft()
robotArm.drop()

for z in range(7):
    robotArm.moveRight()
robotArm.grab()
for e in range(7):
    robotArm.moveLeft()
robotArm.drop()

for z in range(8):
    robotArm.moveRight()
robotArm.grab()
for e in range(8):
    robotArm.moveLeft()
robotArm.drop()



robotArm.wait()