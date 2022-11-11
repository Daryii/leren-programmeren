from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
x=9
y=8
for i in range(5): 
    print(i)
    robotArm.grab()
    for s in range(x): 
        robotArm.moveRight()
    robotArm.drop()
    for r in range(y):
        robotArm.moveLeft() 
    x = x - 2
    y = y - 2


robotArm.wait()