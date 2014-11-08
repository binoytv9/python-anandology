class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[' '] * width for i in range(height)]

    def setpixel(self, row, col):
        self.data[row][col] = '*'

    def getpixel(self, row, col):
        return self.data[row][col]

    def display(self):
        print "\n".join(["".join(row) for row in self.data])

class Shape:
    def paint(self, canvas): pass

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def hline(self, canvas, x, y, w):
	for i in range(w+1):
		canvas.setpixel(x,y+i)

    def vline(self, canvas, x, y, h):
	for i in range(h+1):
		canvas.setpixel(x+i,y)

    def paint(self, canvas):
        self.hline(canvas,self.x, self.y, self.w)
        self.hline(canvas,self.x + self.h, self.y, self.w)
        self.vline(canvas,self.x, self.y, self.h)
        self.vline(canvas,self.x, self.y + self.w, self.h)

class Square(Rectangle):
    def __init__(self, x, y, size):
        Rectangle.__init__(self, x, y, size, size)

class CompoundShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes

    def paint(self, canvas):
        for s in self.shapes:
            s.paint(canvas)


if __name__ == '__main__':
	c=Canvas(50,50)
	c.display()
	r=Rectangle(1,10,10,4)
	r.paint(c)
	c.display()
