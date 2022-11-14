from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# for
#     robotArm.grab()
#     if robotArm.scan() == "red":
#         u =  u + 1
#         for i in range(9):
#             robotArm.moveRight()
#         robotArm.drop()
#         for t in range(9):
#             robotArm.moveLeft()
#     else:
#         robotArm.drop()
#         robotArm.moveRight()
color = "red"
recht = 9
links = 9

for i in range(9):
    robotArm.grab()
    if robotArm.scan() == color:
        for y in range(recht-i):
            robotArm.moveRight()
        robotArm.drop()
        for r in range(links-i):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
    

robotArm.wait()