import math

class Scanner:
    
    def __init__(self,
                 distance,
                 radius,
                 max_height,
                 plot = False,
                 steps = 360):
        self.distance = distance
        self.radius = radius
        self.max_height = max_height
        self.angle = 0
        self.height = 0
        self.plot = plot
        self.steps = steps
        
    def get_distance(self):
##      returns the distance measured from the distance sensor
##      maps the value to be between -1 and 1
##      if the value is out off bounds returns None        
        return 1

    def rotate_table(self, t):
##      rotates the table t degress        
        self.angle += t
##      rotate_motor(t)

    def rise_sensor(self, h):
##      rises the sensor h milimeters
        if h > 0 and self.height < self.max_height or h < 0 and self.height > 0:
            self.height += h
##          rise_motor(h) 
        else:
            print ("sensor height limit is reached")

    def get_rotation(self):
##      returns the change of degrees from the original position
        return self.angle

    def get_height(self):
##      returns the current height of the sensor
        return self.height
    
    def rotate_point (self, d, t):
##      returns the x,z coordinates calculated by the rotation matrix
        return d*math.cos(math.radians(t)),d*math.sin(math.radians(t))
    
    def scan(self, t = 1, h = 1):
##      t is the angle of a single rotation        
        none_count = 0
        points = []
        while none_count < self.steps and self.height < self.max_height:
            if self.height != self.max_height and self.angle%360 == 0:
                self.rise_sensor(h)
            distance = self.get_distance()
            if distance is not None:
                print(self.height)
                x,z = self.rotate_point (distance, self.angle)
                points.append([x,self.height,z])
                self.rotate_table(t)
            else:
                none_count += 1
        self.write_to_PCD_file(point_array = points,
                               points = len(points))
        print("scan completed")
            
        
##      scans the whole object and outputs a PCD file of points
        return

    def write_to_PCD_file(self,
                          point_array,
                          points,
                          version = ".7",
                          fields = "x y z",
                          size = "4 4 4",
                          field_type = "F F F",
                          count = "1 1 1",
                          width = "1",
                          height = "1",
                          viewpoint = "0 0 0 1 0 0 0",
                          data = "ascii",
                          file_name = "scan.PCD"):
##      writes the point array into a PCD file
        PCD = open(file_name,"w")
        PCD.write("VERSION " + version)
        PCD.write("\n")
        PCD.write("FIELDS " + fields)
        PCD.write("\n")
        PCD.write("SIZE " + size)
        PCD.write("\n")
        PCD.write("TYPE " + field_type)
        PCD.write("\n")
        PCD.write("COUNT " + count)
        PCD.write("\n")
        PCD.write("WIDTH " + str(points))
        PCD.write("\n")
        PCD.write("HEIGHT " + height)
        PCD.write("\n")
        PCD.write("VIEWPOINT " + viewpoint)
        PCD.write("\n")
        PCD.write("POINTS " + str(points))
        PCD.write("\n")
        PCD.write("DATA " + data)
        PCD.write("\n")
        for point in point_array:
            PCD.write(str(point[0]) + " " + str(point[1]) + " " + str(point[2]))
            PCD.write("\n")
        PCD.close()
    
        return

    def plot(self):
##      plots the point cloud on-run if self.plot is True
        return
    
scanner = Scanner(distance = 30, radius = 10, max_height = 10)
scanner.scan()
        
