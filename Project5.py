#Jennifer Gonzales
#project 5
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    def get_area(self):
        return self.width * self.height
    def print_perimeter(self):
        print("Rectangle perimeter:", self.get_perimeter())
    def print_area(self):
        ("Rectangle area:", self.get_area())
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def print_perimeter(self):
        print("Square perimeter:", self.get_perimeter())
    def print_area(self):
        print("Square area:", self.got_area())
        
def main():
    shapes=[]
    while True:
        choice = input("Rectangle or Square (r/s): ")
        if choice == 'r':
            width = float(input("Width: "))
            height = float(input("Heigth: "))
            shape = Rectangle(width, height)
            shapes.append(shape)
        elif choice == 's':
            length = float(input("Length: "))
            shape = Square(length)
            shapes.append(shape)
        else:
            print("Invalid shape")
        continue_choice = input("Continue? y/n: ")
        if continue_choice.lower() != 'y':
            break
    print("\nThank you for using my app!")
    
if __name__ == '__main__':
    main()