import math

class Scanner:
    
    def __init__(self,
                 distance,
                 radius,
                 max_height,
                 plot = False):
        self.distance = distance
        self.radius = radius
        self.max_height = max_height
        self.angle = 0
        self.height = 0
        self.plot = plot
        
    def get_distance():
##      returns the distance measured from the distance sensor
        return 1

    def rotate_table(t):
##      rotates the table t degress        
        self.angle += t
##      rotate_motor(t)

    def rise_sensor(h):
##      rises the sensor h milimeters
        if h > 0 and self.height < max_height or h < 0 and self.height > 0:
            self.height += h
##          rise_motor(h) 
        else:
            print ("sensor height limit is reached")

    def get_rotation():
##      returns the change of degrees from the original position
        return self.angle

    def get_height():
##      returns the current height of the sensor
        return self.height
    def rotate_point (d,t):
##      returns the (x,z) coordinates calculated by the rotation matrix
        return (d*math.cos(math.radians(t)),d*math.sin(math.radians(t)))
    def scan():
##      scans the whole object and outputs a PCD file of points
        return 1

    def write_to_PCD_file(width,
                          point_array,
                          points,
                          version = ".7",
                          field = "x y z",
                          size = "4 4 4",
                          field_type = "F F F",
                          count = "1 1 1",
                          height = "1",
                          viewpoint = "0 0 0 1 0 0 0",
                          data = "ascii",
                          file_name = "scan.PCD"):
##      writes the point array into a PCD file        
        return 1

    def plot():
##      plots the point cloud on-run if self.plot is True
        return 1
    
    
        
