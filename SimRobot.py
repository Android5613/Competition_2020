import wpilib
from wpilib.drive import DifferentialDrive


class MyRobot(wpilib.TimedRobot):

    RLMotorChannel = 1
    RRMotorChannel = 2
    FLMotorChannel = 3
    FRMotorChannel = 4

    DriveStickChannel = 0

    def robotInit(self):

        RLMotor = wpilib.Spark(self.RLMotorChannel)
        RRMotor = wpilib.Spark(self.RRMotorChannel)
        FLMotor = wpilib.Spark(self.FLMotorChannel)
        FRMotor = wpilib.Spark(self.FRMotorChannel)

        self.Left = wpilib.SpeedControllerGroup(RLMotor, FLMotor)
        self.Right = wpilib.SpeedControllerGroup(RRMotor, FRMotor)

        self.DriveStick = wpilib.Joystick(self.DriveStickChannel)

        self.drive = DifferentialDrive(self.Left, self.Right)

        self.drive.setExpiration(0.1)

    def operatorControl(self):

        self.drive.setSafetyEnabled(True)
        while self.isEnabled() and self.isOperatorControl():

            self.drive.arcadeDrive(
                self.DriveStick.getX(),
                self.DriveStick.getY(),
                squareInputs=True
            )

        f
if __name__ == "__main__":
    wpilib.run(MyRobot)