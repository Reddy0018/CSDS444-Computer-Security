import argparse
import pygame
from pygame.locals import *

class TrafficLight:
    def __init__(self, green: bool, yellow: bool, red: bool):
        self.green = green
        self.yellow = yellow
        self.red = red

    def setGreen(self):
        self.green = True
        self.yellow = False
        self.red = False

    def setYellow(self):
        self.green = False
        self.yellow = True
        self.red = False

    def setRed(self):
        self.green = False
        self.yellow = False
        self.red = True

    def getGreen(self):
        return self.green

    def getYellow(self):
        return self.yellow

    def getRed(self):
        return self.red


class PedestrianLight:
    def __init__(self, walk: bool, stop: bool):
        self.walk = walk
        self.stop = stop

    def setWalk(self):
        self.walk = True
        self.stop = False

    def setStop(self):
        self.walk = False
        self.stop = True

    def getWalk(self):
        return self.walk

    def getStop(self):
        return self.stop


class TrafficSystem:
    def __init__(self, northLight: TrafficLight, southLight: TrafficLight, eastLight: TrafficLight,
                 westLight: TrafficLight,
                 northCross: PedestrianLight, southCross: PedestrianLight, eastCross: PedestrianLight,
                 westCross: PedestrianLight,
                 redTime: float, greenTime: float, yellowTime: float):
        self.northLight = northLight
        self.southLight = southLight
        self.eastLight = eastLight
        self.westLight = westLight
        self.northCross = northCross
        self.southCross = southCross
        self.eastCross = eastCross
        self.westCross = westCross
        self.redTime = redTime
        self.greenTime = greenTime
        self.yellowTime = yellowTime


def initialize_traffic_system(redTime: float, greenTime: float, yellowTime: float):
    # Initialize the traffic lights
    northLight = TrafficLight(False, False, True)  # Start with North red
    southLight = TrafficLight(False, False, True)  # Start with South red
    eastLight = TrafficLight(True, False, False)  # Start with East green
    westLight = TrafficLight(True, False, False)  # Start with West green
    northCross = PedestrianLight(False, True)  # Start with North cross stop
    southCross = PedestrianLight(False, True)  # Start with South cross stop
    eastCross = PedestrianLight(True, False)  # Start with East cross stop
    westCross = PedestrianLight(True, False)  # Start with West cross stop

    trafficSystem = TrafficSystem(northLight, southLight, eastLight, westLight, northCross, southCross,eastCross, westCross, redTime, greenTime, yellowTime)

    return trafficSystem


def update_traffic_lights(cycleTime: float, trafficSystem: TrafficSystem):
    if cycleTime < trafficSystem.redTime:
        trafficSystem.northLight.setRed()
        trafficSystem.southLight.setRed()
        trafficSystem.northCross.setStop()
        trafficSystem.southCross.setStop()
        trafficSystem.eastLight.setGreen()
        trafficSystem.westLight.setGreen()
        trafficSystem.eastCross.setWalk()
        trafficSystem.westCross.setWalk()
    elif cycleTime < trafficSystem.redTime + trafficSystem.yellowTime:
        trafficSystem.eastLight.setYellow()
        trafficSystem.westLight.setYellow()
    elif cycleTime < trafficSystem.redTime + trafficSystem.yellowTime + trafficSystem.greenTime:
        trafficSystem.northLight.setGreen()
        trafficSystem.southLight.setGreen()
        trafficSystem.northCross.setWalk()
        trafficSystem.southCross.setWalk()
        trafficSystem.eastLight.setRed()
        trafficSystem.westLight.setRed()
        trafficSystem.eastCross.setStop()
        trafficSystem.westCross.setStop()
    elif cycleTime < trafficSystem.redTime + trafficSystem.yellowTime + trafficSystem.greenTime + trafficSystem.yellowTime:
        trafficSystem.northLight.setYellow()
        trafficSystem.southLight.setYellow()


