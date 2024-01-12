from dataclasses import dataclass


@dataclass
class PayloadItem:
    name: str
    diameter: float  # mm
    mass: float  # g
    points: int

    @property
    def volume(self):
        """
        Calculates the volume of the item in cm^3
        """
        return (4 / 3) * 3.14159 * (self.diameter / 20) ** 3


# Current options
PING_PONG_BALL = PayloadItem("Ping Pong Ball", 40.0, 2.7, 10)
GOLF_BALL = PayloadItem("Golf Ball", 42.67, 45.93, 50)
TENNIS_BALL = PayloadItem("Tennis Ball", 68.6, 59.4, 100)

PAYLOAD_ITEMS = [PING_PONG_BALL, GOLF_BALL, TENNIS_BALL]
