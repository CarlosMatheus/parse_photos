import cv2 as cv
import os


class Splitter:
    def __init__(self, quiet=False, log=True):
        self.quiet = quiet
        self.log = log

    def split_image(self, file_name: str, file_input_folder_path: str, file_output_folder_path: str):
        file_path = os.path.join(file_input_folder_path, file_name)
        cropped_images = self.__crop_to_four(file_path)
        self.__save_to_file(cropped_images, file_name, file_output_folder_path)

    def __crop_to_four(self, file_path: str):
        img = cv.imread(file_path)

        cropped_images = [
            img[:img.shape[0]//2, :img.shape[1]//2],
            img[img.shape[0]//2:, :img.shape[1]//2],
            img[:img.shape[0]//2, img.shape[1]//2:],
            img[img.shape[0]//2:, img.shape[1]//2:],
        ]

        if not self.quiet:
            for image in cropped_images:
                cv.imshow('Cropped', image)
                cv.waitKey(0)

        return cropped_images

    def __save_to_file(self, images: 'list[img]', original_file_name: str, file_output_folder_path: str):
        for index, image in enumerate(images):
            file_name, file_extension = os.path.splitext(original_file_name)
            new_name = file_name + '_' + str(index) + file_extension
            new_path = os.path.join(file_output_folder_path, new_name)

            if self.log:
                print(new_path)

            cv.imwrite(new_path, image)


if __name__ == '__main__':
    file_path = 'input'
    file_name = 'IMG_02656.JPG'
    output_folder = 'output'

    splitter = Splitter()
    splitter.split_image(file_name, file_path, output_folder)
