from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

z =1

while z < 9: 
    robotArm.grab()
    if robotArm.scan() == '':
        break
    for f in range(z):
        robotArm.moveRight()
    robotArm.drop()
    for d in range(z):
        robotArm.moveLeft()
    z = z +1
robotArm.wait()