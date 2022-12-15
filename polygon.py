class Polygon:#this is a parent or a base class
    #so here we will not be using any init method because we will not be creating any object for this class ,we will just use it as a base or a parent class
    __width=None
    __height=None
    def set_value(self,width,height):
        self.__width= width
        self.__height= height

    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height