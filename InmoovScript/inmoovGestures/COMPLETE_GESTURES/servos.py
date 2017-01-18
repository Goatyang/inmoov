def servos():
        ear.pauseListening()
        sleep(2)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(79,100)
        i01.moveArm("left",5,119,28,15)
        i01.moveArm("right",5,111,28,15)
        i01.moveHand("left",42,58,87,55,71,35)
        i01.moveHand("right",81,20,82,60,105,113)
        i01.mouth.speakBlocking("I currently have twenty five  hobby servos installed in my body to give me life")
        i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(124,90)
        i01.moveArm("left",89,94,91,35)
        i01.moveArm("right",20,67,31,22)
        i01.moveHand("left",106,41,161,147,138,90)
        i01.moveHand("right",0,0,0,54,91,90)
        i01.mouth.speakBlocking("there's one servo  for moving my mouth up and down")
        sleep(1)
        i01.setHandSpeed("left", 0.85, 0.85, 1.0, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(105,76);
        i01.moveArm("left",89,106,103,35);
        i01.moveArm("right",35,67,31,22);
        i01.moveHand("left",106,0,0,147,138,7);
        i01.moveHand("right",0,0,0,54,91,90);
        i01.mouth.speakBlocking("two for my eyes")
        sleep(0.2)
        i01.setHandSpeed("left", 0.85, 0.85, 1.0, 1.0, 1.0, 0.85)
        i01.moveHand("left",106,0,0,0,0,7);
        i01.mouth.speakBlocking("and two more for my head")
        sleep(0.5)
        i01.setHandSpeed("left", 0.85, 0.9, 0.9, 0.9, 0.9, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(90,40);
        i01.moveArm("left",89,106,103,35);
        i01.moveArm("right",35,67,31,20);
        i01.moveHand("left",106,140,140,140,140,7);
        i01.moveHand("right",0,0,0,54,91,90);
        i01.mouth.speakBlocking("so i can look around")
        sleep(0.5)
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(105,125);
        i01.setArmSpeed("left", 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("left",60,100,85,30);
        i01.mouth.speakBlocking("and see who's there")
        i01.setHeadSpeed(0.65, 0.65)
        i01.moveHead(40,56);
        sleep(0.5)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
        i01.setArmSpeed("right", 0.5, 0.6, 0.5, 0.6);
        i01.moveArm("left",87,41,64,11)
        i01.moveArm("right",5,95,40,11)
        i01.moveHand("left",98,150,160,160,160,104)
        i01.moveHand("right",0,0,50,54,91,90);
        i01.mouth.speakBlocking("there's three servos  in each shoulder")
        i01.moveHead(40,67);
        sleep(2)
        i01.setHandSpeed("left", 0.8, 0.9, 0.8, 0.8, 0.8, 0.8)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.8, 0.8)
        i01.moveHead(43,69)
        i01.moveArm("left",87,41,64,11)
        i01.moveArm("right",5,95,40,42)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("left",42,10,160,160,160,35)
        i01.moveHand("right",81,20,82,60,105,113)
        i01.mouth.speakBlocking("here is the first servo movement")
        sleep(1)
        i01.moveHead(37,60);
        i01.setHandSpeed("left", 1.0, 1.0, 0.9, 0.9, 1.0, 0.8)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.moveArm("right",5,95,67,42)
        i01.moveHand("left",42,10,10,160,160,30)
        i01.mouth.speakBlocking("this is the second one")
        sleep(1)
        i01.moveHead(43,69);
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
        i01.moveArm("right",5,134,67,42)
        i01.moveHand("left",42,10,10,10,160,35)
        i01.mouth.speakBlocking("now you see the third")
        sleep(1)
        i01.setArmSpeed("right", 0.8, 0.8, 0.8, 0.8)
        i01.moveArm("right",20,90,45,16)
        i01.mouth.speakBlocking("they give me a more human like movement")
        sleep(1)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0);
        i01.moveHead(43,72)
        i01.moveArm("left",90,44,66,11)
        i01.moveArm("right",90,100,67,26)
        i01.moveHand("left",42,80,100,80,113,35)
        i01.moveHand("right",81,0,82,60,105,69)
        i01.mouth.speakBlocking("but, i have only  one servo, to move each elbow")
        i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
        i01.setHeadSpeed(0.8, 0.8)
        i01.moveHead(45,62)
        i01.moveArm("left",72,44,90,11)
        i01.moveArm("right",90,95,68,15)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right",81,0,82,60,105,0)
        i01.mouth.speakBlocking("that, leaves me, with one servo per wrist")
        i01.moveHead(40,60)
        i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.setHandSpeed("right", 0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        i01.moveArm("left",72,44,90,9)
        i01.moveArm("right",90,95,68,15)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right", 10, 140,82,60,105,10)
        i01.mouth.speakBlocking("and one servo for each finger.")
        sleep(0.5)
        i01.moveHand("left",42,0,100,80,113,35)
        i01.moveHand("right", 50, 51, 15,23, 30,140);
        i01.mouth.speakBlocking("these servos are located in my forearms")
        i01.setHandSpeed("left", 0.8, 0.8, 0.8, 0.8,0.8, 0.8)
        i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        i01.moveHand("left", 36, 52, 8,22, 20);
        i01.moveHand("right", 120, 147, 130,110, 125);
        removeleftarm()
        sleep(1)
        i01.mouth.speakBlocking("they are hooked up, by the use of tendons")
        i01.moveHand("left",10,20,30,40,60,150);
        i01.moveHand("right",110,137,120,100,105,130);
        i01.setHeadSpeed(1,1)
        i01.setArmSpeed("right", 1.0,1.0, 1.0, 1.0);
        i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0);
        relax()
        sleep(2)
        ear.resumeListening()

