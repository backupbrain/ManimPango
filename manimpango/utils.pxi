from _register_font cimport *

import warnings

cdef inline add_to_fontmap(PangoFontMap* fontmap, str font_path):
    cdef GError *err = NULL
    error_message = ""
    font_path_bytes = font_path.encode('utf-8')
    success = font_map_add_font_file(fontmap, font_path_bytes, &err)
    if err == NULL:
        error_message = "Unknown error"
    else:
        error_message = err.message.decode('utf-8')
    
    if not success:
        warnings.warn(
            f"Failed to add font at {font_path} to fontmap. Reason: {error_message}",
            RuntimeWarning,
            stacklevel=2
        )

    return success
