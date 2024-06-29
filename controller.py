import cv2
import numpy as np
from tkinter import filedialog as fd, messagebox, simpledialog as sd
from PIL import ImageTk, Image, ImageOps


class Controller:
    def __init__(self, master):
        self.master = master
        self.img = None
        self.cv_img = None
        self.image_loaded = False

    def open_image(self):
        filetypes = (
            ("PNG изображение", "*.png"),
            ("JPG изображение", "*.jpg"),
            ("Все файлы", "*.*"),
        )

        filename = fd.askopenfilename(
            title="Выберите файл", initialdir="/", filetypes=filetypes
        )
        try:
            img = Image.open(filename)
            self.img = img

            # Resize image
            img.thumbnail((390, 390))

            self.show_image(img)
            self.image_loaded = True
        except Exception as e:
            messagebox.showerror("Ошибка!", f"Не удалось открыть изображение: {str(e)}")

    def show_image(self, img):

        # Set iamge
        tk_image = ImageTk.PhotoImage(image=img)
        self.master.imagebox.image = tk_image
        self.master.imagebox.config(image=tk_image)

    def capture_image(self):
        cap = cv2.VideoCapture(0)

        # Check webcam
        if not cap.isOpened():
            messagebox.showerror(
                "Ошибка!",
                f"Не удалось найти камеру. Убедитесь, что она подключена и исправна!",
            )
            return

        try:
            # Take a photo
            _, frame = cap.read()

            if _:
                opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                captured_image = Image.fromarray(opencv_image)
                self.img = captured_image
                captured_image.thumbnail((390, 390))
                self.show_image(captured_image)

                self.image_loaded = True

                # Release resources
                cap.release()
                del cap
        except Exception as e:
            messagebox.showerror(
                "Ошибка!", f"Не удалось получить изображение: {str(e)}. "
            )

    def negative_image(self):
        if not self.image_loaded: 
            messagebox.showerror(
                "Ошибка!", "Изображение не загружено!"
            )
            
            return

        self.show_image(ImageOps.invert(self.img))

    def increase_brightness(self):
        """input_image:  color or grayscale image
        brightness:  -255 (all black) to +255 (all white)

        returns image of same type as input_image but with
        brightness adjusted"""

        if not self.image_loaded: 
            messagebox.showerror(
                "Ошибка!", "Изображение не загружено!"
            )
            
            return

        # Convert pil image to np array
        img = self.convert_from_image_to_cv2(self.img)

        value = sd.askinteger(
            "Введите значение", "Требуемая яркость(0 - 255):", minvalue=0, maxvalue=255
        )

        # Increase brightness
        img = cv2.convertScaleAbs(img, img, 1, value)

        # Convert np array to pil image
        img = Image.fromarray(img)

        self.show_image(img)

    def convert_from_image_to_cv2(self, img):
        cv2_img = np.array(img)
        return cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)

    def draw_circle(self):
        if not self.image_loaded: 
            messagebox.showerror(
                "Ошибка!", "Изображение не загружено!"
            )
            
            return

        img = self.convert_from_image_to_cv2(self.img)

        x = sd.askinteger(
            "Введите значение",
            "Координата центра X (0 - 390):",
            minvalue=0,
            maxvalue=390,
        )
        y = sd.askinteger(
            "Введите значение",
            "Координата центра Y (0 - 390):",
            minvalue=0,
            maxvalue=390,
        )
        r = sd.askinteger(
            "Введите значение", "Радиус круга (0 - 180):", minvalue=0, maxvalue=180
        )

        cv2.circle(img, (x, y), r, (255, 0, 0, 255), thickness=4, lineType=8, shift=0)
        img = Image.fromarray(img)
        self.show_image(img)
