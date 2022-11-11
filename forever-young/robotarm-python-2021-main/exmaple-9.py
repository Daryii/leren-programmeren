from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 4

for s in range(1, 5):
  for b in range(s):
    robotArm.grab()
    for m in range(5):
      robotArm.moveRight()
    robotArm.drop()
    for m in range(5 - int(b == s - 1)):
        robotArm.moveLeft()


robotArm.wait()