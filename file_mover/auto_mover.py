import os
import time


class WatchingFolder():

    def __init__(self, path, frequency=5) -> None:
        self.path = path
        self.frequency = frequency
        self.changes = False

        self.base_state = [".placeholder"]

    def check_folder(self):
        """
        Check the folder to see if new files (or directories) are present
        generate the file paths as strings
        """
        current_state = os.listdir(self.path)
        # return [file for file in current_state
        #         if file not in self.base_state]
        for file in current_state:
            if file not in self.base_state:
                yield os.path.join(self.path, file)

    def start_checking(self):
        """Begin repeatedly calling check_folder(), with an interval defined by
        self.frequency (in seconds)

        Update self.changes to reflect whether changes are present
        """
        while True:
            try:
                next(self.check_folder())
                self.changes = True
                break
            except StopIteration:
                self.changes = False
            time.sleep(self.frequency)


class MoveFrom(WatchingFolder):

    def __init__(self, path, destination, **kwargs) -> None:
        super().__init__(path, **kwargs)

        self.destination = destination

    def move_file(self, file_path: str, destination: str = None) -> None:
        """
        Move a provided file from one dir to another

        :param file_path: The path of the file to move
        :type file_path: str
        :param destination: The path of the dir to move to
        :type destination: str
        """
        if not destination:
            destination = self.destination

        file_name = os.path.split(file_path)[1]
        file_title, extension = os.path.splitext(file_name)
        try:
            os.rename(file_path, os.path.join(destination, file_name))
        except FileExistsError: # only works on windows - linux replaces file
            same_name = 1
            while True:
                try:    # try to rename with (`same_name`) at end
                    os.rename(file_path, os.path.join(destination, file_title +
                                                      f" ({same_name})"
                                                      + extension))
                    break
                # there is already the file with the same number
                except FileExistsError:
                    same_name += 1  # increase by one ready to try again

    def auto_move(self):
        self.start_checking()
        while True:
            if self.changes: 
                for file in self.check_folder():
                    self.move_file(file)
                self.start_checking()


if __name__ == '__main__':
    source = MoveFrom("./from_folder", "./destination", frequency=1)
    source.auto_move()
