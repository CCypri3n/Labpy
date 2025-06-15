### CodeSnippets.py ###
# Useful snippets, that can be reused in different codes #
###     


## Center text in window:

text = "Test"

# --- 100% working centering solution for pygame.freetype ---
# Get the bounding rect for the text
text_rect = display_win.font.get_rect(text)
# Center the rect on your window
text_rect.center = win.get_rect().center  # This is the official, robust way!
# Render the text at the rect (NOT just .topleft)
display_win.font.render_to(win, text_rect, text, (255, 255, 255))
# ----------------------------------------------------------
