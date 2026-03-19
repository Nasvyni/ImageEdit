import os
from PIL import Image, ImageFilter, ImageEnhance

class ImageEditor:
    def __init__(self):
        self.original = None
        self.edited = None
        self.filename = ""

    def open_image(self):
        while True:
            self.filename = input("\nEnter image filename (or type 'quit' to exit): ").strip()
            
            if self.filename.lower() == 'quit':
                return False
            
            if os.path.exists(self.filename):
                try:
                    self.original = Image.open(self.filename)
                    print(f"--- Loaded {self.filename} ---")
                    self.original.show()
                    return True
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print(f"File '{self.filename}' not found. Check the folder!")

    def main_loop(self):
        if not self.original:
            return

        base_name, extension = os.path.splitext(self.filename)

        while True:
            print("\n--- EDIT MENU ---")
            print("1. Black & White")
            print("2. Blur")
            print("3. Flip (Mirror)")
            print("4. Rotate 180")
            print("5. Adjust Contrast")
            print("6. Load a DIFFERENT image")
            print("7. EXIT")
            
            choice = input("Choose an option (1-7): ")

            if choice == '7':
                print("Exiting... Goodbye!")
                break
            elif choice == '6':
                if self.open_image():
                    base_name, extension = os.path.splitext(self.filename)
                    continue
                else:
                    break

            filter_name = ""
            if choice == '1':
                self.edited = self.original.convert('L')
                filter_name = "black_white"
            elif choice == '2':
                self.edited = self.original.filter(ImageFilter.BLUR)
                filter_name = "blur"
            elif choice == '3':
                self.edited = self.original.transpose(Image.FLIP_LEFT_RIGHT)
                filter_name = "flip"
            elif choice == '4':
                self.edited = self.original.transpose(Image.ROTATE_180)
                filter_name = "rotate_180"
            elif choice == '5':
                try:
                    level = float(input("Contrast level (e.g. 2.0): "))
                    enhancer = ImageEnhance.Contrast(self.original)
                    self.edited = enhancer.enhance(level)
                    filter_name = f"contrast_{level}"
                except ValueError:
                    print("Please enter a valid number!")
                    continue
            else:
                print("Invalid choice, try again.")
                continue

            if self.edited:
                save_name = f"{filter_name}{extension}"
                
                if self.edited.mode == 'RGBA' and save_name.lower().endswith(('.jpg', '.jpeg')):
                    self.edited = self.edited.convert('RGB')
                
                self.edited.save(save_name)
                self.edited.show()
                print(f"Done! Saved as {save_name}")

editor = ImageEditor()

if editor.open_image():
    editor.main_loop()