def draw_traffic_lights(screen: pygame.Surface, trafficSystem: TrafficSystem):
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    WHITE = (0, 0, 0)
    north_light_color1 = RED if trafficSystem.northLight.getRed() else YELLOW if trafficSystem.northLight.getYellow() else GREEN
    south_light_color1 = RED if trafficSystem.southLight.getRed() else YELLOW if trafficSystem.southLight.getYellow() else GREEN
    east_light_color1 = RED if trafficSystem.eastLight.getRed() else YELLOW if trafficSystem.eastLight.getYellow() else GREEN
    west_light_color1 = RED if trafficSystem.westLight.getRed() else YELLOW if trafficSystem.westLight.getYellow() else GREEN

    if(north_light_color1== RED):
        north_light_color1=RED
        south_light_color1 = RED
        north_light_color2 = WHITE
        south_light_color2 = WHITE
        north_light_color3 = WHITE
        south_light_color3 = WHITE
    elif(north_light_color1==YELLOW):
        north_light_color1=WHITE
        south_light_color1 = WHITE
        north_light_color2 = YELLOW
        south_light_color2 = YELLOW
        north_light_color3 = WHITE
        south_light_color3 = WHITE
    elif(north_light_color1==GREEN):
        north_light_color1=WHITE
        south_light_color1=WHITE
        north_light_color2 = WHITE
        south_light_color2= WHITE
        north_light_color3 = GREEN
        south_light_color3 = GREEN
    
    if(east_light_color1== RED):
        east_light_color1=RED
        west_light_color1 = RED
        east_light_color2 = WHITE
        west_light_color2 = WHITE
        east_light_color3 = WHITE
        west_light_color3 = WHITE
    elif(east_light_color1==YELLOW):
        east_light_color1=WHITE
        west_light_color1 = WHITE
        east_light_color2 = YELLOW
        west_light_color2 = YELLOW
        east_light_color3 = WHITE
        west_light_color3 = WHITE
    elif(east_light_color1==GREEN):
        east_light_color1=WHITE
        west_light_color1=WHITE
        east_light_color2 = WHITE
        west_light_color2= WHITE
        east_light_color3 = GREEN
        west_light_color3 = GREEN


    # Draw traffic lights
    pygame.draw.circle(screen, north_light_color1, (300, 100), 13)  # North traffic light
    pygame.draw.circle(screen, north_light_color2, (300, 125), 13)  # North traffic light
    pygame.draw.circle(screen, north_light_color3, (300, 150), 13)  # North traffic light
    pygame.draw.circle(screen, south_light_color1, (300, 500), 13)  # South traffic light
    pygame.draw.circle(screen, south_light_color2, (300, 475), 13)  # South traffic light
    pygame.draw.circle(screen, south_light_color3, (300, 450), 13)  # South traffic light

    pygame.draw.circle(screen, east_light_color1, (100, 300), 13)  # East traffic light
    pygame.draw.circle(screen, east_light_color2, (125, 300), 13)  # East traffic light
    pygame.draw.circle(screen, east_light_color3, (150, 300), 13)  # East traffic light
    pygame.draw.circle(screen, west_light_color1, (500, 300), 13)  # West traffic light
    pygame.draw.circle(screen, west_light_color2, (475, 300), 13)  # West traffic light
    pygame.draw.circle(screen, west_light_color3, (450, 300), 13)  # West traffic light


