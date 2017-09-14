import sys
import string


def clear_punctuation(document):
    document = str(document)
    try:
        """Remove from document all pontuation signals."""
        if sys.version_info[0] < 3:
            return document.translate(None,string.punctuation)
        else:   
            return document.translate(str.maketrans("", "", string.punctuation))
    except:
        return False;
