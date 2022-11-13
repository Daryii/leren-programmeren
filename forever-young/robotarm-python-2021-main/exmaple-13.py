from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

for u in range(9):
    robotArm.grab()
    for u in range(1 + u):
        robotArm.moveRight()
    robotArm.drop()
    for e in range(1 + u):
        robotArm.moveLeft()
    if robotArm.grab() == False:
        break
robotArm.wait()