def draw_pedestrian_signs(screen: pygame.Surface, trafficSystem: TrafficSystem):
    # North
    font = pygame.font.Font(None, 36)
    border_width = 10
    square_x = 150
    square_y = 150
    square_size = 75
    pygame.draw.rect(screen, (33,19,13), (
        square_x - border_width, square_y - border_width, square_size + 2 * border_width,
        square_size + 2 * border_width))
    pygame.draw.rect(screen,(33,19,13),
                     (square_x, square_y, square_size, square_size))  # Draw the filled square inside the border
    sign_text = "WALK" if trafficSystem.northCross.getWalk() else "STOP"
    sign_color = (255, 255, 255) if trafficSystem.northCross.getWalk() else (255, 0, 0)
    screen.blit(font.render('north', True, (255, 255, 255)), (square_x + 5, square_y + 5))
    screen.blit(font.render(sign_text, True, sign_color), (square_x + 5, square_y + 40))

    # East
    square_x = 375
    square_y = 150
    pygame.draw.rect(screen, (33,19,13), (
        square_x - border_width, square_y - border_width, square_size + 2 * border_width,
        square_size + 2 * border_width))
    pygame.draw.rect(screen, (33,19,13), (square_x, square_y, square_size, square_size))  # Draw the filled square inside the border
    sign_text = "WALK" if trafficSystem.eastCross.getWalk() else "STOP"
    sign_color = (255, 255, 255) if trafficSystem.eastCross.getWalk() else (255, 0, 0)
    screen.blit(font.render('east', True, (255, 255, 255)), (square_x + 5, square_y + 5))
    screen.blit(font.render(sign_text, True, sign_color), (square_x + 5, square_y + 40))

    # West
    font = pygame.font.Font(None, 36)
    square_x = 150
    square_y = 375
    pygame.draw.rect(screen, (33,19,13), (
        square_x - border_width, square_y - border_width, square_size + 2 * border_width,
        square_size + 2 * border_width))
    pygame.draw.rect(screen, (33,19,13), (square_x, square_y, square_size, square_size))  # Draw the filled square inside the border
    sign_text = "WALK" if trafficSystem.westCross.getWalk() else "STOP"
    sign_color = (255, 255, 255) if trafficSystem.westCross.getWalk() else (255, 0, 0)
    screen.blit(font.render('west', True, (255, 255, 255)), (square_x + 5, square_y + 5))
    screen.blit(font.render(sign_text, True, sign_color), (square_x + 5, square_y + 40))

    # South
    font = pygame.font.Font(None, 36)
    square_x = 375
    square_y = 375
    pygame.draw.rect(screen, (33,19,13), (
        square_x - border_width, square_y - border_width, square_size + 2 * border_width,
        square_size + 2 * border_width))
    pygame.draw.rect(screen, (33,19,13), (square_x, square_y, square_size, square_size))  # Draw the filled square inside the border
    sign_text = "WALK" if trafficSystem.southCross.getWalk() else "STOP"
    sign_color = (255, 255, 255) if trafficSystem.southCross.getWalk() else (255, 0, 0)
    screen.blit(font.render('south', True, (255, 255, 255)), (square_x + 5, square_y + 5))
    screen.blit(font.render(sign_text, True, sign_color), (square_x + 5, square_y + 40))

def find_time_till_next_light_change(cycleTime: float, screen: pygame.surface, trafficSystem: TrafficSystem):
    # Draw the current time remaining onto the screen in the top right corner
    east_west_green = cycleTime < trafficSystem.redTime
    east_west_yellow = cycleTime < trafficSystem.redTime + trafficSystem.yellowTime
    north_south_green = cycleTime < trafficSystem.redTime + trafficSystem.yellowTime + trafficSystem.greenTime
    north_south_yellow = cycleTime < trafficSystem.redTime + trafficSystem.yellowTime + trafficSystem.greenTime + trafficSystem.yellowTime
    font = pygame.font.Font(None, 24)
    time_left_text_first_half = 'Time Remaining Until'
    time_left_text_second_half = ''

    # Repetition is done due to the pattern of the lights
    if east_west_green:
        time_left_text_second_half += str(round(trafficSystem.redTime - cycleTime, 2))
    elif east_west_yellow:
        time_left_text_second_half += str(round(trafficSystem.yellowTime + trafficSystem.redTime - cycleTime, 2))
    elif north_south_green:
        time_left_text_second_half += (
            str(round(trafficSystem.greenTime + trafficSystem.yellowTime + trafficSystem.redTime - cycleTime, 2)))
    elif north_south_yellow:
        time_left_text_second_half += (
            str(round(trafficSystem.yellowTime + trafficSystem.greenTime + trafficSystem.yellowTime + trafficSystem.redTime - cycleTime, 2)))

    # Overwrite existing text
    pygame.draw.rect(screen, (33,19,13), (400, 10, 200, 50))

    #screen.blit(font.render(time_left_text_first_half, True, (0, 110, 20)), (100, 10))
    screen.blit(font.render(time_left_text_second_half, True, (255, 255, 255)), (500, 40))

