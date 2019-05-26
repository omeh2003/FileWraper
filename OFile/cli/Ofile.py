import os
import shutil


class OFile:

    @staticmethod
    def string_to_path(setlinkpath: str) -> str:
        """
        Args:
            setlinkpath (str):
            :rtype: str
        """
        _stink = os.path.normcase(setlinkpath)
        _path = os.path.normpath(_stink)

        return _path

    @staticmethod
    def is_file(setlinkpath) -> bool:

        _s = OFile.string_to_path(setlinkpath)
        if os.path.isfile(_s):
            return True
        else:
            return False

    def is_dir(self, setlinkpath) -> bool:
        """
        Args:
            setlinkpath: str
        """
        _s = self.string_to_path(setlinkpath)
        if os.path.isdir(_s):
            return True
        else:
            return False

    def copy_file_to_dir(self, file, srcdir):
        """

        :param file: str
        :type srcdir: str
        """
        _s = self.string_to_path(file)
        _d = self.string_to_path(srcdir)
        if self.is_file(_s) & self.is_dir(_d):
            _f = shutil.copy(_s, _d)
            if self.is_file(_f):
                return _f
        return None
