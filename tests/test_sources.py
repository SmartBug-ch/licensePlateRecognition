from src.adapters.sources.folder_source import FolderSource
import pytest



def test_error_folder_not_found_source():
    with pytest.raises(FileNotFoundError):
        FolderSource("dieser_pfad_gibt_es_sicher_nicht.ch")

def test_folder_gives_image_back_from_source():
    test_folder_source = FolderSource("sample_images")
    
    frame = test_folder_source.get_next_frame()
    frame_two = test_folder_source.get_next_frame()

    assert frame is not None
    assert frame_two == None




