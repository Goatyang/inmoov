def daVinci():
  i01.rightArm.enableAutoDisable(0)
  i01.leftArm.enableAutoDisable(0)
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 0.65)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 0.65)
  i01.setArmSpeed("left", 0.80, 0.80, 0.80, 0.80)
  i01.setArmSpeed("right", 0.80, 0.80, 0.80, 0.80)
  i01.setHeadSpeed(0.75, 0.75)
  i01.moveHead(80,90)
  i01.moveArm("left",0,118,29,74)
  i01.moveArm("right",0,118,29,74)
  i01.moveHand("left",50,40,30,20,10,47)
  i01.moveHand("right",50,40,30,20,10,137)

