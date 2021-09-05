"""
Find SWF files and embed them into a HTML file to allow you to open them with web browsers that support Flash.
"""
import os


class SWFUtility:
    def __init__(self):
        self.swf_files = self.find_swf_files()
        self.embed_swf()

    def find_swf_files(self):
        """
        Returns a list of swf files that are located in the current directory
        """
        print('Looking for SWF files in current directory.')
        swf_files = []
        for file in os.listdir("./"):
            if file.endswith(".swf"):
                swf_files.append(file)
        return swf_files

    def embed_swf(self):
        """
        Embeds the swf files into a html page that can be ran in a web browser that supports Flash
        """
        print('Embedding SWF files into HTML files.')
        for file in self.swf_files:
            with open(file.replace('.swf', '_embedded.html'), 'w') as f:
                f.write('<object type="application/x-shockwave-flash" data="{0}" width="100%" height="100%"></object>'.format(file))


if __name__ == '__main__':
    swf_utility = SWFUtility()
    input('Program complete. Hit enter to quit.')