def main(redTime: float, greenTime: float, yellowTime: float):
    pygame.init()

    screenWidth = 600
    screenHeight = 600
    screenSize = (screenWidth, screenHeight)
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Traffic System")
    clock = pygame.time.Clock()

    trafficSystem = initialize_traffic_system(redTime, greenTime, yellowTime)
    screen.fill((33,19,13))  # Clear the screen

    # Draw roads
    GRAY = (40, 40, 40)
    LIGHT_YELLOW = (200, 200, 0)
    pygame.draw.rect(screen, GRAY, pygame.Rect(0, 250, 600, 100))           # Horizontal road
    pygame.draw.rect(screen, LIGHT_YELLOW, pygame.Rect(0, 295, 600, 10))    # Horizontal road line
    pygame.draw.rect(screen, GRAY, pygame.Rect(250, 0, 100, 600))           # Vertical road
    pygame.draw.rect(screen, LIGHT_YELLOW, pygame.Rect(295, 0, 10, 250))    # Vertical road line (top)
    pygame.draw.rect(screen, LIGHT_YELLOW, pygame.Rect(295, 350, 10, 250))  # Vertical road line (bottom)

    WHITE = (200, 200, 200)
    pygame.draw.rect(screen, WHITE, pygame.Rect(240, 250, 10, 100)) #west1
    pygame.draw.rect(screen, WHITE, pygame.Rect(205, 250, 10, 100)) #west2

    pygame.draw.rect(screen, WHITE, pygame.Rect(350, 250, 10, 100)) #east1
    pygame.draw.rect(screen, WHITE, pygame.Rect(385, 250, 10, 100)) #east2

    pygame.draw.rect(screen, WHITE, pygame.Rect(250, 215, 100, 10)) #north
    pygame.draw.rect(screen, WHITE, pygame.Rect(250, 250, 100, 10)) #north

    pygame.draw.rect(screen, WHITE, pygame.Rect(250, 350, 100, 10)) #south
    pygame.draw.rect(screen, WHITE, pygame.Rect(250, 385, 100, 10)) #south

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the traffic lights based on elapsed time
        elapsed_time = pygame.time.get_ticks() / 1000  # convert milliseconds to seconds
        cycleTime = elapsed_time % (trafficSystem.redTime + trafficSystem.yellowTime + trafficSystem.greenTime + trafficSystem.yellowTime)
        update_traffic_lights(cycleTime, trafficSystem)

        # Draw traffic lights
        draw_traffic_lights(screen, trafficSystem)

        # Draw pedestrian crossing signs
        draw_pedestrian_signs(screen, trafficSystem)

        # Draw the amount of time till the next light change onto the screen
        find_time_till_next_light_change(cycleTime, screen, trafficSystem)

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Control the frame rate
    pygame.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Traffic System',
        description='Simulates a basic traffic system'
    )
    parser.add_argument('--redTime', type=float, default=10.0, help='The time (secs) that the red light is on')
    parser.add_argument('--greenTime', type=float, default=10.0, help='The time (secs) that the green light is on')
    parser.add_argument('--yellowTime', type=float, default=5.0, help='The time (secs) that the yellow light is on')

    args = parser.parse_args()
    redTime: float = float(args.redTime)
    greenTime: float = float(args.greenTime)
    yellowTime: float = float(args.yellowTime)

    main(redTime, greenTime, yellowTime)